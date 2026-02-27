## assets_managers_t

### 概述

在某些情况下，需要多个资源管理器。比如在手表系统里，每个小应用或表盘，可能放在独立的资源包中， 此时优先加载应用自己的资源，如果没有就加载系统的资源。

> 通常AWTK是单进程应用程序，为了避免概念混淆，我们把这些独立可安装的小应用成为”applet”。

* * *

### 函数

函数名称 | 说明  
---|---  
assets_manager_get_theme_name | 获取当前的主题名称。  
assets_managers_add_applet_res_root | 添加小应用程序(applet)的资源根目录。  
assets_managers_clear_applet_res_roots | 清除全部小应用程序(applet)的资源根目录。  
assets_managers_clear_cache | 清除指定类型的全部缓存。  
assets_managers_is_applet_assets_supported | 是否支持小应用程序(applet)拥有独立资源目录。  
assets_managers_ref | 获取指定小应用程序(applet)的资源管理器。  
assets_managers_remove_applet_res_root | 删除小应用程序(applet)的资源根目录。  
assets_managers_set_applet_res_root | 设置小应用程序(applet)的资源根目录。  
assets_managers_set_theme | 设置当前的主题。  
assets_managers_unref | 释放指定小应用程序(applet)的资源管理器。  
  
#### assets_manager_get_theme_name 函数

* * *

  * 函数功能：



> 获取当前的主题名称。

  * 函数原型：


    
    
    const char* assets_manager_get_theme_name (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回主题名称。  
am | assets_manager_t* | 资源管理器对象。  
  
#### assets_managers_add_applet_res_root 函数

* * *

  * 函数功能：



> 添加小应用程序(applet)的资源根目录。

  * 函数原型：


    
    
    ret_t assets_managers_add_applet_res_root (const char* res_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
res_root | const char* | 资源根目录。  
  
#### assets_managers_clear_applet_res_roots 函数

* * *

  * 函数功能：



> 清除全部小应用程序(applet)的资源根目录。

  * 函数原型：


    
    
    ret_t assets_managers_clear_applet_res_roots ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### assets_managers_clear_cache 函数

* * *

  * 函数功能：



> 清除指定类型的全部缓存。

  * 函数原型：


    
    
    ret_t assets_managers_clear_cache (asset_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
type | asset_type_t | 资源的类型。  
  
#### assets_managers_is_applet_assets_supported 函数

* * *

  * 函数功能：



> 是否支持小应用程序(applet)拥有独立资源目录。

  * 函数原型：


    
    
    bool_t assets_managers_is_applet_assets_supported ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示支持，否则表示不支持。  
  
#### assets_managers_ref 函数

* * *

  * 函数功能：



> 获取指定小应用程序(applet)的资源管理器。

  * 函数原型：


    
    
    assets_manager_t* assets_managers_ref (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | assets_manager_t* | 返回asset manager对象。  
name | const char* | 小应用程序(applet)的名称。  
  
#### assets_managers_remove_applet_res_root 函数

* * *

  * 函数功能：



> 删除小应用程序(applet)的资源根目录。

  * 函数原型：


    
    
    ret_t assets_managers_remove_applet_res_root (const char* res_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
res_root | const char* | 资源根目录。  
  
#### assets_managers_set_applet_res_root 函数

* * *

  * 函数功能：



> 设置小应用程序(applet)的资源根目录。

  * 函数原型：


    
    
    ret_t assets_managers_set_applet_res_root (const char* res_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
res_root | const char* | 资源根目录。  
  
#### assets_managers_set_theme 函数

* * *

  * 函数功能：



> 设置当前的主题。

  * 函数原型：


    
    
    ret_t assets_managers_set_theme (const char* theme);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
theme | const char* | 主题名称。  
  
#### assets_managers_unref 函数

* * *

  * 函数功能：



> 释放指定小应用程序(applet)的资源管理器。

  * 函数原型：


    
    
    ret_t assets_managers_unref (assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | assets_manager_t* | 资源管理器对象。
