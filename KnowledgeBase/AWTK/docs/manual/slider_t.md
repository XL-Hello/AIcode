## slider_t

### 概述

![image](images/slider_t_0.png)

滑块控件。

slider_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于slider_t控件。

在xml中使用”slider”标签创建滑块控件。如：
    
    
    <slider x="center" y="10" w="80%" h="20" value="10"/>
    <slider style="img" x="center" y="50" w="80%" h="30" value="20" />
    <slider style="img" x="center" y="90" w="80%" h="30" value="30" min="5" max="50" step="5"/>
    

> 更多用法请参考： [basic](https://github.com/zlgopen/awtk/blob/master/design/default/ui/basic.xml)

在c代码中使用函数slider_create创建滑块控件。如：
    
    
    widget_t* slider = slider_create(win, 10, 10, 200, 30);
    widget_on(slider, EVT_VALUE_CHANGED, on_changed, NULL);
    widget_on(slider, EVT_VALUE_CHANGING, on_changing, NULL);
    

> 完整示例请参考： [slider demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/slider.c)

可用通过style来设置控件的显示风格，如图片和颜色等等。如：
    
    
    <style name="img" bg_image="slider_bg" fg_image="slider_fg">
    <normal icon="slider_drag"/>
    <pressed icon="slider_drag_p"/>
    <over icon="slider_drag_o"/>
    </style>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L179)

* * *

### 函数

函数名称 | 说明  
---|---  
slider_cast | 转换为slider对象(供脚本语言使用)。  
slider_create | 创建slider对象  
slider_get_widget_vtable | 获取 slider 虚表。  
slider_set_bar_size | 设置bar的宽度或高度。  
slider_set_drag_threshold | 设置拖拽临界值。  
slider_set_line_cap | 设置前景色的线帽形状。（默认为跟随风格的圆角设置，但是在没有设置圆角的时候无法使用 “round” 来设置圆角）  
slider_set_max | 设置滑块的最大值。  
slider_set_min | 设置滑块的最小值。  
slider_set_step | 设置滑块的拖动的最小单位。  
slider_set_value | 设置滑块的值。  
slider_set_value_internal | 设置滑块的值(public for test)。  
slider_set_vertical | 设置滑块的方向。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
bar_size | uint32_t | 轴的宽度或高度（单位：像素），为0表示为控件的宽度或高度的一半，缺省为0。  
drag_threshold | uint32_t | 拖动临界值。  
dragger_adapt_to_icon | bool_t | 滑块的宽度或高度是否与icon适应，缺省为true。  
dragger_size | uint32_t | 滑块的宽度或高度（单位：像素），缺省为 bar_size * 1.5。  
line_cap | char* | 前景色的线帽形状。（取值：butt  
max | double | 最大值。  
min | double | 最小值。  
slide_with_bar | bool_t | 是否允许在轴上滑动来改变滑块位置，缺省为FALSE。  
step | double | 拖动的最小单位。  
value | double | 值。  
vertical | bool_t | 滑块的是否为垂直方向。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值即将改变事件。  
EVT_VALUE_CHANGING | value_change_event_t | 值正在改变事件(拖动中)。  
EVT_VALUE_CHANGED | value_change_event_t | 值改变事件。  
  
#### slider_cast 函数

* * *

  * 函数功能：



> 转换为slider对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* slider_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | slider对象。  
widget | widget_t* | slider对象。  
  
#### slider_create 函数

* * *

  * 函数功能：



> 创建slider对象

  * 函数原型：


    
    
    widget_t* slider_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### slider_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 slider 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* slider_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 slider 虚表。  
  
#### slider_set_bar_size 函数

* * *

  * 函数功能：



> 设置bar的宽度或高度。

  * 函数原型：


    
    
    ret_t slider_set_bar_size (widget_t* widget, uint32_t bar_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
bar_size | uint32_t | bar的宽度或高度。  
  
#### slider_set_drag_threshold 函数

* * *

  * 函数功能：



> 设置拖拽临界值。

  * 函数原型：


    
    
    ret_t slider_set_drag_threshold (widget_t* widget, uint32_t drag_threshold);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
drag_threshold | uint32_t | 拖拽临界值。  
  
#### slider_set_line_cap 函数

* * *

  * 函数功能：



> 设置前景色的线帽形状。（默认为跟随风格的圆角设置，但是在没有设置圆角的时候无法使用 “round” 来设置圆角）

  * 函数原型：


    
    
    ret_t slider_set_line_cap (widget_t* widget, const char* line_cap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
line_cap | const char* | 前景色的线帽形状，取值为：butt  
  
#### slider_set_max 函数

* * *

  * 函数功能：



> 设置滑块的最大值。

  * 函数原型：


    
    
    ret_t slider_set_max (widget_t* widget, double max);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
max | double | 最大值  
  
#### slider_set_min 函数

* * *

  * 函数功能：



> 设置滑块的最小值。

  * 函数原型：


    
    
    ret_t slider_set_min (widget_t* widget, double min);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
min | double | 最小值  
  
#### slider_set_step 函数

* * *

  * 函数功能：



> 设置滑块的拖动的最小单位。

  * 函数原型：


    
    
    ret_t slider_set_step (widget_t* widget, double step);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
step | double | 拖动的最小单位。  
  
#### slider_set_value 函数

* * *

  * 函数功能：



> 设置滑块的值。

  * 函数原型：


    
    
    ret_t slider_set_value (widget_t* widget, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
value | double | 值  
  
#### slider_set_value_internal 函数

* * *

  * 函数功能：



> 设置滑块的值(public for test)。

  * 函数原型：


    
    
    ret_t slider_set_value_internal (widget_t* widget, double value, uint32_t etype, bool_t force);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
value | double | 值。  
etype | uint32_t | 触发事件。  
force | bool_t | 不管有没有变化都设置。  
  
#### slider_set_vertical 函数

* * *

  * 函数功能：



> 设置滑块的方向。

  * 函数原型：


    
    
    ret_t slider_set_vertical (widget_t* widget, bool_t vertical);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
vertical | bool_t | 是否为垂直方向。  
  
#### bar_size 属性

* * *

> 轴的宽度或高度（单位：像素），为0表示为控件的宽度或高度的一半，缺省为0。

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
  
#### drag_threshold 属性

* * *

> 拖动临界值。

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
  
#### dragger_adapt_to_icon 属性

* * *

> 滑块的宽度或高度是否与icon适应，缺省为true。

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
  
#### dragger_size 属性

* * *

> 滑块的宽度或高度（单位：像素），缺省为 bar_size * 1.5。

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
  
#### line_cap 属性

* * *

> 前景色的线帽形状。（取值：butt|round，默认为跟随风格的圆角设置, 但是在没有设置圆角的时候无法使用 “round” 来设置圆角）

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
  
#### max 属性

* * *

> 最大值。

  * 类型：double

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
  
#### min 属性

* * *

> 最小值。

  * 类型：double

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
  
#### slide_with_bar 属性

* * *

> 是否允许在轴上滑动来改变滑块位置，缺省为FALSE。

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
  
#### step 属性

* * *

> 拖动的最小单位。

  * 类型：double

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

> 值。

  * 类型：double

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
  
#### vertical 属性

* * *

> 滑块的是否为垂直方向。

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
