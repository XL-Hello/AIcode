## action_thread_t

### 概述

执行action的线程。

## > 每个线程都有一个action queue，可以是共享的queue，也可以是私有的queue。

### 函数

函数名称 | 说明  
---|---  
action_thread_create | 创建action_thread对象。  
action_thread_create_ex | 创建action_thread对象。  
action_thread_create_with_queue | 创建action_thread对象。  
action_thread_create_with_queue_ex | 创建action_thread对象。  
action_thread_destroy | 销毁。  
action_thread_exec | 让线程执行action。  
action_thread_set_on_idle | 设置空闲时的回调函数。  
action_thread_set_on_quit | 设置退出时的回调函数。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
executed_actions_nr | uint32_t | 已经执行action的个数。  
queue | waitable_action_queue_t* | action queue。  
thread | tk_thread_t* | 线程对象。  
  
#### action_thread_create 函数

* * *

  * 函数功能：



> 创建action_thread对象。

  * 函数原型：


    
    
    action_thread_t* action_thread_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_thread_t* | action_thread对象。  
  
#### action_thread_create_ex 函数

* * *

  * 函数功能：



> 创建action_thread对象。

  * 函数原型：


    
    
    action_thread_t* action_thread_create_ex (const char* name, uint32_t stack_size, tk_thread_priority_t priority);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_thread_t* | action_thread对象。  
name | const char* | 名称。  
stack_size | uint32_t | 栈的大小。  
priority | tk_thread_priority_t | 优先级。  
  
#### action_thread_create_with_queue 函数

* * *

  * 函数功能：



> 创建action_thread对象。

  * 函数原型：


    
    
    action_thread_t* action_thread_create_with_queue (waitable_action_queue_t* queue);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_thread_t* | action_thread对象。  
queue | waitable_action_queue_t* | queue对象。  
  
#### action_thread_create_with_queue_ex 函数

* * *

  * 函数功能：



> 创建action_thread对象。

  * 函数原型：


    
    
    action_thread_t* action_thread_create_with_queue_ex (waitable_action_queue_t* queue, const char* name, uint32_t stack_size, tk_thread_priority_t priority);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_thread_t* | action_thread对象。  
queue | waitable_action_queue_t* | queue对象。  
name | const char* | 名称。  
stack_size | uint32_t | 栈的大小。  
priority | tk_thread_priority_t | 优先级。  
  
#### action_thread_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t action_thread_destroy (action_thread_t* thread);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_thread_t* | action_thread对象。  
  
#### action_thread_exec 函数

* * *

  * 函数功能：



> 让线程执行action。

  * 函数原型：


    
    
    ret_t action_thread_exec (action_thread_t* thread, qaction_t* action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_thread_t* | action_thread对象。  
action | qaction_t* | action对象。  
  
#### action_thread_set_on_idle 函数

* * *

  * 函数功能：



> 设置空闲时的回调函数。

  * 函数原型：


    
    
    ret_t action_thread_set_on_idle (action_thread_t* thread, action_thread_on_idle_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_thread_t* | action_thread对象。  
on_idle | action_thread_on_idle_t | 空闲时的回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### action_thread_set_on_quit 函数

* * *

  * 函数功能：



> 设置退出时的回调函数。

  * 函数原型：


    
    
    ret_t action_thread_set_on_quit (action_thread_t* thread, action_thread_on_quit_t on_quit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | action_thread_t* | action_thread对象。  
on_quit | action_thread_on_quit_t | 退出时的回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### executed_actions_nr 属性

* * *

> 已经执行action的个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### queue 属性

* * *

> action queue。

  * 类型：waitable_action_queue_t*

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
