## file_chooser_t

### 概述

![image](images/file_chooser_t_0.png)

## 文件/目录选择器

### 函数

函数名称 | 说明  
---|---  
file_chooser_cast | 转换为file_chooser对象(供脚本语言使用)。  
file_chooser_choose_file_for_open | 为了打开而选择文件。  
file_chooser_choose_file_for_save | 为了保存而选择文件。  
file_chooser_choose_folder | 选择目录。  
file_chooser_create | 创建file_chooser对象  
file_chooser_destroy | 销毁file_chooser对象(选择完成后自动调用)。  
file_chooser_get_dir | 获取目录。  
file_chooser_get_filename | 获取文件名。  
file_chooser_is_aborted | 用户是否取消了选择。  
file_chooser_set_filter | 设置过滤规则。  
file_chooser_set_init_dir | 设置初始目录。  
file_chooser_set_top_dir | 设置初始目录。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
aborted | bool_t | 是否取消了选择。  
cwd | str_t | 当前路径。  
filename | str_t | 当前选择的文件。  
filter | char* | 过滤规则。  
init_dir | char* | 初始目录。  
on_done | tk_on_done_t | 接受结果的回调函数。  
on_done_ctx | void* | 用户数据。  
top_dir | char* | 最顶层目录。到达本目录后，不允许往上。  
  
#### file_chooser_cast 函数

* * *

  * 函数功能：



> 转换为file_chooser对象(供脚本语言使用)。

  * 函数原型：


    
    
    file_chooser_t* file_chooser_cast (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | file_chooser_t* | 对象。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_choose_file_for_open 函数

* * *

  * 函数功能：



> 为了打开而选择文件。

  * 函数原型：


    
    
    ret_t file_chooser_choose_file_for_open (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_choose_file_for_save 函数

* * *

  * 函数功能：



> 为了保存而选择文件。

  * 函数原型：


    
    
    ret_t file_chooser_choose_file_for_save (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_choose_folder 函数

* * *

  * 函数功能：



> 选择目录。

  * 函数原型：


    
    
    ret_t file_chooser_choose_folder (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_create 函数

* * *

  * 函数功能：



> 创建file_chooser对象

  * 函数原型：


    
    
    file_chooser_t* file_chooser_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | file_chooser_t* | 对象。  
  
#### file_chooser_destroy 函数

* * *

  * 函数功能：



> 销毁file_chooser对象(选择完成后自动调用)。

  * 函数原型：


    
    
    ret_t file_chooser_destroy (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_get_dir 函数

* * *

  * 函数功能：



> 获取目录。

  * 函数原型：


    
    
    const char* file_chooser_get_dir (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回选择的目录。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_get_filename 函数

* * *

  * 函数功能：



> 获取文件名。

  * 函数原型：


    
    
    const char* file_chooser_get_filename (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回选择的文件名。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_is_aborted 函数

* * *

  * 函数功能：



> 用户是否取消了选择。

  * 函数原型：


    
    
    bool_t file_chooser_is_aborted (file_chooser_t* chooser);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回用户是否取消了选择。  
chooser | file_chooser_t* | file_chooser对象。  
  
#### file_chooser_set_filter 函数

* * *

  * 函数功能：



> 设置过滤规则。 files_only 表示只列出文件，dir_only 表示只列出目录，其它表示只列出满足扩展名文件集合(如：.jpg.png.gif)。

  * 函数原型：


    
    
    ret_t file_chooser_set_filter (file_chooser_t* chooser, const char* filter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
chooser | file_chooser_t* | file_chooser对象。  
filter | const char* | 过滤规则。  
  
#### file_chooser_set_init_dir 函数

* * *

  * 函数功能：



> 设置初始目录。

  * 函数原型：


    
    
    ret_t file_chooser_set_init_dir (file_chooser_t* chooser, const char* init_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
chooser | file_chooser_t* | file_chooser对象。  
init_dir | const char* | 初始目录  
  
#### file_chooser_set_top_dir 函数

* * *

  * 函数功能：



> 设置初始目录。

  * 函数原型：


    
    
    ret_t file_chooser_set_top_dir (file_chooser_t* chooser, const char* top_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
chooser | file_chooser_t* | file_chooser对象。  
top_dir | const char* | 初始目录  
  
#### aborted 属性

* * *

> 是否取消了选择。

  * 类型：bool_t



#### cwd 属性

* * *

> 当前路径。

  * 类型：str_t



#### filename 属性

* * *

> 当前选择的文件。

  * 类型：str_t



#### filter 属性

* * *

> 过滤规则。

  * 类型：char*



#### init_dir 属性

* * *

> 初始目录。

  * 类型：char*



#### on_done 属性

* * *

> 接受结果的回调函数。

  * 类型：tk_on_done_t



#### on_done_ctx 属性

* * *

> 用户数据。

  * 类型：void*



#### top_dir 属性

* * *

> 最顶层目录。到达本目录后，不允许往上。

  * 类型：char*


