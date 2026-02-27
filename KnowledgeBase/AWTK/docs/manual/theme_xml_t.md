## theme_xml_t

### 概述

## XML格式的窗体样式。

### 函数

函数名称 | 说明  
---|---  
theme_xml_create | 创建窗体样式对象。  
theme_xml_gen | 生成二进制的数据。  
  
#### theme_xml_create 函数

* * *

  * 函数功能：



> 创建窗体样式对象。

  * 函数原型：


    
    
    theme_t* theme_xml_create (const char* xml);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | theme_t* | 返回窗体样式对象。  
xml | const char* | XML格式窗体样式数据。  
  
#### theme_xml_gen 函数

* * *

  * 函数功能：



> 生成二进制的数据。

  * 函数原型：


    
    
    uint8_t* theme_xml_gen (const char* xml, uint32_t* size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回二进制的数据。  
xml | const char* | XML格式窗体样式数据。  
size | uint32_t* | 用于返回数据长度。
