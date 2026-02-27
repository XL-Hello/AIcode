## progress_circle_t

### 概述

![image](images/progress_circle_t_0.png)

进度圆环控件。

progress_circle_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于progress_circle_t控件。

在xml中使用”progress_circle”标签创建进度圆环控件。如：
    
    
    <progress_circle max="360" show_text="true" start_angle="90" />
    

> 更多用法请参考： [progress_circle.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/progress_circle.xml)

在c代码中使用函数progress_circle_create创建进度圆环控件。如：
    
    
    progress_circle = progress_circle_create(win, 10, 10, 200, 200);
    progress_circle_set_max(progress_circle, 360);
    widget_set_value(progress_circle, 128);
    

> 完整示例请参考： [progress_circle demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/progress_circle.c)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <style name="default">
    <normal text_color="green" fg_color="black" />
    </style>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L467)

* * *

### 函数

函数名称 | 说明  
---|---  
progress_circle_calc_line_dirty_rect | 获取progress_circle的新值和旧值之间的绘制脏矩形。  
progress_circle_cast | 转换为progress_circle对象(供脚本语言使用)。  
progress_circle_create | 创建progress_circle对象  
progress_circle_get_widget_vtable | 获取 progress_circle 虚表。  
progress_circle_set_counter_clock_wise | 设置是否为逆时针方向。  
progress_circle_set_format | 设置格式。  
progress_circle_set_line_cap | 设置线帽类型。  
progress_circle_set_line_width | 设置环线的厚度。  
progress_circle_set_max | 设置最大值。  
progress_circle_set_show_text | 设置是否显示文本。  
progress_circle_set_start_angle | 设置起始角度。  
progress_circle_set_value | 设置值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
counter_clock_wise | bool_t | 是否为逆时针方向(缺省为FALSE)。  
format | char* | 数值到字符串转换时的格式，缺省为”%d”。  
line_cap | char* | 线帽类型(round:圆头，square:方头，butt:平头)。  
line_width | uint32_t | 环线的厚度(缺省为8)，line_width > r/2时，使用扇形绘制。  
max | float_t | 最大值(缺省为100)。  
show_text | bool_t | 是否显示文本(缺省为TRUE)。  
start_angle | int32_t | 起始角度(单位为度，缺省-90)。  
value | float_t | 值(缺省为0)。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值改变事件。  
  
#### progress_circle_calc_line_dirty_rect 函数

* * *

  * 函数功能：



> 获取progress_circle的新值和旧值之间的绘制脏矩形。

  * 函数原型：


    
    
    rect_t progress_circle_calc_line_dirty_rect (widget_t* widget, float_t old_value, float_t new_value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t | 返回脏矩形。  
widget | widget_t* | progress_circle控件对象。  
old_value | float_t | 旧值。  
new_value | float_t | 新值。  
  
#### progress_circle_cast 函数

* * *

  * 函数功能：



> 转换为progress_circle对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* progress_circle_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | progress_circle对象。  
widget | widget_t* | progress_circle对象。  
  
#### progress_circle_create 函数

* * *

  * 函数功能：



> 创建progress_circle对象

  * 函数原型：


    
    
    widget_t* progress_circle_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### progress_circle_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 progress_circle 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* progress_circle_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 progress_circle 虚表。  
  
#### progress_circle_set_counter_clock_wise 函数

* * *

  * 函数功能：



> 设置是否为逆时针方向。

  * 函数原型：


    
    
    ret_t progress_circle_set_counter_clock_wise (widget_t* widget, bool_t counter_clock_wise);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
counter_clock_wise | bool_t | 是否为逆时针方向。  
  
#### progress_circle_set_format 函数

* * *

  * 函数功能：



> 设置格式。

  * 函数原型：


    
    
    ret_t progress_circle_set_format (widget_t* widget, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | progress_circle对象。  
format | const char* | 格式。  
  
#### progress_circle_set_line_cap 函数

* * *

  * 函数功能：



> 设置线帽类型。

  * 函数原型：


    
    
    ret_t progress_circle_set_line_cap (widget_t* widget, const char* line_cap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
line_cap | const char* | 线帽类型(round:圆头，square:方头)。。  
  
#### progress_circle_set_line_width 函数

* * *

  * 函数功能：



> 设置环线的厚度。

  * 函数原型：


    
    
    ret_t progress_circle_set_line_width (widget_t* widget, uint32_t line_width);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
line_width | uint32_t | 环线的厚度。  
  
#### progress_circle_set_max 函数

* * *

  * 函数功能：



> 设置最大值。

  * 函数原型：


    
    
    ret_t progress_circle_set_max (widget_t* widget, uint32_t max);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
max | uint32_t | 最大值。  
  
#### progress_circle_set_show_text 函数

* * *

  * 函数功能：



> 设置是否显示文本。

  * 函数原型：


    
    
    ret_t progress_circle_set_show_text (widget_t* widget, bool_t show_text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
show_text | bool_t | 是否显示文本。  
  
#### progress_circle_set_start_angle 函数

* * *

  * 函数功能：



> 设置起始角度。

  * 函数原型：


    
    
    ret_t progress_circle_set_start_angle (widget_t* widget, int32_t start_angle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
start_angle | int32_t | 起始角度。  
  
#### progress_circle_set_value 函数

* * *

  * 函数功能：



> 设置值。

  * 函数原型：


    
    
    ret_t progress_circle_set_value (widget_t* widget, float_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
value | float_t | 值。  
  
#### counter_clock_wise 属性

* * *

> 是否为逆时针方向(缺省为FALSE)。

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
  
#### format 属性

* * *

> 数值到字符串转换时的格式，缺省为”%d”。

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
  
#### line_cap 属性

* * *

> 线帽类型(round:圆头，square:方头，butt:平头)。

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
  
#### line_width 属性

* * *

> 环线的厚度(缺省为8)，line_width > r/2时，使用扇形绘制。

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
  
#### max 属性

* * *

> 最大值(缺省为100)。

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
  
#### show_text 属性

* * *

> 是否显示文本(缺省为TRUE)。

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
  
#### start_angle 属性

* * *

> 起始角度(单位为度，缺省-90)。

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
  
#### value 属性

* * *

> 值(缺省为0)。

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
