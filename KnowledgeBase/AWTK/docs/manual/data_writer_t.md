## data_writer_t

### 概述

数据写入接口。

## >对可写的媒介，如内存、文件、flash和其它媒介提供一个统一的写入接口。

### 函数

函数名称 | 说明  
---|---  
data_writer_clear | 清除指定URL的数据。  
data_writer_destroy | 销毁writer对象。  
data_writer_flush | flush数据。  
data_writer_truncate | 截去指定长度之后的数据。  
data_writer_write | 在指定位置写入数据。  
data_writer_write_all | 写入全部数据。  
  
#### data_writer_clear 函数

* * *

  * 函数功能：



> 清除指定URL的数据。

  * 函数原型：


    
    
    ret_t data_writer_clear (const char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | const char* | URL。  
  
#### data_writer_destroy 函数

* * *

  * 函数功能：



> 销毁writer对象。

  * 函数原型：


    
    
    ret_t data_writer_destroy (data_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | data_writer_t* | writer对象。  
  
#### data_writer_flush 函数

* * *

  * 函数功能：



> flush数据。

  * 函数原型：


    
    
    ret_t data_writer_flush (data_writer_t* writer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | data_writer_t* | writer对象。  
  
#### data_writer_truncate 函数

* * *

  * 函数功能：



> 截去指定长度之后的数据。

  * 函数原型：


    
    
    ret_t data_writer_truncate (data_writer_t* writer, uint64_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
writer | data_writer_t* | writer对象。  
size | uint64_t | 保留长度。  
  
#### data_writer_write 函数

* * *

  * 函数功能：



> 在指定位置写入数据。

  * 函数原型：


    
    
    int32_t data_writer_write (data_writer_t* writer, uint64_t offset, const void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际读取数据的长度。  
writer | data_writer_t* | writer对象。  
offset | uint64_t | 偏移量。  
data | const void* | 数据缓冲区。  
size | uint32_t | 数据长度。  
  
#### data_writer_write_all 函数

* * *

  * 函数功能：



> 写入全部数据。

  * 函数原型：


    
    
    int32_t data_writer_write_all (const char* url, const void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际写入数据的长度。  
url | const char* | URL。  
data | const void* | 数据缓冲区。  
size | uint32_t | 数据长度。
