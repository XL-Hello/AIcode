## event_source_idle_t

### 概述

![image](images/event_source_idle_t_0.png)

## idle事件源。

### 函数

函数名称 | 说明  
---|---  
event_source_idle_create | 创建idle事件源。  
  
#### event_source_idle_create 函数

* * *

  * 函数功能：



> 创建idle事件源。

  * 函数原型：


    
    
    event_source_t* event_source_idle_create (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_source_t* | 返回事件源对象。  
idle_manager | idle_manager_t* | 定时器管理器对象。
