## color_parser_t

### 概述

颜色解析相关函数。

示例：
    
    
    color_t c;
    c = color_parse("#112233");
    c = color_parse("white");
    c = color_parse("rgb(11,22,33)");
    c = color_parse("rgba(11,22,33,0.5)");
    

* * *

### 函数

函数名称 | 说明  
---|---  
color_parse | 把字符串格式的颜色转换成color_t对象。  
  
#### color_parse 函数

* * *

  * 函数功能：



> 把字符串格式的颜色转换成color_t对象。

目前支持下列格式：

  * 16进制格式。如：”#112233”
  * 颜色名称格式。如：”green”
  * rgb格式。如：”rgb(11,22,33)”
  * rgba格式。如：”rgba(11,22,33,0.5)”

  * 函数原型：



    
    
    color_t color_parse (const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t | 返回color_t对象。  
color | const char* | 字符串格式的颜色。
