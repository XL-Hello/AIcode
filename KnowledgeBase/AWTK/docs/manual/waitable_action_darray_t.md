## waitable_action_darray_t

### 概述

## waitable actionqueue

### 函数

函数名称 | 说明  
---|---  
waitable_action_darray_create | 创建waitable_action_darray对象。  
waitable_action_darray_destroy | 销毁。  
waitable_action_darray_find | 查找 qaction  
waitable_action_darray_find_ex | 查找 qaction  
waitable_action_darray_recv | 接收一个请求。  
waitable_action_darray_remove | 从 darray 中移除并销毁 qaction 对象  
waitable_action_darray_remove_ex | 从 darray 中移除并销毁 qaction 对象  
waitable_action_darray_replace | 替换 qaction，旧的 qaction 会被销毁  
waitable_action_darray_replace_ex | 替换 qaction  
waitable_action_darray_send | 发送一个请求。  
  
#### waitable_action_darray_create 函数

* * *

  * 函数功能：



> 创建waitable_action_darray对象。

  * 函数原型：


    
    
    waitable_action_darray_t* waitable_action_darray_create (uint16_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | waitable_action_darray_t* | waitable_action_darray对象。  
capacity | uint16_t | action的容量。  
  
#### waitable_action_darray_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t waitable_action_darray_destroy (waitable_action_darray_t* q);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
q | waitable_action_darray_t* | waitable_action_darray对象。  
  
#### waitable_action_darray_find 函数

* * *

  * 函数功能：



> 查找 qaction

  * 函数原型：


    
    
    qaction_t* waitable_action_darray_find (waitable_action_darray_t* q, qaction_exec_t exec);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | qaction_t* | 返回 qaction_t对象  
q | waitable_action_darray_t* | waitable_action_darray对象。  
exec | qaction_exec_t | action 中的函数回调  
  
#### waitable_action_darray_find_ex 函数

* * *

  * 函数功能：



> 查找 qaction

  * 函数原型：


    
    
    qaction_t* waitable_action_darray_find_ex (waitable_action_darray_t* q, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | qaction_t* | 返回 qaction_t对象  
q | waitable_action_darray_t* | waitable_action_darray对象。  
cmp | tk_compare_t | 比较函数  
ctx | void* | 比较函数参数  
  
#### waitable_action_darray_recv 函数

* * *

  * 函数功能：



> 接收一个请求。

  * 函数原型：


    
    
    ret_t waitable_action_darray_recv (waitable_action_darray_t* q, qaction_t** action, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
q | waitable_action_darray_t* | waitable_action_darray对象。  
action | qaction_t** | 用于返回action对象。  
timeout_ms | uint32_t | 超时时间(毫秒)  
  
#### waitable_action_darray_remove 函数

* * *

  * 函数功能：



> 从 darray 中移除并销毁 qaction 对象

  * 函数原型：


    
    
    ret_t waitable_action_darray_remove (waitable_action_darray_t* q, qaction_exec_t exec);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t值  
q | waitable_action_darray_t* | waitable_action_darray对象。  
exec | qaction_exec_t | action 中的函数回调  
  
#### waitable_action_darray_remove_ex 函数

* * *

  * 函数功能：



> 从 darray 中移除并销毁 qaction 对象

  * 函数原型：


    
    
    ret_t waitable_action_darray_remove_ex (waitable_action_darray_t* q, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t值  
q | waitable_action_darray_t* | waitable_action_darray对象。  
cmp | tk_compare_t | 比较函数  
ctx | void* | 比较函数参数  
  
#### waitable_action_darray_replace 函数

* * *

  * 函数功能：



> 替换 qaction，旧的 qaction 会被销毁

  * 函数原型：


    
    
    ret_t waitable_action_darray_replace (waitable_action_darray_t* q, qaction_t* new_action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t值  
q | waitable_action_darray_t* | waitable_action_darray对象。  
new_action | qaction_t* | 新的 action 对象  
  
#### waitable_action_darray_replace_ex 函数

* * *

  * 函数功能：



> 替换 qaction

  * 函数原型：


    
    
    ret_t waitable_action_darray_replace_ex (waitable_action_darray_t* q, qaction_exec_t exec, qaction_t* new_action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t值  
q | waitable_action_darray_t* | waitable_action_darray对象。  
exec | qaction_exec_t | 旧 action 中的函数回调  
new_action | qaction_t* | 新的 action 对象  
  
#### waitable_action_darray_send 函数

* * *

  * 函数功能：



> 发送一个请求。

  * 函数原型：


    
    
    ret_t waitable_action_darray_send (waitable_action_darray_t* q, qaction_t* action, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
q | waitable_action_darray_t* | waitable_action_darray对象。  
action | qaction_t* | action对象。  
timeout_ms | uint32_t | 超时时间(毫秒)
