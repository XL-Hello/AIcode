# 固件 Bug 分析说明

这份文档用于指导后续分析 `bug_fix` 目录中的固件问题，按“类技能说明”组织，目标是让分析过程固定、可复用、可追溯。

## 1. 输入材料

本次分析的固定输入如下：

- 固件包和符号文件：`bug_fix/bin`
- 固件分析辅助文档：`bug_fix/bin_help/compilation_analysis_help.md`
- MAP HTML 分析脚本：`bug_fix/bin_help/map_html_analyzer.py`
- 用户日志：`bug_fix/bug.log`
- Bug 描述与已有分析结果：`bug_fix/bug.md`
- 编译脚本：`dreame.sh`

分析时先看 `bug_fix/bug.md`，明确现象、时间线、已有结论、仍未确认项，再回到 `bug_fix/bug.log`、ELF、MAP 做证据核对，不要直接继承旧结论。

## 2. 分析目标

目标不是只找“最后一条业务日志”，而是尽量回答下面 5 个问题：

1. 第一现场是谁先异常，AP、A7、audio、ota 还是别的核/模块。
2. 日志里的回溯是首个 fault 点，还是 panic 后批量 dump 出来的被动线程栈。
3. 崩溃点对应到本项目哪个源码模块、哪个仓库、哪个函数。
4. 当前问题更像业务崩溃、跨核通信异常、资源竞争、栈溢出，还是二次故障。
5. 如果怀疑内存布局或模块膨胀，哪个段、哪个目录、哪个模块占用异常。

## 3. 固定分析流程

### 3.1 先读问题描述

先阅读：

- `bug_fix/bug.md`
- `bug_fix/bug.log`

先整理出：

- 触发场景
- 关键时间点
- 最后一批正常业务日志
- 第一条 panic/assert/fault 日志
- 是否出现 `dump_task`、`backtrace_unwind`、`sched_dumpstack` 之类的全局 dump

### 3.2 用 ELF 做地址符号化

符号化方法以 `bug_fix/bin_help/compilation_analysis_help.md` 为准。核心原则：

- AP 地址优先对 `bug_fix/bin/debug/nuttx_ap.elf`
- A7 地址优先对 `bug_fix/bin/debug/nuttx_a7.elf`
- OTA/bootloader 相关问题，再看 `nuttx_ota.elf`、`nuttx_bl.elf`
- 只看线程回溯不够，必须结合日志时间线和任务名

可直接复用的起手命令：

```bash
./setup_cross_compiler.sh

rg -o "0x[0-9a-f]{8}" bug_fix/bug.log | sort | uniq > /tmp/crash_addrs.txt
awk '/^0x0c|^0x00/{print}' /tmp/crash_addrs.txt > /tmp/ap_addrs.txt
awk '/^0x34|^0x38/{print}' /tmp/crash_addrs.txt > /tmp/a7_addrs.txt

arm-none-eabi-addr2line -piCfe bug_fix/bin/debug/nuttx_ap.elf $(cat /tmp/ap_addrs.txt)
arm-none-eabi-addr2line -piCfe bug_fix/bin/debug/nuttx_a7.elf $(cat /tmp/a7_addrs.txt)
```

如果已经怀疑某个函数，可以再用 `nm` 验证日志地址是否真的命中了它，而不是因为业务时序接近就误判。

### 3.3 用 MAP HTML 分析器辅助定位模块归属

当你遇到下面这些场景时，不要只看 `addr2line`，要补一轮 MAP 分析：

- 怀疑某个模块异常膨胀
- 需要判断 `.text`、`.bss`、`.data` 是谁贡献的
- 需要快速看 AWTK、audio、bus、devicemanager 等目录的占用
- 需要辅助解释内存超限、段布局异常、镜像变大

`map_html_analyzer.py` 的推荐用法：

1. 把 `bug_fix/bin_help/map_html_analyzer.py` 拷贝到 `WB100-SDK/rtos/nuttx/`
2. 在 `WB100-SDK/rtos/nuttx/` 执行：

```bash
python3 map_html_analyzer.py nuttx_a7.map -o report.html
```

或直接分析问题现场 map：

```bash
cp -a bug_fix/bin_help/map_html_analyzer.py WB100-SDK/rtos/nuttx/
cd WB100-SDK/rtos/nuttx
python3 map_html_analyzer.py /home/xl/dreame/RTOS/001/dreame_rtos_4inch_project/bug_fix/bin/debug/nuttx_a7.map -o /tmp/nuttx_a7_report.html
```

它更适合回答：

- 哪个段最大
- 哪个目录占用最多
- 哪个模块把镜像撑大了

不要把它当成崩溃地址符号化工具，它和 `addr2line` 是互补关系。

### 3.4 判断“首个 fault”还是“panic 后现场”

这是最容易误判的地方。

如果地址或栈主要落在以下函数：

- `sched_backtrace`
- `backtrace_unwind`
- `sched_dumpstack`
- `sem_wait`
- `pthread_cond_wait`
- `sleep`
- `epoll_wait`

通常说明这是 panic 后的线程快照，不是根因函数。

真正更有价值的证据通常是：

- 第一条 assert/panic/fault 日志
- 当时的任务名
- 对应的 PC/LR/SP
- IRQ/跨核中断/共享内存处理链路

### 3.5 回到源码定位调用链

