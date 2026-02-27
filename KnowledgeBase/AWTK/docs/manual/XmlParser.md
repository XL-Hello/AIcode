## XmlParser

### 概述

## xml解析器

### 函数

函数名称 | 说明  
---|---  
xml_parser_create | 创建解析器。  
xml_parser_destroy | 销毁parser对象。  
xml_parser_parse | 解析数据。  
xml_parser_parse_file | 解析文件。  
xml_parser_set_builder | 设置builder。  
xml_parser_set_trim_text | 设置是否去掉文本两端的空白字符。  
  
#### xml_parser_create 函数

* * *

  * 函数功能：



> 创建解析器。

  * 函数原型：


    
    
    XmlParser* xml_parser_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | XmlParser* | 返回parser对象。  
  
#### xml_parser_destroy 函数

* * *

  * 函数功能：



> 销毁parser对象。

  * 函数原型：


    
    
    void xml_parser_destroy (XmlParser* parser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回无。  
parser | XmlParser* | parser对象。  
  
#### xml_parser_parse 函数

* * *

  * 函数功能：



> 解析数据。

  * 函数原型：


    
    
    void xml_parser_parse (XmlParser* parser, const char* xml, int length);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回无。  
parser | XmlParser* | parser对象。  
xml | const char* | 数据。  
length | int | 数据长度。  
  
#### xml_parser_parse_file 函数

* * *

  * 函数功能：



> 解析文件。

  * 函数原型：


    
    
    void xml_parser_parse_file (XmlParser* parser, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回无。  
parser | XmlParser* | parser对象。  
filename | const char* | 文件名。  
  
#### xml_parser_set_builder 函数

* * *

  * 函数功能：



> 设置builder。

  * 函数原型：


    
    
    void xml_parser_set_builder (XmlParser* parser, XmlBuilder* builder);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回无。  
parser | XmlParser* | parser对象。  
builder | XmlBuilder* | builder对象。  
  
#### xml_parser_set_trim_text 函数

* * *

  * 函数功能：



> 设置是否去掉文本两端的空白字符。
> 
> 默认值为去掉文本两端的空白字符，如果不希望去掉，调用本函数设置为FALSE。

  * 函数原型：


    
    
    void xml_parser_set_trim_text (XmlParser* parser, bool_t trim_text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回无。  
parser | XmlParser* | parser对象。  
trim_text | bool_t | 是否去掉文本两端的空白字符。
