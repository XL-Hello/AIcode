## utf8

### 概述

wchar_t和char类型转换接口。

示例：
    
    
     const char* str = "hello";
     const wchar_t* wstr = L"hello";
     char res_str[128];
     wchar_t res_wstr[128];
    
     tk_utf8_to_utf16(str, res_wstr, ARRAY_SIZE(res_wstr));
     tk_utf8_from_utf16(wstr, res_str, ARRAY_SIZE(res_str));
    

* * *

### 函数

函数名称 | 说明  
---|---  
tk_\utf8_from_utf16 |   
tk_utf8_to_utf16 |   
  
#### utf8_from_utf16 函数

* * *

  * 函数功能：



> 将wchar_t类型转换为char类型。

  * 函数原型：


    
    
    char* tk_utf8_from_utf16 (const wchar_t* str, const char* out, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 值。  
str | const wchar_t* | str。  
out | const char* | 返回结果缓冲区。  
size | uint32_t | 缓冲区大小。  
  
#### utf8_from_utf16 函数

* * *

  * 函数功能：



> 将char类型转换为wchar_t类型。

  * 函数原型：


    
    
    wchar_t* tk_utf8_to_utf16 (const char* str, const wchar_t* out, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wchar_t* | 值。  
str | const char* | str。  
out | const wchar_t* | 返回结果缓冲区。  
size | uint32_t | 缓冲区大小。
