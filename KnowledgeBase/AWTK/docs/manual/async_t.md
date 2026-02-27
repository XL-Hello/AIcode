## async_t

### 概述

## 在后台线程执行指定函数，不会阻塞UI线程。

### 函数

函数名称 | 说明  
---|---  
async_call | 异步执行exec函数，执行完成后，在后台线程调用on_result函数。  
async_call_deinit | 全局~初始化。  
async_call_init_ex | 全局初始化。  
async_call_init_ex2 | 全局初始化。  
  
#### async_call 函数

* * *

  * 函数功能：



> 异步执行exec函数，执行完成后，在后台线程调用on_result函数。

  * 函数原型：


    
    
    ret_t async_call (async_exec_t exec, async_on_result_t on_result, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
exec | async_exec_t | 需要异步支持的函数。  
on_result | async_on_result_t | 返回执行结果(可选)  
ctx | void* | 两个回调函数的上下文。  
  
#### async_call_deinit 函数

* * *

  * 函数功能：



> 全局~初始化。

  * 函数原型：


    
    
    ret_t async_call_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### async_call_init_ex 函数

* * *

  * 函数功能：



> 全局初始化。

  * 函数原型：


    
    
    ret_t async_call_init_ex (uint32_t max_threads, uint32_t min_threads);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
max_threads | uint32_t | 最大线程数。  
min_threads | uint32_t | 最小线程数(必须大于0)。  
  
#### async_call_init_ex2 函数

* * *

  * 函数功能：



> 全局初始化。

  * 函数原型：


    
    
    ret_t async_call_init_ex2 (uint32_t max_threads, uint32_t min_threads, uint32_t stack_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
max_threads | uint32_t | 最大线程数。  
min_threads | uint32_t | 最小线程数(必须大于0)。  
stack_size | uint32_t | 栈空间大小(字节)。
