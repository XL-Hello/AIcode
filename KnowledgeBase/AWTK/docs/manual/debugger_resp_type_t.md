## debugger_resp_type_t

### 概述

响应/推送的消息类型。

### 常量

名称 | 说明  
---|---  
DEBUGGER_RESP_ATTACH | attach响应码。  
DEBUGGER_RESP_STOP | 停止运行响应码。  
DEBUGGER_RESP_IS_PAUSED | 查询是否处于暂停状态响应码。  
DEBUGGER_RESP_PAUSE | 暂停运行响应码。  
DEBUGGER_RESP_STEP_IN | 运行进入函数响应码。  
DEBUGGER_RESP_STEP_OUT | 运行退出函数响应码。  
DEBUGGER_RESP_STEP_OVER | 运行下一步响应码。  
DEBUGGER_RESP_STEP_LOOP_OVER | 运行下一行响应码。（跳出循环）  
DEBUGGER_RESP_CONTINUE | 运行到下一个断点响应码。  
DEBUGGER_RESP_SET_BREAK_POINT | 设置断点响应码。  
DEBUGGER_RESP_REMOVE_BREAK_POINT | 移除断点响应码。  
DEBUGGER_RESP_CLEAR_BREAK_POINTS | 清除断点响应码。  
DEBUGGER_RESP_GET_SELF | 获取self对象响应码。  
DEBUGGER_RESP_GET_LOCAL | 获取局部变量和函数参数对象响应码。  
DEBUGGER_RESP_GET_GLOBAL | 获取global对象响应码。  
DEBUGGER_RESP_GET_CODE | 获取源代码响应码。  
DEBUGGER_RESP_GET_DEBUGGERS | 获取调试器列表响应码。  
DEBUGGER_RESP_GET_BREAK_POINTS | 获取断点列表响应码。  
DEBUGGER_RESP_GET_CALLSTACK | 获取callstack响应码。  
DEBUGGER_RESP_UPDATE_CODE | 更新源代码响应码。  
DEBUGGER_RESP_LAUNCH | 执行代码响应码。  
DEBUGGER_RESP_DEINIT | 断开调试器响应码。  
DEBUGGER_RESP_MSG_LOG | 程序打印日志的响应码/事件码。  
DEBUGGER_RESP_MSG_ERROR | 程序出现错误的响应码/事件码。  
DEBUGGER_RESP_MSG_BREAKED | 程序中断的响应码/事件码。  
DEBUGGER_RESP_MSG_FRAME_CHANGED | 用户切换调用堆栈的frame.  
DEBUGGER_RESP_MSG_COMPLETED | 程序执行完成的响应码/事件码。
