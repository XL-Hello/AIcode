## value_t

### 概述

一个通用数据类型，用来存放整数、浮点数、字符串和其它对象。

在C/C++中，一般不需动态创建对象，直接声明并初始化即可。如：
    
    
    value_t v;
    value_set_int(&v, 100);
    

## > 在脚本语言中，需要动态创建对象。

### 函数

函数名称 | 说明  
---|---  
value_abs | 将v取绝对值，并放入result对象。  
value_add | 将v和other求和，并放入result对象。  
value_binary_data | 获取为binary_data的值。  
value_bit_and | 将v和other按位取与，并放入result对象。  
value_bit_not | 将v按位取反，并放入result对象。  
value_bit_or | 将v和other按位取或，并放入result对象。  
value_bit_xor | 将v和other按位取异或，并放入result对象。  
value_bitmap | 获取类型为位图对象。  
value_bool | 获取类型为bool的值。  
value_cast | 转换为value对象。  
value_copy | 拷贝value的值。  
value_create | 创建value对象。  
value_deep_copy | 深拷贝value的值。  
value_destroy | 销毁value对象。  
value_div | 将v和other求商，并放入result对象。  
value_double | 获取类型为double的值。  
value_dup_binary_data | 设置类型为binary_data的值(复制数据)。  
value_dup_str | 设置类型为字符串的值(并拷贝字符串)。  
value_dup_str_with_len | 设置类型为字符串的值(并拷贝字符串)。  
value_dup_wstr | 设置类型为宽字符串的值(并拷贝宽字符串)。  
value_equal | 判断两个value是否相同。  
value_expt | 计算v的other次幂，并放入result对象。  
value_float | 获取类型为float_t的值。  
value_float32 | 获取类型为float的值。  
value_func | 获取类型为func的值。  
value_func_def | 获取类型为func_def的值。  
value_get_bit | 将v指定的位数取出，并放入result对象。  
value_gradient | 获取为gradient的值。  
value_id | 获取类型为ID的值。  
value_int | 转换为int的值。  
value_int16 | 获取类型为int16的值。  
value_int32 | 获取类型为int32的值。  
value_int64 | 获取类型为int64的值。  
value_int8 | 获取类型为int8的值。  
value_is_null | 判断value是否为空值。  
value_lshift | 将v左移指定的位数，并将结果放入result对象。  
value_lshift_r | 将v循环左移指定的位数，并将结果放入result对象。  
value_max | 从数组中选择最大值，并放入result对象。  
value_min | 从数组中选择最小值，并放入result对象。  
value_mod | 将v和other求模，并放入result对象。  
value_mul | 将v和other求积，并放入result对象。  
value_object | 转换为object的值。  
value_pointer | 获取类型为pointer的值。  
value_rect | 获取类型为矩形区域数据。  
value_reset | 重置value对象。  
value_rshift | 将v右移指定的位数，并将结果放入result对象。  
value_rshift_r | 将v循环右移指定的位数，并将结果放入result对象。  
value_set_binary_data | 设置类型为binary_data的值。  
value_set_bit | 将v指定的位数设置为bit，并放入result对象。  
value_set_bitmap | 设置类型为位图对象。  
value_set_bool | 设置类型为bool的值。  
value_set_double | 设置类型为double的值。  
value_set_float | 设置类型为float_t的值。  
value_set_float32 | 设置类型为float的值。  
value_set_func | 设置类型为func的值。  
value_set_func_def | 设置类型为func_def的值。  
value_set_gradient | 设置类型为gradient的值。  
value_set_id | 设置类型为ID的值。  
value_set_int | 设置类型为int的值。  
value_set_int16 | 设置类型为int16的值。  
value_set_int32 | 设置类型为int32的值。  
value_set_int64 | 设置类型为int64的值。  
value_set_int8 | 设置类型为int8的值。  
value_set_object | 设置类型为object的值。  
value_set_pointer | 设置类型为pointer的值。  
value_set_pointer_ex | 设置类型为pointer的值。  
value_set_rect | 设置类型为矩形区域数据。  
value_set_sized_str | 设置类型为带长度的字符串的值。  
value_set_str | 设置类型为字符串的值。  
value_set_token | 设置类型为token的值。  
value_set_ubjson | 设置类型为ubjson的值。  
value_set_uint16 | 设置类型为uint16的值。  
value_set_uint32 | 设置类型为uint32的值。  
value_set_uint64 | 设置类型为uint64的值。  
value_set_uint8 | 设置类型为uint8的值。  
value_set_wstr | 设置类型为宽字符串的值。  
value_sized_str | 获取为sized_str的值。  
value_str | 获取类型为字符串的值。  
value_str_ex | 获取类型为字符串的值。  
value_sub | 将v和other求差，并放入result对象。  
value_toggle_bit | 将v指定的位数取反，并将结果放入result对象。  
value_token | 获取token的值。  
value_type_name | 获取指定类型数据的名称。  
value_type_size | 获取指定类型数据大小。  
value_ubjson | 获取为ubjson的值。  
value_uint16 | 获取类型为uint16的值。  
value_uint32 | 获取类型为uint32的值。  
value_uint64 | 获取类型为uint64的值。  
value_uint8 | 获取类型为uint8的值。  
value_wstr | 获取类型为宽字符串的值。  
  
