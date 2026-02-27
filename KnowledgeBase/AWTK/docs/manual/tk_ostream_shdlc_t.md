## tk_ostream_shdlc_t

### 概述

![image](images/tk_ostream_shdlc_t_0.png)

## reliable ostream base on simple HDLC

### 函数

函数名称 | 说明  
---|---  
tk_ostream_shdlc_create | 创建ostream对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
compress_threshold | uint32_t | 激活压缩的阈值。  
retry_times | uint8_t | 失败重传次数。  
timeout | uint32_t | 读写超时时间(毫秒)  
  
#### tk_ostream_shdlc_create 函数

* * *

  * 函数功能：



> 创建ostream对象。
> 
> 只能由iostream_shdlc调用。

  * 函数原型：


    
    
    tk_ostream_t* tk_ostream_shdlc_create (tk_iostream_shdlc_t* iostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_ostream_t* | 返回ostream对象。  
iostream | tk_iostream_shdlc_t* | iostream对象。  
  
#### compress_threshold 属性

* * *

> 激活压缩的阈值。

  * 类型：uint32_t



#### retry_times 属性

* * *

> 失败重传次数。

  * 类型：uint8_t



#### timeout 属性

* * *

> 读写超时时间(毫秒)

  * 类型：uint32_t


