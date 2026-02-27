## object_array_t

### 概述

![image](images/object_array_t_0.png)

简单的动态数组，内部存放value对象。

访问时属性名称为：

  * “size”/”length” 用于获取数组的长度。
  * index 用于访问属性，-1可以用来追加新元素。



* * *

### 函数

函数名称 | 说明  
---|---  
object_array_avg | 求平均值。  
object_array_cast | 转换为object_array对象。  
object_array_clear_props | 清除全部属性。  
object_array_clone | 克隆对象。  
object_array_create | 创建对象。  
object_array_create_with_str | 通过字符串构建数组。  
object_array_dup | 复制部分或全部元素。  
object_array_get | 获取指定序数的元素。  
object_array_get_and_remove | 在指定位置删除一个元素，并返回它。  
object_array_index_of | 查找元素出现的第一个位置。  
object_array_insert | 在指定位置插入一个元素。  
object_array_join | 使用分隔符把各个元素拼接起来。  
object_array_last_index_of | 查找元素出现的最后一个位置。  
object_array_max | 查找最大值。  
object_array_min | 查找最小值。  
object_array_pop | 弹出最后一个元素。  
object_array_push | 追加一个元素。  
object_array_remove | 在指定位置删除一个元素。  
object_array_remove_value | 删除指定的值。  
object_array_reverse | 反向。  
object_array_set | 设置指定序数的元素。  
object_array_shift | 弹出第一个元素。  
object_array_sort | 排序。  
object_array_sort_as_double | 按浮点数排序。  
object_array_sort_as_int | 按整数排序。  
object_array_sort_as_str | 按字符串排序。  
object_array_sum | 求和。  
object_array_unref | for script gc  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
capacity | uint32_t | 属性数组的容量。  
props | value_t* | 属性数组。  
size | uint32_t | 属性个数。  
  
#### object_array_avg 函数

* * *

  * 函数功能：



