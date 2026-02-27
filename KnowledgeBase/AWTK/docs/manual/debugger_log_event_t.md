## debugger_log_event_t

### 概述

![image](images/debugger_log_event_t_0.png)

## 调试器打印日志的事件。

### 函数

函数名称 | 说明  
---|---  
debugger_log_event_cast | 把event对象转debugger_log_event_t对象。  
debugger_log_event_init | 初始调试器打印日志的事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
line | int32_t | 打印日志的行号(<0表示原生代码打印的日志)。  
message | const char* | 日志消息。  
  
#### debugger_log_event_cast 函数

* * *

  * 函数功能：



> 把event对象转debugger_log_event_t对象。

  * 函数原型：


    
    
    debugger_log_event_t* debugger_log_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_log_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### debugger_log_event_init 函数

* * *

  * 函数功能：



> 初始调试器打印日志的事件。

  * 函数原型：


    
    
    event_t* debugger_log_event_init (debugger_log_event_t* event, uint32_t line, const char* message);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | debugger_log_event_t* | event对象。  
line | uint32_t | 打印日志的行号。  
message | const char* | 日志。  
  
#### line 属性

* * *

> 打印日志的行号(<0表示原生代码打印的日志)。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### message 属性

* * *

> 日志消息。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
