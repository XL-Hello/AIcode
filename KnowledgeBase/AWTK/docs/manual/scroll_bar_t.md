## scroll_bar_t

### 概述

![image](images/scroll_bar_t_0.png)

滚动条控件。

> 目前只支持垂直滚动。

scroll_bar_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于scroll_bar_t控件。

在xml中使用”scroll_bar”或”scroll_bar_d”或”scroll_bar_m”标签创建滚动条控件。如：
    
    
    <list_view x="0"  y="30" w="100%" h="-80" item_height="60">
    <scroll_view name="view" x="0"  y="0" w="100%" h="100%">
    ...
    </scroll_view>
    <scroll_bar_m name="bar" x="right" y="0" w="6" h="100%" value="0"/>
    </list_view>
    

> 更多用法请参考：[list_view_m.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/list_view_m.xml)

在c代码中使用函数scroll_bar_create创建列表项控件。如：
    
    
    widget_t* scroll_bar = scroll_bar_create(list_view, 0, 0, 0, 0);
    
    
    
    <style name="default">
    <normal bg_color="#c0c0c0" fg_color="#808080"/>
    <over bg_color="#c0c0c0" fg_color="#808080"/>
    <pressed bg_color="#c0c0c0" fg_color="#808080"/>
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L350)

* * *

### 函数

函数名称 | 说明  
---|---  
scroll_bar_add_delta | 在当前的值上增加一个值，并触发EVT_VALUE_CHANGED事件。  
scroll_bar_cast | 转换为scroll_bar对象(供脚本语言使用)。  
scroll_bar_create | 创建scroll_bar对象  
scroll_bar_create_desktop | 创建desktop风格的scroll_bar对象  
scroll_bar_create_mobile | 创建mobile风格的scroll_bar对象  
scroll_bar_hide_by_opacity_animation | 通过动画隐藏滚动条。  
scroll_bar_is_mobile | 判断是否是mobile风格的滚动条。  
scroll_bar_scroll_delta | 在当前的值上增加一个值，并滚动到新的值，并触发EVT_VALUE_CHANGED事件。  
scroll_bar_scroll_to | 滚动到指定的值。  
scroll_bar_set_animator_time | 设置翻页滚动动画时间(毫秒)。  
scroll_bar_set_auto_hide | 设置auto_hide属性。  
scroll_bar_set_params | 设置参数。  
scroll_bar_set_scroll_delta | 设置鼠标滚轮幅度(仅对desktop风格的滚动条有效)。  
scroll_bar_set_value | 设置值，并触发EVT_VALUE_CHANGED事件。  
scroll_bar_set_value_only | 设置值，但不触发EVT_VALUE_CHANGED事件。  
scroll_bar_set_wheel_scroll | 设置鼠标滚轮是否滚动(仅对desktop风格的滚动条有效)。  
scroll_bar_show_by_opacity_animation | 通过动画显示滚动条。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
animatable | bool_t | 滚动时是否启用动画。  
animator_time | uint32_t | 翻页滚动动画时间(毫秒)。  
auto_hide | bool_t | 是否自动隐藏(仅对mobile风格的滚动条有效)。  
row | int32_t | 行的高度。  
scroll_delta | uint32_t | 每次鼠标滚动值。（缺省值为0，0 则使用鼠标滚动默认值）  
value | int32_t | 当前的值。  
virtual_size | int32_t | 虚拟宽度或高度。  
wheel_scroll | bool_t | 设置鼠标滚轮是否滚动(仅对desktop风格的滚动条有效)（垂直滚动条缺省值为TRUE，水平滚动条缺省值为FALSE）。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(滚动值)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(滚动值)改变事件。  
  
#### scroll_bar_add_delta 函数

* * *

  * 函数功能：



