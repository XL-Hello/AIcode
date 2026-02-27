## idle_t

### 概述

idle可以看作是duration为0的定时器。

> idle可以用来实现一些异步处理。

示例：
    
    
    static ret_t something_on_idle(const idle_info_t* info) {
    widget_t* widget = WIDGET(info->ctx);
    edit_t* edit = EDIT(widget);
    ...
    return RET_REMOVE;
    }
    
    ...
    
    idle_add(something_on_idle, edit);
    

## > 在非GUI线程请用idle_queue。

### 函数

函数名称 | 说明  
---|---  
idle_add | 增加一个idle。  
idle_count | 返回idle的个数。  
idle_dispatch | 调用全部idle的函数。  
idle_exist | idle是否存在。  
idle_find | 查找指定ID的idle。  
idle_queue | 用于非GUI线程增加一个idle，本函数向主循环的事件队列中发送一个增加idle的请求。  
idle_queue_ex | 用于非GUI线程增加一个idle，本函数向主循环的事件队列中发送一个增加idle的请求。  
idle_remove | 删除指定的idle。  
idle_remove_all_by_ctx | 根据上下文删除所有对应的idle。  
idle_set_on_destroy | 设置一个回调函数，在idle被销毁时调用(方便脚本语言去释放回调函数)。  
  
#### idle_add 函数

* * *

  * 函数功能：



> 增加一个idle。

  * 函数原型：


    
    
    uint32_t idle_add (idle_func_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle的ID，0表示失败。  
on_idle | idle_func_t | idle回调函数，回调函数返回RET_REPEAT，则下次继续执行，否则自动移出。  
ctx | void* | idle回调函数的上下文。  
  
#### idle_count 函数

* * *

  * 函数功能：



> 返回idle的个数。

  * 函数原型：


    
    
    uint32_t idle_count ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle的个数。  
  
#### idle_dispatch 函数

* * *

  * 函数功能：



> 调用全部idle的函数。

  * 函数原型：


    
    
    ret_t idle_dispatch ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### idle_exist 函数

* * *

  * 函数功能：



> idle是否存在。

  * 函数原型：


    
    
    bool_t idle_exist (idle_func_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | idle回调函数的上下文。  
  
#### idle_find 函数

* * *

  * 函数功能：



> 查找指定ID的idle。

  * 函数原型：


    
    
    const idle_info_t* idle_find (uint32_t idle_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const idle_info_t* | 返回idle的信息。  
idle_id | uint32_t | idleID。  
  
#### idle_queue 函数

* * *

  * 函数功能：



> 用于非GUI线程增加一个idle，本函数向主循环的事件队列中发送一个增加idle的请求。

  * 函数原型：


    
    
    ret_t idle_queue (idle_func_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | idle回调函数的上下文。  
  
#### idle_queue_ex 函数

* * *

  * 函数功能：



> 用于非GUI线程增加一个idle，本函数向主循环的事件队列中发送一个增加idle的请求。

  * 函数原型：


    
    
    ret_t idle_queue_ex (idle_func_t on_idle, void* ctx, tk_destroy_t on_destroy, void* on_destroy_ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | idle回调函数的上下文。  
on_destroy | tk_destroy_t | 回调函数。  
on_destroy_ctx | void* | 回调函数上下文。  
  
#### idle_remove 函数

* * *

  * 函数功能：



> 删除指定的idle。

  * 函数原型：


    
    
    ret_t idle_remove (uint32_t idle_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_id | uint32_t | idleID。  
  
#### idle_remove_all_by_ctx 函数

* * *

  * 函数功能：



> 根据上下文删除所有对应的idle。

  * 函数原型：


    
    
    ret_t idle_remove_all_by_ctx (void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ctx | void* | idle回调函数的上下文  
  
#### idle_set_on_destroy 函数

* * *

  * 函数功能：



> 设置一个回调函数，在idle被销毁时调用(方便脚本语言去释放回调函数)。

  * 函数原型：


    
    
    ret_t idle_set_on_destroy (uint32_t idle_id, tk_destroy_t on_destroy, void* on_destroy_ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_id | uint32_t | idleID。  
on_destroy | tk_destroy_t | 回调函数。  
on_destroy_ctx | void* | 回调函数上下文。
