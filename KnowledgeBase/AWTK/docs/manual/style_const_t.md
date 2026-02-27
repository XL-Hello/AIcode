## style_const_t

### 概述

![image](images/style_const_t_0.png)

只读的style，从theme_t中获取数据。

## tools/theme_gen用于把XML的窗体样式数据转换成常量数据。

### 函数

函数名称 | 说明  
---|---  
style_const_create | 创建只读的style对象。  
  
#### style_const_create 函数

* * *

  * 函数功能：



> 创建只读的style对象。

  * 函数原型：


    
    
    style_t* style_const_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | style_t* | 返回style对象。
