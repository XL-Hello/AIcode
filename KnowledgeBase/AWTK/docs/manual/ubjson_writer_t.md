## ubjson_writer_t

### 概述

## ubjson writer

### 函数

函数名称 | 说明  
---|---  
ubjson_writer_init | 初始化。  
ubjson_writer_write_array_begin | 写入数组开始。  
ubjson_writer_write_array_end | 写入数组结束。  
ubjson_writer_write_char | 写入char。  
ubjson_writer_write_data | 写入二进制数据。  
ubjson_writer_write_false | 写入false。  
ubjson_writer_write_float32 | 写入float。  
ubjson_writer_write_float64 | 写入double。  
ubjson_writer_write_int | 写入int。  
ubjson_writer_write_int16 | 写入int16。  
ubjson_writer_write_int32 | 写入int32。  
ubjson_writer_write_int64 | 写入int64。  
ubjson_writer_write_int8 | 写入int8。  
ubjson_writer_write_key | 写入key。  
ubjson_writer_write_kv_array_begin | 写key和数组的开始。  
ubjson_writer_write_kv_bool | 写入key和bool的值。  
ubjson_writer_write_kv_double | 写入key和double的值。  
ubjson_writer_write_kv_float | 写入key和float的值。  
ubjson_writer_write_kv_int | 写入key和int的值。  
ubjson_writer_write_kv_int16 | 写入key和int的值。  
ubjson_writer_write_kv_int32 | 写入key和int的值。  
ubjson_writer_write_kv_int64 | 写入key和int64_t的值。  
ubjson_writer_write_kv_int8 | 写入key和int的值。  
ubjson_writer_write_kv_object | 写key和对象。  
ubjson_writer_write_kv_object_begin | 写key和对象的开始。  
ubjson_writer_write_kv_pointer | 写入key和uint64_t的地址值。  
ubjson_writer_write_kv_str | 写入key和str的值。  
ubjson_writer_write_kv_str_len | 写入key和str的值。  
ubjson_writer_write_kv_uint16 | 写入key和int的值。  
ubjson_writer_write_kv_uint32 | 写入key和int的值。  
ubjson_writer_write_kv_uint64 | 写入key和int64_t的值。  
ubjson_writer_write_kv_uint8 | 写入key和int的值。  
ubjson_writer_write_kv_value | 写入key和value_t的值。  
ubjson_writer_write_kv_wstr | 写入key和wstr的值。  
ubjson_writer_write_kv_wstr_len | 写入key和wstr的值。  
ubjson_writer_write_noop | 写入noop。  
ubjson_writer_write_null | 写入null。  
ubjson_writer_write_object | 写入obj。  
ubjson_writer_write_object_begin | 写入对象开始。  
ubjson_writer_write_object_end | 写入对象结束。  
ubjson_writer_write_pointer | 写入地址。  
ubjson_writer_write_str | 写入str。  
ubjson_writer_write_str_len | 写入str。  
ubjson_writer_write_true | 写入true。  
ubjson_writer_write_uint16 | 写入uint16。  
ubjson_writer_write_uint32 | 写入uint32。  
ubjson_writer_write_uint64 | 写入uint64。  
ubjson_writer_write_uint8 | 写入uint8。  
ubjson_writer_write_wstr | 写入wstr。  
ubjson_writer_write_wstr_len | 写入wstr。  
  
#### ubjson_writer_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    ubjson_writer_t* ubjson_writer_init (ubjson_writer_t* writer, ubjson_write_callback_t write, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ubjson_writer_t* | 返回writer对象。  
writer | ubjson_writer_t* | writer对象。  
write | ubjson_write_callback_t | 真正写入数据的函数。  
ctx | void* | write函数的上下文。  
  
#### ubjson_writer_write_array_begin 函数

* * *

  * 函数功能：



