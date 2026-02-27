## timer_t

### 概述

定时器系统。

> 本定时器精度较低，最高精度为1000/FPS，如果需要高精度的定时器，请用OS提供的定时器。

示例：
    
    
    static ret_t my_on_timer(const timer_info_t* info) {
    widget_t* widget = WIDGET(info->ctx);
    ...
    return RET_REPEAT;
    }
    
    ...
    
    timer_add(my_on_timer, widget, 1000);
    

## > 在非GUI线程请用timer_queue。

### 函数

函数名称 | 说明  
---|---  
timer_add | 增加一个timer。  
timer_count | 返回timer的个数。  
timer_find | 查找指定ID的timer。  
timer_modify | 修改指定的timer的duration，修改之后定时器重新开始计时。  
timer_next_time | 返回最近的timer到期时间(毫秒)。  
timer_queue | 用于非GUI线程增加一个timer，本函数向主循环的事件队列中发送一个增加timer的请求。  
timer_queue_ex | 用于非GUI线程增加一个timer，本函数向主循环的事件队列中发送一个增加timer的请求。  
timer_remove | 删除指定的timer。  
timer_remove_all_by_ctx | 根据上下文删除所有对应的timer。  
timer_reset | 重置指定的timer，重置之后定时器重新开始计时。  
timer_resume | 唤醒挂起指定的timer，并且重置定时器重新开始计时  
timer_set_on_destroy | 设置一个回调函数，在timer被销毁时调用(方便脚本语言去释放回调函数)。  
timer_suspend | 挂起指定的timer，一般用于不断循环触发的计时器。  
  
#### timer_add 函数

* * *

  * 函数功能：



> 增加一个timer。

  * 函数原型：


    
    
    uint32_t timer_add (timer_func_t on_timer, void* ctx, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回timer的ID，TK_INVALID_ID表示失败。  
on_timer | timer_func_t | timer回调函数。  
ctx | void* | timer回调函数的上下文。  
duration | uint32_t | 时间(毫秒)。  
  
#### timer_count 函数

* * *

  * 函数功能：



> 返回timer的个数。

  * 函数原型：


    
    
    uint32_t timer_count ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回timer的个数。  
  
#### timer_find 函数

* * *

  * 函数功能：



> 查找指定ID的timer。

  * 函数原型：


    
    
    const timer_info_t* timer_find (uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const timer_info_t* | 返回timer的信息。  
timer_id | uint32_t | timerID。  
  
#### timer_modify 函数

* * *

  * 函数功能：



> 修改指定的timer的duration，修改之后定时器重新开始计时。

  * 函数原型：


    
    
    ret_t timer_modify (uint32_t timer_id, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_id | uint32_t | timerID。  
duration | uint32_t | 新的时间(毫秒)。  
  
#### timer_next_time 函数

* * *

  * 函数功能：



> 返回最近的timer到期时间(毫秒)。

  * 函数原型：


    
    
    uint32_t timer_next_time ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回最近的timer到期时间(毫秒)。  
  
#### timer_queue 函数

* * *

  * 函数功能：



> 用于非GUI线程增加一个timer，本函数向主循环的事件队列中发送一个增加timer的请求。

  * 函数原型：


    
    
    ret_t timer_queue (timer_func_t on_timer, void* ctx, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
on_timer | timer_func_t | timer回调函数，回调函数返回RET_REPEAT，则下次继续执行，否则自动移出。  
ctx | void* | timer回调函数的上下文。  
duration | uint32_t | 时间(毫秒)。  
  
#### timer_queue_ex 函数

* * *

  * 函数功能：



> 用于非GUI线程增加一个timer，本函数向主循环的事件队列中发送一个增加timer的请求。

  * 函数原型：


    
    
    ret_t timer_queue_ex (timer_func_t on_timer, void* ctx, uint32_t duration, tk_destroy_t on_destroy, void* on_destroy_ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
on_timer | timer_func_t | timer回调函数，回调函数返回RET_REPEAT，则下次继续执行，否则自动移出。  
ctx | void* | timer回调函数的上下文。  
duration | uint32_t | 时间(毫秒)。  
on_destroy | tk_destroy_t | 回调函数。  
on_destroy_ctx | void* | 回调函数上下文。  
  
#### timer_remove 函数

* * *

  * 函数功能：



> 删除指定的timer。

  * 函数原型：


    
    
    ret_t timer_remove (uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_id | uint32_t | timerID。  
  
#### timer_remove_all_by_ctx 函数

* * *

  * 函数功能：



> 根据上下文删除所有对应的timer。

  * 函数原型：


    
    
    ret_t timer_remove_all_by_ctx (void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ctx | void* | timer回调函数的上下文。  
  
#### timer_reset 函数

* * *

  * 函数功能：



> 重置指定的timer，重置之后定时器重新开始计时。

  * 函数原型：


    
    
    ret_t timer_reset (uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_id | uint32_t | timerID。  
  
#### timer_resume 函数

* * *

  * 函数功能：



> 唤醒挂起指定的timer，并且重置定时器重新开始计时

  * 函数原型：


    
    
    ret_t timer_resume (uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_id | uint32_t | timerID。  
  
#### timer_set_on_destroy 函数

* * *

  * 函数功能：



> 设置一个回调函数，在timer被销毁时调用(方便脚本语言去释放回调函数)。

  * 函数原型：


    
    
    ret_t timer_set_on_destroy (uint32_t timer_id, tk_destroy_t on_destroy, void* on_destroy_ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_id | uint32_t | timerID。  
on_destroy | tk_destroy_t | 回调函数。  
on_destroy_ctx | void* | 回调函数上下文。  
  
#### timer_suspend 函数

* * *

  * 函数功能：



> 挂起指定的timer，一般用于不断循环触发的计时器。

  * 函数原型：


    
    
    ret_t timer_suspend (uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_id | uint32_t | timerID。
