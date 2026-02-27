## ubjson_parser_t

### 概述

## ubjson parser

### 函数

函数名称 | 说明  
---|---  
ubjson_dump | 将ubjson数据打印到控制台。  
ubjson_parse | 解析ubjson数据，遇到key/value时调用提供的回调函数。  
ubjson_to_object | 解析ubjson数据，生成object对象。  
  
#### ubjson_dump 函数

* * *

  * 函数功能：



> 将ubjson数据打印到控制台。

  * 函数原型：


    
    
    ret_t ubjson_dump (void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
data | void* | 数据。  
size | uint32_t | 数据的长度。  
  
#### ubjson_parse 函数

* * *

  * 函数功能：



> 解析ubjson数据，遇到key/value时调用提供的回调函数。

  * 函数原型：


    
    
    ret_t ubjson_parse (void* data, uint32_t size, ubjson_on_key_value_t on_key_value, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
data | void* | 数据。  
size | uint32_t | 数据的长度。  
on_key_value | ubjson_on_key_value_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### ubjson_to_object 函数

* * *

  * 函数功能：



> 解析ubjson数据，生成object对象。

  * 函数原型：


    
    
    tk_object_t* ubjson_to_object (void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object表示的数据。  
data | void* | 数据。  
size | uint32_t | 数据的长度。
