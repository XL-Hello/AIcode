## assets_manager_t

### 概述

![image](images/assets_manager_t_0.png)

资源管理器。 这里的资源管理器并非Windows下的文件浏览器，而是负责对各种资源，比如字体、窗体样式、图片、界面数据、字符串和其它数据的进行集中管理的组件。引入资源管理器的目的有以下几个：

  * 让上层不需要了解存储的方式。 在没有文件系统时或者内存紧缺时，把资源转成常量数组直接编译到代码中。在有文件系统而且内存充足时，资源放在文件系统中。在有网络时，资源也可以存放在服务器上(暂未实现)。资源管理器为上层提供统一的接口，让上层而不用关心底层的存储方式。

  * 让上层不需要了解资源的具体格式。 比如一个名为earth的图片，没有文件系统或内存紧缺，图片直接用位图数据格式存在ROM中，而有文件系统时，则用PNG格式存放在文件系统中。资源管理器让上层不需要关心图片的格式，访问时指定图片的名称即可(不用指定扩展名)。

  * 让上层不需要了解屏幕的密度。 不同的屏幕密度下需要加载不同的图片，比如MacPro的Retina屏就需要用双倍解析度的图片，否则就出现界面模糊。AWTK以后会支持PC软件和手机软件的开发，所以资源管理器需要为此提供支持，让上层不需关心屏幕的密度。

  * 对资源进行内存缓存。 不同类型的资源使用方式是不一样的，比如字体和窗体样式加载之后会一直使用，UI文件在生成界面之后就暂时不需要了，PNG文件解码之后就只需要保留解码的位图数据即可。资源管理器配合图片管理器等其它组件实现资源的自动缓存。




当从文件系统加载资源时，目录结构要求如下：
    
    
    assets/{theme}/raw/
    fonts   字体
    images  图片
    x1   普通密度屏幕的图片。
    x2   2倍密度屏幕的图片。
    x3   3倍密度屏幕的图片。
    xx   密度无关的图片。
    strings 需要翻译的字符串。
    styles  窗体样式数据。
    ui      UI描述数据。
    

* * *

### 函数

函数名称 | 说明  
---|---  
assets_manager | 获取缺省资源管理器。  
assets_manager_add | 向资源管理器中增加一个资源。  
assets_manager_add_data | 向资源管理器中增加一个资源data。  
assets_manager_build_asset_filename | 构建资源文件名。  
assets_manager_clear_all | 清除全部缓存的资源。  
assets_manager_clear_all_cache | 清除缓存。  
assets_manager_clear_cache | 清除指定类型的缓存。  
assets_manager_clear_cache_ex | 清除指定类型和名称的缓存。  
assets_manager_create | 创建资源管理器。  
assets_manager_deinit | 释放全部资源。  
assets_manager_destroy | 释放全部资源并销毁asset manager对象。  
assets_manager_dump | 输出资源管理器的信息。  
assets_manager_find_in_cache | 在资源管理器的缓存中查找指定的资源(不引用)。  
assets_manager_get_res_root | 获取资源所在的目录(其下目录结构请参考demos)。  
assets_manager_init | 初始化资源管理器。  
assets_manager_is_save_assets_list | 检查指定类型是否需要保存。  
assets_manager_load | 从文件系统中加载指定的资源，并缓存到内存中。在定义了宏WITH_FS_RES时才生效。  
assets_manager_load_ex | 从文件系统中加载指定的资源，并缓存到内存中。在定义了宏WITH_FS_RES时才生效。  
assets_manager_load_file | 获取path里的资源。  
assets_manager_preload | 从文件系统中加载指定的资源，并缓存到内存中。在定义了宏WITH_FS_RES时才生效。  
assets_manager_ref | 在资源管理器的缓存中查找指定的资源并引用它，如果缓存中不存在，尝试加载该资源。  
assets_manager_ref_ex | 在资源管理器的缓存中查找指定的资源并引用它，如果缓存中不存在，尝试加载该资源。  
assets_manager_set | 设置缺省资源管理器。  
assets_manager_set_custom_build_asset_dir | 设置一个函数，该函数用于生成资源路径。  
assets_manager_set_custom_load_asset | 设置一个函数，该函数用于实现自定义加载资源。  
assets_manager_set_fallback_load_asset | 设置一个函数，该函数在找不到资源时加载后补资源。  
assets_manager_set_loader | 设置loader。  
assets_manager_set_locale_info | 设置locale_info对象。  
assets_manager_set_res_root | 设置资源所在的目录(其下目录结构请参考demos)。  
assets_manager_set_system_info | 设置system_info对象。  
assets_manager_set_theme | 设置当前的主题。  
assets_manager_unref | 释放指定的资源。  
  
