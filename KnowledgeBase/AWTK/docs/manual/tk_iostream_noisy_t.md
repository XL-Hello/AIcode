## tk_iostream_noisy_t

### 概述

![image](images/tk_iostream_noisy_t_0.png)

## 在输出流中注入错误，方便进行可靠性测试。

### 函数

函数名称 | 说明  
---|---  
tk_iostream_noisy_create | 创建iostream对象。  
  
#### tk_iostream_noisy_create 函数

* * *

  * 函数功能：



> 创建iostream对象。

本函数自动增加real_iostream的引用计数。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_noisy_create (tk_iostream_t* real_iostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
real_iostream | tk_iostream_t* | 底层的iostream。
