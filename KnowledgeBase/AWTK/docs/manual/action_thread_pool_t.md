## action_thread_pool_t

### 概述

## action线程池。

### 函数

函数名称 | 说明  
---|---  
action_thread_pool_create | 创建action_thread_pool对象。  
action_thread_pool_create_ex | 创建action_thread_pool对象。  
action_thread_pool_destroy | 销毁。  
action_thread_pool_exec | 执行action。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
max_thread_nr | uint32_t | 最大线程数。  
min_idle_nr | uint32_t | 最小空闲线程数  
priority | tk_thread_priority_t | 线程池中的线程优先级  
stack_size | uint32_t | 线程池中的线程栈大小  
  
#### action_thread_pool_create 函数

* * *

  * 函数功能：



> 创建action_thread_pool对象。

  * 函数原型：


    
    
    action_thread_pool_t* action_thread_pool_create (uint16_t max_thread_nr, uint16_t min_idle_nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_thread_pool_t* | action_thread_pool对象。  
max_thread_nr | uint16_t | 最大线程数。  
min_idle_nr | uint16_t | 最小空闲线程数(必须大于0)。  
  
#### action_thread_pool_create_ex 函数

* * *

  * 函数功能：



> 创建action_thread_pool对象。

  * 函数原型：


    
    
    action_thread_pool_t* action_thread_pool_create_ex (uint16_t max_thread_nr, uint16_t min_idle_nr, uint32_t stack_size, tk_thread_priority_t priority);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | action_thread_pool_t* | action_thread_pool对象。  
max_thread_nr | uint16_t | 最大线程数。  
min_idle_nr | uint16_t | 最小空闲线程数(必须大于0)。  
stack_size | uint32_t | 栈的大小。  
priority | tk_thread_priority_t | 优先级  
  
#### action_thread_pool_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t action_thread_pool_destroy (action_thread_pool_t* thread_pool);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread_pool | action_thread_pool_t* | action_thread_pool对象。  
  
#### action_thread_pool_exec 函数

* * *

  * 函数功能：



> 执行action。

  * 函数原型：


    
    
    ret_t action_thread_pool_exec (action_thread_pool_t* thread_pool, qaction_t* action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread_pool | action_thread_pool_t* | action_thread_pool对象。  
action | qaction_t* | action对象。  
  
#### max_thread_nr 属性

* * *

> 最大线程数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### min_idle_nr 属性

* * *

> 最小空闲线程数

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### priority 属性

* * *

> 线程池中的线程优先级

  * 类型：tk_thread_priority_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### stack_size 属性

* * *

> 线程池中的线程栈大小

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
