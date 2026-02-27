## window_t

### 概述

![image](images/window_t_0.png)

窗口。

缺省的应用程序窗口，占用除system_bar_t之外的整个区域，请不要修改它的位置和大小(除非你清楚后果)。

window_t是[window_base_t](window_base_t.html)的子类控件，window_base_t的函数均适用于window_t控件。

在xml中使用”window”标签创建窗口。无需指定坐标和大小，可以指定窗体样式和动画名称。如：
    
    
    <window theme="basic" anim_hint="htranslate">
    ...
    </window>
    

> 更多用法请参考：[window.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/)

在c代码中使用函数window_create创建窗口。如：
    
    
    widget_t* window = window_create(NULL, 0, 0, 0, 0);
    

> 无需指定父控件、坐标和大小，使用0即可。
> 
> 完整示例请参考：[window demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/)

可用通过style来设置窗口的风格，如背景颜色或图片等。如：
    
    
    <style name="bricks">
    <normal bg_image="bricks"  bg_image_draw_type="repeat"/>
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L0)

* * *

### 函数

函数名称 | 说明  
---|---  
image_blend | 把图片指定的区域渲染到framebuffer指定的区域，src的大小和dst的大小不一致则进行缩放。  
image_clear | 用颜色填充指定的区域。  
image_copy | 把图片指定的区域拷贝到framebuffer中。  
image_fill | 用颜色绘制指定的区域。  
image_rotate | 把图片指定的区域进行旋转并拷贝到framebuffer相应的区域，本函数主要用于辅助实现横屏和竖屏的切换，一般支持90度旋转即可。  
image_rotate_blend | 把图片指定的区域渲染到framebuffer指定的区域，src的大小和dst的大小不一致则进行缩放以及旋转。  
image_rotate_ex | 把图片指定的区域进行旋转。  
window_cast | 转换为window对象(供脚本语言使用)。  
window_close | 关闭窗口。  
window_close_force | 立即无条件关闭窗口(无动画)。  
window_create | 创建window对象  
window_create_default | 以缺省的方式创建window对象。  
window_get_widget_vtable | 获取 window 虚表。  
window_open | 从资源文件中加载并创建window_base对象。本函数在ui_loader/ui_builder_default里实现。  
window_open_and_close | 从资源文件中加载并创建window对象。本函数在ui_loader/ui_builder_default里实现。  
window_set_auto_scale_children | 当设计分辨率和实际分辨率不一致时，自动调整子控件的位置和大小。  
window_set_fullscreen | 设置为全屏窗口。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
fullscreen | bool_t | 是否全屏。  
  
#### image_blend 函数

* * *

  * 函数功能：



> 把图片指定的区域渲染到framebuffer指定的区域，src的大小和dst的大小不一致则进行缩放。

  * 函数原型：


    
    
    ret_t image_blend (bitmap_t* dst, bitmap_t* src, const rectf_t* dst_r, const rectf_t* src_r, uint8_t global_alpha);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败，返回失败则上层用软件实现。  
dst | bitmap_t* | 目标图片对象。  
src | bitmap_t* | 源图片对象。  
dst_r | const rectf_t* | 目的区域。  
src_r | const rectf_t* | 源区域。  
global_alpha | uint8_t | 全局alpha。  
  
#### image_clear 函数

* * *

  * 函数功能：



