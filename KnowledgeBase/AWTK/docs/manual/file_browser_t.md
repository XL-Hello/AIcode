## file_browser_t

### 概述

## 文件浏览器模型。

### 函数

函数名称 | 说明  
---|---  
file_browser_create | 创建file_browser对象  
file_browser_create_dir | 在当前目录下创建指定子目录。  
file_browser_create_file | 在当前目录下创建指定文件。  
file_browser_destroy | 销毁file_browser对象  
file_browser_enter | 进入当前目录下的指定子目录。  
file_browser_get_item | 获取指定项序数的项目。  
file_browser_get_items_nr | 获取当前目录下文件项个数。  
file_browser_refresh | 刷新。  
file_browser_remove | 删除当前目录下的指定子目录或文件。  
file_browser_set_compare | 设置排序用的比较函数。  
file_browser_set_cwd | 设置当前目录。  
file_browser_set_filter | 设置过滤函数。  
file_browser_set_ignore_hidden_files | 设置是否忽略隐藏文件。  
file_browser_set_top_dir | 设置顶层目录。  
file_browser_sort_by_mtime | 按修改时间排序。  
file_browser_sort_by_name | 按名称排序。  
file_browser_sort_by_size | 按大小排序。  
file_browser_sort_by_type | 按类型排序。  
file_browser_up | 返回上一级目录。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
cwd | char* | 当前路径。  
top_dir | char* | 最顶层目录。到达本目录后，不允许往上。  
  
#### file_browser_create 函数

* * *

  * 函数功能：



> 创建file_browser对象

  * 函数原型：


    
    
    file_browser_t* file_browser_create (fs_t* fs);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | file_browser_t* | 对象。  
fs | fs_t* | 文件系统对象。  
  
#### file_browser_create_dir 函数

* * *

  * 函数功能：



> 在当前目录下创建指定子目录。

  * 函数原型：


    
    
    ret_t file_browser_create_dir (file_browser_t* fb, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
name | const char* | 当前目录下的子目录名。  
  
#### file_browser_create_file 函数

* * *

  * 函数功能：



> 在当前目录下创建指定文件。

  * 函数原型：


    
    
    ret_t file_browser_create_file (file_browser_t* fb, const char* name, const void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
name | const char* | 当前目录下的文件名。  
buff | const void* | 文件内容。  
size | uint32_t | 文件内容的长度。  
  
#### file_browser_destroy 函数

* * *

  * 函数功能：



> 销毁file_browser对象

  * 函数原型：


    
    
    ret_t file_browser_destroy (file_browser_t* fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
  
#### file_browser_enter 函数

* * *

  * 函数功能：



> 进入当前目录下的指定子目录。

  * 函数原型：


    
    
    ret_t file_browser_enter (file_browser_t* fb, const char* dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
dir | const char* | 当前目录下的子目录名。  
  
#### file_browser_get_item 函数

* * *

  * 函数功能：



> 获取指定项序数的项目。

  * 函数原型：


    
    
    fb_item_t* file_browser_get_item (file_browser_t* fb, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fb_item_t* | 返回指定项序数的项目。  
fb | file_browser_t* | file browser对象。  
index | uint32_t | 序数。  
  
#### file_browser_get_items_nr 函数

* * *

  * 函数功能：



> 获取当前目录下文件项个数。

  * 函数原型：


    
    
    uint32_t file_browser_get_items_nr (file_browser_t* fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回当前目录下文件项个数。  
fb | file_browser_t* | file browser对象。  
  
#### file_browser_refresh 函数

* * *

  * 函数功能：



> 刷新。

  * 函数原型：


    
    
    ret_t file_browser_refresh (file_browser_t* fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
  
#### file_browser_remove 函数

* * *

  * 函数功能：



> 删除当前目录下的指定子目录或文件。

  * 函数原型：


    
    
    ret_t file_browser_remove (file_browser_t* fb, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
name | const char* | 当前目录下的子目录名/文件名。  
  
#### file_browser_set_compare 函数

* * *

  * 函数功能：



> 设置排序用的比较函数。

  * 函数原型：


    
    
    ret_t file_browser_set_compare (file_browser_t* fb, tk_compare_t compare);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
compare | tk_compare_t | 排序用的比较函数。  
  
#### file_browser_set_cwd 函数

* * *

  * 函数功能：



> 设置当前目录。 目录支持变量：
    
    
    ${app_dir} -> app 文件目录。
    ${temp_dir} -> 临时文件目录。
    ${user_dir} -> 用户目录。
    

  * 函数原型：


    
    
    ret_t file_browser_set_cwd (file_browser_t* fb, const char* cwd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
cwd | const char* | 当前目录。  
  
#### file_browser_set_filter 函数

* * *

  * 函数功能：



> 设置过滤函数。

  * 函数原型：


    
    
    ret_t file_browser_set_filter (file_browser_t* fb, tk_filter_t filter, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
filter | tk_filter_t | 过滤函数。  
ctx | void* | 过滤函数的上下文。  
  
#### file_browser_set_ignore_hidden_files 函数

* * *

  * 函数功能：



> 设置是否忽略隐藏文件。

  * 函数原型：


    
    
    ret_t file_browser_set_ignore_hidden_files (file_browser_t* fb, bool_t ignore_hidden_files);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
ignore_hidden_files | bool_t | 是否忽略隐藏文件。  
  
#### file_browser_set_top_dir 函数

* * *

  * 函数功能：



> 设置顶层目录。

目录支持变量：
    
    
    ${app_dir} -> app 文件目录。
    ${temp_dir} -> 临时文件目录。
    ${user_dir} -> 用户目录。
    

  * 函数原型：


    
    
    ret_t file_browser_set_top_dir (file_browser_t* fb, const char* top_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
top_dir | const char* | 顶层目录。  
  
#### file_browser_sort_by_mtime 函数

* * *

  * 函数功能：



> 按修改时间排序。

  * 函数原型：


    
    
    ret_t file_browser_sort_by_mtime (file_browser_t* fb, bool_t ascending);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
ascending | bool_t | 按升序排。  
  
#### file_browser_sort_by_name 函数

* * *

  * 函数功能：



> 按名称排序。

  * 函数原型：


    
    
    ret_t file_browser_sort_by_name (file_browser_t* fb, bool_t ascending);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
ascending | bool_t | 按升序排。  
  
#### file_browser_sort_by_size 函数

* * *

  * 函数功能：



> 按大小排序。

  * 函数原型：


    
    
    ret_t file_browser_sort_by_size (file_browser_t* fb, bool_t ascending);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
ascending | bool_t | 按升序排。  
  
#### file_browser_sort_by_type 函数

* * *

  * 函数功能：



> 按类型排序。

  * 函数原型：


    
    
    ret_t file_browser_sort_by_type (file_browser_t* fb, bool_t ascending);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
ascending | bool_t | 按升序排。  
  
#### file_browser_up 函数

* * *

  * 函数功能：



> 返回上一级目录。

  * 函数原型：


    
    
    ret_t file_browser_up (file_browser_t* fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fb | file_browser_t* | file browser对象。  
  
#### cwd 属性

* * *

> 当前路径。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### top_dir 属性

* * *

> 最顶层目录。到达本目录后，不允许往上。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
