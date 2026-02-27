## tk_istream_t

### 概述

![image](images/tk_istream_t_0.png)

## 输入流的接口。

### 函数

函数名称 | 说明  
---|---  
tk_istream_eos | 判断数据是否读完。  
tk_istream_flush | 刷新数据。  
tk_istream_read | 读取数据。  
tk_istream_read_double | 写入double数据。  
tk_istream_read_float | 写入float数据。  
tk_istream_read_int16 | 写入int16数据。  
tk_istream_read_int32 | 写入int32数据。  
tk_istream_read_int64 | 写入int64数据。  
tk_istream_read_int8 | 写入int8数据。  
tk_istream_read_len | 读取指定长度的数据。  
tk_istream_read_line | 读取一行数据。  
tk_istream_read_line_str | 读取一行数据。  
tk_istream_read_uint16 | 写入uint16数据。  
tk_istream_read_uint32 | 写入uint32数据。  
tk_istream_read_uint64 | 写入uint64数据。  
tk_istream_read_uint8 | 写入uint8数据。  
tk_istream_seek | 设置偏移量。  
tk_istream_tell | 获取当前读取位置。  
tk_istream_unref | 引用计数减1。引用计数为0时，销毁对象。  
tk_istream_wait_for_data | 等待数据。  
  
#### tk_istream_eos 函数

* * *

  * 函数功能：



> 判断数据是否读完。

  * 函数原型：


    
    
    bool_t tk_istream_eos (tk_istream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示数据读完，否则表示还有数据。  
stream | tk_istream_t* | istream对象。  
  
#### tk_istream_flush 函数

* * *

  * 函数功能：



> 刷新数据。

  * 函数原型：


    
    
    ret_t tk_istream_flush (tk_istream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
  
#### tk_istream_read 函数

* * *

  * 函数功能：



> 读取数据。

  * 函数原型：


    
    
    int32_t tk_istream_read (tk_istream_t* stream, void* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示读取失败，否则返回实际读取数据的长度。  
stream | tk_istream_t* | istream对象。  
buff | void* | 返回数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
  
#### tk_istream_read_double 函数

* * *

  * 函数功能：



> 写入double数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_double (tk_istream_t* stream, double* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | double* | 数据。  
  
#### tk_istream_read_float 函数

* * *

  * 函数功能：



> 写入float数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_float (tk_istream_t* stream, float* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | float* | 数据。  
  
#### tk_istream_read_int16 函数

* * *

  * 函数功能：



> 写入int16数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_int16 (tk_istream_t* stream, int16_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | int16_t* | 数据。  
  
#### tk_istream_read_int32 函数

* * *

  * 函数功能：



> 写入int32数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_int32 (tk_istream_t* stream, int32_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | int32_t* | 数据。  
  
#### tk_istream_read_int64 函数

* * *

  * 函数功能：



> 写入int64数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_int64 (tk_istream_t* stream, int64_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | int64_t* | 数据。  
  
#### tk_istream_read_int8 函数

* * *

  * 函数功能：



> 写入int8数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_int8 (tk_istream_t* stream, int8_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | int8_t* | 数据。  
  
#### tk_istream_read_len 函数

* * *

  * 函数功能：



> 读取指定长度的数据。

  * 函数原型：


    
    
    int32_t tk_istream_read_len (tk_istream_t* stream, void* buff, uint32_t max_size, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示读取失败，否则返回实际读取数据的长度。  
stream | tk_istream_t* | istream对象。  
buff | void* | 返回数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
timeout_ms | uint32_t | timeout.  
  
#### tk_istream_read_line 函数

* * *

  * 函数功能：



> 读取一行数据。

  * 函数原型：


    
    
    int32_t tk_istream_read_line (tk_istream_t* stream, void* buff, uint32_t max_size, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示读取失败，否则返回实际读取数据的长度。  
stream | tk_istream_t* | istream对象。  
buff | void* | 返回数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
timeout_ms | uint32_t | timeout.  
  
#### tk_istream_read_line_str 函数

* * *

  * 函数功能：



> 读取一行数据。 istream必须支持随机读写(seek/tell)。

  * 函数原型：


    
    
    ret_t tk_istream_read_line_str (tk_istream_t* stream, str_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
str | str_t* | 返回数据的str对象。  
  
#### tk_istream_read_uint16 函数

* * *

  * 函数功能：



> 写入uint16数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_uint16 (tk_istream_t* stream, uint16_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | uint16_t* | 数据。  
  
#### tk_istream_read_uint32 函数

* * *

  * 函数功能：



> 写入uint32数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_uint32 (tk_istream_t* stream, uint32_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | uint32_t* | 数据。  
  
#### tk_istream_read_uint64 函数

* * *

  * 函数功能：



> 写入uint64数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_uint64 (tk_istream_t* stream, uint64_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | uint64_t* | 数据。  
  
#### tk_istream_read_uint8 函数

* * *

  * 函数功能：



> 写入uint8数据。

  * 函数原型：


    
    
    ret_t tk_istream_read_uint8 (tk_istream_t* stream, uint8_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
value | uint8_t* | 数据。  
  
#### tk_istream_seek 函数

* * *

  * 函数功能：



> 设置偏移量。

  * 函数原型：


    
    
    ret_t tk_istream_seek (tk_istream_t* stream, uint32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
offset | uint32_t | 偏移量。  
  
#### tk_istream_tell 函数

* * *

  * 函数功能：



> 获取当前读取位置。

  * 函数原型：


    
    
    int32_t tk_istream_tell (tk_istream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示失败，否则返回当前读取位置。  
stream | tk_istream_t* | istream对象。  
  
#### tk_istream_unref 函数

* * *

  * 函数功能：



> 引用计数减1。引用计数为0时，销毁对象。

  * 函数原型：


    
    
    ret_t tk_istream_unref (tk_istream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
  
#### tk_istream_wait_for_data 函数

* * *

  * 函数功能：



> 等待数据。

  * 函数原型：


    
    
    ret_t tk_istream_wait_for_data (tk_istream_t* stream, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
timeout_ms | uint32_t | 超时时间(毫秒)。
