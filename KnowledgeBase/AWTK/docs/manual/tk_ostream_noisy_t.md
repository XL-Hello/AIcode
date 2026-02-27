## tk_ostream_noisy_t

### 概述

![image](images/tk_ostream_noisy_t_0.png)

## 在输出流中注入错误，方便进行可靠性测试。

### 函数

函数名称 | 说明  
---|---  
tk_ostream_noisy_create | 创建ostream对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
error_count | uint32_t | 注入的错误数。  
error_level | uint32_t | error level.  
write_count | uint32_t | 写入的次数。  
  
#### tk_ostream_noisy_create 函数

* * *

  * 函数功能：



> 创建ostream对象。
> 
> 只能由iostream_noisy调用。

  * 函数原型：


    
    
    tk_ostream_t* tk_ostream_noisy_create (tk_ostream_t* real_ostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_ostream_t* | 返回ostream对象。  
real_ostream | tk_ostream_t* | 实际的ostream对象。  
  
#### error_count 属性

* * *

> 注入的错误数。

  * 类型：uint32_t



#### error_level 属性

* * *

> error level.

  * 类型：uint32_t



#### write_count 属性

* * *

> 写入的次数。

  * 类型：uint32_t


