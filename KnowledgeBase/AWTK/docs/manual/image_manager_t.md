## image_manager_t

### 概述

## 图片管理器。负责加载，解码和缓存图片。

### 函数

函数名称 | 说明  
---|---  
image_manager | 获取缺省的图片管理器。  
image_manager_create | 创建图片管理器。  
image_manager_deinit | 析构图片管理器。  
image_manager_destroy | 析构并释放图片管理器。  
image_manager_dump | 输出图片管理器的信息。  
image_manager_get_bitmap | 获取指定的图片。  
image_manager_has_bitmap | 图片是否在图片管理中。  
image_manager_init | 初始化图片管理器。  
image_manager_preload | 预加载指定的图片。  
image_manager_set | 设置缺省的图片管理器。  
image_manager_set_assets_manager | 设置资源管理器对象。  
image_manager_set_fallback_get_bitmap | 设置一个函数，该函数在找不到图片时加载后补图片。  
image_manager_set_max_mem_size_of_cached_images | 设置图片缓存占用的最大内存。  
image_manager_unload_all | 卸载全部图片。  
image_manager_unload_bitmap | 从图片管理器中卸载指定的图片。  
image_manager_unload_bitmap_by_name | 从图片管理器中卸载指定的图片。  
image_manager_unload_unused | 从图片管理器中卸载指定时间内没有使用的图片。  
image_manager_update_specific | 更新缓存中图片的specific信息。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
|  |   
  
#### image_manager 函数

* * *

  * 函数功能：



> 获取缺省的图片管理器。

  * 函数原型：


    
    
    image_manager_t* image_manager ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | image_manager_t* | 返回图片管理器对象。  
  
#### image_manager_create 函数

* * *

  * 函数功能：



> 创建图片管理器。

  * 函数原型：


    
    
    image_manager_t* image_manager_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | image_manager_t* | 返回图片管理器对象。  
  
#### image_manager_deinit 函数

* * *

  * 函数功能：



> 析构图片管理器。

  * 函数原型：


    
    
    ret_t image_manager_deinit (image_manager_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | image_manager_t* | 图片管理器对象。  
  
#### image_manager_destroy 函数

* * *

  * 函数功能：



> 析构并释放图片管理器。

  * 函数原型：


    
    
    ret_t image_manager_destroy (image_manager_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | image_manager_t* | 图片管理器对象。  
  
#### image_manager_dump 函数

* * *

  * 函数功能：



> 输出图片管理器的信息。

  * 函数原型：


    
    
    ret_t image_manager_dump (image_manager_t* im, str_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | image_manager_t* | 图片管理器对象。  
result | str_t* | 用于返回图片管理器的信息。  
  
#### image_manager_get_bitmap 函数

* * *

  * 函数功能：



> 获取指定的图片。 先从缓存查找，如果没找到，再加载并缓存。

  * 函数原型：


    
    
    ret_t image_manager_get_bitmap (image_manager_t* imm, const char* name, bitmap_t* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
name | const char* | 图片名称。  
image | bitmap_t* | 用于返回图片。  
  
#### image_manager_has_bitmap 函数

* * *

  * 函数功能：



> 图片是否在图片管理中。

  * 函数原型：


    
    
    bool_t image_manager_has_bitmap (image_manager_t* imm, bitmap_t* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
imm | image_manager_t* | 图片管理器对象。  
image | bitmap_t* | 图片。  
  
#### image_manager_init 函数

* * *

  * 函数功能：



> 初始化图片管理器。

  * 函数原型：


    
    
    image_manager_t* image_manager_init (image_manager_t* imm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | image_manager_t* | 返回图片管理器对象。  
imm | image_manager_t* | 图片管理器对象。  
  
#### image_manager_preload 函数

* * *

  * 函数功能：



> 预加载指定的图片。

  * 函数原型：


    
    
    ret_t image_manager_preload (image_manager_t* imm, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
name | const char* | 图片名称。  
  
#### image_manager_set 函数

* * *

  * 函数功能：



> 设置缺省的图片管理器。

  * 函数原型：


    
    
    ret_t image_manager_set (image_manager_t* imm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
  
#### image_manager_set_assets_manager 函数

* * *

  * 函数功能：



> 设置资源管理器对象。

之所以需要设置资源管理器对象，而不是使用缺省的资源管理器对象，是因为在designer中有两个图片管理器：

  * 一个用于designer本身加载图片。

  * 一个用于被设计的窗口加载图片。




这两个图片管理器需要从不同的路径加载资源。

  * 函数原型：


    
    
    ret_t image_manager_set_assets_manager (image_manager_t* imm, assets_manager_t* assets_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
assets_manager | assets_manager_t* | 资源管理器。  
  
#### image_manager_set_fallback_get_bitmap 函数

* * *

  * 函数功能：



> 设置一个函数，该函数在找不到图片时加载后补图片。

  * 函数原型：


    
    
    ret_t image_manager_set_fallback_get_bitmap (image_manager_t* imm, image_manager_get_bitmap_t fallback_get_bitmap, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | image manager对象。  
fallback_get_bitmap | image_manager_get_bitmap_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### image_manager_set_max_mem_size_of_cached_images 函数

* * *

  * 函数功能：



> 设置图片缓存占用的最大内存。

  * 函数原型：


    
    
    ret_t image_manager_set_max_mem_size_of_cached_images (image_manager_t* imm, uint32_t max_mem_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
max_mem_size | uint32_t | 最大缓存内存(字节数)。  
  
#### image_manager_unload_all 函数

* * *

  * 函数功能：



> 卸载全部图片。

  * 函数原型：


    
    
    ret_t image_manager_unload_all (image_manager_t* imm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
  
#### image_manager_unload_bitmap 函数

* * *

  * 函数功能：



> 从图片管理器中卸载指定的图片。

  * 函数原型：


    
    
    ret_t image_manager_unload_bitmap (image_manager_t* imm, bitmap_t* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
image | bitmap_t* | 图片。  
  
#### image_manager_unload_bitmap_by_name 函数

* * *

  * 函数功能：



> 从图片管理器中卸载指定的图片。

  * 函数原型：


    
    
    ret_t image_manager_unload_bitmap_by_name (image_manager_t* imm, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
name | const char* | 图片。  
  
#### image_manager_unload_unused 函数

* * *

  * 函数功能：



> 从图片管理器中卸载指定时间内没有使用的图片。

  * 函数原型：


    
    
    ret_t image_manager_unload_unused (image_manager_t* imm, uint32_t time_delta_s);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
time_delta_s | uint32_t | 时间范围，单位为秒。  
  
#### image_manager_update_specific 函数

* * *

  * 函数功能：



> 更新缓存中图片的specific信息。

  * 函数原型：


    
    
    ret_t image_manager_update_specific (image_manager_t* imm, bitmap_t* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
imm | image_manager_t* | 图片管理器对象。  
image | bitmap_t* | 返回图片信息。
