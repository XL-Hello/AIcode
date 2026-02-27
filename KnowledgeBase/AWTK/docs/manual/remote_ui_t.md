## remote_ui_t

### 概述

## remote ui客户端。

### 函数

函数名称 | 说明  
---|---  
remote_ui_back_to_home | 返回主窗口。  
remote_ui_back_to_prev | 返回上一个窗口。  
remote_ui_click | 点击指定的控件。  
remote_ui_close_window | 关闭窗口。  
remote_ui_create | 创建remote ui客户端。  
remote_ui_create_dir | 创建目录。  
remote_ui_create_widget | 创建控件。  
remote_ui_destroy | 销毁remote ui客户端。  
remote_ui_destroy_widget | 销毁控件。  
remote_ui_dispatch | 分发事件。  
remote_ui_download_file | 下载文件。  
remote_ui_exec_fscript | 执行fscript脚本。  
remote_ui_get_dev_info | 获取设备信息。  
remote_ui_get_loaded_assets_info | 获取已经加载的资源。  
remote_ui_get_loaded_images_info | 获取已经加载的图片。  
remote_ui_get_manifest | 获取manifest。  
remote_ui_get_prop | 获取属性。  
remote_ui_get_xml_source | 获取当前窗口的XML源码。  
remote_ui_hook_log | 设置log钩子函数。  
remote_ui_key | 发送按键给控件。  
remote_ui_login | 登录。  
remote_ui_logout | 登出。  
remote_ui_move_widget | 移动控件。  
remote_ui_off_event | 注销事件。  
remote_ui_on_event | 注册事件。  
remote_ui_open_window | 打开窗口。  
remote_ui_reboot | 重新启动。  
remote_ui_remove_dir | 删除目录。  
remote_ui_remove_file | 删除文件。  
remote_ui_resize_widget | 调整控件大小。  
remote_ui_send_event | 发送事件。  
remote_ui_set_language | 设置语言。  
remote_ui_set_prop | 设置属性。  
remote_ui_set_theme | 设置主题。  
remote_ui_show_confirm | 显示确认对话框。  
remote_ui_show_info | 显示信息对话框。  
remote_ui_show_toast | 显示信息对话框。  
remote_ui_show_warn | 显示警告对话框。  
remote_ui_take_snapshot | 截屏。  
remote_ui_unhook_log | 取消log钩子函数。  
remote_ui_upload_file | 上传文件。  
  
#### remote_ui_back_to_home 函数

* * *

  * 函数功能：



> 返回主窗口。

  * 函数原型：


    
    
    ret_t remote_ui_back_to_home (remote_ui_t* ui);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
  
#### remote_ui_back_to_prev 函数

* * *

  * 函数功能：



> 返回上一个窗口。

  * 函数原型：


    
    
    ret_t remote_ui_back_to_prev (remote_ui_t* ui);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
  
#### remote_ui_click 函数

* * *

  * 函数功能：



> 点击指定的控件。

  * 函数原型：


    
    
    ret_t remote_ui_click (remote_ui_t* ui, const char* target);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
  
#### remote_ui_close_window 函数

* * *

  * 函数功能：



