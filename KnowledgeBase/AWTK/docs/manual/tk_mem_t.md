## tk_mem_t

### 概述

内存管理相关的宏和函数。

示例：
    
    
    char* str = (char*)TKMEM_ALLOC(100);
    ...
    TKMEM_FREE(str);
    
    
    
    char* str = (char*)TKMEM_ALLOC(100);
    ...
    str = (char*)TKMEM_REALLOC(str, 128);
    ...
    TKMEM_FREE(str);
    

* * *

### 函数

函数名称 | 说明  
---|---  
tk_mem_dump | 显示内存信息。  
tk_mem_init | 初始化内存。  
tk_mem_init_ex | 初始化内存，支持多块不连续的内存。  
tk_mem_init_stage2 | 初始化互斥和oom。  
tk_mem_is_valid_addr | 检查给定的地址是否是一个有效的heap地址。  
tk_mem_set_on_out_of_memory | 设置内存耗尽时的处理函数。  
TKMEM_ALLOC | 分配一块内存。  
TKMEM_CALLOC | 分配一块内存，并将内容清零。  
TKMEM_FREE | 释放内存。  
TKMEM_REALLOC | 重新分配一块内存，如果原来的内存块大于等于需要的空间，直接返回原来的内存块。  
  
#### tk_mem_dump 函数

* * *

  * 函数功能：



> 显示内存信息。

  * 函数原型：


    
    
    void tk_mem_dump ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回void。  
  
#### tk_mem_init 函数

* * *

  * 函数功能：



> 初始化内存。

  * 函数原型：


    
    
    ret_t tk_mem_init (void* buffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | void* | 内存地址。  
size | uint32_t | 内存长度。  
  
#### tk_mem_init_ex 函数

* * *

  * 函数功能：



> 初始化内存，支持多块不连续的内存。 最后一个参数必须为NULL。

示例：
    
    
    tk_mem_init_ex(mem1, sizeof(mem1), mem2, sizeof(mem2), mem3, sizeof(mem3), NULL);
    

  * 函数原型：


    
    
    ret_t tk_mem_init_ex (void* buffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | void* | 内存地址。  
size | uint32_t | 内存长度。  
  
#### tk_mem_init_stage2 函数

* * *

  * 函数功能：



> 初始化互斥和oom。

  * 函数原型：


    
    
    ret_t tk_mem_init_stage2 ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_mem_is_valid_addr 函数

* * *

  * 函数功能：



> 检查给定的地址是否是一个有效的heap地址。 用于辅助发现内存问题。

  * 函数原型：


    
    
    bool_t tk_mem_is_valid_addr (void* addr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE一定是无效地址，返回TRUE在PC则不太确定。  
addr | void* | 内存地址。  
  
#### tk_mem_set_on_out_of_memory 函数

* * *

  * 函数功能：



> 设置内存耗尽时的处理函数。

  * 函数原型：


    
    
    ret_t tk_mem_set_on_out_of_memory (tk_mem_on_out_of_memory_t on_out_of_memory, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
on_out_of_memory | tk_mem_on_out_of_memory_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### TKMEM_ALLOC 宏

* * *

  * 函数功能：



> 分配一块内存。

  * 函数原型：


    
    
    void* TKMEM_ALLOC (uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回内存块首地址，失败返回NULL。  
size | uint32_t | 内存大小。  
  
#### TKMEM_CALLOC 宏

* * *

  * 函数功能：



> 分配一块内存，并将内容清零。

  * 函数原型：


    
    
    void* TKMEM_CALLOC (uint32_t nmemb, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回内存块首地址，失败返回NULL。  
nmemb | uint32_t | 内存块数量。  
size | uint32_t | 每一块的大小。  
  
#### TKMEM_FREE 宏

* * *

  * 函数功能：



> 释放内存。

  * 函数原型：


    
    
    void TKMEM_FREE (void* p);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 无。  
p | void* | 内存地址。  
  
#### TKMEM_REALLOC 宏

* * *

  * 函数功能：



> 重新分配一块内存，如果原来的内存块大于等于需要的空间，直接返回原来的内存块。

  * 函数原型：


    
    
    void* TKMEM_REALLOC (void* p, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回内存块首地址，失败返回NULL。  
p | void* | 原来的内存地址。  
size | uint32_t | 每一块的大小。
