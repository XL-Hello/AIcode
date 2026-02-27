## compressor_miniz_t

### 概述

![image](images/compressor_miniz_t_0.png)

## 基于miniz实现的compressor接口。

### 函数

函数名称 | 说明  
---|---  
compressor_miniz_create | 创建compressor对象。  
  
#### compressor_miniz_create 函数

* * *

  * 函数功能：



> 创建compressor对象。

  * 函数原型：


    
    
    compressor_t* compressor_miniz_create (compressor_options_t options);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | compressor_t* | 返回compressor对象。  
options | compressor_options_t | 选项。
