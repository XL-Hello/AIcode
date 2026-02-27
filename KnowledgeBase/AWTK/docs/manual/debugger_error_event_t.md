## debugger_error_event_t

### 概述

![image](images/debugger_error_event_t_0.png)

## 程序错误事件。

### 函数

函数名称 | 说明  
---|---  
debugger_error_event_cast | 把event对象转debugger_error_event_t对象。  
debugger_error_event_init | 初始程序错误的事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
line | uint32_t | 出现错误的行号。  
message | const char* | 错误消息。  
  
#### debugger_error_event_cast 函数

* * *

  * 函数功能：



> 把event对象转debugger_error_event_t对象。

  * 函数原型：


    
    
    debugger_error_event_t* debugger_error_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_error_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### debugger_error_event_init 函数

* * *

  * 函数功能：



> 初始程序错误的事件。

  * 函数原型：


    
    
    event_t* debugger_error_event_init (debugger_error_event_t* event, uint32_t line, const char* message);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | debugger_error_event_t* | event对象。  
line | uint32_t | 出现错误的行号。  
message | const char* | 错误信息。  
  
#### line 属性

* * *

> 出现错误的行号。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### message 属性

* * *

> 错误消息。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
