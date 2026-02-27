## tk_istream_mem_t

### 概述

![image](images/tk_istream_mem_t_0.png)

## 基于内存实现的输入流。

### 函数

函数名称 | 说明  
---|---  
tk_istream_mem_create | 创建istream对象。  
tk_istream_mem_create_simple | 创建istream对象。  
  
#### tk_istream_mem_create 函数

* * *

  * 函数功能：



> 创建istream对象。

  * 函数原型：


    
    
    tk_istream_t* tk_istream_mem_create (void* buff, uint32_t size, uint32_t packet_size, bool_t own_the_buff);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_istream_t* | 返回istream对象。  
buff | void* | 返回数据的缓冲区。  
size | uint32_t | 缓冲区的大小。  
packet_size | uint32_t | 缺省一次读取的数据的长度。  
own_the_buff | bool_t | 是否让istream对象拥有buff。  
  
#### tk_istream_mem_create_simple 函数

* * *

  * 函数功能：



> 创建istream对象。

  * 函数原型：


    
    
    tk_istream_t* tk_istream_mem_create_simple (void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_istream_t* | 返回istream对象。  
buff | void* | 返回数据的缓冲区。  
size | uint32_t | 缓冲区的大小。
