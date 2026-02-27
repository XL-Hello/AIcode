## tk_ostream_t

### 概述

![image](images/tk_ostream_t_0.png)

## 输出流的接口。

### 函数

函数名称 | 说明  
---|---  
tk_ostream_flush | 刷新数据。  
tk_ostream_printf | 写入格式化字符串。  
tk_ostream_seek | 设置偏移量。  
tk_ostream_tell | 获取当前读取位置。  
tk_ostream_unref | 引用计数减1。引用计数为0时，销毁对象。  
tk_ostream_write | 写入数据。  
tk_ostream_write_byte | 写入一个字节的数据。  
tk_ostream_write_double | 写入double数据。  
tk_ostream_write_float | 写入float数据。  
tk_ostream_write_int16 | 写入int16数据。  
tk_ostream_write_int32 | 写入int32数据。  
tk_ostream_write_int64 | 写入int64数据。  
tk_ostream_write_int8 | 写入int8数据。  
tk_ostream_write_len | 写入指定长度的数据。  
tk_ostream_write_str | 写入字符串。  
tk_ostream_write_uint16 | 写入uint16数据。  
tk_ostream_write_uint32 | 写入uint32数据。  
tk_ostream_write_uint64 | 写入uint64数据。  
tk_ostream_write_uint8 | 写入uint8数据。  
  
#### tk_ostream_flush 函数

* * *

  * 函数功能：



> 刷新数据。

  * 函数原型：


    
    
    ret_t tk_ostream_flush (tk_ostream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
  
#### tk_ostream_printf 函数

* * *

  * 函数功能：



> 写入格式化字符串。 长度不超过1024。

  * 函数原型：


    
    
    ret_t tk_ostream_printf (tk_ostream_t* stream, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
format | const char* | 格式化字符串。  
  
#### tk_ostream_seek 函数

* * *

  * 函数功能：



> 设置偏移量。

  * 函数原型：


    
    
    ret_t tk_ostream_seek (tk_ostream_t* stream, uint32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
offset | uint32_t | 偏移量。  
  
#### tk_ostream_tell 函数

* * *

  * 函数功能：



> 获取当前读取位置。

  * 函数原型：


    
    
    int32_t tk_ostream_tell (tk_ostream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示失败，否则返回当前读取位置。  
stream | tk_ostream_t* | ostream对象。  
  
#### tk_ostream_unref 函数

* * *

  * 函数功能：



> 引用计数减1。引用计数为0时，销毁对象。

  * 函数原型：


    
    
    ret_t tk_ostream_unref (tk_ostream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
  
#### tk_ostream_write 函数

* * *

  * 函数功能：



> 写入数据。

  * 函数原型：


    
    
    int32_t tk_ostream_write (tk_ostream_t* stream, const void* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示写入失败，否则返回实际写入数据的长度。  
stream | tk_ostream_t* | ostream对象。  
buff | const void* | 返回数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
  
#### tk_ostream_write_byte 函数

* * *

  * 函数功能：



> 写入一个字节的数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_byte (tk_ostream_t* stream, uint8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | uint8_t | 数据。  
  
#### tk_ostream_write_double 函数

* * *

  * 函数功能：



> 写入double数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_double (tk_ostream_t* stream, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | double | 数据。  
  
#### tk_ostream_write_float 函数

* * *

  * 函数功能：



> 写入float数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_float (tk_ostream_t* stream, float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | float | 数据。  
  
#### tk_ostream_write_int16 函数

* * *

  * 函数功能：



> 写入int16数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_int16 (tk_ostream_t* stream, int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | int16_t | 数据。  
  
#### tk_ostream_write_int32 函数

* * *

  * 函数功能：



> 写入int32数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_int32 (tk_ostream_t* stream, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | int32_t | 数据。  
  
#### tk_ostream_write_int64 函数

* * *

  * 函数功能：



> 写入int64数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_int64 (tk_ostream_t* stream, int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | int64_t | 数据。  
  
#### tk_ostream_write_int8 函数

* * *

  * 函数功能：



> 写入int8数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_int8 (tk_ostream_t* stream, int8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | int8_t | 数据。  
  
#### tk_ostream_write_len 函数

* * *

  * 函数功能：



> 写入指定长度的数据。

  * 函数原型：


    
    
    int32_t tk_ostream_write_len (tk_ostream_t* stream, const void* buff, uint32_t max_size, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示写入失败，否则返回实际写入数据的长度。  
stream | tk_ostream_t* | ostream对象。  
buff | const void* | 数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
timeout_ms | uint32_t | timeout.  
  
#### tk_ostream_write_str 函数

* * *

  * 函数功能：



> 写入字符串。

  * 函数原型：


    
    
    ret_t tk_ostream_write_str (tk_ostream_t* stream, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
str | const char* | 字符串。  
  
#### tk_ostream_write_uint16 函数

* * *

  * 函数功能：



> 写入uint16数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_uint16 (tk_ostream_t* stream, uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | uint16_t | 数据。  
  
#### tk_ostream_write_uint32 函数

* * *

  * 函数功能：



> 写入uint32数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_uint32 (tk_ostream_t* stream, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | uint32_t | 数据。  
  
#### tk_ostream_write_uint64 函数

* * *

  * 函数功能：



> 写入uint64数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_uint64 (tk_ostream_t* stream, uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | uint64_t | 数据。  
  
#### tk_ostream_write_uint8 函数

* * *

  * 函数功能：



> 写入uint8数据。

  * 函数原型：


    
    
    ret_t tk_ostream_write_uint8 (tk_ostream_t* stream, uint8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_ostream_t* | ostream对象。  
value | uint8_t | 数据。
