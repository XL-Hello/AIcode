## data_reader_t

### 概述

数据读取接口。

## >对可读的媒介，如内存、文件、flash、资源和其它媒介提供一个统一的读取接口。

### 函数

函数名称 | 说明  
---|---  
data_reader_can_read | 查询 url 中是否有数据。  
data_reader_destroy | 销毁reader对象。  
data_reader_get_size | 获取数据长度。  
data_reader_read | 在指定位置读取数据。  
data_reader_read_all | 从指定的URL读取全部数据。  
  
#### data_reader_can_read 函数

* * *

  * 函数功能：



> 查询 url 中是否有数据。

  * 函数原型：


    
    
    bool_t data_reader_can_read (const char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回 bool_t 值。  
url | const char* | URL。  
  
#### data_reader_destroy 函数

* * *

  * 函数功能：



> 销毁reader对象。

  * 函数原型：


    
    
    ret_t data_reader_destroy (data_reader_t* reader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
reader | data_reader_t* | reader对象。  
  
#### data_reader_get_size 函数

* * *

  * 函数功能：



> 获取数据长度。

  * 函数原型：


    
    
    uint64_t data_reader_get_size (data_reader_t* reader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回数据长度。  
reader | data_reader_t* | reader对象。  
  
#### data_reader_read 函数

* * *

  * 函数功能：



> 在指定位置读取数据。

  * 函数原型：


    
    
    int32_t data_reader_read (data_reader_t* reader, uint64_t offset, void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际读取数据的长度。  
reader | data_reader_t* | reader对象。  
offset | uint64_t | 偏移量。  
data | void* | 用于读取数据的缓冲区。  
size | uint32_t | 最大读取数据长度。  
  
#### data_reader_read_all 函数

* * *

  * 函数功能：



> 从指定的URL读取全部数据。

  * 函数原型：


    
    
    void* data_reader_read_all (const char* url, uint32_t* size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回全部数据，调用者需要调用TKMEM_FREE释放返回值。  
url | const char* | URL。  
size | uint32_t* | 返回数据长度。
