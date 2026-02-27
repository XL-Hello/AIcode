## input_method_sdl_t

### 概述

![image](images/input_method_sdl_t_0.png)

SDL输入法实现。

## SDL输入法使用平台自身的输入法引擎，一般在桌面Linux、MacOS、Windows、Android和iOS上使用。

### 函数

函数名称 | 说明  
---|---  
input_method_sdl_create | 创建SDL输入法对象。  
  
#### input_method_sdl_create 函数

* * *

  * 函数功能：



> 创建SDL输入法对象。

  * 函数原型：


    
    
    input_method_t* input_method_sdl_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | input_method_t* | 返回输入法对象。
