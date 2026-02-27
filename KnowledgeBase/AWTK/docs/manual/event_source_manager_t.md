## event_source_manager_t

### 概述

## 事件源管理器。

### 函数

函数名称 | 说明  
---|---  
event_source_manager_add | 增加事件源对象。  
event_source_manager_deinit | ~初始化。  
event_source_manager_destroy | 销毁事件源管理器。  
event_source_manager_dispatch | 分发事件。  
event_source_manager_get_wakeup_time | 获取wakeup时间(微秒)  
event_source_manager_init | 初始化。  
event_source_manager_remove | 移除事件源对象。  
event_source_manager_remove_by_tag | 移除所有tag相同的事件源对象。  
event_source_manager_set_min_sleep_time | 设置默认最小睡眠时间(毫秒)。  
event_source_manager_set_min_sleep_time_us | 设置默认最小睡眠时间(微秒)。  
  
#### event_source_manager_add 函数

* * *

  * 函数功能：



> 增加事件源对象。

  * 函数原型：


    
    
    ret_t event_source_manager_add (event_source_manager_t* manager, event_source_t* source);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
source | event_source_t* | event_source对象。  
  
#### event_source_manager_deinit 函数

* * *

  * 函数功能：



> ~初始化。

  * 函数原型：


    
    
    ret_t event_source_manager_deinit (event_source_manager_t* manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
  
#### event_source_manager_destroy 函数

* * *

  * 函数功能：



> 销毁事件源管理器。

  * 函数原型：


    
    
    ret_t event_source_manager_destroy (event_source_manager_t* manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
  
#### event_source_manager_dispatch 函数

* * *

  * 函数功能：



> 分发事件。

  * 函数原型：


    
    
    ret_t event_source_manager_dispatch (event_source_manager_t* manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
  
#### event_source_manager_get_wakeup_time 函数

* * *

  * 函数功能：



> 获取wakeup时间(微秒)

  * 函数原型：


    
    
    uint64_t event_source_manager_get_wakeup_time (event_source_manager_t* manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回wakeup时间(微秒)。  
manager | event_source_manager_t* | event_source_manager对象。  
  
#### event_source_manager_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    ret_t event_source_manager_init (event_source_manager_t* manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
  
#### event_source_manager_remove 函数

* * *

  * 函数功能：



> 移除事件源对象。

  * 函数原型：


    
    
    ret_t event_source_manager_remove (event_source_manager_t* manager, event_source_t* source);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
source | event_source_t* | event_source对象。  
  
#### event_source_manager_remove_by_tag 函数

* * *

  * 函数功能：



> 移除所有tag相同的事件源对象。

  * 函数原型：


    
    
    ret_t event_source_manager_remove_by_tag (event_source_manager_t* manager, void* tag);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
tag | void* | tag。  
  
#### event_source_manager_set_min_sleep_time 函数

* * *

  * 函数功能：



> 设置默认最小睡眠时间(毫秒)。

  * 函数原型：


    
    
    ret_t event_source_manager_set_min_sleep_time (event_source_manager_t* manager, uint32_t sleep_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
sleep_time | uint32_t | 默认最小睡眠时间(毫秒)。  
  
#### event_source_manager_set_min_sleep_time_us 函数

* * *

  * 函数功能：



> 设置默认最小睡眠时间(微秒)。

  * 函数原型：


    
    
    ret_t event_source_manager_set_min_sleep_time_us (event_source_manager_t* manager, uint32_t sleep_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
manager | event_source_manager_t* | event_source_manager对象。  
sleep_time | uint32_t | 默认最小睡眠时间(微秒)。
