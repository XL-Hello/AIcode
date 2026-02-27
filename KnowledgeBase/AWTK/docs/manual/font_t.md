## font_t

### 概述

## 代表一种字体。

### 函数

函数名称 | 说明  
---|---  
font_destroy | 销毁font对象。  
font_get_glyph | 获取指定字符和大小的字模。  
font_get_vmetrics | 获取字体的高度信息。  
font_match | 检查当前字体是否与指定名称和大小相匹配。  
font_shrink_cache | 清除最近没使用的字模。  
  
#### font_destroy 函数

* * *

  * 函数功能：



> 销毁font对象。

  * 函数原型：


    
    
    ret_t font_destroy (font_t* font);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
font | font_t* | font对象。  
  
#### font_get_glyph 函数

* * *

  * 函数功能：



> 获取指定字符和大小的字模。

  * 函数原型：


    
    
    ret_t font_get_glyph (font_t* font, wchar_t chr, font_size_t font_size, glyph_t* glyph);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
font | font_t* | font对象。  
chr | wchar_t | 字符。  
font_size | font_size_t | 字体大小。  
glyph | glyph_t* | 返回字模数据。  
  
#### font_get_vmetrics 函数

* * *

  * 函数功能：



> 获取字体的高度信息。

  * 函数原型：


    
    
    font_vmetrics_t font_get_vmetrics (font_t* font, font_size_t font_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_vmetrics_t | 返回字体的高度信息。  
font | font_t* | font对象。  
font_size | font_size_t | 字体大小。  
  
#### font_match 函数

* * *

  * 函数功能：



> 检查当前字体是否与指定名称和大小相匹配。

  * 函数原型：


    
    
    bool_t font_match (font_t* font, const char* font_name, font_size_t font_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示成功，FALSE表示失败。  
font | font_t* | font对象。  
font_name | const char* | 字体名称。  
font_size | font_size_t | 字体大小。  
  
#### font_shrink_cache 函数

* * *

  * 函数功能：



> 清除最近没使用的字模。

  * 函数原型：


    
    
    ret_t font_shrink_cache (font_t* font, uint32_t cache_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
font | font_t* | font对象。  
cache_size | uint32_t | 保留缓存字模的个数。
