## typed_array_t

### 概述

带类型的动态数组，根据元素个数动态调整数组的容量。

示例：
    
    
    value_t v;
    typed_array_t* a = typed_array_create(VALUE_TYPE_INT, 10);
    typed_array_push(a, value_set_int(&v, 123));
    typed_array_push(a, value_set_int(&v, 234));
    ...
    typed_array_destroy(a);
    

* * *

### 函数

函数名称 | 说明  
---|---  
typed_array_clear | 清除全部元素。  
typed_array_create | 创建typed_array对象。  
typed_array_destroy | 销毁typed_array对象。  
typed_array_extend | 扩展typed_array到指定容量。  
typed_array_get | 获取指定序数的元素。  
typed_array_insert | 在指定序数插入元素。  
typed_array_pop | 弹出最后一个元素。  
typed_array_push | 在尾巴追加一个元素。  
typed_array_remove | 删除指定位置的元素。  
typed_array_set | 设置指定序数的元素。  
typed_array_tail | 返回最后一个元素。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
capacity | uint32_t | 数组的容量大小。  
data | uint8_t* | 数组中的元素。  
element_size | uint32_t | 单个元素的大小。  
size | uint32_t | 数组中元素的个数。  
type | value_type_t | 元素的类型。  
  
#### typed_array_clear 函数

* * *

  * 函数功能：



> 清除全部元素。

  * 函数原型：


    
    
    ret_t typed_array_clear (typed_array_t* typed_array);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
  
#### typed_array_create 函数

* * *

  * 函数功能：



> 创建typed_array对象。

  * 函数原型：


    
    
    typed_array_t* typed_array_create (value_type_t type, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | typed_array_t* | 数组对象。  
type | value_type_t | 元素的类型。  
capacity | uint32_t | 数组的初始容量(元素个数)。  
  
#### typed_array_destroy 函数

* * *

  * 函数功能：



> 销毁typed_array对象。

  * 函数原型：


    
    
    ret_t typed_array_destroy (typed_array_t* typed_array);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
  
#### typed_array_extend 函数

* * *

  * 函数功能：



> 扩展typed_array到指定容量。

  * 函数原型：


    
    
    ret_t typed_array_extend (typed_array_t* typed_array, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 元素的类型。  
capacity | uint32_t | 数组的容量(元素个数)。  
  
#### typed_array_get 函数

* * *

  * 函数功能：



> 获取指定序数的元素。

  * 函数原型：


    
    
    ret_t typed_array_get (typed_array_t* typed_array, uint32_t index, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
index | uint32_t | 序数。  
v | value_t* | 返回的元素。  
  
#### typed_array_insert 函数

* * *

  * 函数功能：



> 在指定序数插入元素。

  * 函数原型：


    
    
    ret_t typed_array_insert (typed_array_t* typed_array, uint32_t index, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
index | uint32_t | 序数。  
v | const value_t* | 元素。  
  
#### typed_array_pop 函数

* * *

  * 函数功能：



> 弹出最后一个元素。

  * 函数原型：


    
    
    ret_t typed_array_pop (typed_array_t* typed_array, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
v | value_t* | 弹出的元素。  
  
#### typed_array_push 函数

* * *

  * 函数功能：



> 在尾巴追加一个元素。

  * 函数原型：


    
    
    ret_t typed_array_push (typed_array_t* typed_array, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
v | const value_t* | 待追加的元素。  
  
#### typed_array_remove 函数

* * *

  * 函数功能：



> 删除指定位置的元素。

  * 函数原型：


    
    
    ret_t typed_array_remove (typed_array_t* typed_array, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
index | uint32_t | 位置序数。  
  
#### typed_array_set 函数

* * *

  * 函数功能：



> 设置指定序数的元素。

  * 函数原型：


    
    
    ret_t typed_array_set (typed_array_t* typed_array, uint32_t index, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
index | uint32_t | 序数。  
v | const value_t* | 元素。  
  
#### typed_array_tail 函数

* * *

  * 函数功能：



> 返回最后一个元素。

  * 函数原型：


    
    
    ret_t typed_array_tail (typed_array_t* typed_array, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
typed_array | typed_array_t* | 数组对象。  
v | value_t* | 返回的元素。  
  
#### capacity 属性

* * *

> 数组的容量大小。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### data 属性

* * *

> 数组中的元素。

  * 类型：uint8_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### element_size 属性

* * *

> 单个元素的大小。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 数组中元素的个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### type 属性

* * *

> 元素的类型。

  * 类型：value_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
