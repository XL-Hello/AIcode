## window_manager_t

### 概述

![image](images/window_manager_t_0.png)

## 窗口管理器。

### 函数

函数名称 | 说明  
---|---  
window_manager | 获取全局window_manager对象  
window_manager_back | 请求关闭顶层窗口。  
window_manager_back_to | 回到指定的窗口，关闭之上的全部窗口。  
window_manager_back_to_home | 回到主窗口，关闭之上的全部窗口。  
window_manager_begin_wait_pointer_cursor | 开始等待鼠标指针。  
window_manager_cast | 转换为window_manager对象(供脚本语言使用)。  
window_manager_check_and_layout | 检查各个窗口的layout并且把有需要的执行对应的layout。  
window_manager_close_all | 关闭全部窗口。  
window_manager_close_window_force | 强制立即关闭窗口(内部使用函数，关闭窗口请使用 window_manager_close_window)。  
window_manager_destroy | 销毁window_manager。  
window_manager_dispatch_input_event | 分发输入事件。  
window_manager_dispatch_native_window_event | 处理native window事件。  
window_manager_end_wait_pointer_cursor | 结束等待鼠标指针。  
window_manager_get_foreground_window | 获取前景窗口。  
window_manager_get_input_device_status | 获取输入设备状态。  
window_manager_get_pointer_pressed | 获取指针当前是否按下。  
window_manager_get_pointer_x | 获取指针当前的X坐标。  
window_manager_get_pointer_y | 获取指针当前的Y坐标。  
window_manager_get_prev_window | 获取前一个的窗口。  
window_manager_get_top_main_window | 获取最上面的主窗口。  
window_manager_get_top_window | 获取最上面的窗口。  
window_manager_init | 初始化window_manager。  
window_manager_is_animating | 获取当前窗口动画是否正在播放。  
window_manager_open_window | 打开窗口。  
window_manager_paint | 绘制。  
window_manager_resize | 调整原生窗口的大小。  
window_manager_set | 设置缺省的窗口管理器。  
window_manager_set_cursor | 设置鼠标指针。  
window_manager_set_fullscreen | 设置原生窗口是否全屏。  
window_manager_set_ignore_input_events | 设置是否忽略用户输入事件。  
window_manager_set_max_fps | 限制最大帧率。  
window_manager_set_screen_saver_time | 设置屏保时间(毫秒)。  
window_manager_set_show_fps | 设置是否显示FPS。  
window_manager_set_show_fps_position | 设置显示FPS的起始坐标。  
window_manager_switch_to | 切换到指定窗口。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
global_emitter | emitter_t* | 全局事情分发器。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_TOP_WINDOW_CHANGED | window_event_t | 顶层窗口改变的事件。  
EVT_SCREEN_SAVER | window_event_t | 在指定的时间内，没有用户输入事件，由窗口管理器触发。  
EVT_ORIENTATION_CHANGED | event_t | 屏幕旋转事件。  
EVT_SYSTEM | system_event_t | SDL系统事件。  
  
#### window_manager 函数

* * *

  * 函数功能：



> 获取全局window_manager对象

  * 函数原型：


    
    
    widget_t* window_manager ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
  
#### window_manager_back 函数

* * *

  * 函数功能：



