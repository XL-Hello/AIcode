## tk_iostream_t

### 概述

![image](images/tk_iostream_t_0.png)

## 输入输出流的接口。

### 函数

函数名称 | 说明  
---|---  
tk_iostream_get_istream | 获取输入流对象(不再使用时，无需UNREF返回的对象)。  
tk_iostream_get_ostream | 获取输出流对象(不再使用时，无需UNREF返回的对象)。  
tk_iostream_read | 读取数据。  
tk_iostream_read_len | 读取指定长度的数据。  
tk_iostream_unref | 引用计数减1。引用计数为0时，销毁对象。  
tk_iostream_write | 写入数据。  
tk_iostream_write_len | 写入指定长度的数据。  
  
#### tk_iostream_get_istream 函数

* * *

  * 函数功能：



> 获取输入流对象(不再使用时，无需UNREF返回的对象)。

  * 函数原型：


    
    
    tk_istream_t* tk_iostream_get_istream (tk_iostream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_istream_t* | 返回输入流对象。  
stream | tk_iostream_t* | iostream对象。  
  
#### tk_iostream_get_ostream 函数

* * *

  * 函数功能：



> 获取输出流对象(不再使用时，无需UNREF返回的对象)。

  * 函数原型：


    
    
    tk_ostream_t* tk_iostream_get_ostream (tk_iostream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_ostream_t* | 返回输出流对象。  
stream | tk_iostream_t* | iostream对象。  
  
#### tk_iostream_read 函数

* * *

  * 函数功能：



> 读取数据。

  * 函数原型：


    
    
    int32_t tk_iostream_read (tk_iostream_t* stream, void* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示读取失败，否则返回实际读取数据的长度。  
stream | tk_iostream_t* | iostream对象。  
buff | void* | 返回数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
  
#### tk_iostream_read_len 函数

* * *

  * 函数功能：



> 读取指定长度的数据。

  * 函数原型：


    
    
    int32_t tk_iostream_read_len (tk_iostream_t* stream, void* buff, uint32_t max_size, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示读取失败，否则返回实际读取数据的长度。  
stream | tk_iostream_t* | iostream对象。  
buff | void* | 返回数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
timeout_ms | uint32_t | timeout.  
  
#### tk_iostream_unref 函数

* * *

  * 函数功能：



> 引用计数减1。引用计数为0时，销毁对象。

  * 函数原型：


    
    
    ret_t tk_iostream_unref (tk_iostream_t* stream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_iostream_t* | iostream对象。  
  
#### tk_iostream_write 函数

* * *

  * 函数功能：



> 写入数据。

  * 函数原型：


    
    
    int32_t tk_iostream_write (tk_iostream_t* stream, const void* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示写入失败，否则返回实际写入数据的长度。  
stream | tk_iostream_t* | iostream对象。  
buff | const void* | 返回数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
  
#### tk_iostream_write_len 函数

* * *

  * 函数功能：



> 写入指定长度的数据。

  * 函数原型：


    
    
    int32_t tk_iostream_write_len (tk_iostream_t* stream, const void* buff, uint32_t max_size, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回负数表示写入失败，否则返回实际写入数据的长度。  
stream | tk_iostream_t* | iostream对象。  
buff | const void* | 数据的缓冲区。  
max_size | uint32_t | 缓冲区的大小。  
timeout_ms | uint32_t | timeout.
