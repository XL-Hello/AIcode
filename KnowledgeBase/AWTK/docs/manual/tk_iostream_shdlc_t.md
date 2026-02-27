## tk_iostream_shdlc_t

### 概述

![image](images/tk_iostream_shdlc_t_0.png)

基于简化版的HDLC协议实现可靠的iostream。

## 一般用于串口通信。

### 函数

函数名称 | 说明  
---|---  
tk_iostream_shdlc_create | 创建iostream对象。  
  
#### tk_iostream_shdlc_create 函数

* * *

  * 函数功能：



> 创建iostream对象。

本函数自动增加real_iostream的引用计数。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_shdlc_create (tk_iostream_t* real_iostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
real_iostream | tk_iostream_t* | 底层的iostream。
