## theme_default_t

### 概述

窗体样式默认实现。 负责管理缺省的窗体样式数据，方便实现style_const。

* * *

### 函数

函数名称 | 说明  
---|---  
theme_default_create | 创建窗体样式对象。  
theme_default_create_ex | 创建窗体样式对象。  
  
#### theme_default_create 函数

* * *

  * 函数功能：



> 创建窗体样式对象。

  * 函数原型：


    
    
    theme_t* theme_default_create (const uint8_t* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | theme_t* | 返回窗体样式对象。  
data | const uint8_t* | 窗体样式数据。  
  
#### theme_default_create_ex 函数

* * *

  * 函数功能：



> 创建窗体样式对象。

  * 函数原型：


    
    
    theme_t* theme_default_create_ex (const uint8_t* data, bool_t need_free_data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | theme_t* | 返回窗体样式对象。  
data | const uint8_t* | 窗体样式数据。  
need_free_data | bool_t | 销毁时是否释放数据。
