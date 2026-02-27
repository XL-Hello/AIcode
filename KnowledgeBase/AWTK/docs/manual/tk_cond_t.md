## tk_cond_t

### 概述

## 条件变量。

### 函数

函数名称 | 说明  
---|---  
tk_cond_create | 创建cond。  
tk_cond_destroy | 销毁cond对象。  
tk_cond_signal | 唤醒。  
tk_cond_wait | 等待。  
tk_cond_wait_timeout | 等待指定时间(毫秒)。  
  
#### tk_cond_create 函数

* * *

  * 函数功能：



> 创建cond。

  * 函数原型：


    
    
    tk_cond_t* tk_cond_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_cond_t* | cond对象。  
  
#### tk_cond_destroy 函数

* * *

  * 函数功能：



> 销毁cond对象。

  * 函数原型：


    
    
    ret_t tk_cond_destroy (tk_cond_t* cond);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cond | tk_cond_t* | cond对象。  
  
#### tk_cond_signal 函数

* * *

  * 函数功能：



> 唤醒。

  * 函数原型：


    
    
    ret_t tk_cond_signal (tk_cond_t* cond);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cond | tk_cond_t* | cond对象。  
  
#### tk_cond_wait 函数

* * *

  * 函数功能：



> 等待。

  * 函数原型：


    
    
    ret_t tk_cond_wait (tk_cond_t* cond, tk_mutex_t* mutex);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cond | tk_cond_t* | cond对象。  
mutex | tk_mutex_t* | mutex对象。  
  
#### tk_cond_wait_timeout 函数

* * *

  * 函数功能：



> 等待指定时间(毫秒)。

  * 函数原型：


    
    
    ret_t tk_cond_wait_timeout (tk_cond_t* cond, tk_mutex_t* mutex, uint32_t timeout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cond | tk_cond_t* | cond对象。  
mutex | tk_mutex_t* | mutex对象。  
timeout | uint32_t | 最长等待时间(毫秒)。
