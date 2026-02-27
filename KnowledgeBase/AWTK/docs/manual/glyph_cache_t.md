## glyph_cache_t

### 概述

## glyph cache

### 函数

函数名称 | 说明  
---|---  
glyph_cache_add | 增加一个glyph对象到cache。  
glyph_cache_deinit | 释放全部cache。  
glyph_cache_init | 初始化glyph_cache对象。  
glyph_cache_lookup | 查找glyph对象。  
glyph_cache_shrink | 释放部分glyph。  
  
#### glyph_cache_add 函数

* * *

  * 函数功能：



> 增加一个glyph对象到cache。

  * 函数原型：


    
    
    ret_t glyph_cache_add (glyph_cache_t* cache, wchar_t code, font_size_t size, glyph_t* g);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cache | glyph_cache_t* | cache对象。  
code | wchar_t | 字符。  
size | font_size_t | 字体大小。  
g | glyph_t* | glyph对象。  
  
#### glyph_cache_deinit 函数

* * *

  * 函数功能：



> 释放全部cache。

  * 函数原型：


    
    
    ret_t glyph_cache_deinit (glyph_cache_t* cache);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cache | glyph_cache_t* | cache对象。  
  
#### glyph_cache_init 函数

* * *

  * 函数功能：



> 初始化glyph_cache对象。

  * 函数原型：


    
    
    glyph_cache_t* glyph_cache_init (glyph_cache_t* cache, uint32_t capacity, tk_destroy_t destroy_glyph);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | glyph_cache_t* | 返回cache对象。  
cache | glyph_cache_t* | cache对象。  
capacity | uint32_t | 最大容量。  
destroy_glyph | tk_destroy_t | 销毁函数。  
  
#### glyph_cache_lookup 函数

* * *

  * 函数功能：



> 查找glyph对象。

  * 函数原型：


    
    
    ret_t glyph_cache_lookup (glyph_cache_t* cache, wchar_t code, font_size_t size, glyph_t* g);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cache | glyph_cache_t* | cache对象。  
code | wchar_t | 字符。  
size | font_size_t | 字体大小。  
g | glyph_t* | glyph对象(用于返回glyph)。  
  
#### glyph_cache_shrink 函数

* * *

  * 函数功能：



> 释放部分glyph。

  * 函数原型：


    
    
    ret_t glyph_cache_shrink (glyph_cache_t* cache, uint32_t cache_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cache | glyph_cache_t* | cache对象。  
cache_size | uint32_t | 保留cache个数。
