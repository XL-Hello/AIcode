## system_event_t

### 概述

![image](images/system_event_t_0.png)

## 系统事件。

### 函数

函数名称 | 说明  
---|---  
system_event_cast | 把event对象转system_event_t对象。  
system_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
sdl_event | void* | SDL_Event。  
  
#### system_event_cast 函数

* * *

  * 函数功能：



> 把event对象转system_event_t对象。

  * 函数原型：


    
    
    system_event_t* system_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | system_event_t* | event 对象。  
event | event_t* | event对象。  
  
#### system_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* system_event_init (system_event_t* event, void* target, void* sdl_event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | system_event_t* | event对象。  
target | void* | 事件目标。  
sdl_event | void* | SDL_Event对象。  
  
#### sdl_event 属性

* * *

> SDL_Event。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
