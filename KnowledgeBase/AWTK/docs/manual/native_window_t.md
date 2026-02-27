## native_window_t

### 概述

![image](images/native_window_t_0.png)

## 原生窗口。

### 函数

函数名称 | 说明  
---|---  
native_window_center | 窗口居中。  
native_window_create | 创建win对象。  
native_window_get_canvas | 获取canvas。  
native_window_get_info | 获取窗口信息。  
native_window_gl_make_current | 设置当前的opengl上下文。  
native_window_invalidate | 请求重绘指定区域。  
native_window_maximize | 最大化窗口。  
native_window_minimize | 最小化窗口。  
native_window_move | 移动窗口。  
native_window_preprocess_event | 预处理事件。  
native_window_resize | 调整窗口大小。  
native_window_restore | 恢复窗口大小。  
native_window_set_cursor | 设置鼠标光标。  
native_window_set_fullscreen | 是否全屏。  
native_window_set_orientation | 调整窗口旋转。  
native_window_set_title | 设置程序窗口的名称。  
native_window_set_window_hit_test | 设置hitTest。  
native_window_show_border | 是否显示边框。  
native_window_swap_buffer | 交换缓冲区。  
  
#### native_window_center 函数

* * *

  * 函数功能：



> 窗口居中。

  * 函数原型：


    
    
    ret_t native_window_center (native_window_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
  
#### native_window_create 函数

* * *

  * 函数功能：



> 创建win对象。

  * 函数原型：


    
    
    native_window_t* native_window_create (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | native_window_t* | 返回win对象。  
widget | widget_t* | widget对象。  
  
#### native_window_get_canvas 函数

* * *

  * 函数功能：



> 获取canvas。

  * 函数原型：


    
    
    canvas_t* native_window_get_canvas (native_window_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | 返回canvas对象。  
win | native_window_t* | win对象。  
  
#### native_window_get_info 函数

* * *

  * 函数功能：



> 获取窗口信息。

  * 函数原型：


    
    
    ret_t native_window_get_info (native_window_t* win, native_window_info_t* info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
info | native_window_info_t* | 窗口信息。  
  
#### native_window_gl_make_current 函数

* * *

  * 函数功能：



> 设置当前的opengl上下文。

  * 函数原型：


    
    
    ret_t native_window_gl_make_current (native_window_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
  
#### native_window_invalidate 函数

* * *

  * 函数功能：



> 请求重绘指定区域。

  * 函数原型：


    
    
    ret_t native_window_invalidate (native_window_t* win, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
r | const rect_t* | 重绘区域。  
  
#### native_window_maximize 函数

* * *

  * 函数功能：



> 最大化窗口。

  * 函数原型：


    
    
    ret_t native_window_maximize (native_window_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
  
#### native_window_minimize 函数

* * *

  * 函数功能：



> 最小化窗口。

  * 函数原型：


    
    
    ret_t native_window_minimize (native_window_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
  
#### native_window_move 函数

* * *

  * 函数功能：



> 移动窗口。

  * 函数原型：


    
    
    ret_t native_window_move (native_window_t* win, xy_t x, xy_t y, bool_t force);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
force | bool_t | 无论是否shared都move。  
  
#### native_window_preprocess_event 函数

* * *

  * 函数功能：



> 预处理事件。

  * 函数原型：


    
    
    ret_t native_window_preprocess_event (native_window_t* win, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
e | event_t* | 事件。  
  
#### native_window_resize 函数

* * *

  * 函数功能：



> 调整窗口大小。

  * 函数原型：


    
    
    ret_t native_window_resize (native_window_t* win, wh_t w, wh_t h, bool_t force);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
w | wh_t | 宽。  
h | wh_t | 高。  
force | bool_t | 无论是否shared都resize。  
  
#### native_window_restore 函数

* * *

  * 函数功能：



> 恢复窗口大小。

  * 函数原型：


    
    
    ret_t native_window_restore (native_window_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
  
#### native_window_set_cursor 函数

* * *

  * 函数功能：



> 设置鼠标光标。

  * 函数原型：


    
    
    ret_t native_window_set_cursor (native_window_t* win, const char* name, bitmap_t* img);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
name | const char* | 鼠标光标的名称。  
img | bitmap_t* | 鼠标光标的图片。  
  
#### native_window_set_fullscreen 函数

* * *

  * 函数功能：



> 是否全屏。

  * 函数原型：


    
    
    ret_t native_window_set_fullscreen (native_window_t* win, bool_t fullscreen);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
fullscreen | bool_t | 是否全屏。  
  
#### native_window_set_orientation 函数

* * *

  * 函数功能：



> 调整窗口旋转。

  * 函数原型：


    
    
    ret_t native_window_set_orientation (native_window_t* win, lcd_orientation_t old_orientation, lcd_orientation_t new_orientation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
old_orientation | lcd_orientation_t | 旧的旋转角度。  
new_orientation | lcd_orientation_t | 新的旋转角度。  
  
#### native_window_set_title 函数

* * *

  * 函数功能：



> 设置程序窗口的名称。

  * 函数原型：


    
    
    ret_t native_window_set_title (native_window_t* win, const char* app_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
app_name | const char* | 程序窗口的名称。  
  
#### native_window_set_window_hit_test 函数

* * *

  * 函数功能：



> 设置hitTest。

  * 函数原型：


    
    
    ret_t native_window_set_window_hit_test (native_window_t* win, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | w宽度。  
h | wh_t | h高度。  
  
#### native_window_show_border 函数

* * *

  * 函数功能：



> 是否显示边框。

  * 函数原型：


    
    
    ret_t native_window_show_border (native_window_t* win, bool_t show);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。  
show | bool_t | 是否显示。  
  
#### native_window_swap_buffer 函数

* * *

  * 函数功能：



> 交换缓冲区。

  * 函数原型：


    
    
    ret_t native_window_swap_buffer (native_window_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
win | native_window_t* | win对象。