#### assets_manager 函数

* * *

  * 函数功能：



> 获取缺省资源管理器。

  * 函数原型：


    
    
    assets_manager_t* assets_manager ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | assets_manager_t* | 返回asset manager对象。  
  
#### assets_manager_add 函数

* * *

  * 函数功能：



> 向资源管理器中增加一个资源。 备注： 1\. 同一份资源多次调用会出现缓存叠加的问题，导致内存泄露 2\. 该资源需要用户自己管理，AWTK 内部只会增加引用计数而已。

  * 函数原型：


    
    
    ret_t assets_manager_add (assets_manager_t* am, const void* info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
info | const void* | 待增加的资源。  
  
#### assets_manager_add_data 函数

* * *

  * 函数功能：



> 向资源管理器中增加一个资源data。 备注： 1\. 同一份资源多次调用会出现缓存叠加的问题，导致内存泄露 2\. 该资源会交给 AWTK 内部托管管理，data 数据就可以删除了。

  * 函数原型：


    
    
    ret_t assets_manager_add_data (assets_manager_t* am, const char* name, uint16_t type, uint16_t subtype, uint8_t* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
name | const char* | 待增加的资源的名字。  
type | uint16_t | 待增加的资源的主类型枚举。  
subtype | uint16_t | 待增加的资源的子类型枚举。  
buff | uint8_t* | 待增加的资源的data数据。  
size | uint32_t | 待增加的资源的data数据长度。  
  
#### assets_manager_build_asset_filename 函数

* * *

  * 函数功能：



> 构建资源文件名。

  * 函数原型：


    
    
    ret_t assets_manager_build_asset_filename (assets_manager_t* am, char* path, uint32_t size, const char* theme, bool_t ratio_sensitive, const char* subpath, const char* name, const char* extname);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功。  
am | assets_manager_t* | asset manager对象。  
path | char* | 文件名。  
size | uint32_t | 文件名长度。  
theme | const char* | 主题。  
ratio_sensitive | bool_t | 是否按像素比查找。  
subpath | const char* | 自路径。  
name | const char* | 名称。  
extname | const char* | 扩展名。  
  
#### assets_manager_clear_all 函数

* * *

  * 函数功能：



> 清除全部缓存的资源。

  * 函数原型：


    
    
    ret_t assets_manager_clear_all (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
  
#### assets_manager_clear_all_cache 函数

* * *

  * 函数功能：



> 清除缓存。

  * 函数原型：


    
    
    ret_t assets_manager_clear_all_cache (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
  
#### assets_manager_clear_cache 函数

* * *

  * 函数功能：



> 清除指定类型的缓存。

  * 函数原型：


    
    
    ret_t assets_manager_clear_cache (assets_manager_t* am, asset_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
  
#### assets_manager_clear_cache_ex 函数

* * *

  * 函数功能：



> 清除指定类型和名称的缓存。

  * 函数原型：


    
    
    ret_t assets_manager_clear_cache_ex (assets_manager_t* am, asset_type_t type, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
name | const char* | 资源的名称。  
  
#### assets_manager_create 函数

* * *

  * 函数功能：



> 创建资源管理器。

  * 函数原型：


    
    
    assets_manager_t* assets_manager_create (uint32_t init_nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | assets_manager_t* | 返回asset manager对象。  
init_nr | uint32_t | 预先分配资源的个数。  
  
#### assets_manager_deinit 函数

* * *

  * 函数功能：



> 释放全部资源。

  * 函数原型：


    
    
    ret_t assets_manager_deinit (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
  
#### assets_manager_destroy 函数

* * *

  * 函数功能：



> 释放全部资源并销毁asset manager对象。

  * 函数原型：


    
    
    ret_t assets_manager_destroy (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
  
#### assets_manager_dump 函数

* * *

  * 函数功能：



> 输出资源管理器的信息。

  * 函数原型：


    
    
    ret_t assets_manager_dump (assets_manager_t* am, str_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
result | str_t* | 输出的字符串。  
  
#### assets_manager_find_in_cache 函数

* * *

  * 函数功能：



> 在资源管理器的缓存中查找指定的资源(不引用)。

  * 函数原型：


    
    
    const asset_info_t* assets_manager_find_in_cache (assets_manager_t* am, asset_type_t type, uint16_t subtype, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const asset_info_t* | 返回资源。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
subtype | uint16_t | 资源的子类型。  
name | const char* | 资源的名称。  
  
#### assets_manager_get_res_root 函数

* * *

  * 函数功能：



> 获取资源所在的目录(其下目录结构请参考demos)。

  * 函数原型：


    
    
    const char* assets_manager_get_res_root (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回资源所在的目录。  
am | assets_manager_t* | asset manager对象。  
  
#### assets_manager_init 函数

* * *

  * 函数功能：



> 初始化资源管理器。

  * 函数原型：


    
    
    assets_manager_t* assets_manager_init (assets_manager_t* am, uint32_t init_nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | assets_manager_t* | 返回asset manager对象。  
am | assets_manager_t* | asset manager对象。  
init_nr | uint32_t | 预先分配资源的个数。  
  
#### assets_manager_is_save_assets_list 函数

* * *

  * 函数功能：



> 检查指定类型是否需要保存。

  * 函数原型：


    
    
    bool_t assets_manager_is_save_assets_list (asset_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示需要保持，否则不需要保存。  
type | asset_type_t | 资源类型。  
  
#### assets_manager_load 函数

* * *

  * 函数功能：



> 从文件系统中加载指定的资源，并缓存到内存中。在定义了宏WITH_FS_RES时才生效。 备注：内部使用的，如果是加载资源的话，建议使用 assets_manager_ref 函数。

  * 函数原型：


    
    
    asset_info_t* assets_manager_load (assets_manager_t* am, asset_type_t type, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | asset_info_t* | 返回资源。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
name | const char* | 资源的名称。  
  
#### assets_manager_load_ex 函数

* * *

  * 函数功能：



> 从文件系统中加载指定的资源，并缓存到内存中。在定义了宏WITH_FS_RES时才生效。 备注：内部使用的，如果是加载资源的话，建议使用 assets_manager_ref_ex 函数。

  * 函数原型：


    
    
    asset_info_t* assets_manager_load_ex (assets_manager_t* am, asset_type_t type, uint16_t subtype, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | asset_info_t* | 返回资源。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
subtype | uint16_t | 资源的子类型。  
name | const char* | 资源的名称。  
  
#### assets_manager_load_file 函数

* * *

  * 函数功能：



> 获取path里的资源。

  * 函数原型：


    
    
    asset_info_t* assets_manager_load_file (assets_manager_t* am, asset_type_t type, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | asset_info_t* | 返回asset_info_t。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源类型。  
path | const char* | 目录。  
  
#### assets_manager_preload 函数

* * *

  * 函数功能：



> 从文件系统中加载指定的资源，并缓存到内存中。在定义了宏WITH_FS_RES时才生效。 备注：内部使用的，不建议用户自行调用。

  * 函数原型：


    
    
    ret_t assets_manager_preload (assets_manager_t* am, asset_type_t type, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
name | const char* | 资源的名称。  
  
#### assets_manager_ref 函数

* * *

  * 函数功能：



> 在资源管理器的缓存中查找指定的资源并引用它，如果缓存中不存在，尝试加载该资源。

  * 函数原型：


    
    
    const asset_info_t* assets_manager_ref (assets_manager_t* am, asset_type_t type, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const asset_info_t* | 返回资源。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
name | const char* | 资源的名称。  
  
#### assets_manager_ref_ex 函数

* * *

  * 函数功能：



> 在资源管理器的缓存中查找指定的资源并引用它，如果缓存中不存在，尝试加载该资源。

  * 函数原型：


    
    
    const asset_info_t* assets_manager_ref_ex (assets_manager_t* am, asset_type_t type, uint16_t subtype, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const asset_info_t* | 返回资源。  
am | assets_manager_t* | asset manager对象。  
type | asset_type_t | 资源的类型。  
subtype | uint16_t | 资源的子类型。  
name | const char* | 资源的名称。  
  
#### assets_manager_set 函数

* * *

  * 函数功能：



> 设置缺省资源管理器。

  * 函数原型：


    
    
    ret_t assets_manager_set (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
  
#### assets_manager_set_custom_build_asset_dir 函数

* * *

  * 函数功能：



> 设置一个函数，该函数用于生成资源路径。
> 
> 有时我们需要优先加载用户自定义的资源，加载失败才加载系统缺省的，可用设置一个函数去实现这类功能。

  * 函数原型：


    
    
    ret_t assets_manager_set_custom_build_asset_dir (assets_manager_t* am, assets_manager_build_asset_dir_t custom_build_asset_dir, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
custom_build_asset_dir | assets_manager_build_asset_dir_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### assets_manager_set_custom_load_asset 函数

* * *

  * 函数功能：



> 设置一个函数，该函数用于实现自定义加载资源。
> 
> 如果不支持文件系统，开发者可以设置一个加载资源的回调函数，从flash或其它地方读取资源。

  * 函数原型：


    
    
    ret_t assets_manager_set_custom_load_asset (assets_manager_t* am, assets_manager_load_asset_t custom_load_asset, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
custom_load_asset | assets_manager_load_asset_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### assets_manager_set_fallback_load_asset 函数

* * *

  * 函数功能：



> 设置一个函数，该函数在找不到资源时加载后补资源。

  * 函数原型：


    
    
    ret_t assets_manager_set_fallback_load_asset (assets_manager_t* am, assets_manager_load_asset_t fallback_load_asset, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
fallback_load_asset | assets_manager_load_asset_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### assets_manager_set_loader 函数

* * *

  * 函数功能：



> 设置loader。

  * 函数原型：


    
    
    ret_t assets_manager_set_loader (assets_manager_t* am, asset_loader_t* loader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
loader | asset_loader_t* | 加载器(由assets manager销毁)。  
  
#### assets_manager_set_locale_info 函数

* * *

  * 函数功能：



> 设置locale_info对象。

  * 函数原型：


    
    
    ret_t assets_manager_set_locale_info (assets_manager_t* am, locale_info_t* locale_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
locale_info | locale_info_t* | locale_info对象。。  
  
#### assets_manager_set_res_root 函数

* * *

  * 函数功能：



> 设置资源所在的目录(其下目录结构请参考demos)。

  * 函数原型：


    
    
    ret_t assets_manager_set_res_root (assets_manager_t* am, const char* res_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
res_root | const char* | 资源所在的目录。  
  
#### assets_manager_set_system_info 函数

* * *

  * 函数功能：



> 设置system_info对象。

  * 函数原型：


    
    
    ret_t assets_manager_set_system_info (assets_manager_t* am, system_info_t* system_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
system_info | system_info_t* | system_info对象。。  
  
#### assets_manager_set_theme 函数

* * *

  * 函数功能：



> 设置当前的主题。

  * 函数原型：


    
    
    ret_t assets_manager_set_theme (assets_manager_t* am, const char* theme);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
theme | const char* | 主题名称。  
  
#### assets_manager_unref 函数

* * *

  * 函数功能：



> 释放指定的资源。

  * 函数原型：


    
    
    ret_t assets_manager_unref (assets_manager_t* am, const asset_info_t* info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | asset manager对象。  
info | const asset_info_t* | 资源。
