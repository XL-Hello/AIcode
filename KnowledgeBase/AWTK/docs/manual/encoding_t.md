## encoding_t

### 概述

encoding conversion

示例：
    
    
    

* * *

### 函数

函数名称 | 说明  
---|---  
encoding_convert | 字符集转换。  
encoding_gbk_to_utf8 | 将gbk转换成utf8编码。  
encoding_utf8_to_gbk | 将utf8转换成gbk编码。  
  
#### encoding_convert 函数

* * *

  * 函数功能：



> 字符集转换。

  * 函数原型：


    
    
    ret_t encoding_convert (encoding_name_t from, const char* from_str, uint32_t from_size, encoding_name_t to, char* to_str, uint32_t to_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
from | encoding_name_t | 源字符串的编码名称。  
from_str | const char* | 源字符串。  
from_size | uint32_t | 源字符串的长度。  
to | encoding_name_t | 目标字符串的编码名称。  
to_str | char* | 目标字符串。  
to_size | uint32_t | 目标字符串的最大长度。  
  
#### encoding_gbk_to_utf8 函数

* * *

  * 函数功能：



> 将gbk转换成utf8编码。

  * 函数原型：


    
    
    ret_t encoding_gbk_to_utf8 (const char* from_str, uint32_t from_size, char* to_str, uint32_t to_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
from_str | const char* | 源字符串(gbk)。  
from_size | uint32_t | 源字符串的长度。  
to_str | char* | 目标字符串(utf8)。  
to_size | uint32_t | 目标字符串的最大长度。  
  
#### encoding_utf8_to_gbk 函数

* * *

  * 函数功能：



> 将utf8转换成gbk编码。

  * 函数原型：


    
    
    ret_t encoding_utf8_to_gbk (const char* from_str, uint32_t from_size, char* to_str, uint32_t to_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
from_str | const char* | 源字符串(utf8)。  
from_size | uint32_t | 源字符串的长度。  
to_str | char* | 目标字符串(gbk)。  
to_size | uint32_t | 目标字符串的最大长度。
