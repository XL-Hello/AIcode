## debugger_frame_changed_event_t

### 概述

![image](images/debugger_frame_changed_event_t_0.png)

## 用户切换到调用堆栈指定的frame的事件。

### 函数

函数名称 | 说明  
---|---  
debugger_frame_changed_event_cast | 把event对象转debugger_frame_changed_event_t对象。  
debugger_frame_changed_event_init | 初始化  
debugger_frame_changed_event_init_ex | 初始化  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
file_path | const char* | 文件路径。（备注：可能文件路径为空）  
func | const char* | 函数名。  
line | uint32_t | 行号。  
  
#### debugger_frame_changed_event_cast 函数

* * *

  * 函数功能：



> 把event对象转debugger_frame_changed_event_t对象。

  * 函数原型：


    
    
    debugger_frame_changed_event_t* debugger_frame_changed_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_frame_changed_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### debugger_frame_changed_event_init 函数

* * *

  * 函数功能：



> 初始化

  * 函数原型：


    
    
    event_t* debugger_frame_changed_event_init (debugger_frame_changed_event_t* event, const char* func, uint32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | debugger_frame_changed_event_t* | event对象。  
func | const char* | 函数名。  
line | uint32_t | 行号。  
  
#### debugger_frame_changed_event_init_ex 函数

* * *

  * 函数功能：



> 初始化

  * 函数原型：


    
    
    event_t* debugger_frame_changed_event_init_ex (debugger_frame_changed_event_t* event, const char* func, uint32_t line, const char* file_path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | debugger_frame_changed_event_t* | event对象。  
func | const char* | 函数名。  
line | uint32_t | 行号。  
file_path | const char* | 文件路径。  
  
#### file_path 属性

* * *

> 文件路径。（备注：可能文件路径为空）

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### func 属性

* * *

> 函数名。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### line 属性

* * *

> 行号。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