#### value_abs 函数

* * *

  * 函数功能：



> 将v取绝对值，并放入result对象。

  * 函数原型：


    
    
    ret_t value_abs (value_t* v, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是数值类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_add 函数

* * *

  * 函数功能：



> 将v和other求和，并放入result对象。

  * 函数原型：


    
    
    ret_t value_add (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是数值类型)。  
other | value_t* | value对象(必须是数值类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_binary_data 函数

* * *

  * 函数功能：



> 获取为binary_data的值。

  * 函数原型：


    
    
    binary_data_t* value_binary_data (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | binary_data_t* | 值。  
v | const value_t* | value对象。  
  
#### value_bit_and 函数

* * *

  * 函数功能：



> 将v和other按位取与，并放入result对象。

  * 函数原型：


    
    
    ret_t value_bit_and (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
other | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_bit_not 函数

* * *

  * 函数功能：



> 将v按位取反，并放入result对象。

  * 函数原型：


    
    
    ret_t value_bit_not (value_t* v, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_bit_or 函数

* * *

  * 函数功能：



> 将v和other按位取或，并放入result对象。

  * 函数原型：


    
    
    ret_t value_bit_or (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
other | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_bit_xor 函数

* * *

  * 函数功能：



> 将v和other按位取异或，并放入result对象。

  * 函数原型：


    
    
    ret_t value_bit_xor (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
other | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_bitmap 函数

* * *

  * 函数功能：



> 获取类型为位图对象。

  * 函数原型：


    
    
    void* value_bitmap (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 位图对象。  
v | const value_t* | value对象。  
  
#### value_bool 函数

* * *

  * 函数功能：



> 获取类型为bool的值。

  * 函数原型：


    
    
    bool_t value_bool (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 值。  
v | const value_t* | value对象。  
  
#### value_cast 函数

* * *

  * 函数功能：



> 转换为value对象。
> 
> 供脚本语言使用

  * 函数原型：


    
    
    value_t* value_cast (value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | 对象。  
value | value_t* | value对象。  
  
#### value_copy 函数

* * *

  * 函数功能：



> 拷贝value的值。

  * 函数原型：


    
    
    ret_t value_copy (value_t* dst, const value_t* src);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dst | value_t* | 目的value对象。  
src | const value_t* | 源value对象。  
  
#### value_create 函数

* * *

  * 函数功能：



> 创建value对象。

  * 函数原型：


    
    
    value_t* value_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | 对象。  
  
#### value_deep_copy 函数

* * *

  * 函数功能：



> 深拷贝value的值。 dst使用完成后，要调用value_reset，确保不会发生内存泄漏。

  * 函数原型：


    
    
    ret_t value_deep_copy (value_t* dst, const value_t* src);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dst | value_t* | 目的value对象。  
src | const value_t* | 源value对象。  
  
#### value_destroy 函数

* * *

  * 函数功能：



> 销毁value对象。

  * 函数原型：


    
    
    ret_t value_destroy (value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象。  
  
#### value_div 函数

* * *

  * 函数功能：



> 将v和other求商，并放入result对象。

  * 函数原型：


    
    
    ret_t value_div (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是数值类型)。  
other | value_t* | value对象(必须是数值类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_double 函数

* * *

  * 函数功能：



> 获取类型为double的值。

  * 函数原型：


    
    
    double value_double (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 值。  
v | const value_t* | value对象。  
  
#### value_dup_binary_data 函数

* * *

  * 函数功能：



> 设置类型为binary_data的值(复制数据)。

  * 函数原型：


    
    
    value_t* value_dup_binary_data (value_t* v, const void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
data | const void* | 待设置的值。  
size | uint32_t | 长度。  
  
#### value_dup_str 函数

* * *

  * 函数功能：



> 设置类型为字符串的值(并拷贝字符串)。

  * 函数原型：


    
    
    value_t* value_dup_str (value_t* v, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | const char* | 待设置的值。  
  
#### value_dup_str_with_len 函数

* * *

  * 函数功能：



> 设置类型为字符串的值(并拷贝字符串)。

  * 函数原型：


    
    
    value_t* value_dup_str_with_len (value_t* v, const char* value, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | const char* | 待设置的值。  
len | uint32_t | 长度。  
  
#### value_dup_wstr 函数

* * *

  * 函数功能：



> 设置类型为宽字符串的值(并拷贝宽字符串)。

  * 函数原型：


    
    
    value_t* value_dup_wstr (value_t* v, const wchar_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | const wchar_t* | 待设置的值。  
  
#### value_equal 函数

* * *

  * 函数功能：



> 判断两个value是否相同。

  * 函数原型：


    
    
    bool_t value_equal (const value_t* value, const value_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 为空值返回TRUE，否则返回FALSE。  
value | const value_t* | value对象。  
other | const value_t* | value对象。  
  
#### value_expt 函数

* * *

  * 函数功能：



> 计算v的other次幂，并放入result对象。

  * 函数原型：


    
    
    ret_t value_expt (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是数值类型)。  
other | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_float 函数

* * *

  * 函数功能：



> 获取类型为float_t的值。

  * 函数原型：


    
    
    float_t value_float (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 值。  
v | const value_t* | value对象。  
  
#### value_float32 函数

* * *

  * 函数功能：



> 获取类型为float的值。

  * 函数原型：


    
    
    float value_float32 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 值。  
v | const value_t* | value对象。  
  
#### value_func 函数

* * *

  * 函数功能：



> 获取类型为func的值。

  * 函数原型：


    
    
    void* value_func (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 值。  
v | const value_t* | value对象。  
  
#### value_func_def 函数

* * *

  * 函数功能：



> 获取类型为func_def的值。

  * 函数原型：


    
    
    void* value_func_def (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 值。  
v | const value_t* | value对象。  
  
#### value_get_bit 函数

* * *

  * 函数功能：



> 将v指定的位数取出，并放入result对象。

  * 函数原型：


    
    
    ret_t value_get_bit (value_t* v, value_t* result, uint32_t n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
n | uint32_t | 位数。  
  
#### value_gradient 函数

* * *

  * 函数功能：



> 获取为gradient的值。

  * 函数原型：


    
    
    binary_data_t* value_gradient (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | binary_data_t* | 值。  
v | const value_t* | value对象。  
  
#### value_id 函数

* * *

  * 函数功能：



> 获取类型为ID的值。

  * 函数原型：


    
    
    const char* value_id (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 值。  
v | const value_t* | value对象。  
  
#### value_int 函数

* * *

  * 函数功能：



> 转换为int的值。

  * 函数原型：


    
    
    int value_int (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 值。  
v | const value_t* | value对象。  
  
#### value_int16 函数

* * *

  * 函数功能：



> 获取类型为int16的值。

  * 函数原型：


    
    
    int16_t value_int16 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int16_t | 值。  
v | const value_t* | value对象。  
  
#### value_int32 函数

* * *

  * 函数功能：



> 获取类型为int32的值。

  * 函数原型：


    
    
    int32_t value_int32 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 值。  
v | const value_t* | value对象。  
  
#### value_int64 函数

* * *

  * 函数功能：



> 获取类型为int64的值。

  * 函数原型：


    
    
    int64_t value_int64 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 值。  
v | const value_t* | value对象。  
  
#### value_int8 函数

* * *

  * 函数功能：



> 获取类型为int8的值。

  * 函数原型：


    
    
    int8_t value_int8 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int8_t | 值。  
v | const value_t* | value对象。  
  
#### value_is_null 函数

* * *

  * 函数功能：



> 判断value是否为空值。

  * 函数原型：


    
    
    bool_t value_is_null (value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 为空值返回TRUE，否则返回FALSE。  
value | value_t* | value对象。  
  
#### value_lshift 函数

* * *

  * 函数功能：



> 将v左移指定的位数，并将结果放入result对象。

  * 函数原型：


    
    
    ret_t value_lshift (value_t* v, value_t* result, uint32_t n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
n | uint32_t | 位数。  
  
#### value_lshift_r 函数

* * *

  * 函数功能：



> 将v循环左移指定的位数，并将结果放入result对象。

  * 函数原型：


    
    
    ret_t value_lshift_r (value_t* v, value_t* result, uint32_t n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
n | uint32_t | 位数。  
  
#### value_max 函数

* * *

  * 函数功能：



> 从数组中选择最大值，并放入result对象。

  * 函数原型：


    
    
    ret_t value_max (value_t* arr, uint32_t size, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
arr | value_t* | 数组。  
size | uint32_t | 数组元素个数  
result | value_t* | 返回结果的value对象。  
  
#### value_min 函数

* * *

  * 函数功能：



> 从数组中选择最小值，并放入result对象。

  * 函数原型：


    
    
    ret_t value_min (value_t* arr, uint32_t size, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
arr | value_t* | 数组。  
size | uint32_t | 数组元素个数  
result | value_t* | 返回结果的value对象。  
  
#### value_mod 函数

* * *

  * 函数功能：



> 将v和other求模，并放入result对象。

  * 函数原型：


    
    
    ret_t value_mod (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
other | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_mul 函数

* * *

  * 函数功能：



> 将v和other求积，并放入result对象。

  * 函数原型：


    
    
    ret_t value_mul (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是数值类型)。  
other | value_t* | value对象(必须是数值类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_object 函数

* * *

  * 函数功能：



> 转换为object的值。

  * 函数原型：


    
    
    tk_object_t* value_object (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 值。  
v | const value_t* | value对象。  
  
#### value_pointer 函数

* * *

  * 函数功能：



> 获取类型为pointer的值。

  * 函数原型：


    
    
    void* value_pointer (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 值。  
v | const value_t* | value对象。  
  
#### value_rect 函数

* * *

  * 函数功能：



> 获取类型为矩形区域数据。

  * 函数原型：


    
    
    rect_t* value_rect (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t* | 返回矩形区域数据。  
v | const value_t* | value对象。  
  
#### value_reset 函数

* * *

  * 函数功能：



> 重置value对象。

  * 函数原型：


    
    
    ret_t value_reset (value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象。  
  
#### value_rshift 函数

* * *

  * 函数功能：



> 将v右移指定的位数，并将结果放入result对象。

  * 函数原型：


    
    
    ret_t value_rshift (value_t* v, value_t* result, uint32_t n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
n | uint32_t | 位数。  
  
#### value_rshift_r 函数

* * *

  * 函数功能：



> 将v循环右移指定的位数，并将结果放入result对象。

  * 函数原型：


    
    
    ret_t value_rshift_r (value_t* v, value_t* result, uint32_t n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
n | uint32_t | 位数。  
  
#### value_set_binary_data 函数

* * *

  * 函数功能：



> 设置类型为binary_data的值。

  * 函数原型：


    
    
    value_t* value_set_binary_data (value_t* v, void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
data | void* | 待设置的值。  
size | uint32_t | 长度。  
  
#### value_set_bit 函数

* * *

  * 函数功能：



> 将v指定的位数设置为bit，并放入result对象。

  * 函数原型：


    
    
    ret_t value_set_bit (value_t* v, value_t* result, uint32_t n, bool_t bit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
n | uint32_t | 位数。  
bit | bool_t | 值。  
  
#### value_set_bitmap 函数

* * *

  * 函数功能：



> 设置类型为位图对象。

  * 函数原型：


    
    
    value_t* value_set_bitmap (value_t* v, void* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
bitmap | void* | 待设置的值。  
  
#### value_set_bool 函数

* * *

  * 函数功能：



> 设置类型为bool的值。

  * 函数原型：


    
    
    value_t* value_set_bool (value_t* v, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | bool_t | 待设置的值。  
  
#### value_set_double 函数

* * *

  * 函数功能：



> 设置类型为double的值。

  * 函数原型：


    
    
    value_t* value_set_double (value_t* v, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | double | 待设置的值。  
  
#### value_set_float 函数

* * *

  * 函数功能：



> 设置类型为float_t的值。

  * 函数原型：


    
    
    value_t* value_set_float (value_t* v, float_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | float_t | 待设置的值。  
  
#### value_set_float32 函数

* * *

  * 函数功能：



> 设置类型为float的值。

  * 函数原型：


    
    
    value_t* value_set_float32 (value_t* v, float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | float | 待设置的值。  
  
#### value_set_func 函数

* * *

  * 函数功能：



> 设置类型为func的值。

  * 函数原型：


    
    
    value_t* value_set_func (value_t* v, void* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | void* | 待设置的值。  
  
#### value_set_func_def 函数

* * *

  * 函数功能：



> 设置类型为func_def的值。

  * 函数原型：


    
    
    value_t* value_set_func_def (value_t* v, void* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | void* | 待设置的值。  
  
#### value_set_gradient 函数

* * *

  * 函数功能：



> 设置类型为gradient的值。

  * 函数原型：


    
    
    value_t* value_set_gradient (value_t* v, void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
data | void* | 待设置的值。  
size | uint32_t | 长度。  
  
#### value_set_id 函数

* * *

  * 函数功能：



> 设置类型为ID的值。

  * 函数原型：


    
    
    value_t* value_set_id (value_t* v, const char* value, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | const char* | 待设置的值。  
len | uint32_t | 长度。  
  
#### value_set_int 函数

* * *

  * 函数功能：



> 设置类型为int的值。

  * 函数原型：


    
    
    value_t* value_set_int (value_t* v, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | int32_t | 待设置的值。  
  
#### value_set_int16 函数

* * *

  * 函数功能：



> 设置类型为int16的值。

  * 函数原型：


    
    
    value_t* value_set_int16 (value_t* v, int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | int16_t | 待设置的值。  
  
#### value_set_int32 函数

* * *

  * 函数功能：



> 设置类型为int32的值。

  * 函数原型：


    
    
    value_t* value_set_int32 (value_t* v, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | int32_t | 待设置的值。  
  
#### value_set_int64 函数

* * *

  * 函数功能：



> 设置类型为int64的值。

  * 函数原型：


    
    
    value_t* value_set_int64 (value_t* v, int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | int64_t | 待设置的值。  
  
#### value_set_int8 函数

* * *

  * 函数功能：



> 设置类型为int8的值。

  * 函数原型：


    
    
    value_t* value_set_int8 (value_t* v, int8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | int8_t | 待设置的值。  
  
#### value_set_object 函数

* * *

  * 函数功能：



> 设置类型为object的值。

  * 函数原型：


    
    
    value_t* value_set_object (value_t* v, tk_object_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | tk_object_t* | 待设置的值。  
  
#### value_set_pointer 函数

* * *

  * 函数功能：



> 设置类型为pointer的值。

  * 函数原型：


    
    
    value_t* value_set_pointer (value_t* v, void* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | void* | 待设置的值。  
  
#### value_set_pointer_ex 函数

* * *

  * 函数功能：



> 设置类型为pointer的值。

  * 函数原型：


    
    
    value_t* value_set_pointer_ex (value_t* v, void* value, tk_destroy_t destroy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | void* | 待设置的值。  
destroy | tk_destroy_t | 销毁函数。  
  
#### value_set_rect 函数

* * *

  * 函数功能：



> 设置类型为矩形区域数据。

  * 函数原型：


    
    
    value_t* value_set_rect (value_t* v, rect_t r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
r | rect_t | 待设置的值。  
  
#### value_set_sized_str 函数

* * *

  * 函数功能：



> 设置类型为带长度的字符串的值。

  * 函数原型：


    
    
    value_t* value_set_sized_str (value_t* v, char* str, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
str | char* | 待设置的值。  
size | uint32_t | 长度。  
  
#### value_set_str 函数

* * *

  * 函数功能：



> 设置类型为字符串的值。

  * 函数原型：


    
    
    value_t* value_set_str (value_t* v, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | const char* | 待设置的值。  
  
#### value_set_token 函数

* * *

  * 函数功能：



> 设置类型为token的值。

  * 函数原型：


    
    
    value_t* value_set_token (value_t* v, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | uint32_t | 待设置的值。  
  
#### value_set_ubjson 函数

* * *

  * 函数功能：



> 设置类型为ubjson的值。

  * 函数原型：


    
    
    value_t* value_set_ubjson (value_t* v, void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
data | void* | 待设置的值。  
size | uint32_t | 长度。  
  
#### value_set_uint16 函数

* * *

  * 函数功能：



> 设置类型为uint16的值。

  * 函数原型：


    
    
    value_t* value_set_uint16 (value_t* v, uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | uint16_t | 待设置的值。  
  
#### value_set_uint32 函数

* * *

  * 函数功能：



> 设置类型为uint32的值。

  * 函数原型：


    
    
    value_t* value_set_uint32 (value_t* v, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | uint32_t | 待设置的值。  
  
#### value_set_uint64 函数

* * *

  * 函数功能：



> 设置类型为uint64的值。

  * 函数原型：


    
    
    value_t* value_set_uint64 (value_t* v, uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | uint64_t | 待设置的值。  
  
#### value_set_uint8 函数

* * *

  * 函数功能：



> 设置类型为uint8的值。

  * 函数原型：


    
    
    value_t* value_set_uint8 (value_t* v, uint8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | uint8_t | 待设置的值。  
  
#### value_set_wstr 函数

* * *

  * 函数功能：



> 设置类型为宽字符串的值。

  * 函数原型：


    
    
    value_t* value_set_wstr (value_t* v, const wchar_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | value对象本身。  
v | value_t* | value对象。  
value | const wchar_t* | 待设置的值。  
  
#### value_sized_str 函数

* * *

  * 函数功能：



> 获取为sized_str的值。

  * 函数原型：


    
    
    sized_str_t* value_sized_str (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | sized_str_t* | 值。  
v | const value_t* | value对象。  
  
#### value_str 函数

* * *

  * 函数功能：



> 获取类型为字符串的值。

  * 函数原型：


    
    
    const char* value_str (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 值。  
v | const value_t* | value对象。  
  
#### value_str_ex 函数

* * *

  * 函数功能：



> 获取类型为字符串的值。

  * 函数原型：


    
    
    const char* value_str_ex (const value_t* v, char* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 值。  
v | const value_t* | value对象。  
buff | char* | 用于格式转换的缓冲区（如果 v 对象为 string 类型的话，不会把字符串数据拷贝到 buff 中）。  
size | uint32_t | 缓冲区大小。  
  
#### value_sub 函数

* * *

  * 函数功能：



> 将v和other求差，并放入result对象。

  * 函数原型：


    
    
    ret_t value_sub (value_t* v, value_t* other, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是数值类型)。  
other | value_t* | value对象(必须是数值类型)。  
result | value_t* | 返回结果的value对象。  
  
#### value_toggle_bit 函数

* * *

  * 函数功能：



> 将v指定的位数取反，并将结果放入result对象。

  * 函数原型：


    
    
    ret_t value_toggle_bit (value_t* v, value_t* result, uint32_t n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | value_t* | value对象(必须是整数类型)。  
result | value_t* | 返回结果的value对象。  
n | uint32_t | 位数。  
  
#### value_token 函数

* * *

  * 函数功能：



> 获取token的值。

  * 函数原型：


    
    
    uint32_t value_token (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 值。  
v | const value_t* | value对象。  
  
#### value_type_name 函数

* * *

  * 函数功能：



> 获取指定类型数据的名称。

  * 函数原型：


    
    
    const char* value_type_name (value_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回对应数据类型的名称。  
type | value_type_t | 类型。  
  
#### value_type_size 函数

* * *

  * 函数功能：



> 获取指定类型数据大小。

  * 函数原型：


    
    
    uint32_t value_type_size (value_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回对应数据类型的长度。  
type | value_type_t | 类型。  
  
#### value_ubjson 函数

* * *

  * 函数功能：



> 获取为ubjson的值。

  * 函数原型：


    
    
    binary_data_t* value_ubjson (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | binary_data_t* | 值。  
v | const value_t* | value对象。  
  
#### value_uint16 函数

* * *

  * 函数功能：



> 获取类型为uint16的值。

  * 函数原型：


    
    
    uint16_t value_uint16 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 值。  
v | const value_t* | value对象。  
  
#### value_uint32 函数

* * *

  * 函数功能：



> 获取类型为uint32的值。

  * 函数原型：


    
    
    uint32_t value_uint32 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 值。  
v | const value_t* | value对象。  
  
#### value_uint64 函数

* * *

  * 函数功能：



> 获取类型为uint64的值。

  * 函数原型：


    
    
    uint64_t value_uint64 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 值。  
v | const value_t* | value对象。  
  
#### value_uint8 函数

* * *

  * 函数功能：



> 获取类型为uint8的值。

  * 函数原型：


    
    
    uint8_t value_uint8 (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t | 值。  
v | const value_t* | value对象。  
  
#### value_wstr 函数

* * *

  * 函数功能：



> 获取类型为宽字符串的值。

  * 函数原型：


    
    
    const wchar_t* value_wstr (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const wchar_t* | 值。  
v | const value_t* | value对象。
