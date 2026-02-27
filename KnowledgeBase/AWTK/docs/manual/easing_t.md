## easing_t

### 概述

## 动画趋势类。

### 函数

函数名称 | 说明  
---|---  
easing_get | 获取对应类型的操作函数。  
easing_register | 注册指定名称的动画趋势。  
  
#### easing_get 函数

* * *

  * 函数功能：



> 获取对应类型的操作函数。

  * 函数原型：


    
    
    easing_func_t easing_get (easing_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | easing_func_t | 返回对应的操作函数地址。  
type | easing_type_t | 类型。  
  
#### easing_register 函数

* * *

  * 函数功能：



> 注册指定名称的动画趋势。

  * 函数原型：


    
    
    uint32_t easing_register (const char* type_name, easing_func_t easing_func);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回对应类型。  
type_name | const char* | 类型名称。  
easing_func | easing_func_t | 动画趋势函数。
