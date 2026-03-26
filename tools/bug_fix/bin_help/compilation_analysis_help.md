# 崩溃日志 + 固件符号 + MAP 可视化联合分析指南

本文档用于指导如何结合下面几类材料定位固件问题：

- 崩溃日志：如 `bug_fix/bug.log`
- 原始固件符号文件：如 `bug_fix/bin/debug/*.elf`
- 链接映射文件：如 `bug_fix/bin/debug/*.map`
- MAP HTML 分析脚本：`bug_fix/bin_help/map_html_analyzer.py`

目标不是只看到 panic 后的线程回溯，而是尽量还原真正的崩溃点、模块归属和可疑内存占用来源。

---

## 1. 前置准备

在仓库根目录执行：

```bash
./setup_cross_compiler.sh
```

确认工具可用：

```bash
which arm-none-eabi-addr2line
which arm-none-eabi-nm
which python3
```

本项目常用符号文件：

- AP：`bug_fix/bin/debug/nuttx_ap.elf`
- A7：`bug_fix/bin/debug/nuttx_a7.elf`
- OTA：`bug_fix/bin/debug/nuttx_ota.elf`
- Bootloader：`bug_fix/bin/debug/nuttx_bl.elf`

本项目常用 map 文件：

- AP：`bug_fix/bin/debug/nuttx_ap.map`
- A7：`bug_fix/bin/debug/nuttx_a7.map`

---

## 2. 第一步：从日志提取地址

示例：提取所有 8 位十六进制地址。

```bash
rg -o "0x[0-9a-f]{8}" bug_fix/bug.log | sort | uniq > /tmp/crash_addrs.txt
wc -l /tmp/crash_addrs.txt
```

按地址段分组，分别喂给不同 ELF：

```bash
# AP 常见地址段示例：0x0cxxxxxx / 0x00xxxxxx
awk '/^0x0c|^0x00/{print}' /tmp/crash_addrs.txt > /tmp/ap_addrs.txt

# A7 常见地址段示例：0x34xxxxxx / 0x38xxxxxx
awk '/^0x34|^0x38/{print}' /tmp/crash_addrs.txt > /tmp/a7_addrs.txt
```

---

## 3. 第二步：分别符号化 AP/A7 地址

### 3.1 AP 地址符号化

```bash
arm-none-eabi-addr2line -piCfe bug_fix/bin/debug/nuttx_ap.elf $(cat /tmp/ap_addrs.txt)
```

### 3.2 A7 地址符号化

```bash
arm-none-eabi-addr2line -piCfe bug_fix/bin/debug/nuttx_a7.elf $(cat /tmp/a7_addrs.txt)
```

如果是 OTA 或 bootloader 问题，把 ELF 切到对应产物即可。

---

## 4. 第三步：验证“怀疑函数是否命中地址集”

有时你怀疑某个函数，但回溯未直接显示。先用 `nm` 查该函数地址，再与日志地址集合比对。

```bash
arm-none-eabi-nm -n bug_fix/bin/debug/nuttx_ap.elf | rg "zbDevice_versionSet|zbDeviceOta_start|zbhost_deviceOta_Start|_zb_upgradeStatusChanged"
```

如果函数地址不在日志地址集合中，说明当前 dump 栈没有直接命中该函数，不能只因时序接近就定责。

---

## 5. 第四步：使用 MAP HTML 分析器看段占用和目录归属

当需要回答下面这类问题时，优先补充 MAP 分析：

- 哪个段占用最大
- 哪个目录或模块把 `.text`、`.bss`、`.data` 撑大了
- AWTK、audio、bus、devicemanager 等模块到底占了多少
- 某个问题是否和内存布局、段膨胀、模块体积异常有关

### 5.1 使用方法

`map_html_analyzer.md` 中的方法可直接落到当前目录结构里：

1. 把 `bug_fix/bin_help/map_html_analyzer.py` 拷贝到 `WB100-SDK/rtos/nuttx/` 目录。
2. 在 `WB100-SDK/rtos/nuttx/` 下执行：

```bash
python3 map_html_analyzer.py nuttx_a7.map -o report.html
```

如果分析 AP map，对应改成：

```bash
python3 map_html_analyzer.py nuttx_ap.map -o report.html
```

### 5.2 建议执行方式

如果不想手动拷贝，可在仓库根目录执行：