> 用颜色填充指定的区域。

  * 函数原型：


    
    
    ret_t image_clear (bitmap_t* dst, const rect_t* dst_r, color_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败，返回失败则上层用软件实现。  
dst | bitmap_t* | 目标图片对象。  
dst_r | const rect_t* | 要填充的目标区域。  
c | color_t | 颜色。  
  
#### image_copy 函数

* * *

  * 函数功能：



> 把图片指定的区域拷贝到framebuffer中。

  * 函数原型：


    
    
    ret_t image_copy (bitmap_t* dst, bitmap_t* src, const rect_t* src_r, xy_t dx, xy_t dy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败，返回失败则上层用软件实现。  
dst | bitmap_t* | 目标图片对象。  
src | bitmap_t* | 源图片对象。  
src_r | const rect_t* | 要拷贝的区域。  
dx | xy_t | 目标位置的x坐标。  
dy | xy_t | 目标位置的y坐标。  
  
#### image_fill 函数

* * *

  * 函数功能：



> 用颜色绘制指定的区域。

  * 函数原型：


    
    
    ret_t image_fill (bitmap_t* dst, const rect_t* dst_r, color_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败，返回失败则上层用软件实现。  
dst | bitmap_t* | 目标图片对象。  
dst_r | const rect_t* | 要填充的目标区域。  
c | color_t | 颜色。  
  
#### image_rotate 函数

* * *

  * 函数功能：



> 把图片指定的区域进行旋转并拷贝到framebuffer相应的区域，本函数主要用于辅助实现横屏和竖屏的切换，一般支持90度旋转即可。 备注：旋转方向为逆时针。

  * 函数原型：


    
    
    ret_t image_rotate (bitmap_t* dst, bitmap_t* src, const rect_t* src_r, lcd_orientation_t o);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败，返回失败则上层用软件实现。  
dst | bitmap_t* | 目标图片对象。  
src | bitmap_t* | 源图片对象。  
src_r | const rect_t* | 要旋转并拷贝的区域。  
o | lcd_orientation_t | 旋转角度(一般支持90度即可)。  
  
#### image_rotate_blend 函数

* * *

  * 函数功能：



> 把图片指定的区域渲染到framebuffer指定的区域，src的大小和dst的大小不一致则进行缩放以及旋转。

  * 函数原型：


    
    
    ret_t image_rotate_blend (bitmap_t* dst, bitmap_t* src, const rectf_t* dst_r, const rectf_t* src_r, uint8_t global_alpha, lcd_orientation_t o);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败，返回失败则上层用软件实现。  
dst | bitmap_t* | 目标图片对象。  
src | bitmap_t* | 源图片对象。  
dst_r | const rectf_t* | 目的区域。（坐标原点为旋转后的坐标系原点，并非是 dst 的左上角）  
src_r | const rectf_t* | 源区域。  
global_alpha | uint8_t | 全局alpha。  
o | lcd_orientation_t | 旋转角度(一般支持90度即可，旋转方向为逆时针)。  
  
#### image_rotate_ex 函数

* * *

  * 函数功能：



> 把图片指定的区域进行旋转。

  * 函数原型：


    
    
    ret_t image_rotate_ex (bitmap_t* dst, bitmap_t* src, const rect_t* src_r, xy_t dx, xy_t dy, lcd_orientation_t o);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败，返回失败则上层用软件实现。  
dst | bitmap_t* | 目标图片对象。  
src | bitmap_t* | 源图片对象。  
src_r | const rect_t* | 要旋转并拷贝的区域。  
dx | xy_t | 目标位置的x坐标。（坐标原点为旋转后的坐标系原点，并非是 dst 的左上角）  
dy | xy_t | 目标位置的y坐标。（坐标原点为旋转后的坐标系原点，并非是 dst 的左上角）  
o | lcd_orientation_t | 旋转角度(一般支持90度即可，旋转方向为逆时针)。  
  
#### window_cast 函数

* * *

  * 函数功能：



> 转换为window对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* window_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | window对象。  
widget | widget_t* | window对象。  
  
#### window_close 函数

* * *

  * 函数功能：



> 关闭窗口。

  * 函数原型：


    
    
    ret_t window_close (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window对象。  
  
#### window_close_force 函数

* * *

  * 函数功能：



> 立即无条件关闭窗口(无动画)。

  * 函数原型：


    
    
    ret_t window_close_force (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window对象。  
  
#### window_create 函数

* * *

  * 函数功能：



> 创建window对象

  * 函数原型：


    
    
    widget_t* window_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### window_create_default 函数

* * *

  * 函数功能：



> 以缺省的方式创建window对象。

  * 函数原型：


    
    
    widget_t* window_create_default ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
  
#### window_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 window 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* window_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 window 虚表。  
  
#### window_open 函数

* * *

  * 函数功能：



> 从资源文件中加载并创建window_base对象。本函数在ui_loader/ui_builder_default里实现。

  * 函数原型：


    
    
    widget_t* window_open (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
name | const char* | window的名称。  
  
#### window_open_and_close 函数

* * *

  * 函数功能：



> 从资源文件中加载并创建window对象。本函数在ui_loader/ui_builder_default里实现。

  * 函数原型：


    
    
    widget_t* window_open_and_close (const char* name, widget_t* to_close);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
name | const char* | window的名称。  
to_close | widget_t* | 关闭该窗口。  
  
#### window_set_auto_scale_children 函数

* * *

  * 函数功能：



> 当设计分辨率和实际分辨率不一致时，自动调整子控件的位置和大小。
> 
> 当子控件有self_layout参数或者子控件的父控件有children_layout参数时，不会自动调整。

  * 函数原型：


    
    
    ret_t window_set_auto_scale_children (widget_t* widget, uint32_t design_w, uint32_t design_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window对象。  
design_w | uint32_t | 设计时宽度。  
design_h | uint32_t | 设计时高度。  
  
#### window_set_fullscreen 函数

* * *

  * 函数功能：



> 设置为全屏窗口。
> 
> 如果app_type是SIMULATOR，全屏是指与LCD相同大小，而非让SDL窗口全屏。

  * 函数原型：


    
    
    ret_t window_set_fullscreen (widget_t* widget, bool_t fullscreen);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window对象。  
fullscreen | bool_t | 是否全屏。  
  
#### fullscreen 属性

* * *

> 是否全屏。
> 
> 对于模拟器，全屏是让窗口和LCD具有相同大小，而非让SDL窗口全屏。

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
