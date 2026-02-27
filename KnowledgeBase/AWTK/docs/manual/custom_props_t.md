## custom_props_t

### 概述

widget自定义属性集合。

* * *

### 函数

函数名称 | 说明  
---|---  
custom_props_create | 创建custom_props对象  
custom_props_destroy | 销毁属性集合。  
custom_props_get | 获取属性的值。  
custom_props_set | 设置属性的值。  
  
#### custom_props_create 函数

* * *

  * 函数功能：



> 创建custom_props对象

  * 函数原型：


    
    
    custom_props_t* custom_props_create (uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | custom_props_t* | custom_props对象。  
capacity | uint32_t | 初始容量。  
  
#### custom_props_destroy 函数

* * *

  * 函数功能：



> 销毁属性集合。

  * 函数原型：


    
    
    ret_t custom_props_destroy (custom_props_t props);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
props | custom_props_t | 属性集合对象。  
  
#### custom_props_get 函数

* * *

  * 函数功能：



> 获取属性的值。

  * 函数原型：


    
    
    ret_t custom_props_get (custom_props_t props, char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
props | custom_props_t | 属性集合对象。  
name | char* | 属性的名称。  
v | value_t* | 用于返回属性的值。  
  
#### custom_props_set 函数

* * *

  * 函数功能：



> 设置属性的值。

  * 函数原型：


    
    
    ret_t custom_props_set (custom_props_t props, char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
props | custom_props_t | 属性集合对象。  
name | char* | 属性的名称。  
v | value_t* | 属性的值。