> 求平均值。

  * 函数原型：


    
    
    ret_t object_array_avg (tk_object_t* obj, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
result | value_t* | 结果。  
  
#### object_array_cast 函数

* * *

  * 函数功能：



> 转换为object_array对象。

  * 函数原型：


    
    
    object_array_t* object_array_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_array_t* | object_array对象。  
obj | tk_object_t* | object_array对象。  
  
#### object_array_clear_props 函数

* * *

  * 函数功能：



> 清除全部属性。

  * 函数原型：


    
    
    ret_t object_array_clear_props (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
  
#### object_array_clone 函数

* * *

  * 函数功能：



> 克隆对象。

  * 函数原型：


    
    
    tk_object_t* object_array_clone (tk_object_t* o);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
o | tk_object_t* | 被克隆的对象。  
  
#### object_array_create 函数

* * *

  * 函数功能：



> 创建对象。

  * 函数原型：


    
    
    tk_object_t* object_array_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
  
#### object_array_create_with_str 函数

* * *

  * 函数功能：



> 通过字符串构建数组。

  * 函数原型：


    
    
    tk_object_t* object_array_create_with_str (const char* str, const char* sep, value_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
str | const char* | 字符串  
sep | const char* | 分隔符。  
type | value_type_t | 类型。  
  
#### object_array_dup 函数

* * *

  * 函数功能：



> 复制部分或全部元素。

  * 函数原型：


    
    
    tk_object_t* object_array_dup (tk_object_t* obj, uint32_t start, uint32_t end);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
obj | tk_object_t* | 数组对象。  
start | uint32_t | 开始的位置。  
end | uint32_t | 结束的位置(不包含)。  
  
#### object_array_get 函数

* * *

  * 函数功能：



> 获取指定序数的元素。

  * 函数原型：


    
    
    ret_t object_array_get (tk_object_t* obj, uint32_t i, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
i | uint32_t | 序数。  
v | value_t* | 返回的元素。  
  
#### object_array_get_and_remove 函数

* * *

  * 函数功能：



> 在指定位置删除一个元素，并返回它。

  * 函数原型：


    
    
    ret_t object_array_get_and_remove (tk_object_t* obj, uint32_t index, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
index | uint32_t | 位置。  
v | value_t* | 用于返回值。  
  
#### object_array_index_of 函数

* * *

  * 函数功能：



> 查找元素出现的第一个位置。

  * 函数原型：


    
    
    int32_t object_array_index_of (tk_object_t* obj, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果找到返回其位置，否则返回-1。  
obj | tk_object_t* | 对象。  
v | const value_t* | 值。  
  
#### object_array_insert 函数

* * *

  * 函数功能：



> 在指定位置插入一个元素。

  * 函数原型：


    
    
    ret_t object_array_insert (tk_object_t* obj, uint32_t index, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
index | uint32_t | 位置。  
v | const value_t* | 值。  
  
#### object_array_join 函数

* * *

  * 函数功能：



> 使用分隔符把各个元素拼接起来。

  * 函数原型：


    
    
    ret_t object_array_join (tk_object_t* obj, const char* sep, str_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
sep | const char* | 分隔符。  
result | str_t* | 生成的字符串。  
  
#### object_array_last_index_of 函数

* * *

  * 函数功能：



> 查找元素出现的最后一个位置。

  * 函数原型：


    
    
    int32_t object_array_last_index_of (tk_object_t* obj, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果找到返回其位置，否则返回-1。  
obj | tk_object_t* | 对象。  
v | const value_t* | 值。  
  
#### object_array_max 函数

* * *

  * 函数功能：



> 查找最大值。

  * 函数原型：


    
    
    ret_t object_array_max (tk_object_t* obj, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
result | value_t* | 结果。  
  
#### object_array_min 函数

* * *

  * 函数功能：



> 查找最小值。

  * 函数原型：


    
    
    ret_t object_array_min (tk_object_t* obj, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
result | value_t* | 结果。  
  
#### object_array_pop 函数

* * *

  * 函数功能：



> 弹出最后一个元素。

  * 函数原型：


    
    
    ret_t object_array_pop (tk_object_t* obj, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
v | value_t* | 返回值。  
  
#### object_array_push 函数

* * *

  * 函数功能：



> 追加一个元素。

  * 函数原型：


    
    
    ret_t object_array_push (tk_object_t* obj, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
v | const value_t* | 值。  
  
#### object_array_remove 函数

* * *

  * 函数功能：



> 在指定位置删除一个元素。

  * 函数原型：


    
    
    ret_t object_array_remove (tk_object_t* obj, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
index | uint32_t | 位置。  
  
#### object_array_remove_value 函数

* * *

  * 函数功能：



> 删除指定的值。

  * 函数原型：


    
    
    ret_t object_array_remove_value (tk_object_t* obj, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
v | value_t* | 值。  
  
#### object_array_reverse 函数

* * *

  * 函数功能：



> 反向。

  * 函数原型：


    
    
    ret_t object_array_reverse (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
  
#### object_array_set 函数

* * *

  * 函数功能：



> 设置指定序数的元素。

  * 函数原型：


    
    
    ret_t object_array_set (tk_object_t* obj, uint32_t i, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
i | uint32_t | 序数。  
v | const value_t* | 元素。  
  
#### object_array_shift 函数

* * *

  * 函数功能：



> 弹出第一个元素。

  * 函数原型：


    
    
    ret_t object_array_shift (tk_object_t* obj, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
v | value_t* | 返回值。  
  
#### object_array_sort 函数

* * *

  * 函数功能：



> 排序。

  * 函数原型：


    
    
    ret_t object_array_sort (tk_object_t* obj, tk_compare_t cmp);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
cmp | tk_compare_t | 比较函数。  
  
#### object_array_sort_as_double 函数

* * *

  * 函数功能：



> 按浮点数排序。

  * 函数原型：


    
    
    ret_t object_array_sort_as_double (tk_object_t* obj, bool_t ascending);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
ascending | bool_t | 升序或降序。  
  
#### object_array_sort_as_int 函数

* * *

  * 函数功能：



> 按整数排序。

  * 函数原型：


    
    
    ret_t object_array_sort_as_int (tk_object_t* obj, bool_t ascending);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
ascending | bool_t | 升序或降序。  
  
#### object_array_sort_as_str 函数

* * *

  * 函数功能：



> 按字符串排序。

  * 函数原型：


    
    
    ret_t object_array_sort_as_str (tk_object_t* obj, bool_t ascending, bool_t ignore_case);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
ascending | bool_t | 升序或降序。  
ignore_case | bool_t | 是否忽略大小写。  
  
#### object_array_sum 函数

* * *

  * 函数功能：



> 求和。

  * 函数原型：


    
    
    ret_t object_array_sum (tk_object_t* obj, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 数组对象。  
result | value_t* | 结果。  
  
#### object_array_unref 函数

* * *

  * 函数功能：



> for script gc

  * 函数原型：


    
    
    ret_t object_array_unref (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
  
#### capacity 属性

* * *

> 属性数组的容量。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### props 属性

* * *

> 属性数组。

  * 类型：value_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 属性个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
