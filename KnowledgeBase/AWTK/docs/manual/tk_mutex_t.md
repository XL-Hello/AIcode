## tk_mutex_t

### 概述

## 互斥锁。

### 函数

函数名称 | 说明  
---|---  
tk_mutex_create | 创建mutex。  
tk_mutex_destroy | 销毁mutex对象。  
tk_mutex_lock | 加锁。  
tk_mutex_try_lock | 尝试加锁。  
tk_mutex_unlock | 解锁。  
  
#### tk_mutex_create 函数

* * *

  * 函数功能：



> 创建mutex。

  * 函数原型：


    
    
    tk_mutex_t* tk_mutex_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_mutex_t* | mutex对象。  
  
#### tk_mutex_destroy 函数

* * *

  * 函数功能：



> 销毁mutex对象。

  * 函数原型：


    
    
    ret_t tk_mutex_destroy (tk_mutex_t* mutex);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex | tk_mutex_t* | mutex对象。  
  
#### tk_mutex_lock 函数

* * *

  * 函数功能：



> 加锁。

  * 函数原型：


    
    
    ret_t tk_mutex_lock (tk_mutex_t* mutex);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex | tk_mutex_t* | mutex对象。  
  
#### tk_mutex_try_lock 函数

* * *

  * 函数功能：



> 尝试加锁。

  * 函数原型：


    
    
    ret_t tk_mutex_try_lock (tk_mutex_t* mutex);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex | tk_mutex_t* | mutex对象。  
  
#### tk_mutex_unlock 函数

* * *

  * 函数功能：



> 解锁。

  * 函数原型：


    
    
    ret_t tk_mutex_unlock (tk_mutex_t* mutex);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex | tk_mutex_t* | mutex对象。