符号化出函数名后，按下面顺序回源码：

1. 在当前仓库先用 `rg` 搜函数名、日志 tag、任务名。
2. 如果命中 `dreame/apps` 或 `dreame/boards/...`，同时核对它在 `WB100-SDK` 下的真实位置。
3. 如果命中的是应用子仓代码，优先到对应的 `WB100-SDK/apps/<module>` 目录分析。
4. 如果 MAP 报告显示某个目录段占用异常，再回到该目录结合函数和任务名继续缩小范围。

推荐命令：

```bash
rg -n "函数名|日志关键字|任务名" .
rg -n "函数名|日志关键字|任务名" WB100-SDK/apps
```

## 4. 源码目录判定规则

所有代码都在当前项目里，但分析时要注意这是一个“挂载入口 + SDK 真源码”的结构。

### 4.1 本仓库里的入口目录

从 `dreame.sh` 可知，脚本会把以下目录绑定到 `WB100-SDK` 内：

- `dreame/apps` -> `WB100-SDK/apps`
- `dreame/boards/best2003_ep` -> `WB100-SDK/boards/best2003_ep`

这意味着：

- 如果你在 `dreame/apps/<module>` 看到了怀疑代码，它通常对应 `WB100-SDK/apps/<module>`
- 如果需要看真实编译输入、子仓历史、模块边界，优先看 `WB100-SDK` 下的目录

### 4.2 应用子仓位置

`WB100-SDK/apps` 下有大量独立模块，很多本身就是单独 git 仓库，例如：

- `WB100-SDK/apps/devicemanager`
- `WB100-SDK/apps/bus`
- `WB100-SDK/apps/system_ctrl`
- `WB100-SDK/apps/awtk_launch`
- `WB100-SDK/apps/dreame_ota`

当符号化结果或 MAP 报告落到这些模块时，分析动作应包括：

1. 找到具体函数和调用链。
2. 查看该模块自己的日志、线程、消息收发路径。
3. 必要时直接在对应子仓范围内继续搜索，而不是只停留在顶层调用点。

## 5. 如何结合编译脚本判断产物归属

`dreame.sh` 是本项目的主构建脚本，至少要掌握下面几点：

- 支持的构建目标：`audio`、`ap`、`ota`、`bootloader`
- 构建命令：`./dreame.sh build [模块名]`
- 默认构建会编译所有模块
- 调试符号文件最终会被拷贝到 `output/debug`

脚本里定义的调试产物包括：

- `nuttx_ap.elf`
- `nuttx_a7.elf`
- `nuttx_bl.elf`
- `nuttx_ota.elf`
- 对应 `.map` 文件

所以分析时要建立这层映射：

- `bug_fix/bin/debug/*.elf` 和 `bug_fix/bin/debug/*.map` 是问题现场对应的分析输入
- `output/debug/*.elf` 和 `output/debug/*.map` 是你本地重新编译后得到的最新产物

如果要验证“某个修复是否真的进入固件”，要重新编译后对比 `output/debug` 中的符号、map 和源码，而不是只看 `bug_fix/bin/debug`。

## 6. 常见怀疑方向

拿到首现场后，优先判断属于哪一类：

- 业务逻辑直接崩溃：空指针、数组越界、非法字符串、JSON 处理错误
- 跨核通信异常：rpmsg、共享内存、remote panic、IRQ 回调
- 音频链路异常：`audio_flinger`、`pcm`、播放提示音、语音播报
- UI/A7 伴生告警：界面设备不存在、状态不同步，但未必是根因
- 内存/段布局异常：某个目录或模块把关键段撑大
- 二次故障：首个 panic 后又触发 `Stack Overflow`、信号量/中断上下文错误

分析时把“首因”和“二次故障”拆开写，也把“直接崩溃点”和“体积/内存风险”拆开写。

## 7. 建议输出格式

每次分析都建议按下面结构写：

1. 现象描述
2. 时间线
3. 首现场证据
4. 符号化结果
5. MAP 结果和模块归属
6. 对应源码模块和仓库位置
7. 已排除项
8. 当前最可信根因方向
9. 下一步验证动作

## 8. 对当前 bug 的使用方式

针对 `bug`，建议按下面顺序执行：

1. 先读 `bug_fix/bug.md`，明确已有判断和怀疑方向。
2. 再从 `bug_fix/bug.log` 提取首个 panic、任务名、回溯地址。
3. 用 `bug_fix/bin/debug/nuttx_ap.elf` 和 `nuttx_a7.elf` 复核符号化结果。
4. 必要时用 `bug_fix/bin/debug/*.map` 配合 `bug_fix/bin_help/map_html_analyzer.py` 看段和目录占用。
5. 回源码检查 AP、audio、rpmsg、共享内存相关链路。
6. 若命中应用子仓，直接转到 `WB100-SDK/apps/<module>` 深挖。
7. 若需要验证修复，再用 `./dreame.sh build ap`、`./dreame.sh build audio` 或默认全编译生成新产物。

## 9. 最后原则

分析固件 bug 时，优先级永远是：

1. 首现场
2. 符号化
3. 时间线
4. 源码调用链
5. MAP 段和目录归属
6. 重新编译验证

不要因为某条业务日志离崩溃最近就直接定责，也不要因为某个目录占用很大就把它直接当根因。
