## object_typed_array_t

### 概述

![image](images/object_typed_array_t_0.png)

## 将typed_array包装成object。

### 函数

函数名称 | 说明  
---|---  
object_typed_array_cast | 转换为object_typed_array对象。  
object_typed_array_create | 创建对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
arr | typed_array_t* | typed array对象。  
  
#### object_typed_array_cast 函数

* * *

  * 函数功能：



> 转换为object_typed_array对象。

  * 函数原型：


    
    
    object_typed_array_t* object_typed_array_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_typed_array_t* | object_typed_array对象。  
obj | tk_object_t* | object_typed_array对象。  
  
#### object_typed_array_create 函数

* * *

  * 函数功能：



> 创建对象。

  * 函数原型：


    
    
    tk_object_t* object_typed_array_create (value_type_t type, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
type | value_type_t | 元素的类型。  
capacity | uint32_t | 数组的初始容量(元素个数)。  
  
#### arr 属性

* * *

> typed array对象。

  * 类型：typed_array_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
