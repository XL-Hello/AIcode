## event_source_timer_t

### 概述

![image](images/event_source_timer_t_0.png)

## timer事件源。

### 函数

函数名称 | 说明  
---|---  
event_source_timer_create | 创建timer事件源。  
  
#### event_source_timer_create 函数

* * *

  * 函数功能：



> 创建timer事件源。

  * 函数原型：


    
    
    event_source_t* event_source_timer_create (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_source_t* | 返回事件源对象。  
timer_manager | timer_manager_t* | 定时器管理器对象。
