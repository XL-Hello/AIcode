## line_break_check

### 概述

## 换行相关函数。

### 函数

函数名称 | 说明  
---|---  
line_break | 解析字符串，对于每一行调用on_line函数。  
line_break_check | 检查两个字符之间是否允许换行。  
line_break_count | 统计行数。  
word_break_check | 检查两个字符之间是否允许单词分割。  
  
#### line_break 函数

* * *

  * 函数功能：



> 解析字符串，对于每一行调用on_line函数。

  * 函数原型：


    
    
    ret_t line_break (const wchar_t* str, line_break_on_line_t on_line, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | const wchar_t* | 字符串。  
on_line | line_break_on_line_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### line_break_check 函数

* * *

  * 函数功能：



> 检查两个字符之间是否允许换行。

  * 函数原型：


    
    
    line_break_type_t line_break_check (wchar_t c1, wchar_t c2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | line_break_type_t | 返回类型。  
c1 | wchar_t | 前面的字符。  
c2 | wchar_t | 后面的字符。  
  
#### line_break_count 函数

* * *

  * 函数功能：



> 统计行数。

  * 函数原型：


    
    
    uint32_t line_break_count (const wchar_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回行数。  
str | const wchar_t* | 字符串。  
  
#### word_break_check 函数

* * *

  * 函数功能：



> 检查两个字符之间是否允许单词分割。

  * 函数原型：


    
    
    line_break_type_t word_break_check (wchar_t c1, wchar_t c2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | line_break_type_t | 返回类型。  
c1 | wchar_t | 前面的字符。  
c2 | wchar_t | 后面的字符。
