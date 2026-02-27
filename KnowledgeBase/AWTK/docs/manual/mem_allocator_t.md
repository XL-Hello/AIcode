## mem_allocator_t

### 概述

## 内存分配接口。

### 函数

函数名称 | 说明  
---|---  
mem_allocator_alloc | 分配指定大小的内存。  
mem_allocator_destroy | 销毁内存分配器。  
mem_allocator_dump | 显示内存信息，用于调试。  
mem_allocator_free | 释放内存。  
mem_allocator_realloc | 重新分配指定大小的内存。  
  
#### mem_allocator_alloc 函数

* * *

  * 函数功能：



> 分配指定大小的内存。

  * 函数原型：


    
    
    void* mem_allocator_alloc (mem_allocator_t* allocator, uint32_t size, const char* func, uint32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回内存块的地址，失败返回NULL。  
allocator | mem_allocator_t* | allocator对象。  
size | uint32_t | 内存的大小。  
func | const char* | 分配内存的函数(用于调试)。  
line | uint32_t | 分配内存的行数(用于调试)。  
  
#### mem_allocator_destroy 函数

* * *

  * 函数功能：



> 销毁内存分配器。

  * 函数原型：


    
    
    ret_t mem_allocator_destroy (mem_allocator_t* allocator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
allocator | mem_allocator_t* | allocator对象。  
  
#### mem_allocator_dump 函数

* * *

  * 函数功能：



> 显示内存信息，用于调试。

  * 函数原型：


    
    
    ret_t mem_allocator_dump (mem_allocator_t* allocator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
allocator | mem_allocator_t* | allocator对象。  
  
#### mem_allocator_free 函数

* * *

  * 函数功能：



> 释放内存。

  * 函数原型：


    
    
    void mem_allocator_free (mem_allocator_t* allocator, void* ptr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 无。  
allocator | mem_allocator_t* | allocator对象。  
ptr | void* | 内存的地址。  
  
#### mem_allocator_realloc 函数

* * *

  * 函数功能：



> 重新分配指定大小的内存。

  * 函数原型：


    
    
    void* mem_allocator_realloc (mem_allocator_t* allocator, void* ptr, uint32_t size, const char* func, uint32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回内存块的地址，失败返回NULL。  
allocator | mem_allocator_t* | allocator对象。  
ptr | void* | 原来内存的地址。  
size | uint32_t | 内存的大小。  
func | const char* | 分配内存的函数(用于调试)。  
line | uint32_t | 分配内存的行数(用于调试)。
