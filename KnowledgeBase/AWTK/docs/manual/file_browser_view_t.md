## file_browser_view_t

### 概述

![image](images/file_browser_view_t_0.png)

文件管理/浏览/选择控件。

file_browser_view_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于file_browser_view_t控件。

考虑到文件浏览器界面呈现的多样性，界面呈现工作完全有子控件来完成。

file_browser_view_t负责关联文件/文件夹数据到子控件上，子控件需要特定的规范命名。

  * 名为 “cwd” 的子控件用于显示当前路径。

  * 名为 “selected_file” 的子控件用于显示当前选择的文件。

  * 名为 “file” 的子控件用于显示文件项的模板控件。

  * 名为 “folder” 的子控件用于显示文件夹项的模板控件。

  * 名为 “return_up” 的子控件用于返回上一级文件夹的模板控件。

  * 名为 “container” 的子控件为容器控件，通常是scrollview。

  * 名为 “name” 的子控件用于显示文件和文件夹的名称(放在列表项目内)。

  * 名为 “size” 的子控件用于显示文件和文件夹的大小(放在列表项目内)。

  * 名为 “mtime” 的子控件用于显示文件和文件夹的修改时间(放在列表项目内)。

  * 名为 “ctime” 的子控件用于显示文件和文件夹的创建时间(放在列表项目内)。

  * 名为 “icon” 的子控件用于显示文件和文件夹的图标(放在列表项目内)。

  * 类型为 “check_button” 的子控件用于选择(放在列表项目内)。




完整示例请参考：

## https://github.com/zlgopen/awtk/blob/master/design/default/ui/file_chooser_for_open.xml

### 函数

函数名称 | 说明  
---|---  
file_browser_view_cast | 转换为file_browser_view对象(供脚本语言使用)。  
file_browser_view_create | 创建file_browser_view对象  
file_browser_view_create_dir | 在当前文件夹创建子文件夹。  
file_browser_view_create_file | 在当前文件夹创建文件。  
file_browser_view_get_cwd | 获取当前路径。  
file_browser_view_get_selected_items | 返回当前选中的项目。  
file_browser_view_get_widget_vtable | 获取 file_browser_view 虚表。  
file_browser_view_reload | 重新加载。  
file_browser_view_set_even_item_style | 设置 偶数项样式。  
file_browser_view_set_filter | 设置 过滤规则。  
file_browser_view_set_ignore_hidden_files | 设置 忽略隐藏文件。  
file_browser_view_set_init_dir | 设置 初始文件夹。  
file_browser_view_set_odd_item_style | 设置 奇数项样式。  
file_browser_view_set_show_check_button | 设置 是否显示checkbutton。  
file_browser_view_set_sort_ascending | 设置 是否为升序排序。  
file_browser_view_set_sort_by | 设置 排序方式。可选值(name, size, mtime, type)。  
file_browser_view_set_top_dir | 设置 顶层文件夹。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
even_item_style | char* | 偶数项样式。  
filter | char* | 过滤规则。  
ignore_hidden_files | bool_t | 是否忽略隐藏文件。  
init_dir | char* | 初始文件夹。  
odd_item_style | char* | 奇数项样式。  
show_check_button | bool_t | 是否显示checkbutton。  
sort_ascending | bool_t | 是否为升序排序。  
sort_by | char* | 排序方式。可选值(name, size, mtime, type)。  
top_dir | char* | 最顶层目录。到达本目录后，不允许往上。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_CHANGED | value_change_event_t | 值(当前显示目录)改变事件。  
  
#### file_browser_view_cast 函数

* * *

  * 函数功能：



> 转换为file_browser_view对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* file_browser_view_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | file_browser_view对象。  
widget | widget_t* | file_browser_view对象。  
  
#### file_browser_view_create 函数

* * *

  * 函数功能：



> 创建file_browser_view对象

  * 函数原型：


    
    
    widget_t* file_browser_view_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### file_browser_view_create_dir 函数

* * *

  * 函数功能：