```bash
cp -a bug_fix/bin_help/map_html_analyzer.py WB100-SDK/rtos/nuttx/
cd WB100-SDK/rtos/nuttx
python3 map_html_analyzer.py /home/xl/dreame/RTOS/001/dreame_rtos_4inch_project/bug_fix/bin/debug/nuttx_a7.map -o /tmp/nuttx_a7_report.html
```

### 5.3 这个脚本能看什么

结合脚本实现，`report.html` 主要提供两类视图：

- 所有段的总览
- 目录树占用视图，按目录层级统计文件大小和占比

脚本会从 map 文件中提取：

- 段名、起始地址、段大小
- 各文件在段内的占用
- 各目录层级的累计占用

对定位“某个模块是否异常膨胀”很有帮助，尤其适合：

- 内存超限
- 大模块归属不清
- 怀疑某次改动把 AWTK、audio、bus、devicemanager 某个目录整体撑大

### 5.4 什么时候用 MAP 分析，什么时候用 addr2line

- `addr2line`：回答“这个地址落在哪个函数”
- `nm`：回答“怀疑函数的地址是否命中”
- `map_html_analyzer.py`：回答“这个固件的段和目录占用是谁贡献的”

三者互补，不互相替代。

---

## 6. 第五步：判断“真正崩溃点”还是“被动线程栈”

这是最关键的一步。

### 6.1 常见误区

- 误把 `sched_dumpstack`、`backtrace_unwind` 当成崩溃业务函数。
- 误把 panic 后批量打印的线程栈当成根因。
- 误把内存占用最大的模块直接当成崩溃点。

### 6.2 判定规则

如果地址主要落在下面这些函数：

- `sched_backtrace`
- `backtrace_unwind`
- `sched_dumpstack`
- `sem_wait`
- `pthread_cond_wait`
- `sleep`
- `epoll_wait`

通常说明这是 panic 后现场快照，不是首个 fault 点。

真正更有价值的证据通常是：

- fault 当下 PC/LR/SP
- 当前任务名和寄存器现场
- assert 原始触发函数/行号
- 第一条 panic/assert/fault 日志

---

## 7. 建议输出模板

建议在分析文档中按下面结构写结论：

1. 时间线：触发时间、panic 时间、重启时间
2. 符号化结果：AP 与 A7 分开列出
3. MAP 结果：段占用、目录占用、异常模块
4. 证据强度分级：
   - 已命中调用栈
   - 强可疑但未直接命中
   - 通用防御项
5. 下一步最小改动：
   - 先补首现场日志
   - 再修边界问题或资源问题

---

## 8. 本项目可直接复用的命令

```bash
./setup_cross_compiler.sh

rg -o "0x[0-9a-f]{8}" bug_fix/bug.log | sort | uniq > /tmp/crash_addrs.txt
awk '/^0x0c|^0x00/{print}' /tmp/crash_addrs.txt > /tmp/ap_addrs.txt
awk '/^0x34|^0x38/{print}' /tmp/crash_addrs.txt > /tmp/a7_addrs.txt

arm-none-eabi-addr2line -piCfe bug_fix/bin/debug/nuttx_ap.elf $(cat /tmp/ap_addrs.txt)
arm-none-eabi-addr2line -piCfe bug_fix/bin/debug/nuttx_a7.elf $(cat /tmp/a7_addrs.txt)

arm-none-eabi-nm -n bug_fix/bin/debug/nuttx_ap.elf | rg "zbDevice_versionSet|zbDeviceOta_start|zbhost_deviceOta_Start|_zb_upgradeStatusChanged"

cp -a bug_fix/bin_help/map_html_analyzer.py WB100-SDK/rtos/nuttx/
cd WB100-SDK/rtos/nuttx
python3 map_html_analyzer.py /home/xl/dreame/RTOS/001/dreame_rtos_4inch_project/bug_fix/bin/debug/nuttx_a7.map -o /tmp/nuttx_a7_report.html
```

---

## 9. 结论

`addr2line` 的价值是把地址翻译成函数，`nm` 的价值是校验怀疑函数是否真的命中，`map_html_analyzer.py` 的价值是把 map 文件转成更容易浏览的段/目录占用报告。

根因定位仍然必须结合：

- 时序
- 首现场寄存器
- 任务名
- 跨核链路
- 模块归属

如果只看到 `sched_dumpstack + 多线程阻塞栈`，说明证据不足；如果只看到某个目录占用很大，也不能直接拍板它就是崩溃根因。
