## tk_semaphore_t

### 概述

## 信号量。

### 函数

函数名称 | 说明  
---|---  
tk_semaphore_create | 创建信号量对象。  
tk_semaphore_destroy | 销毁信号量对象。  
tk_semaphore_post | 释放资源。  
tk_semaphore_wait | 获取资源。  
  
#### tk_semaphore_create 函数

* * *

  * 函数功能：



> 创建信号量对象。

  * 函数原型：


    
    
    tk_semaphore_t* tk_semaphore_create (uint32_t value, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_semaphore_t* | semaphore对象。  
value | uint32_t | 初始值。  
name | const char* | 名称。  
  
#### tk_semaphore_destroy 函数

* * *

  * 函数功能：



> 销毁信号量对象。

  * 函数原型：


    
    
    ret_t tk_semaphore_destroy (tk_semaphore_t* semaphore);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
semaphore | tk_semaphore_t* | 信号量对象。  
  
#### tk_semaphore_post 函数

* * *

  * 函数功能：



> 释放资源。

  * 函数原型：


    
    
    ret_t tk_semaphore_post (tk_semaphore_t* semaphore);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
semaphore | tk_semaphore_t* | 信号量对象。  
  
#### tk_semaphore_wait 函数

* * *

  * 函数功能：



> 获取资源。

  * 函数原型：


    
    
    ret_t tk_semaphore_wait (tk_semaphore_t* semaphore, uint32_t timeout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
semaphore | tk_semaphore_t* | 信号量对象。  
timeout | uint32_t | 超时时间(毫秒)。