> 在当前文件夹创建子文件夹。

  * 函数原型：


    
    
    ret_t file_browser_view_create_dir (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
name | const char* | 子文件夹名。  
  
#### file_browser_view_create_file 函数

* * *

  * 函数功能：



> 在当前文件夹创建文件。

  * 函数原型：


    
    
    ret_t file_browser_view_create_file (widget_t* widget, const char* name, const char* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
name | const char* | 文件名。  
data | const char* | 数据。  
size | uint32_t | 数据长度。  
  
#### file_browser_view_get_cwd 函数

* * *

  * 函数功能：



> 获取当前路径。

  * 函数原型：


    
    
    const char* file_browser_view_get_cwd (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回当前路径。  
widget | widget_t* | widget对象。  
  
#### file_browser_view_get_selected_items 函数

* * *

  * 函数功能：



> 返回当前选中的项目。
> 
> 在返回数组中，每个元素是一个fb_item_t对象。 调用者无需释放返回值，返回值只在当次调用有效。

  * 函数原型：


    
    
    darray_t* file_browser_view_get_selected_items (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | darray_t* | 返回当前选中的项目。  
widget | widget_t* | widget对象。  
  
#### file_browser_view_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 file_browser_view 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* file_browser_view_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 file_browser_view 虚表。  
  
#### file_browser_view_reload 函数

* * *

  * 函数功能：



> 重新加载。

  * 函数原型：


    
    
    ret_t file_browser_view_reload (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### file_browser_view_set_even_item_style 函数

* * *

  * 函数功能：



> 设置 偶数项样式。

  * 函数原型：


    
    
    ret_t file_browser_view_set_even_item_style (widget_t* widget, const char* even_item_style);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
even_item_style | const char* | 奇数项样式。  
  
#### file_browser_view_set_filter 函数

* * *

  * 函数功能：



> 设置 过滤规则。 files_only 表示只列出文件，dir_only 表示只列出目录，其它表示只列出满足扩展名文件集合(如：.jpg.png.gif)。

  * 函数原型：


    
    
    ret_t file_browser_view_set_filter (widget_t* widget, const char* filter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
filter | const char* | 过滤规则。  
  
#### file_browser_view_set_ignore_hidden_files 函数

* * *

  * 函数功能：



> 设置 忽略隐藏文件。

  * 函数原型：


    
    
    ret_t file_browser_view_set_ignore_hidden_files (widget_t* widget, bool_t ignore_hidden_files);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
ignore_hidden_files | bool_t | 忽略隐藏文件。  
  
#### file_browser_view_set_init_dir 函数

* * *

  * 函数功能：



> 设置 初始文件夹。

  * 函数原型：


    
    
    ret_t file_browser_view_set_init_dir (widget_t* widget, const char* init_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
init_dir | const char* | 初始文件夹。  
  
#### file_browser_view_set_odd_item_style 函数

* * *

  * 函数功能：



> 设置 奇数项样式。

  * 函数原型：


    
    
    ret_t file_browser_view_set_odd_item_style (widget_t* widget, const char* odd_item_style);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
odd_item_style | const char* | 奇数项样式。  
  
#### file_browser_view_set_show_check_button 函数

* * *

  * 函数功能：



> 设置 是否显示checkbutton。

  * 函数原型：


    
    
    ret_t file_browser_view_set_show_check_button (widget_t* widget, bool_t show_check_button);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
show_check_button | bool_t | 是否显示checkbutton。  
  
#### file_browser_view_set_sort_ascending 函数

* * *

  * 函数功能：



> 设置 是否为升序排序。

  * 函数原型：


    
    
    ret_t file_browser_view_set_sort_ascending (widget_t* widget, bool_t sort_ascending);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
sort_ascending | bool_t | 是否为升序排序。  
  
#### file_browser_view_set_sort_by 函数

* * *

  * 函数功能：



> 设置 排序方式。可选值(name, size, mtime, type)。

  * 函数原型：


    
    
    ret_t file_browser_view_set_sort_by (widget_t* widget, const char* sort_by);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
sort_by | const char* | 排序方式。可选值(name, size, mtime, type)。  
  
#### file_browser_view_set_top_dir 函数

* * *

  * 函数功能：



> 设置 顶层文件夹。

  * 函数原型：


    
    
    ret_t file_browser_view_set_top_dir (widget_t* widget, const char* top_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
top_dir | const char* | 初始文件夹。  
  
#### even_item_style 属性

* * *

> 偶数项样式。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### filter 属性

* * *

> 过滤规则。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### ignore_hidden_files 属性

* * *

> 是否忽略隐藏文件。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### init_dir 属性

* * *

> 初始文件夹。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### odd_item_style 属性

* * *

> 奇数项样式。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### show_check_button 属性

* * *

> 是否显示checkbutton。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### sort_ascending 属性

* * *

> 是否为升序排序。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### sort_by 属性

* * *

> 排序方式。可选值(name, size, mtime, type)。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### top_dir 属性

* * *

> 最顶层目录。到达本目录后，不允许往上。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是