> 写入数组开始。 即： [

  * 函数原型：


    
    
    ret_t ubjson_writer_write_array_begin (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_array_end 函数

* * *

  * 函数功能：



> 写入数组结束。 即： ]

  * 函数原型：


    
    
    ret_t ubjson_writer_write_array_end (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_char 函数

* * *

  * 函数功能：



> 写入char。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_char (ubjson_writer_t* writer, char value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | char | 要写入的值。  
  
#### ubjson_writer_write_data 函数

* * *

  * 函数功能：



> 写入二进制数据。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_data (ubjson_writer_t* writer, const void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
data | const void* | 数据。  
size | uint32_t | 数据长度。  
  
#### ubjson_writer_write_false 函数

* * *

  * 函数功能：



> 写入false。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_false (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_float32 函数

* * *

  * 函数功能：



> 写入float。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_float32 (ubjson_writer_t* writer, float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | float | 要写入的值。  
  
#### ubjson_writer_write_float64 函数

* * *

  * 函数功能：



> 写入double。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_float64 (ubjson_writer_t* writer, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | double | 要写入的值。  
  
#### ubjson_writer_write_int 函数

* * *

  * 函数功能：



> 写入int。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_int (ubjson_writer_t* writer, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | int32_t | 要写入的值。  
  
#### ubjson_writer_write_int16 函数

* * *

  * 函数功能：



> 写入int16。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_int16 (ubjson_writer_t* writer, int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | int16_t | 要写入的值。  
  
#### ubjson_writer_write_int32 函数

* * *

  * 函数功能：



> 写入int32。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_int32 (ubjson_writer_t* writer, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | int32_t | 要写入的值。  
  
#### ubjson_writer_write_int64 函数

* * *

  * 函数功能：



> 写入int64。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_int64 (ubjson_writer_t* writer, int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | int64_t | 要写入的值。  
  
#### ubjson_writer_write_int8 函数

* * *

  * 函数功能：



> 写入int8。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_int8 (ubjson_writer_t* writer, int8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | int8_t | 要写入的值。  
  
#### ubjson_writer_write_key 函数

* * *

  * 函数功能：



> 写入key。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_key (ubjson_writer_t* writer, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | const char* | key的名称。  
  
#### ubjson_writer_write_kv_array_begin 函数

* * *

  * 函数功能：



> 写key和数组的开始。
> 
> 即：”key”: [

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_array_begin (ubjson_writer_t* writer, const char* key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键值。  
  
#### ubjson_writer_write_kv_bool 函数

* * *

  * 函数功能：



> 写入key和bool的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_bool (ubjson_writer_t* writer, const char* key, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | bool_t | 值。  
  
#### ubjson_writer_write_kv_double 函数

* * *

  * 函数功能：



> 写入key和double的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_double (ubjson_writer_t* writer, const char* key, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | double | 值。  
  
#### ubjson_writer_write_kv_float 函数

* * *

  * 函数功能：



> 写入key和float的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_float (ubjson_writer_t* writer, const char* key, float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | float | 值。  
  
#### ubjson_writer_write_kv_int 函数

* * *

  * 函数功能：



> 写入key和int的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_int (ubjson_writer_t* writer, const char* key, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | int32_t | 值。  
  
#### ubjson_writer_write_kv_int16 函数

* * *

  * 函数功能：



> 写入key和int的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_int16 (ubjson_writer_t* writer, const char* key, int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | int16_t | 值。  
  
#### ubjson_writer_write_kv_int32 函数

* * *

  * 函数功能：



> 写入key和int的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_int32 (ubjson_writer_t* writer, const char* key, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | int32_t | 值。  
  
#### ubjson_writer_write_kv_int64 函数

* * *

  * 函数功能：



> 写入key和int64_t的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_int64 (ubjson_writer_t* writer, const char* key, int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | int64_t | 值。  
  
#### ubjson_writer_write_kv_int8 函数

* * *

  * 函数功能：



> 写入key和int的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_int8 (ubjson_writer_t* writer, const char* key, int8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | int8_t | 值。  
  
#### ubjson_writer_write_kv_object 函数

* * *

  * 函数功能：



> 写key和对象。
> 
> 即：”key”: { object }

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_object (ubjson_writer_t* writer, const char* key, tk_object_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | tk_object_t* | 对象。  
  
#### ubjson_writer_write_kv_object_begin 函数

* * *

  * 函数功能：



> 写key和对象的开始。
> 
> 即：”key”: {

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_object_begin (ubjson_writer_t* writer, const char* key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键值。  
  
#### ubjson_writer_write_kv_pointer 函数

* * *

  * 函数功能：



> 写入key和uint64_t的地址值。
> 
> 即：”key”: value (其中 value 为 uint64_t 地址整型，需要强转为指针才可以使用。)

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_pointer (ubjson_writer_t* writer, const char* key, void* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | void* | 值。  
  
#### ubjson_writer_write_kv_str 函数

* * *

  * 函数功能：



> 写入key和str的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_str (ubjson_writer_t* writer, const char* key, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | const char* | 字符串。  
  
#### ubjson_writer_write_kv_str_len 函数

* * *

  * 函数功能：



> 写入key和str的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_str_len (ubjson_writer_t* writer, const char* key, const char* value, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | const char* | 字符串。  
len | uint32_t | 字符串的长度。  
  
#### ubjson_writer_write_kv_uint16 函数

* * *

  * 函数功能：



> 写入key和int的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_uint16 (ubjson_writer_t* writer, const char* key, uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | uint16_t | 值。  
  
#### ubjson_writer_write_kv_uint32 函数

* * *

  * 函数功能：



> 写入key和int的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_uint32 (ubjson_writer_t* writer, const char* key, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | uint32_t | 值。  
  
#### ubjson_writer_write_kv_uint64 函数

* * *

  * 函数功能：



> 写入key和int64_t的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_uint64 (ubjson_writer_t* writer, const char* key, uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | uint64_t | 值。  
  
#### ubjson_writer_write_kv_uint8 函数

* * *

  * 函数功能：



> 写入key和int的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_uint8 (ubjson_writer_t* writer, const char* key, uint8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | uint8_t | 值。  
  
#### ubjson_writer_write_kv_value 函数

* * *

  * 函数功能：



> 写入key和value_t的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_value (ubjson_writer_t* writer, const char* key, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | const value_t* | 值。  
  
#### ubjson_writer_write_kv_wstr 函数

* * *

  * 函数功能：



> 写入key和wstr的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_wstr (ubjson_writer_t* writer, const char* key, const wchar_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | const wchar_t* | 字符串。  
  
#### ubjson_writer_write_kv_wstr_len 函数

* * *

  * 函数功能：



> 写入key和wstr的值。
> 
> 即：”key”: value

  * 函数原型：


    
    
    ret_t ubjson_writer_write_kv_wstr_len (ubjson_writer_t* writer, const char* key, const wchar_t* value, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
key | const char* | 键名。  
value | const wchar_t* | 字符串。  
len | uint32_t | 字符串的长度。  
  
#### ubjson_writer_write_noop 函数

* * *

  * 函数功能：



> 写入noop。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_noop (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_null 函数

* * *

  * 函数功能：



> 写入null。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_null (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_object 函数

* * *

  * 函数功能：



> 写入obj。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_object (ubjson_writer_t* writer, tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
obj | tk_object_t* | 要写入的对象。  
  
#### ubjson_writer_write_object_begin 函数

* * *

  * 函数功能：



> 写入对象开始。 即： {

  * 函数原型：


    
    
    ret_t ubjson_writer_write_object_begin (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_object_end 函数

* * *

  * 函数功能：



> 写入对象结束。 即：}

  * 函数原型：


    
    
    ret_t ubjson_writer_write_object_end (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_pointer 函数

* * *

  * 函数功能：



> 写入地址。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_pointer (ubjson_writer_t* writer, void* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | void* | 要写入的地址。  
  
#### ubjson_writer_write_str 函数

* * *

  * 函数功能：



> 写入str。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_str (ubjson_writer_t* writer, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | const char* | 要写入的字符串。  
  
#### ubjson_writer_write_str_len 函数

* * *

  * 函数功能：



> 写入str。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_str_len (ubjson_writer_t* writer, const char* value, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | const char* | 要写入的字符串。  
len | uint32_t | 字符串的长度。  
  
#### ubjson_writer_write_true 函数

* * *

  * 函数功能：



> 写入true。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_true (ubjson_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
  
#### ubjson_writer_write_uint16 函数

* * *

  * 函数功能：



> 写入uint16。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_uint16 (ubjson_writer_t* writer, uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | uint16_t | 要写入的值。  
  
#### ubjson_writer_write_uint32 函数

* * *

  * 函数功能：



> 写入uint32。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_uint32 (ubjson_writer_t* writer, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | uint32_t | 要写入的值。  
  
#### ubjson_writer_write_uint64 函数

* * *

  * 函数功能：



> 写入uint64。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_uint64 (ubjson_writer_t* writer, uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | uint64_t | 要写入的值。  
  
#### ubjson_writer_write_uint8 函数

* * *

  * 函数功能：



> 写入uint8。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_uint8 (ubjson_writer_t* writer, uint8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | uint8_t | 要写入的值。  
  
#### ubjson_writer_write_wstr 函数

* * *

  * 函数功能：



> 写入wstr。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_wstr (ubjson_writer_t* writer, const wchar_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | const wchar_t* | 要写入的字符串。  
  
#### ubjson_writer_write_wstr_len 函数

* * *

  * 函数功能：



> 写入wstr。

  * 函数原型：


    
    
    ret_t ubjson_writer_write_wstr_len (ubjson_writer_t* writer, const wchar_t* value, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | ubjson_writer_t* | writer对象。  
value | const wchar_t* | 要写入的字符串。  
len | uint32_t | 字符串的长度。
