## tk_mutex_nest_t

### 概述

## 嵌套互斥锁。允许同一个线程多次加锁。

### 函数

函数名称 | 说明  
---|---  
tk_mutex_nest_create | 创建嵌套互斥锁。  
tk_mutex_nest_destroy | 销毁mutex_nest对象。  
tk_mutex_nest_lock | 加锁。  
tk_mutex_nest_try_lock | 尝试加锁。  
tk_mutex_nest_unlock | 解锁。只允许解锁当前线程所加的锁。  
  
#### tk_mutex_nest_create 函数

* * *

  * 函数功能：



> 创建嵌套互斥锁。

  * 函数原型：


    
    
    tk_mutex_nest_t* tk_mutex_nest_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_mutex_nest_t* | mutex_nest对象。  
  
#### tk_mutex_nest_destroy 函数

* * *

  * 函数功能：



> 销毁mutex_nest对象。

  * 函数原型：


    
    
    ret_t tk_mutex_nest_destroy (tk_mutex_nest_t* mutex_nest);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex_nest | tk_mutex_nest_t* | mutex_nest对象。  
  
#### tk_mutex_nest_lock 函数

* * *

  * 函数功能：



> 加锁。

  * 函数原型：


    
    
    ret_t tk_mutex_nest_lock (tk_mutex_nest_t* mutex_nest);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex_nest | tk_mutex_nest_t* | mutex_nest对象。  
  
#### tk_mutex_nest_try_lock 函数

* * *

  * 函数功能：



> 尝试加锁。

  * 函数原型：


    
    
    ret_t tk_mutex_nest_try_lock (tk_mutex_nest_t* mutex_nest);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex_nest | tk_mutex_nest_t* | mutex_nest对象。  
  
#### tk_mutex_nest_unlock 函数

* * *

  * 函数功能：



> 解锁。只允许解锁当前线程所加的锁。

  * 函数原型：


    
    
    ret_t tk_mutex_nest_unlock (tk_mutex_nest_t* mutex_nest);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mutex_nest | tk_mutex_nest_t* | mutex_nest对象。
