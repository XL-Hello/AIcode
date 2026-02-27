## debugger_breaked_event_t

### 概述

![image](images/debugger_breaked_event_t_0.png)

## 调试器中断运行的事件。

### 函数

函数名称 | 说明  
---|---  
debugger_breaked_event_cast | 把event对象转debugger_breaked_event_t对象。  
debugger_breaked_event_init | 初始调试器中断运行的事件。  
debugger_breaked_event_init_ex | 初始调试器中断运行的事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
file_path | const char* | 中断运行的文件路径。（备注：可能文件路径为空）  
frame_name | const char* | 中断运行的函数名字。（备注：可能文件路径为空）  
line | uint32_t | 中断运行的行号。  
  
#### debugger_breaked_event_cast 函数

* * *

  * 函数功能：



> 把event对象转debugger_breaked_event_t对象。

  * 函数原型：


    
    
    debugger_breaked_event_t* debugger_breaked_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_breaked_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### debugger_breaked_event_init 函数

* * *

  * 函数功能：



> 初始调试器中断运行的事件。

  * 函数原型：


    
    
    event_t* debugger_breaked_event_init (debugger_breaked_event_t* event, uint32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | debugger_breaked_event_t* | event对象。  
line | uint32_t | 中断运行的行号。  
  
#### debugger_breaked_event_init_ex 函数

* * *

  * 函数功能：



> 初始调试器中断运行的事件。

  * 函数原型：


    
    
    event_t* debugger_breaked_event_init_ex (debugger_breaked_event_t* event, uint32_t line, const char* file_path, const char* frame_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | debugger_breaked_event_t* | event对象。  
line | uint32_t | 中断运行的行号。  
file_path | const char* | 中断运行的行号。  
frame_name | const char* | 中断运行的函数。  
  
#### file_path 属性

* * *

> 中断运行的文件路径。（备注：可能文件路径为空）

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### frame_name 属性

* * *

> 中断运行的函数名字。（备注：可能文件路径为空）

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### line 属性

* * *

> 中断运行的行号。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
