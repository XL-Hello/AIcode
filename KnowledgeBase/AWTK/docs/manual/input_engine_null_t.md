## input_engine_null_t

### 概述

![image](images/input_engine_null_t_0.png)

空输入法引擎实现。

## 缺省输入法可以选择启用软键盘，但不启用具体的输入法引擎，此时可以选择空输入法引擎实现。

### 函数

函数名称 | 说明  
---|---  
input_engine_create | 创建空输入法引擎对象。  
  
#### input_engine_create 函数

* * *

  * 函数功能：



> 创建空输入法引擎对象。

  * 函数原型：


    
    
    input_engine_t* input_engine_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | input_engine_t* | 返回输入法引擎对象。
