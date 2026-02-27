## plugin_manager_t

### 概述

## 插件管理器。

### 函数

函数名称 | 说明  
---|---  
plugin_manager_create | 创建插件管理器。  
plugin_manager_destroy | 卸载全部插件，并销毁插件管理器对象。  
plugin_manager_dump | 显示所有的插件。  
plugin_manager_exist | 检查指定的插件是否存在。  
plugin_manager_refresh | 重新扫描目录中的插件，加载没有加载的插件。  
plugin_manager_reload | 卸载所有插件并重新加载。  
  
#### plugin_manager_create 函数

* * *

  * 函数功能：



> 创建插件管理器。

  * 函数原型：


    
    
    plugin_manager_t* plugin_manager_create (const char* path, plugin_get_init_func_name_t get_init, plugin_get_deinit_func_name_t get_deinit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | plugin_manager_t* | 动态链接库对象。  
path | const char* | 插件所在的目录。  
get_init | plugin_get_init_func_name_t | 获取初始化函数的函数名。为NULL时使用”init”。  
get_deinit | plugin_get_deinit_func_name_t | 获取~初始化函数的函数名。为NULL时使用”deinit”。  
  
#### plugin_manager_destroy 函数

* * *

  * 函数功能：



> 卸载全部插件，并销毁插件管理器对象。

  * 函数原型：


    
    
    ret_t plugin_manager_destroy (plugin_manager_t* plugin_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
plugin_manager | plugin_manager_t* | plugin_manager对象。  
  
#### plugin_manager_dump 函数

* * *

  * 函数功能：



> 显示所有的插件。

  * 函数原型：


    
    
    ret_t plugin_manager_dump (plugin_manager_t* plugin_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
plugin_manager | plugin_manager_t* | plugin_manager对象。  
  
#### plugin_manager_exist 函数

* * *

  * 函数功能：



> 检查指定的插件是否存在。

  * 函数原型：


    
    
    bool_t plugin_manager_exist (plugin_manager_t* plugin_manager, const char* lib_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
plugin_manager | plugin_manager_t* | plugin_manager对象。  
lib_name | const char* | 动态库的名称。  
  
#### plugin_manager_refresh 函数

* * *

  * 函数功能：



> 重新扫描目录中的插件，加载没有加载的插件。

  * 函数原型：


    
    
    ret_t plugin_manager_refresh (plugin_manager_t* plugin_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
plugin_manager | plugin_manager_t* | plugin_manager对象。  
  
#### plugin_manager_reload 函数

* * *

  * 函数功能：



> 卸载所有插件并重新加载。

  * 函数原型：


    
    
    ret_t plugin_manager_reload (plugin_manager_t* plugin_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
plugin_manager | plugin_manager_t* | plugin_manager对象。
