## text_selector_t

### 概述

![image](images/text_selector_t_0.png)

文本选择器控件，通常用于选择日期和时间等。

> XXX: 目前需要先设置options和visible_nr，再设置其它参数(在XML中也需要按此顺序)。

text_selector_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于text_selector_t控件。

在xml中使用”text_selector”标签创建文本选择器控件。如：
    
    
    <text_selector options="red;green;blue;gold;orange" visible_nr="3" text="red"/>
    

> 更多用法请参考：[text_selector.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/text_selector.xml)

在c代码中使用函数text_selector_create创建文本选择器控件。如：
    
    
    widget_t* ts = text_selector_create(win, 10, 10, 80, 150);
    text_selector_set_options(ts, "1:red;2:green;3:blue;4:orange;5:gold");
    text_selector_set_value(ts, 1);
    widget_use_style(ts, "dark");
    

> 完整示例请参考：[text_selector demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/text_selector.c)

可用通过style来设置控件的显示风格，如字体和背景颜色等。如：
    
    
    <style name="dark" fg_color="#a0a0a0"  text_color="black" text_align_h="center">
    <normal     bg_color="#ffffff" mask_color="#404040" border_color="#404040"/>
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L443)

* * *

### 函数

函数名称 | 说明  
---|---  
text_selector_append_option | 追加一个选项。  
text_selector_cast | 转换text_selector对象(供脚本语言使用)。  
text_selector_count_options | 获取选项个数。  
text_selector_create | 创建text_selector对象  
text_selector_get_option | 获取第index个选项。  
text_selector_get_text | 获取text_selector的文本。  
text_selector_get_value | 获取text_selector的值。  
text_selector_get_widget_vtable | 获取 text_selector 虚表。  
text_selector_reset_options | 重置所有选项。  
text_selector_set_animating_time | 设置滚动动画播放时间。  
text_selector_set_ellipses | 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为…  
text_selector_set_enable_value_animator | 设置是否修改值时启用动画。  
text_selector_set_localize_options | 设置是否本地化(翻译)选项。  
text_selector_set_loop_options | 设置是否循环选项。  
text_selector_set_mask_area_scale | 设置绘制蒙版的区域占比（范围0~1）。  
text_selector_set_mask_easing | 设置绘制蒙版的变化趋势。  
text_selector_set_options | 设置选项。  
text_selector_set_range_options | 设置一系列的整数选项。  
text_selector_set_range_options_ex | 设置一系列的整数选项。  
text_selector_set_selected_index | 设置第index个选项为当前选中的选项。  
text_selector_set_text | 设置text_selector的文本。  
text_selector_set_value | 设置text_selector的值。  
text_selector_set_visible_nr | 设置可见的选项数。  
text_selector_set_yspeed_scale | 设置Y轴偏移速度比例。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
animating_time | uint32_t | 滚动动画播放时间。(单位毫秒)  
ellipses | bool_t | 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为…  
enable_value_animator | bool_t | 是否修改值时启用动画。  
localize_options | bool_t | 是否本地化(翻译)选项(缺省为FALSE)。  
loop_options | bool_t | 是否循环选项(缺省为FALSE)。  
mask_area_scale | float_t | 绘制蒙版的区域占比（范围0~1）。  
mask_easing | easing_type_t | 绘制蒙版的变化趋势。  
options | char* | 设置可选项(英文冒号(:)分隔值和文本，英文分号(;)分隔选项，如:1:red;2:green;3:blue)。  
selected_index | int32_t | 当前选中的选项。  
visible_nr | uint32_t | 可见的选项数量(只能是1或者3或者5，缺省为5)。  
yspeed_scale | float_t | y偏移速度比例。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(当前项)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(当前项)改变事件。  
  
#### text_selector_append_option 函数

* * *

  * 函数功能：



