## tk_iostream_stats_t

### 概述

![image](images/tk_iostream_stats_t_0.png)

## 带统计功能的输入输出流。

### 函数

函数名称 | 说明  
---|---  
tk_iostream_stats_create | 创建iostream对象。  
  
#### tk_iostream_stats_create 函数

* * *

  * 函数功能：



> 创建iostream对象。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_stats_create (tk_iostream_t* impl);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
impl | tk_iostream_t* | 被统计的流对象。
