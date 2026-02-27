## tk_ostream_buffered_t

### 概述

![image](images/tk_ostream_buffered_t_0.png)

## 先将数据写入一个缓存区，调用flush时才真正写入底层的ostream。

### 函数

函数名称 | 说明  
---|---  
tk_ostream_buffered_create | 创建ostream对象。  
tk_ostream_buffered_get_size | 获取当前缓存数据的长度。  
  
#### tk_ostream_buffered_create 函数

* * *

  * 函数功能：



> 创建ostream对象。

本函数自动增加real_ostream的引用计数。

  * 函数原型：


    
    
    tk_ostream_t* tk_ostream_buffered_create (tk_ostream_t* real_ostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_ostream_t* | 返回ostream对象。  
real_ostream | tk_ostream_t* | 实际的ostream对象。  
  
#### tk_ostream_buffered_get_size 函数

* * *

  * 函数功能：



> 获取当前缓存数据的长度。

  * 函数原型：


    
    
    uint32_t tk_ostream_buffered_get_size (tk_ostream_t* ostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回缓存数据的长度。  
ostream | tk_ostream_t* | ostream对象。
