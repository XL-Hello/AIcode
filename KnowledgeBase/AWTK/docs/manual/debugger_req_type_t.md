## debugger_req_type_t

### 概述

请求的消息类型。

### 常量

名称 | 说明  
---|---  
DEBUGGER_REQ_ATTACH | attach请求码。  
DEBUGGER_REQ_STOP | 停止运行请求码。  
DEBUGGER_REQ_PAUSE | 暂停运行请求码。  
DEBUGGER_REQ_IS_PAUSED | 查询是否处于暂停状态请求码。  
DEBUGGER_REQ_STEP_IN | 运行进入函数请求码。  
DEBUGGER_REQ_STEP_OUT | 运行退出函数请求码。  
DEBUGGER_REQ_STEP_OVER | 运行下一步请求码。  
DEBUGGER_REQ_STEP_LOOP_OVER | 运行下一行请求码。（跳转循环）  
DEBUGGER_REQ_CONTINUE | 运行到下一个断点请求码。  
DEBUGGER_REQ_SET_BREAK_POINT | 设置断点请求码。  
DEBUGGER_REQ_REMOVE_BREAK_POINT | 移除断点请求码。  
DEBUGGER_REQ_CLEAR_BREAK_POINTS | 清除断点请求码。  
DEBUGGER_REQ_GET_SELF | 获取self对象请求码。  
DEBUGGER_REQ_GET_LOCAL | 获取局部变量和函数参数对象请求码。  
DEBUGGER_REQ_GET_GLOBAL | 获取global对象请求码。  
DEBUGGER_REQ_GET_CODE | 获取源代码请求码。  
DEBUGGER_REQ_GET_DEBUGGERS | 获取调试器列表。  
DEBUGGER_REQ_GET_BREAK_POINTS | 获取断点列表。  
DEBUGGER_REQ_GET_CALLSTACK | 获取callstack请求码。  
DEBUGGER_REQ_UPDATE_CODE | 更新源代码请求码。  
DEBUGGER_REQ_LAUNCH | 执行代码请求码。  
DEBUGGER_REQ_DEINIT | 断开调试器请求码。  
DEBUGGER_REQ_RESTART | 重新运行运行请求码。
