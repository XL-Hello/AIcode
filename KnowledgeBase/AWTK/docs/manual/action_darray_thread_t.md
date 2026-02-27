## action_darray_thread_t

### 概述

执行action的线程。

## > 每个线程都有一个action darray，可以是共享的darray，也可以是私有的darray。

### 函数

函数名称 | 说明  
---|---  
action_darray_thread_create | 创建action_darray_thread对象。  
action_darray_thread_create_ex | 创建action_darray_thread对象。  
action_darray_thread_create_with_darray | 创建action_darray_thread对象。  
action_darray_thread_create_with_darray_ex | 创建action_darray_thread对象。  
action_darray_thread_destroy | 销毁。  
action_darray_thread_exec | 让线程执行action。  
action_darray_thread_set_idle_interval | 设置空闲时的时间间隔。  
action_darray_thread_set_on_idle | 设置空闲时的回调函数。  
action_darray_thread_set_on_quit | 设置退出时的回调函数。  
action_darray_thread_set_strategy | 设置策略  
action_queue_create | 创建action_queue对象。  
action_queue_destroy | 销毁。  
action_queue_recv | 接收一个请求。  
action_queue_send | 发送一个请求。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
darray | waitable_action_darray_t* | action darray。  
executed_actions_nr | uint32_t | 已经执行action的个数。  
idle_interval | uint32_t | 空闲时的时间间隔。  
thread | tk_thread_t* | 线程对象。  
  
#### action_darray_thread_create 函数

* * *

  * 函数功能：



> 创建action_darray_thread对象。

  * 函数原型：


    
    
    action_darray_thread_t* action_darray_thread_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_darray_thread_t* | action_darray_thread对象。  
  
#### action_darray_thread_create_ex 函数

* * *

  * 函数功能：



> 创建action_darray_thread对象。

  * 函数原型：


    
    
    action_darray_thread_t* action_darray_thread_create_ex (const char* name, uint32_t stack_size, tk_thread_priority_t priority);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_darray_thread_t* | action_darray_thread对象。  
name | const char* | 名称。  
stack_size | uint32_t | 栈的大小。  
priority | tk_thread_priority_t | 优先级。  
  
#### action_darray_thread_create_with_darray 函数

* * *

  * 函数功能：



> 创建action_darray_thread对象。

  * 函数原型：


    
    
    action_darray_thread_t* action_darray_thread_create_with_darray (waitable_action_darray_t* darray);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_darray_thread_t* | action_darray_thread对象。  
darray | waitable_action_darray_t* | darray对象。  
  
#### action_darray_thread_create_with_darray_ex 函数

* * *

  * 函数功能：



> 创建action_darray_thread对象。

  * 函数原型：


    
    
    action_darray_thread_t* action_darray_thread_create_with_darray_ex (waitable_action_darray_t* darray, const char* name, uint32_t stack_size, tk_thread_priority_t priority);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_darray_thread_t* | action_darray_thread对象。  
darray | waitable_action_darray_t* | darray对象。  
name | const char* | 名称。  
stack_size | uint32_t | 栈的大小。  
priority | tk_thread_priority_t | 优先级。  
  
#### action_darray_thread_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t action_darray_thread_destroy (action_darray_thread_t* thread);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_darray_thread_t* | action_darray_thread对象。  
  
#### action_darray_thread_exec 函数

* * *

  * 函数功能：



> 让线程执行action。

  * 函数原型：


    
    
    ret_t action_darray_thread_exec (action_darray_thread_t* thread, qaction_t* action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_darray_thread_t* | action_darray_thread对象。  
action | qaction_t* | action对象。  
  
#### action_darray_thread_set_idle_interval 函数

* * *

  * 函数功能：



> 设置空闲时的时间间隔。

  * 函数原型：


    
    
    ret_t action_darray_thread_set_idle_interval (action_darray_thread_t* thread, uint32_t interval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_darray_thread_t* | action_darray_thread对象。  
interval | uint32_t | 时间间隔(毫秒)。  
  
#### action_darray_thread_set_on_idle 函数

* * *

  * 函数功能：



> 设置空闲时的回调函数。

  * 函数原型：


    
    
    ret_t action_darray_thread_set_on_idle (action_darray_thread_t* thread, action_darray_thread_on_idle_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_darray_thread_t* | action_darray_thread对象。  
on_idle | action_darray_thread_on_idle_t | 空闲时的回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### action_darray_thread_set_on_quit 函数

* * *

  * 函数功能：



> 设置退出时的回调函数。

  * 函数原型：


    
    
    ret_t action_darray_thread_set_on_quit (action_darray_thread_t* thread, action_darray_thread_on_quit_t on_quit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_darray_thread_t* | action_darray_thread对象。  
on_quit | action_darray_thread_on_quit_t | 退出时的回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### action_darray_thread_set_strategy 函数

* * *

  * 函数功能：



> 设置策略

  * 函数原型：


    
    
    ret_t action_darray_thread_set_strategy (action_darray_thread_t* thread, action_darray_thread_strategy_t strategy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t值  
thread | action_darray_thread_t* | action_darray_thread对象。  
strategy | action_darray_thread_strategy_t | 策略  
  
#### action_queue_create 函数

* * *

  * 函数功能：



> 创建action_queue对象。

  * 函数原型：


    
    
    action_queue_t* action_queue_create (uint16_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_queue_t* | action_queue对象。  
capacity | uint16_t | action的容量。  
  
#### action_queue_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t action_queue_destroy (action_queue_t* q);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
q | action_queue_t* | action_queue对象。  
  
#### action_queue_recv 函数

* * *

  * 函数功能：



> 接收一个请求。

  * 函数原型：


    
    
    ret_t action_queue_recv (action_queue_t* q, qaction_t** action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
q | action_queue_t* | action_queue对象。  
action | qaction_t** | 用于返回action对象。  
  
#### action_queue_send 函数

* * *

  * 函数功能：



> 发送一个请求。

  * 函数原型：


    
    
    ret_t action_queue_send (action_queue_t* q, qaction_t* action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
q | action_queue_t* | action_queue对象。  
action | qaction_t* | action对象。  
  
#### darray 属性

* * *

> action darray。

  * 类型：waitable_action_darray_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### executed_actions_nr 属性

* * *

> 已经执行action的个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### idle_interval 属性

* * *

> 空闲时的时间间隔。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### thread 属性

* * *

> 线程对象。

  * 类型：tk_thread_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
