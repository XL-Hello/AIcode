## font_manager_t

### 概述

![image](images/font_manager_t_0.png)

字体管理器，负责字体的加载和缓存管理。 (如果使用nanovg，字体由nanovg内部管理)

* * *

### 函数

函数名称 | 说明  
---|---  
font_manager | 获取缺省的字体管理器。  
font_manager_add_font | 向缓存中加入字体。  
font_manager_create | 创建字体管理器。  
font_manager_deinit | 析构字体管理器。  
font_manager_destroy | 析构并释放字体管理器。  
font_manager_get_font | 从缓存中查找字体，如果没找到，再加载字体，并缓存。  
font_manager_get_standard_font_size | 获取是否使用标准字号  
font_manager_init | 初始化字体管理器。  
font_manager_lookup | 查找字体。  
font_manager_set | 设置缺省的字体管理器。  
font_manager_set_assets_manager | 设置资源管理器对象  
font_manager_set_fallback_get_font | 设置一个函数，该函数在找不到字体时加载后补字体。  
font_manager_set_standard_font_size | 设置是否使用标准字号  
font_manager_shrink_cache | 清除最久没有被使用的缓冲字模。  
font_manager_unload_all | 卸载全部字体。  
font_manager_unload_font | 卸载指定的字体。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
|  |   
  
#### font_manager 函数

* * *

  * 函数功能：



> 获取缺省的字体管理器。

  * 函数原型：


    
    
    font_manager_t* font_manager ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_manager_t* | 返回字体管理器对象。  
  
#### font_manager_add_font 函数

* * *

  * 函数功能：



> 向缓存中加入字体。

  * 函数原型：


    
    
    ret_t font_manager_add_font (font_manager_t* fm, font_t* font);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
font | font_t* | 字体。  
  
#### font_manager_create 函数

* * *

  * 函数功能：



> 创建字体管理器。

  * 函数原型：


    
    
    font_manager_t* font_manager_create (font_loader_t* loader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_manager_t* | 返回字体管理器对象。  
loader | font_loader_t* | 字体加载器。  
  
#### font_manager_deinit 函数

* * *

  * 函数功能：



> 析构字体管理器。

  * 函数原型：


    
    
    ret_t font_manager_deinit (font_manager_t* fm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
  
#### font_manager_destroy 函数

* * *

  * 函数功能：



> 析构并释放字体管理器。

  * 函数原型：


    
    
    ret_t font_manager_destroy (font_manager_t* fm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
  
#### font_manager_get_font 函数

* * *

  * 函数功能：



> 从缓存中查找字体，如果没找到，再加载字体，并缓存。

  * 函数原型：


    
    
    font_t* font_manager_get_font (font_manager_t* fm, const char* name, font_size_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_t* | 返回字体对象。  
fm | font_manager_t* | 字体管理器对象。  
name | const char* | 字体名，为NULL时使用缺省字体。  
size | font_size_t | 字体的大小。  
  
#### font_manager_get_standard_font_size 函数

* * *

  * 函数功能：



> 获取是否使用标准字号

  * 函数原型：


    
    
    bool_t font_manager_get_standard_font_size (font_manager_t* fm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示使用标准字号，否则表示不是。  
fm | font_manager_t* | 字体管理器对象。  
  
#### font_manager_init 函数

* * *

  * 函数功能：



> 初始化字体管理器。

  * 函数原型：


    
    
    font_manager_t* font_manager_init (font_manager_t* fm, font_loader_t* loader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_manager_t* | 返回字体管理器对象。  
fm | font_manager_t* | 字体管理器对象。  
loader | font_loader_t* | 字体加载器。  
  
#### font_manager_lookup 函数

* * *

  * 函数功能：



> 查找字体。

  * 函数原型：


    
    
    font_t* font_manager_lookup (font_manager_t* fm, const char* name, font_size_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_t* | 返回字体对象。  
fm | font_manager_t* | 字体管理器对象。  
name | const char* | 字体名称。  
size | font_size_t | 字体大小。  
  
#### font_manager_set 函数

* * *

  * 函数功能：



> 设置缺省的字体管理器。

  * 函数原型：


    
    
    ret_t font_manager_set (font_manager_t* fm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
  
#### font_manager_set_assets_manager 函数

* * *

  * 函数功能：



> 设置资源管理器对象

之所以需要设置资源管理器对象，而不是使用缺省的资源管理器对象，是因为在designer中有两个字体管理器：

  * 一个用于designer本身加载字体。

  * 一个用于被设计的窗口加载字体。




这两个字体管理器需要从不同的路径加载资源。

  * 函数原型：


    
    
    ret_t font_manager_set_assets_manager (font_manager_t* fm, assets_manager_t* assets_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
assets_manager | assets_manager_t* | 资源管理器。  
  
#### font_manager_set_fallback_get_font 函数

* * *

  * 函数功能：



> 设置一个函数，该函数在找不到字体时加载后补字体。

  * 函数原型：


    
    
    ret_t font_manager_set_fallback_get_font (font_manager_t* fm, font_manager_get_font_t fallback_get_font, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
fallback_get_font | font_manager_get_font_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### font_manager_set_standard_font_size 函数

* * *

  * 函数功能：



> 设置是否使用标准字号

  * 函数原型：


    
    
    ret_t font_manager_set_standard_font_size (font_manager_t* fm, bool_t is_standard);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
is_standard | bool_t | 是否使用标准字号  
  
#### font_manager_shrink_cache 函数

* * *

  * 函数功能：



> 清除最久没有被使用的缓冲字模。

  * 函数原型：


    
    
    ret_t font_manager_shrink_cache (font_manager_t* fm, uint32_t cache_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
cache_size | uint32_t | 每种字体保留缓存字模的个数。  
  
#### font_manager_unload_all 函数

* * *

  * 函数功能：



> 卸载全部字体。

  * 函数原型：


    
    
    ret_t font_manager_unload_all (font_manager_t* fm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
  
#### font_manager_unload_font 函数

* * *

  * 函数功能：



> 卸载指定的字体。

  * 函数原型：


    
    
    ret_t font_manager_unload_font (font_manager_t* fm, const char* name, font_size_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fm | font_manager_t* | 字体管理器对象。  
name | const char* | 字体名，为NULL时使用缺省字体。  
size | font_size_t | 字体的大小(矢量字体指定为0即可)。