> 追加一个选项。

  * 函数原型：


    
    
    ret_t text_selector_append_option (widget_t* widget, int32_t value, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
value | int32_t | 值。  
text | const char* | 文本。  
  
#### text_selector_cast 函数

* * *

  * 函数功能：



> 转换text_selector对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* text_selector_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | text_selector对象。  
widget | widget_t* | text_selector对象。  
  
#### text_selector_count_options 函数

* * *

  * 函数功能：



> 获取选项个数。

  * 函数原型：


    
    
    int32_t text_selector_count_options (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回选项个数。  
widget | widget_t* | text_selector对象。  
  
#### text_selector_create 函数

* * *

  * 函数功能：



> 创建text_selector对象

  * 函数原型：


    
    
    widget_t* text_selector_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### text_selector_get_option 函数

* * *

  * 函数功能：



> 获取第index个选项。

  * 函数原型：


    
    
    text_selector_option_t* text_selector_get_option (widget_t* widget, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | text_selector_option_t* | 成功返回选项，失败返回NULL。  
widget | widget_t* | text_selector对象。  
index | uint32_t | 选项的索引。  
  
#### text_selector_get_text 函数

* * *

  * 函数功能：



> 获取text_selector的文本。

  * 函数原型：


    
    
    const char* text_selector_get_text (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回文本。  
widget | widget_t* | text_selector对象。  
  
#### text_selector_get_value 函数

* * *

  * 函数功能：



> 获取text_selector的值。

  * 函数原型：


    
    
    int32_t text_selector_get_value (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回值。  
widget | widget_t* | text_selector对象。  
  
#### text_selector_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 text_selector 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* text_selector_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 text_selector 虚表。  
  
#### text_selector_reset_options 函数

* * *

  * 函数功能：



> 重置所有选项。

  * 函数原型：


    
    
    ret_t text_selector_reset_options (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
  
#### text_selector_set_animating_time 函数

* * *

  * 函数功能：



> 设置滚动动画播放时间。

  * 函数原型：


    
    
    ret_t text_selector_set_animating_time (widget_t* widget, uint32_t animating_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
animating_time | uint32_t | 滚动动画播放时间。(单位毫秒)  
  
#### text_selector_set_ellipses 函数

* * *

  * 函数功能：



> 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为…

  * 函数原型：


    
    
    ret_t text_selector_set_ellipses (widget_t* widget, bool_t ellipses);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
ellipses | bool_t | 是否开启缩写。  
  
#### text_selector_set_enable_value_animator 函数

* * *

  * 函数功能：



> 设置是否修改值时启用动画。

  * 函数原型：


    
    
    ret_t text_selector_set_enable_value_animator (widget_t* widget, bool_t enable_value_animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
enable_value_animator | bool_t | 是否修改值时启用动画  
  
#### text_selector_set_localize_options 函数

* * *

  * 函数功能：



> 设置是否本地化(翻译)选项。

  * 函数原型：


    
    
    ret_t text_selector_set_localize_options (widget_t* widget, bool_t localize_options);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
localize_options | bool_t | 是否本地化(翻译)选项。  
  
#### text_selector_set_loop_options 函数

* * *

  * 函数功能：



> 设置是否循环选项。

  * 函数原型：


    
    
    ret_t text_selector_set_loop_options (widget_t* widget, bool_t loop_options);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
loop_options | bool_t | 是否循环选项。  
  
#### text_selector_set_mask_area_scale 函数

* * *

  * 函数功能：



> 设置绘制蒙版的区域占比（范围0~1）。

  * 函数原型：


    
    
    ret_t text_selector_set_mask_area_scale (widget_t* widget, float_t mask_area_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
mask_area_scale | float_t | 绘制蒙版的区域占比（范围0~1）。  
  
#### text_selector_set_mask_easing 函数

* * *

  * 函数功能：



> 设置绘制蒙版的变化趋势。

  * 函数原型：


    
    
    ret_t text_selector_set_mask_easing (widget_t* widget, easing_type_t mask_easing);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
mask_easing | easing_type_t | 绘制蒙版的变化趋势。  
  
#### text_selector_set_options 函数

* * *

  * 函数功能：



> 设置选项。

  * 函数原型：


    
    
    ret_t text_selector_set_options (widget_t* widget, const char* options);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
options | const char* | 选项。  
  
#### text_selector_set_range_options 函数

* * *

  * 函数功能：



> 设置一系列的整数选项。

  * 函数原型：


    
    
    ret_t text_selector_set_range_options (widget_t* widget, int32_t start, uint32_t nr, int32_t step);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
start | int32_t | 起始值。  
nr | uint32_t | 个数。  
step | int32_t | 步长。  
  
#### text_selector_set_range_options_ex 函数

* * *

  * 函数功能：



> 设置一系列的整数选项。

  * 函数原型：


    
    
    ret_t text_selector_set_range_options_ex (widget_t* widget, int32_t start, uint32_t nr, int32_t step, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
start | int32_t | 起始值。  
nr | uint32_t | 个数。  
step | int32_t | 步长。  
format | const char* | 选项的格式化。  
  
#### text_selector_set_selected_index 函数

* * *

  * 函数功能：



> 设置第index个选项为当前选中的选项。

  * 函数原型：


    
    
    ret_t text_selector_set_selected_index (widget_t* widget, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
index | uint32_t | 选项的索引。  
  
#### text_selector_set_text 函数

* * *

  * 函数功能：



> 设置text_selector的文本。

  * 函数原型：


    
    
    ret_t text_selector_set_text (widget_t* widget, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
text | const char* | 文本。  
  
#### text_selector_set_value 函数

* * *

  * 函数功能：



> 设置text_selector的值。

  * 函数原型：


    
    
    ret_t text_selector_set_value (widget_t* widget, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
value | int32_t | 值。  
  
#### text_selector_set_visible_nr 函数

* * *

  * 函数功能：



> 设置可见的选项数。

  * 函数原型：


    
    
    ret_t text_selector_set_visible_nr (widget_t* widget, uint32_t visible_nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | text_selector对象。  
visible_nr | uint32_t | 选项数。  
  
#### text_selector_set_yspeed_scale 函数

* * *

  * 函数功能：



> 设置Y轴偏移速度比例。

  * 函数原型：


    
    
    ret_t text_selector_set_yspeed_scale (widget_t* widget, float_t yspeed_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
yspeed_scale | float_t | y偏移速度比例。  
  
#### animating_time 属性

* * *

> 滚动动画播放时间。(单位毫秒)

  * 类型：uint32_t

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
  
#### ellipses 属性

* * *

> 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为…

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
  
#### enable_value_animator 属性

* * *

> 是否修改值时启用动画。

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
  
#### localize_options 属性

* * *

> 是否本地化(翻译)选项(缺省为FALSE)。

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
  
#### loop_options 属性

* * *

> 是否循环选项(缺省为FALSE)。

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
  
#### mask_area_scale 属性

* * *

> 绘制蒙版的区域占比（范围0~1）。

  * 类型：float_t

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
  
#### mask_easing 属性

* * *

> 绘制蒙版的变化趋势。

  * 类型：easing_type_t

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
  
#### options 属性

* * *

> 设置可选项(英文冒号(:)分隔值和文本，英文分号(;)分隔选项，如:1:red;2:green;3:blue)。 对于数值选项，也可以指定一个范围，用英文负号(-)分隔起始值、结束值和格式。 如：”1-7-%02d”表示1到7，格式为『02d』，格式为可选，缺省为『%d』。 如果数据本身中有英文冒号(:)、英文分号(;)和英文负号(-)。请用16进制转义。 * 英文冒号(:)写为\x3a * 英文冒号(;)写为\x3b * 英文冒号(-)写为\x2d

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
  
#### selected_index 属性

* * *

> 当前选中的选项。

  * 类型：int32_t

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
  
#### visible_nr 属性

* * *

> 可见的选项数量(只能是1或者3或者5，缺省为5)。

  * 类型：uint32_t

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
  
#### yspeed_scale 属性

* * *

> y偏移速度比例。

  * 类型：float_t

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