> 请求关闭顶层窗口。
> 
> 如果顶层窗口时模态对话框，用DIALOG_QUIT_NONE调用dialog_quit。

  * 函数原型：


    
    
    ret_t window_manager_back (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_back_to 函数

* * *

  * 函数功能：



> 回到指定的窗口，关闭之上的全部窗口。
> 
> 如果顶层窗口时模态对话框，用DIALOG_QUIT_NONE调用dialog_quit。

  * 函数原型：


    
    
    ret_t window_manager_back_to (widget_t* widget, const char* target);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
target | const char* | 目标窗口的名称。  
  
#### window_manager_back_to_home 函数

* * *

  * 函数功能：



> 回到主窗口，关闭之上的全部窗口。
> 
> 如果顶层窗口时模态对话框，用DIALOG_QUIT_NONE调用dialog_quit。

  * 函数原型：


    
    
    ret_t window_manager_back_to_home (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_begin_wait_pointer_cursor 函数

* * *

  * 函数功能：



> 开始等待鼠标指针。

  * 函数原型：


    
    
    ret_t window_manager_begin_wait_pointer_cursor (widget_t* widget, bool_t ignore_user_input);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。。  
widget | widget_t* | 窗口管理器对象。  
ignore_user_input | bool_t | 是否忽略用户输入。  
  
#### window_manager_cast 函数

* * *

  * 函数功能：



> 转换为window_manager对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* window_manager_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | window_manager对象。  
widget | widget_t* | window_manager对象。  
  
#### window_manager_check_and_layout 函数

* * *

  * 函数功能：



> 检查各个窗口的layout并且把有需要的执行对应的layout。
> 
> 仅由主循环调用。

  * 函数原型：


    
    
    ret_t window_manager_check_and_layout (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_close_all 函数

* * *

  * 函数功能：



> 关闭全部窗口。

  * 函数原型：


    
    
    ret_t window_manager_close_all (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_close_window_force 函数

* * *

  * 函数功能：



> 强制立即关闭窗口(内部使用函数，关闭窗口请使用 window_manager_close_window)。
> 
> 本函数不会执行窗口动画。

  * 函数原型：


    
    
    ret_t window_manager_close_window_force (widget_t* widget, widget_t* window);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
window | widget_t* | 窗口对象。  
  
#### window_manager_destroy 函数

* * *

  * 函数功能：



> 销毁window_manager。

  * 函数原型：


    
    
    ret_t window_manager_destroy (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_manager对象。  
  
#### window_manager_dispatch_input_event 函数

* * *

  * 函数功能：



> 分发输入事件。
> 
> 一般仅由主循环调用，特殊情况也可以用来注入事件。

  * 函数原型：


    
    
    ret_t window_manager_dispatch_input_event (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
e | event_t* | 事件对象。  
  
#### window_manager_dispatch_native_window_event 函数

* * *

  * 函数功能：



> 处理native window事件。

  * 函数原型：


    
    
    ret_t window_manager_dispatch_native_window_event (widget_t* widget, event_t* e, void* handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
e | event_t* | 事件。  
handle | void* | native window句柄。  
  
#### window_manager_end_wait_pointer_cursor 函数

* * *

  * 函数功能：



> 结束等待鼠标指针。

  * 函数原型：


    
    
    ret_t window_manager_end_wait_pointer_cursor (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_foreground_window 函数

* * *

  * 函数功能：



> 获取前景窗口。

  * 函数原型：


    
    
    widget_t* window_manager_get_foreground_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回窗口对象。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_input_device_status 函数

* * *

  * 函数功能：



> 获取输入设备状态。

  * 函数原型：


    
    
    input_device_status_t* window_manager_get_input_device_status (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | input_device_status_t* | 返回输入设备状态。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_pointer_pressed 函数

* * *

  * 函数功能：



> 获取指针当前是否按下。

  * 函数原型：


    
    
    bool_t window_manager_get_pointer_pressed (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回指针当前是否按下。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_pointer_x 函数

* * *

  * 函数功能：



> 获取指针当前的X坐标。

  * 函数原型：


    
    
    xy_t window_manager_get_pointer_x (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | xy_t | 返回指针当前的X坐标。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_pointer_y 函数

* * *

  * 函数功能：



> 获取指针当前的Y坐标。

  * 函数原型：


    
    
    xy_t window_manager_get_pointer_y (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | xy_t | 返回指针当前的X坐标。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_prev_window 函数

* * *

  * 函数功能：



> 获取前一个的窗口。

  * 函数原型：


    
    
    widget_t* window_manager_get_prev_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回窗口对象。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_top_main_window 函数

* * *

  * 函数功能：



> 获取最上面的主窗口。

  * 函数原型：


    
    
    widget_t* window_manager_get_top_main_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回窗口对象。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_get_top_window 函数

* * *

  * 函数功能：



> 获取最上面的窗口。

  * 函数原型：


    
    
    widget_t* window_manager_get_top_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回窗口对象。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_init 函数

* * *

  * 函数功能：



> 初始化window_manager。

  * 函数原型：


    
    
    widget_t* window_manager_init (window_manager_t* wm, const widget_vtable_t* wvt, const window_manager_vtable_t* vt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回window_manager对象。  
wm | window_manager_t* | window_manager对象。  
wvt | const widget_vtable_t* | 控件基类虚表。  
vt | const window_manager_vtable_t* | window_manager虚表。  
  
#### window_manager_is_animating 函数

* * *

  * 函数功能：



> 获取当前窗口动画是否正在播放。

  * 函数原型：


    
    
    bool_t window_manager_is_animating (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示正在播放，FALSE表示没有播放。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_open_window 函数

* * *

  * 函数功能：



> 打开窗口。

  * 函数原型：


    
    
    ret_t window_manager_open_window (widget_t* widget, widget_t* window);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
window | widget_t* | 窗口对象。  
  
#### window_manager_paint 函数

* * *

  * 函数功能：



> 绘制。
> 
> 仅由主循环调用。

  * 函数原型：


    
    
    ret_t window_manager_paint (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_resize 函数

* * *

  * 函数功能：



> 调整原生窗口的大小。

  * 函数原型：


    
    
    ret_t window_manager_resize (widget_t* widget, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### window_manager_set 函数

* * *

  * 函数功能：



> 设置缺省的窗口管理器。

  * 函数原型：


    
    
    ret_t window_manager_set (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
  
#### window_manager_set_cursor 函数

* * *

  * 函数功能：



> 设置鼠标指针。

  * 函数原型：


    
    
    ret_t window_manager_set_cursor (widget_t* widget, const char* cursor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
cursor | const char* | 图片名称(从图片管理器中加载)。  
  
#### window_manager_set_fullscreen 函数

* * *

  * 函数功能：



> 设置原生窗口是否全屏。

  * 函数原型：


    
    
    ret_t window_manager_set_fullscreen (widget_t* widget, bool_t fullscreen);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
fullscreen | bool_t | 是否全屏  
  
#### window_manager_set_ignore_input_events 函数

* * *

  * 函数功能：



> 设置是否忽略用户输入事件。

  * 函数原型：


    
    
    ret_t window_manager_set_ignore_input_events (widget_t* widget, bool_t ignore_input_events);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
ignore_input_events | bool_t | 是否忽略用户输入事件。  
  
#### window_manager_set_max_fps 函数

* * *

  * 函数功能：



> 限制最大帧率。
> 
> TK_MAX_LOOP_FPS/max_fps最好是整数，比如TK_MAX_LOOP_FPS为120，max_fps可取60/30/20/10等。

  * 函数原型：


    
    
    ret_t window_manager_set_max_fps (widget_t* widget, uint32_t max_fps);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
max_fps | uint32_t | 最大帧率。  
  
#### window_manager_set_screen_saver_time 函数

* * *

  * 函数功能：



> 设置屏保时间(毫秒)。

  * 函数原型：


    
    
    ret_t window_manager_set_screen_saver_time (widget_t* widget, uint32_t screen_saver_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
screen_saver_time | uint32_t | 屏保时间(单位毫秒), 为0关闭屏保。  
  
#### window_manager_set_show_fps 函数

* * *

  * 函数功能：



> 设置是否显示FPS。

  * 函数原型：


    
    
    ret_t window_manager_set_show_fps (widget_t* widget, bool_t show_fps);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
show_fps | bool_t | 是否显示FPS。  
  
#### window_manager_set_show_fps_position 函数

* * *

  * 函数功能：



> 设置显示FPS的起始坐标。

  * 函数原型：


    
    
    ret_t window_manager_set_show_fps_position (widget_t* widget, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
x | xy_t | 左上角x坐标。  
y | xy_t | 左上角x坐标。  
  
#### window_manager_switch_to 函数

* * *

  * 函数功能：



> 切换到指定窗口。 备注：会受到模态窗口影响，如果切换的窗口是模态窗口之前的窗口就会失败。
    
    
    window_manager_switch_to(wm, win, widget_child(wm, "home"), FALSE);
    

  * 函数原型：


    
    
    ret_t window_manager_switch_to (widget_t* widget, widget_t* curr_win, widget_t* target_win, bool_t close);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 窗口管理器对象。  
curr_win | widget_t* | 当前窗口。  
target_win | widget_t* | 目标窗口(必须存在，可以用widget_child函数到窗口管理器中查找)。  
close | bool_t | 是否关闭当前窗口。  
  
#### global_emitter 属性

* * *

> 全局事情分发器。

  * 类型：emitter_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
