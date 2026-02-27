## mmap_t

### 概述

## 把文件内容映射到内存。

### 函数

函数名称 | 说明  
---|---  
mmap_create | 初始化mmap对象。  
mmap_destroy | 销毁mmap。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
data | void* | 内存地址。  
size | uint32_t | 数据长度。  
  
#### mmap_create 函数

* * *

  * 函数功能：



> 初始化mmap对象。

  * 函数原型：


    
    
    mmap_t* mmap_create (const char* filename, bool_t writable, bool_t shared);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | mmap_t* | mmap对象本身。  
filename | const char* | 文件名。  
writable | bool_t | 是否可写。  
shared | bool_t | 是否共享。  
  
#### mmap_destroy 函数

* * *

  * 函数功能：



> 销毁mmap。

  * 函数原型：


    
    
    ret_t mmap_destroy (mmap_t* mmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mmap | mmap_t* | mmap对象。  
  
#### data 属性

* * *

> 内存地址。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 数据长度。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
