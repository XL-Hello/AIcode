# bug2 问题分析

## 结论先行

这次 `bug_fix/bug2.log` 里的真正崩溃点，不在 `dm_busManager_reportProp()` 或 `deviceCtrlResp.c`，而是在 **AP 收到 audio 子系统 panic 通知后触发断言**。

`reportProp` 只是崩溃前出现的一条业务日志，时序上接近，但从首现场符号化结果看，它不是直接 fault 点。

## 1. 时间线

### 1.1 业务侧最后的正常日志

`49.099s`，AP 侧上报属性：

```text
[gateway W][dm_busManager_reportProp:1180] (serial:548524492)---{"reqId":"...","deviceProps":[{"deviceId":"bc7765e805a14b18c7431000zb3",...,"properties":{"onoff":"off"}}]}
```

对应代码位置在：

- `codes/source/bus/dm_busManager.c:1179-1181`

说明这里只是把 `reportProp` JSON 打印并通过 `dm_dreServerSendEvent_family()` 发出去。

### 1.2 manager_device 正在处理另一条属性上报

`49.140s ~ 49.155s`，`manager_device` 线程在执行 `_dm_msgFunc_reportProp()`，处理的是另一个设备 `f5940c2605a14ae4b1c31018zb1` 的属性上报并写库：

```text
[_dm_msgFunc_reportProp:236] serial:386801988,device:0x3422cb18
reportProp[srcId:f5940c2605a14ae4b1c31018zb1, name:reportProp]:
{"onoff":"off"}
...
[deviceTree_db_saveDeviceProperty:80] start deviceId:f5940c2605a14ae4b1c31018zb1
```

对应代码位置：

- `codes/source/manager/manager_device.c:234-279`

这段逻辑包含：

1. 过滤和裁剪属性
2. 合并到设备树
3. 再次通过 `dm_busManager_reportProp()` 对外上报

从日志看，这里执行到了数据库保存，未出现空指针、JSON parse 失败或数组越界类报错。

### 1.3 A7 侧仅报“找不到设备”

`49.168s ~ 49.179s`，A7 收到 AP 发出的 `reportProp` 后打印：

```text
[dreUI_mgDevice_msgReportProp](549) nofind deviceId:bc7765e805a14b18c7431000zb3
```

这说明 UI 侧设备表里没有这个 `deviceId`，但这只是业务告警，不是系统 crash。

### 1.4 真正首现场：audio 子系统 panic

`49.338s` 出现第一条真正的 panic：

```text
Assertion failed panic: at file: .../bes_global_shmem.h:101 task: audio_flinger process: bes_cmsis_wrapper
```

这条日志非常关键，说明：

1. 当前运行线程是 `audio_flinger`
2. 触发位置是 `bes_global_shmem.h:101`
3. 不是 `manager_device` 线程先崩

## 2. 符号化结果

对 `bug_fix/bin/debug/nuttx_ap.elf` 做 `addr2line` 后，首现场回溯如下：

```text
_assert
bes_rptun_check_cpu
hal_transq_remote_irq_handler
up_irq_handler
arm_doirq
osSignalWaitInner
osSignalWait
af_thread
pthread_proxy
pthread_startup
pthread_start
```

对应含义：

1. `af_thread()` 是 `audio_flinger` 主线程
2. 它在等待 signal 时进入 IRQ
3. IRQ 中执行 `hal_transq_remote_irq_handler()`
4. 再进入 `bes_rptun_check_cpu()`
5. 因检测到 remote cpu 的 panic/reset 信号而触发 `_assert`

也就是说，**AP 不是自己先跑飞，而是收到了 audio 侧异常通知，然后按框架设计 panic**。

## 3. 为什么说不是 `dm_busManager_reportProp` / `deviceCtrlResp`

## 3.1 `dm_busManager_reportProp` 只命中“前序业务日志”

`dm_busManager_reportProp()` 的行为很简单：

- 组装 JSON
- 打印日志
- 发送到总线

对应代码：

- `codes/source/bus/dm_busManager.c:1167-1184`

当前日志中没有证据表明这里发生：

- 空指针解引用
- JSON 内存释放错误
- 发送接口同步崩溃

它只是崩溃前最后一批可见业务日志之一。

## 3.2 `deviceCtrlResp.c` 没有进入本次崩溃链路

这份日志里没有 `deviceCtrlResp_*` 的关键日志。

而且当前代码中 `deviceCtrlResp_Resp()` 一进函数就直接：

```c
return 0;
```

说明这份文件不是本次 panic 的直接参与者。

## 4. 更像什么问题

从日志尾部还能看到一组更强的证据：

```text
Remote: audio headrx 40188
Dump rpmsg info between cpu (master: yes) ap <==> audio
RX buffer, total 16, pending 0
TX buffer, total 16, pending 1
TX buffer 0x387ab050 hold by pcm0c
```

以及稍后又出现：

```text
osSemaphoreNewInner failed, in_isr:1, os_ready:1
...
Usage Fault Reason:
Stack Overflow
```

这更像是：

1. **audio 子系统先发生异常**
2. AP 在处理 audio/rpmsg panic 过程中继续打印大量 dump
3. 后续 reset/panic 路径里又叠加了 secondary fault（`Stack Overflow`）

所以当前更合理的定责方向是：

- **audio_flinger / audio rpmsg / pcm0c 通道**
- **AP <-> audio 跨核共享内存或消息处理链路**

而不是设备属性上报逻辑本身。

## 5. 当前能下到什么强度的结论

### 已确认

1. 首个明确 panic 点在 `bes_global_shmem.h:101`
2. panic 发生在线程 `audio_flinger`
3. 调用链属于 `audio` remote panic 检查路径
4. `dm_busManager_reportProp()` 只是时序上接近的业务动作

### 仍未确认

1. audio 子系统为什么先 panic
2. 是 `pcm0c` 数据流、rpmsg buffer 卡死，还是 audio remote 固件内部先出错
3. A7 的 `nofind deviceId` 是否只是独立 UI 告警，还是业务异常的伴生现象

## 6. 建议下一步

### 优先级最高

1. 用 audio/AP 对应符号文件继续符号化 `audio` 侧回溯，而不是只看 AP panic 后的 dump。
2. 重点检查 `pcm0c`、`audio` endpoint、`hal_transq_remote_irq_handler` 对应的跨核消息收发。
3. 在 audio panic 上报前补首现场日志：消息类型、长度、endpoint、buffer owner、最近一次 audio 指令来源。

### 次优先级

1. 检查崩溃前是否有播放提示音、语音播报、铃声、OTA 提示音等动作。
2. 核对 `reportProp` 之后是否触发了任何音频反馈逻辑，如果有，要把这条业务链继续往 audio 侧追。

### 可以先不作为根因处理

1. `dm_busManager_reportProp()`
2. `deviceCtrlResp.c`
3. A7 侧 `nofind deviceId` 这条 UI 告警

## 7. 最终判断

`bug2` 当前最可信的根因方向是：

**audio 子系统或 AP<->audio 的 rpmsg/共享内存链路异常，导致 audio remote panic，AP 在 `bes_rptun_check_cpu()` 中感知到 panic 后跟随断言。**

`reportProp` 和 `manager_device` 只是崩溃前碰巧还在运行的业务线程，不是当前日志能支持的直接根因。
