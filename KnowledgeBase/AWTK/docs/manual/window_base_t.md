## window_base_t

### 概述

![image](images/window_base_t_0.png)

窗口。

本类把窗口相关的公共行为进行抽象，放到一起方便重用。目前已知的具体实现如下图：

![image](images/window_base_t_1.png)

## > 本类是一个抽象类，不能进行实例化。请在应用程序中使用具体的类，如window_t。

### 函数

函数名称 | 说明  
---|---  
window_base_auto_scale_children | 根据参数自动缩放子控件。  
window_base_cast | 转换为window_base对象(供脚本语言使用)。  
window_base_create | 创建window base对象。  
window_base_get_prop | 窗口get_prop函数的缺省实现。  
window_base_get_widget_vtable | 获取 window_base 虚表。  
window_base_invalidate | 窗口on_invalidate函数的缺省实现。  
window_base_on_copy | 默认拷贝函数。  
window_base_on_destroy | 窗口on_destroy函数的缺省实现。  
window_base_on_event | 窗口on_event函数的缺省实现。  
window_base_on_paint_begin | 窗口on_paint_begin函数的缺省实现。  
window_base_on_paint_end | 窗口on_paint_end函数的缺省实现。  
window_base_on_paint_self | 窗口on_paint_self函数的缺省实现。  
window_base_set_need_relayout | 设置是否需要relayout  
window_base_set_prop | 窗口set_prop函数的缺省实现。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
applet_name | char* | 小应用程序(applet)的名称。  
assets_manager | assets_manager_t* | 获取资源管理器对象。  
auto_scale_children_h | bool_t | 窗口大小与设计时大小不同时，是否自动调整子控件的高度。  
auto_scale_children_w | bool_t | 窗口大小与设计时大小不同时，是否自动调整子控件的宽度。  
auto_scale_children_x | bool_t | 窗口大小与设计时大小不同时，是否自动调整子控件的x坐标。  
auto_scale_children_y | bool_t | 窗口大小与设计时大小不同时，是否自动调整子控件的y坐标。  
closable | window_closable_t | 收到EVT_REQUEST_CLOSE_WINDOW是否自动关闭窗口。  
close_anim_hint | char* | 关闭窗口动画的名称。  
design_h | uint16_t | 设计时高度。  
design_w | uint16_t | 设计时宽度。  
disable_anim | bool_t | 禁用窗口动画。  
font_manager | font_manager_t* | 获取字体管理器对象。  
image_manager | image_manager_t* | 获取图片管理器对象。  
locale_info | locale_info_t* | 获取多国语言字符串管理器对象。  
move_focus_down_key | char* | 向下移动焦点的键值。  
move_focus_left_key | char* | 向左移动焦点的键值。  
move_focus_next_key | char* | 向后移动焦点的键值。  
move_focus_prev_key | char* | 向前移动焦点的键值。  
move_focus_right_key | char* | 向右移动焦点的键值。  
move_focus_up_key | char* | 向上移动焦点的键值。  
open_anim_hint | char* | 打开窗口动画的名称。  
single_instance | bool_t | 单例。如果窗口存在，先关闭再打开。  
stage | window_stage_t | 窗口当前处于的状态。  
strongly_focus | bool_t | 点击非focusable控件时，是否让当前焦点控件失去焦点。比如点击窗口空白区域，是否让编辑器失去焦点。  
theme | char* | 窗体样式资源的名称。  
theme_obj | theme_t* | 窗口的常量窗体样式数据。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_WINDOW_WILL_OPEN | event_t | 窗口即将打开事件。 如果有窗口动画，在窗口动画开始前触发。如果没有窗口动画，在窗口被加载后的下一次循环中触发。  
EVT_WINDOW_OPEN | event_t | 窗口打开事件。 如果有窗口动画，在窗口动画完成时触发。如果没有窗口动画，在窗口被加载后的下一次循环中触发。  
EVT_WINDOW_TO_BACKGROUND | event_t | 窗口被切换到后台事件。 打开新窗口时，当前窗口被切换到后台时，对当前窗口触发本事件。  
EVT_WINDOW_TO_FOREGROUND | event_t | 窗口被切换到前台事件。 关闭当前窗口时，前一个窗口被切换到前台时，对前一个窗口触发本事件。  
EVT_WINDOW_CLOSE | event_t | 窗口关闭事件。  
EVT_WINDOW_LOAD | event_t | 窗口加载完成事件。  
EVT_REQUEST_CLOSE_WINDOW | event_t | 请求关闭窗口的事件。  
EVT_LOCALE_CHANGED | event_t | locale改变的事件。  
  
