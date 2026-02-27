## tk_iostream_mem_t

### 概述

![image](images/tk_iostream_mem_t_0.png)

## 基于内存实现的输入输出流。

### 函数

函数名称 | 说明  
---|---  
tk_iostream_mem_create | 创建iostream对象。  
  
#### tk_iostream_mem_create 函数

* * *

  * 函数功能：



> 创建iostream对象。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_mem_create (void* buff_in, uint32_t size_in, void* buff_out, uint32_t size_out, bool_t own_the_buff);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
buff_in | void* | 输入流缓冲区。  
size_in | uint32_t | 输入流缓冲区大小。  
buff_out | void* | 输入流缓冲区。  
size_out | uint32_t | 输入流缓冲区大小。  
own_the_buff | bool_t | 是否让istream对象拥有buff。
