## tk_cond_var_t

### 概述

## 简化版的条件变量。

### 函数

函数名称 | 说明  
---|---  
tk_cond_var_awake | 唤醒。  
tk_cond_var_create | 创建cond_var。  
tk_cond_var_destroy | 销毁cond_var对象。  
tk_cond_var_wait | 等待。  
  
#### tk_cond_var_awake 函数

* * *

  * 函数功能：



> 唤醒。

  * 函数原型：


    
    
    ret_t tk_cond_var_awake (tk_cond_var_t* cond_var);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cond_var | tk_cond_var_t* | cond_var对象。  
  
#### tk_cond_var_create 函数

* * *

  * 函数功能：



> 创建cond_var。

  * 函数原型：


    
    
    tk_cond_var_t* tk_cond_var_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_cond_var_t* | cond_var对象。  
  
#### tk_cond_var_destroy 函数

* * *

  * 函数功能：



> 销毁cond_var对象。

  * 函数原型：


    
    
    ret_t tk_cond_var_destroy (tk_cond_var_t* cond_var);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cond_var | tk_cond_var_t* | cond_var对象。  
  
#### tk_cond_var_wait 函数

* * *

  * 函数功能：



> 等待。

  * 函数原型：


    
    
    ret_t tk_cond_var_wait (tk_cond_var_t* cond_var, uint32_t timeout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cond_var | tk_cond_var_t* | cond_var对象。  
timeout | uint32_t | 最长等待时间(毫秒)。