#### window_base_auto_scale_children 函数

* * *

  * 函数功能：



> 根据参数自动缩放子控件。

  * 函数原型：


    
    
    ret_t window_base_auto_scale_children (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
  
#### window_base_cast 函数

* * *

  * 函数功能：



> 转换为window_base对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* window_base_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | window_base对象。  
widget | widget_t* | window_base对象。  
  
#### window_base_create 函数

* * *

  * 函数功能：



> 创建window base对象。

  * 函数原型：


    
    
    widget_t* window_base_create (widget_t* parent, const widget_vtable_t* vt, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 窗口对象。  
parent | widget_t* | 父控件  
vt | const widget_vtable_t* | vtable对象。  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### window_base_get_prop 函数

* * *

  * 函数功能：



> 窗口get_prop函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_get_prop (widget_t* widget, const char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。。  
widget | widget_t* | window_base对象。g  
name | const char* | 属性名。  
v | value_t* | value对象  
  
#### window_base_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 window_base 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* window_base_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 window_base 虚表。  
  
#### window_base_invalidate 函数

* * *

  * 函数功能：



> 窗口on_invalidate函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_invalidate (widget_t* widget, const rect_t* rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
rect | const rect_t* | rect对象。  
  
#### window_base_on_copy 函数

* * *

  * 函数功能：



> 默认拷贝函数。

  * 函数原型：


    
    
    ret_t window_base_on_copy (widget_t* widget, widget_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。。  
widget | widget_t* | window_base对象。  
other | widget_t* | other window_base对象。  
  
#### window_base_on_destroy 函数

* * *

  * 函数功能：



> 窗口on_destroy函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_on_destroy (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
  
#### window_base_on_event 函数

* * *

  * 函数功能：



> 窗口on_event函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_on_event (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
e | event_t* | event对象。  
  
#### window_base_on_paint_begin 函数

* * *

  * 函数功能：



> 窗口on_paint_begin函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_on_paint_begin (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
c | canvas_t* | canvas对象。  
  
#### window_base_on_paint_end 函数

* * *

  * 函数功能：



> 窗口on_paint_end函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_on_paint_end (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。1  
widget | widget_t* | window_base对象。  
c | canvas_t* | canvas对象。  
  
#### window_base_on_paint_self 函数

* * *

  * 函数功能：



> 窗口on_paint_self函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_on_paint_self (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
c | canvas_t* | canvas对象。  
  
#### window_base_set_need_relayout 函数

* * *

  * 函数功能：



> 设置是否需要relayout

  * 函数原型：


    
    
    ret_t window_base_set_need_relayout (widget_t* widget, bool_t need_relayout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
need_relayout | bool_t | 是否需要relayout。  
  
#### window_base_set_prop 函数

* * *

  * 函数功能：



> 窗口set_prop函数的缺省实现。

  * 函数原型：


    
    
    ret_t window_base_set_prop (widget_t* widget, const char* name, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | window_base对象。  
name | const char* | 属性名。  
v | const value_t* | value对象  
  
#### applet_name 属性

* * *

> 小应用程序(applet)的名称。
> 
> 如果该窗口属于某个独立的小程序应用(applet)，需要指定它的名称，以便到对应的资源目录查找资源。

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
  
#### assets_manager 属性

* * *

> 获取资源管理器对象。
> 
> 把资源管理器对象与窗口关联起来，是为了解决UI设计器与被设计的窗口需要从不同的位置加载资源资源的问题。

  * 类型：assets_manager_t*

特性 | 是否支持  
---|---  
可直接读取 | 否  
可直接修改 | 否  
可通过widget_get_prop读取 | 是  
  
#### auto_scale_children_h 属性

* * *

> 窗口大小与设计时大小不同时，是否自动调整子控件的高度。

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
  
#### auto_scale_children_w 属性

* * *

> 窗口大小与设计时大小不同时，是否自动调整子控件的宽度。

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
  
#### auto_scale_children_x 属性

* * *

> 窗口大小与设计时大小不同时，是否自动调整子控件的x坐标。

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
  
#### auto_scale_children_y 属性

* * *

> 窗口大小与设计时大小不同时，是否自动调整子控件的y坐标。

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
  
#### closable 属性

* * *

> 收到EVT_REQUEST_CLOSE_WINDOW是否自动关闭窗口。

如果关闭窗口时，需要用户确认:

  * 1.将closable设置为WINDOW_CLOSABLE_CONFIRM

  * 2.处理窗口的EVT_REQUEST_CLOSE_WINDOW事件




> closable在XML中取值为：yes/no/confirm，缺省为yes。

  * 类型：window_closable_t

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
  
#### close_anim_hint 属性

* * *

> 关闭窗口动画的名称。 请参考[窗口动画](https://github.com/zlgopen/awtk/blob/master/docs/window_animator.html)

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
  
#### design_h 属性

* * *

> 设计时高度。

  * 类型：uint16_t

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
  
#### design_w 属性

* * *

> 设计时宽度。

  * 类型：uint16_t

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
  
#### disable_anim 属性

* * *

> 禁用窗口动画。

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
  
#### font_manager 属性

* * *

> 获取字体管理器对象。
> 
> 把字体管理器对象与窗口关联起来，是为了解决UI设计器与被设计的窗口需要从不同的位置加载字体资源的问题。

  * 类型：font_manager_t*

特性 | 是否支持  
---|---  
可直接读取 | 否  
可直接修改 | 否  
可通过widget_get_prop读取 | 是  
  
#### image_manager 属性

* * *

> 获取图片管理器对象。
> 
> 把图片管理器对象与窗口关联起来，是为了解决UI设计器与被设计的窗口需要从不同的位置加载图片资源的问题。

  * 类型：image_manager_t*

特性 | 是否支持  
---|---  
可直接读取 | 否  
可直接修改 | 否  
可通过widget_get_prop读取 | 是  
  
#### locale_info 属性

* * *

> 获取多国语言字符串管理器对象。
> 
> 把多国语言字符串管理器对象与窗口关联起来，是为了解决UI设计器与被设计的窗口需要从不同的位置加载资源资源的问题。

  * 类型：locale_info_t*

特性 | 是否支持  
---|---  
可直接读取 | 否  
可直接修改 | 否  
可通过widget_get_prop读取 | 是  
  
#### move_focus_down_key 属性

* * *

> 向下移动焦点的键值。

请参考[控件焦点](https://github.com/zlgopen/awtk/blob/master/docs/widget_focus.html)

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
  
#### move_focus_left_key 属性

* * *

> 向左移动焦点的键值。

请参考[控件焦点](https://github.com/zlgopen/awtk/blob/master/docs/widget_focus.html)

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
  
#### move_focus_next_key 属性

* * *

> 向后移动焦点的键值。

请参考[控件焦点](https://github.com/zlgopen/awtk/blob/master/docs/widget_focus.html)

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
  
#### move_focus_prev_key 属性

* * *

> 向前移动焦点的键值。

请参考[控件焦点](https://github.com/zlgopen/awtk/blob/master/docs/widget_focus.html)

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
  
#### move_focus_right_key 属性

* * *

> 向右移动焦点的键值。

请参考[控件焦点](https://github.com/zlgopen/awtk/blob/master/docs/widget_focus.html)

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
  
#### move_focus_up_key 属性

* * *

> 向上移动焦点的键值。

请参考[控件焦点](https://github.com/zlgopen/awtk/blob/master/docs/widget_focus.html)

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
  
#### open_anim_hint 属性

* * *

> 打开窗口动画的名称。 请参考[窗口动画](https://github.com/zlgopen/awtk/blob/master/docs/window_animator.html)

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
  
#### single_instance 属性

* * *

> 单例。如果窗口存在，先关闭再打开。

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
  
#### stage 属性

* * *

> 窗口当前处于的状态。

  * 类型：window_stage_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可通过widget_get_prop读取 | 是  
  
#### strongly_focus 属性

* * *

> 点击非focusable控件时，是否让当前焦点控件失去焦点。比如点击窗口空白区域，是否让编辑器失去焦点。

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
  
#### theme 属性

* * *

> 窗体样式资源的名称。 每个窗口都可以有独立的窗体样式文件，如果没指定，则使用系统缺省的窗体样式文件。 窗体样式是一个XML文件，放在assets/raw/styles目录下。 请参考[窗体样式](https://github.com/zlgopen/awtk/blob/master/docs/theme.html)

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
  
#### theme_obj 属性

* * *

> 窗口的常量窗体样式数据。
> 
> 把窗体样式管理器对象与窗口关联起来，是为了解决UI设计器与被设计的窗口需要从不同的位置加载窗体样式资源的问题。

  * 类型：theme_t*

特性 | 是否支持  
---|---  
可直接读取 | 否  
可直接修改 | 否  
可通过widget_get_prop读取 | 是
