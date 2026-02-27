## tk_thread_t

### 概述

## 线程对象。

### 函数

函数名称 | 说明  
---|---  
tk_thread_create | 创建thread对象。  
tk_thread_destroy | 销毁thread对象。  
tk_thread_get_args | 获取线程的参数。  
tk_thread_get_priority_from_platform | 获取平台相关的优先级  
tk_thread_join | 等待线程退出。  
tk_thread_self | 获取当前线程的原生句柄。  
tk_thread_set_name | 设置线程的名称。  
tk_thread_set_priority | 设置线程的优先级。  
tk_thread_set_stack_size | 设置线程的栈大小。  
tk_thread_start | 启动线程。  
  
#### tk_thread_create 函数

* * *

  * 函数功能：



> 创建thread对象。

  * 函数原型：


    
    
    tk_thread_t* tk_thread_create (tk_thread_entry_t entry, void* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_thread_t* | thread对象。  
entry | tk_thread_entry_t | 线程函数。  
args | void* | 线程函数的上下文。  
  
#### tk_thread_destroy 函数

* * *

  * 函数功能：



> 销毁thread对象。 在销毁对象前必须调用 tk_thread_join 函数等待退出线程

  * 函数原型：


    
    
    ret_t tk_thread_destroy (tk_thread_t* thread);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | tk_thread_t* | thread对象。  
  
#### tk_thread_get_args 函数

* * *

  * 函数功能：



> 获取线程的参数。

  * 函数原型：


    
    
    void* tk_thread_get_args (tk_thread_t* thread);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回线程的参数。  
thread | tk_thread_t* | thread对象。  
  
#### tk_thread_get_priority_from_platform 函数

* * *

  * 函数功能：



> 获取平台相关的优先级
> 
> 部分平台支持。 根据 AWTK 通用优先级枚举获取平台相关的优先级

  * 函数原型：


    
    
    int32_t tk_thread_get_priority_from_platform (tk_thread_priority_t priority);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回平台相关的优先级。  
priority | tk_thread_priority_t | 优先级。  
  
#### tk_thread_join 函数

* * *

  * 函数功能：



> 等待线程退出。 必须调用 tk_thread_destroy 函数来释放线程资源，以免出现内存泄漏的问题。

  * 函数原型：


    
    
    ret_t tk_thread_join (tk_thread_t* thread);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | tk_thread_t* | thread对象。  
  
#### tk_thread_self 函数

* * *

  * 函数功能：



> 获取当前线程的原生句柄。

  * 函数原型：


    
    
    uint64_t tk_thread_self ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回当前线程的原生句柄。  
  
#### tk_thread_set_name 函数

* * *

  * 函数功能：



> 设置线程的名称。
> 
> 需要在调用start之前调用本函数。

  * 函数原型：


    
    
    ret_t tk_thread_set_name (tk_thread_t* thread, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | tk_thread_t* | thread对象。  
name | const char* | 名称。  
  
#### tk_thread_set_priority 函数

* * *

  * 函数功能：



> 设置线程的优先级。
> 
> 部分平台支持。

  * 函数原型：


    
    
    ret_t tk_thread_set_priority (tk_thread_t* thread, tk_thread_priority_t priority);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | tk_thread_t* | thread对象。  
priority | tk_thread_priority_t | 优先级。  
  
#### tk_thread_set_stack_size 函数

* * *

  * 函数功能：



> 设置线程的栈大小。
> 
> 需要在调用start之前调用本函数。

  * 函数原型：


    
    
    ret_t tk_thread_set_stack_size (tk_thread_t* thread, uint32_t stack_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | tk_thread_t* | thread对象。  
stack_size | uint32_t | 栈的大小。  
  
#### tk_thread_start 函数

* * *

  * 函数功能：



> 启动线程。

  * 函数原型：


    
    
    ret_t tk_thread_start (tk_thread_t* thread);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
thread | tk_thread_t* | thread对象。