> 关闭窗口。

  * 函数原型：


    
    
    ret_t remote_ui_close_window (remote_ui_t* ui, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
name | const char* | 窗口名称。  
  
#### remote_ui_create 函数

* * *

  * 函数功能：



> 创建remote ui客户端。

  * 函数原型：


    
    
    remote_ui_t* remote_ui_create (tk_iostream_t* io);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | remote_ui_t* | 返回remote ui客户端对象。  
io | tk_iostream_t* | IO流。  
  
#### remote_ui_create_dir 函数

* * *

  * 函数功能：



> 创建目录。

  * 函数原型：


    
    
    ret_t remote_ui_create_dir (remote_ui_t* ui, const char* remote_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
remote_dir | const char* | 远程目录。  
  
#### remote_ui_create_widget 函数

* * *

  * 函数功能：



> 创建控件。

  * 函数原型：


    
    
    ret_t remote_ui_create_widget (remote_ui_t* ui, const char* target, const char* xml);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
xml | const char* | XML。  
  
#### remote_ui_destroy 函数

* * *

  * 函数功能：



> 销毁remote ui客户端。

  * 函数原型：


    
    
    ret_t remote_ui_destroy (remote_ui_t* ui);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
  
#### remote_ui_destroy_widget 函数

* * *

  * 函数功能：



> 销毁控件。

  * 函数原型：


    
    
    ret_t remote_ui_destroy_widget (remote_ui_t* ui, const char* target);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
  
#### remote_ui_dispatch 函数

* * *

  * 函数功能：



> 分发事件。

  * 函数原型：


    
    
    ret_t remote_ui_dispatch (remote_ui_t* ui);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
  
#### remote_ui_download_file 函数

* * *

  * 函数功能：



> 下载文件。

  * 函数原型：


    
    
    ret_t remote_ui_download_file (remote_ui_t* ui, const char* remote_file, const char* local_file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
remote_file | const char* | 远程文件。  
local_file | const char* | 本地文件。  
  
#### remote_ui_exec_fscript 函数

* * *

  * 函数功能：



> 执行fscript脚本。

  * 函数原型：


    
    
    ret_t remote_ui_exec_fscript (remote_ui_t* ui, const char* script, str_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
script | const char* | 脚本。  
result | str_t* | 执行结果。  
  
#### remote_ui_get_dev_info 函数

* * *

  * 函数功能：



> 获取设备信息。

  * 函数原型：


    
    
    ret_t remote_ui_get_dev_info (remote_ui_t* ui, remote_ui_dev_info_t* info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
info | remote_ui_dev_info_t* | 设备信息。  
  
#### remote_ui_get_loaded_assets_info 函数

* * *

  * 函数功能：



> 获取已经加载的资源。

  * 函数原型：


    
    
    ret_t remote_ui_get_loaded_assets_info (remote_ui_t* ui, const char* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
file | const char* | 保存数据的文件名。  
  
#### remote_ui_get_loaded_images_info 函数

* * *

  * 函数功能：



> 获取已经加载的图片。

  * 函数原型：


    
    
    ret_t remote_ui_get_loaded_images_info (remote_ui_t* ui, const char* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
file | const char* | 保存数据的文件名。  
  
#### remote_ui_get_manifest 函数

* * *

  * 函数功能：



> 获取manifest。

  * 函数原型：


    
    
    ret_t remote_ui_get_manifest (remote_ui_t* ui, const char* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
file | const char* | 保存数据的文件名。  
  
#### remote_ui_get_prop 函数

* * *

  * 函数功能：



> 获取属性。

  * 函数原型：


    
    
    ret_t remote_ui_get_prop (remote_ui_t* ui, const char* target, const char* name, value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
name | const char* | 属性名称。  
value | value_t* | 属性值。  
  
#### remote_ui_get_xml_source 函数

* * *

  * 函数功能：



> 获取当前窗口的XML源码。

  * 函数原型：


    
    
    ret_t remote_ui_get_xml_source (remote_ui_t* ui, const char* target, const char* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标控件或窗口。  
file | const char* | 保存数据的文件名。  
  
#### remote_ui_hook_log 函数

* * *

  * 函数功能：



> 设置log钩子函数。

  * 函数原型：


    
    
    ret_t remote_ui_hook_log (remote_ui_t* ui, remote_ui_on_log_message_t log, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
log | remote_ui_on_log_message_t | log hook。  
ctx | void* | 上下文。  
  
#### remote_ui_key 函数

* * *

  * 函数功能：



> 发送按键给控件。

  * 函数原型：


    
    
    ret_t remote_ui_key (remote_ui_t* ui, const char* target, int32_t key_code);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
key_code | int32_t | 按键代码。  
  
#### remote_ui_login 函数

* * *

  * 函数功能：



> 登录。

  * 函数原型：


    
    
    ret_t remote_ui_login (remote_ui_t* ui, const char* username, const char* password);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
username | const char* | 用户名。  
password | const char* | 密码。  
  
#### remote_ui_logout 函数

* * *

  * 函数功能：



> 登出。

  * 函数原型：


    
    
    ret_t remote_ui_logout (remote_ui_t* ui);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
  
#### remote_ui_move_widget 函数

* * *

  * 函数功能：



> 移动控件。

  * 函数原型：


    
    
    ret_t remote_ui_move_widget (remote_ui_t* ui, const char* target, int32_t x, int32_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
x | int32_t | x坐标。  
y | int32_t | y坐标。  
  
#### remote_ui_off_event 函数

* * *

  * 函数功能：



> 注销事件。

  * 函数原型：


    
    
    ret_t remote_ui_off_event (remote_ui_t* ui, const char* target, uint32_t event, event_func_t func, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
event | uint32_t | 事件。  
func | event_func_t | 事件处理函数。  
ctx | void* | 上下文。  
  
#### remote_ui_on_event 函数

* * *

  * 函数功能：



> 注册事件。

  * 函数原型：


    
    
    ret_t remote_ui_on_event (remote_ui_t* ui, const char* target, uint32_t event, event_func_t func, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
event | uint32_t | 事件。  
func | event_func_t | 事件处理函数。  
ctx | void* | 上下文。  
  
#### remote_ui_open_window 函数

* * *

  * 函数功能：



> 打开窗口。

  * 函数原型：


    
    
    ret_t remote_ui_open_window (remote_ui_t* ui, const char* name, const char* xml, const char* init_json);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
name | const char* | 窗口名称。  
xml | const char* | 窗口XML。  
init_json | const char* | 初始化JSON。  
  
#### remote_ui_reboot 函数

* * *

  * 函数功能：



> 重新启动。

  * 函数原型：


    
    
    ret_t remote_ui_reboot (remote_ui_t* ui, remote_ui_reboot_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
type | remote_ui_reboot_type_t | 重启类型。  
  
#### remote_ui_remove_dir 函数

* * *

  * 函数功能：



> 删除目录。

  * 函数原型：


    
    
    ret_t remote_ui_remove_dir (remote_ui_t* ui, const char* remote_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
remote_dir | const char* | 远程目录。  
  
#### remote_ui_remove_file 函数

* * *

  * 函数功能：



> 删除文件。

  * 函数原型：


    
    
    ret_t remote_ui_remove_file (remote_ui_t* ui, const char* remote_file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
remote_file | const char* | 远程文件。  
  
#### remote_ui_resize_widget 函数

* * *

  * 函数功能：



> 调整控件大小。

  * 函数原型：


    
    
    ret_t remote_ui_resize_widget (remote_ui_t* ui, const char* target, uint32_t w, uint32_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
  
#### remote_ui_send_event 函数

* * *

  * 函数功能：



> 发送事件。

  * 函数原型：


    
    
    ret_t remote_ui_send_event (remote_ui_t* ui, const char* target, event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
event | event_t* | 事件。  
  
#### remote_ui_set_language 函数

* * *

  * 函数功能：



> 设置语言。

  * 函数原型：


    
    
    ret_t remote_ui_set_language (remote_ui_t* ui, const char* language);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
language | const char* | 语言名称。  
  
#### remote_ui_set_prop 函数

* * *

  * 函数功能：



> 设置属性。

  * 函数原型：


    
    
    ret_t remote_ui_set_prop (remote_ui_t* ui, const char* target, const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标。  
name | const char* | 属性名称。  
value | const value_t* | 属性值。  
  
#### remote_ui_set_theme 函数

* * *

  * 函数功能：



> 设置主题。

  * 函数原型：


    
    
    ret_t remote_ui_set_theme (remote_ui_t* ui, const char* theme);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
theme | const char* | 主题名称。  
  
#### remote_ui_show_confirm 函数

* * *

  * 函数功能：



> 显示确认对话框。

  * 函数原型：


    
    
    ret_t remote_ui_show_confirm (remote_ui_t* ui, const char* title, const char* content);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
title | const char* | 标题。  
content | const char* | 内容。  
  
#### remote_ui_show_info 函数

* * *

  * 函数功能：



> 显示信息对话框。

  * 函数原型：


    
    
    ret_t remote_ui_show_info (remote_ui_t* ui, const char* title, const char* content);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
title | const char* | 标题。  
content | const char* | 内容。  
  
#### remote_ui_show_toast 函数

* * *

  * 函数功能：



> 显示信息对话框。

  * 函数原型：


    
    
    ret_t remote_ui_show_toast (remote_ui_t* ui, uint32_t duration, const char* content);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
duration | uint32_t | 时长。  
content | const char* | 内容。  
  
#### remote_ui_show_warn 函数

* * *

  * 函数功能：



> 显示警告对话框。

  * 函数原型：


    
    
    ret_t remote_ui_show_warn (remote_ui_t* ui, const char* title, const char* content);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
title | const char* | 标题。  
content | const char* | 内容。  
  
#### remote_ui_take_snapshot 函数

* * *

  * 函数功能：



> 截屏。

  * 函数原型：


    
    
    ret_t remote_ui_take_snapshot (remote_ui_t* ui, const char* target, const char* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
target | const char* | 目标控件或窗口。  
file | const char* | 保存截图文件名。  
  
#### remote_ui_unhook_log 函数

* * *

  * 函数功能：



> 取消log钩子函数。

  * 函数原型：


    
    
    ret_t remote_ui_unhook_log (remote_ui_t* ui);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
  
#### remote_ui_upload_file 函数

* * *

  * 函数功能：



> 上传文件。

  * 函数原型：


    
    
    ret_t remote_ui_upload_file (remote_ui_t* ui, const char* remote_file, const char* local_file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_t* | remote ui客户端对象。  
remote_file | const char* | 远程文件。  
local_file | const char* | 本地文件。