> 在当前的值上增加一个值，并触发EVT_VALUE_CHANGED事件。

  * 函数原型：


    
    
    ret_t scroll_bar_add_delta (widget_t* widget, int32_t delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
delta | int32_t | 值。  
  
#### scroll_bar_cast 函数

* * *

  * 函数功能：



> 转换为scroll_bar对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* scroll_bar_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | scroll_bar对象。  
widget | widget_t* | scroll_bar对象。  
  
#### scroll_bar_create 函数

* * *

  * 函数功能：



> 创建scroll_bar对象
> 
> 根据宏WITH_DESKTOP_STYLE决定创建desktop风格还是mobile风格的滚动条

  * 函数原型：


    
    
    widget_t* scroll_bar_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### scroll_bar_create_desktop 函数

* * *

  * 函数功能：



> 创建desktop风格的scroll_bar对象

  * 函数原型：


    
    
    widget_t* scroll_bar_create_desktop (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### scroll_bar_create_mobile 函数

* * *

  * 函数功能：



> 创建mobile风格的scroll_bar对象

  * 函数原型：


    
    
    widget_t* scroll_bar_create_mobile (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### scroll_bar_hide_by_opacity_animation 函数

* * *

  * 函数功能：



> 通过动画隐藏滚动条。

  * 函数原型：


    
    
    ret_t scroll_bar_hide_by_opacity_animation (widget_t* widget, int32_t duration, int32_t delay);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
duration | int32_t | 动画持续时间(毫秒)。  
delay | int32_t | 动画执行时间(毫秒)。  
  
#### scroll_bar_is_mobile 函数

* * *

  * 函数功能：



> 判断是否是mobile风格的滚动条。

  * 函数原型：


    
    
    bool_t scroll_bar_is_mobile (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是mobile风格的，否则表示不是mobile风格的。  
widget | widget_t* | scroll_bar控件。  
  
#### scroll_bar_scroll_delta 函数

* * *

  * 函数功能：



> 在当前的值上增加一个值，并滚动到新的值，并触发EVT_VALUE_CHANGED事件。

  * 函数原型：


    
    
    ret_t scroll_bar_scroll_delta (widget_t* widget, int32_t delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
delta | int32_t | 值。  
  
#### scroll_bar_scroll_to 函数

* * *

  * 函数功能：



> 滚动到指定的值。

  * 函数原型：


    
    
    ret_t scroll_bar_scroll_to (widget_t* widget, int32_t value, int32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
value | int32_t | 值。  
duration | int32_t | 动画持续时间(毫秒)。  
  
#### scroll_bar_set_animator_time 函数

* * *

  * 函数功能：



> 设置翻页滚动动画时间(毫秒)。

  * 函数原型：


    
    
    ret_t scroll_bar_set_animator_time (widget_t* widget, uint32_t animator_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
animator_time | uint32_t | 时间(毫秒)。  
  
#### scroll_bar_set_auto_hide 函数

* * *

  * 函数功能：



> 设置auto_hide属性。
> 
> 仅对mobile风格的滚动条有效

  * 函数原型：


    
    
    ret_t scroll_bar_set_auto_hide (widget_t* widget, bool_t auto_hide);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
auto_hide | bool_t | 值。  
  
#### scroll_bar_set_params 函数

* * *

  * 函数功能：



> 设置参数。

  * 函数原型：


    
    
    ret_t scroll_bar_set_params (widget_t* widget, int32_t virtual_size, int32_t row);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
virtual_size | int32_t | 虚拟高度。  
row | int32_t | 每一行的高度。  
  
#### scroll_bar_set_scroll_delta 函数

* * *

  * 函数功能：



> 设置鼠标滚轮幅度(仅对desktop风格的滚动条有效)。

  * 函数原型：


    
    
    ret_t scroll_bar_set_scroll_delta (widget_t* widget, uint32_t scroll_delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
scroll_delta | uint32_t | 滚动幅度。  
  
#### scroll_bar_set_value 函数

* * *

  * 函数功能：



> 设置值，并触发EVT_VALUE_CHANGED事件。

  * 函数原型：


    
    
    ret_t scroll_bar_set_value (widget_t* widget, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
value | int32_t | 值。  
  
#### scroll_bar_set_value_only 函数

* * *

  * 函数功能：



> 设置值，但不触发EVT_VALUE_CHANGED事件。

  * 函数原型：


    
    
    ret_t scroll_bar_set_value_only (widget_t* widget, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
value | int32_t | 值。  
  
#### scroll_bar_set_wheel_scroll 函数

* * *

  * 函数功能：



> 设置鼠标滚轮是否滚动(仅对desktop风格的滚动条有效)。

  * 函数原型：


    
    
    ret_t scroll_bar_set_wheel_scroll (widget_t* widget, bool_t scroll);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
scroll | bool_t | 是否设置该功能。  
  
#### scroll_bar_show_by_opacity_animation 函数

* * *

  * 函数功能：



> 通过动画显示滚动条。

  * 函数原型：


    
    
    ret_t scroll_bar_show_by_opacity_animation (widget_t* widget, int32_t duration, int32_t delay);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | scroll_bar控件。  
duration | int32_t | 动画持续时间(毫秒)。  
delay | int32_t | 动画执行时间(毫秒)。  
  
#### animatable 属性

* * *

> 滚动时是否启用动画。

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
  
#### animator_time 属性

* * *

> 翻页滚动动画时间(毫秒)。

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
  
#### auto_hide 属性

* * *

> 是否自动隐藏(仅对mobile风格的滚动条有效)。

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
  
#### row 属性

* * *

> 行的高度。

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
  
#### scroll_delta 属性

* * *

> 每次鼠标滚动值。（缺省值为0，0 则使用鼠标滚动默认值）

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
  
#### value 属性

* * *

> 当前的值。

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
  
#### virtual_size 属性

* * *

> 虚拟宽度或高度。

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
  
#### wheel_scroll 属性

* * *

> 设置鼠标滚轮是否滚动(仅对desktop风格的滚动条有效)（垂直滚动条缺省值为TRUE，水平滚动条缺省值为FALSE）。

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
