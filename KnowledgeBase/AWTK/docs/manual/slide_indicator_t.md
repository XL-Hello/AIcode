## slide_indicator_t

### 概述

![image](images/slide_indicator_t_0.png)

slide_view的指示器控件。

> 支持直线、弧线排布，默认有4种绘制样式，若设置了icon/active_icon，则优先使用icon/active_icon

slide_indicator_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于slide_indicator_t控件。

在xml中使用”slide_indicator”或”slide_indicator_arc”标签创建指示器控件。如：
    
    
    <slide_view name="view" x="0"  y="0" w="100%" h="100%">
    ...
    </slide_view>
    <slide_indicator name="indicator" x="right" y="0" w="6" h="100%"/>
    

> 更多用法请参考：[slide_view.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/slide_view.xml)

在c代码中使用函数slide_indicator_create创建指示器控件。如：
    
    
    widget_t* slide_indicator = slide_indicator_create(parent, 0, 0, 0, 0);
    
    
    
    <style name="default">
    <normal fg_color="#FFFFFF80" selected_fg_color="#FFFFFF"/>
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L350)

* * *

### 函数

函数名称 | 说明  
---|---  
slide_indicator_cast | 转换为slide_indicator对象(供脚本语言使用)。  
slide_indicator_create | 创建slide_indicator对象  
slide_indicator_create_arc | 创建slide_indicator对象（圆弧显示）  
slide_indicator_create_linear | 创建slide_indicator对象（线性显示）  
slide_indicator_set_anchor | 设置旋转锚点。  
slide_indicator_set_auto_hide | 设置指示器是否自动隐藏。  
slide_indicator_set_default_paint | 设置指示器的默认绘制类型。  
slide_indicator_set_indicated_target | 设置指示器指示的目标。  
slide_indicator_set_margin | 设置指示器的边距(默认为10像素)。  
slide_indicator_set_max | 设置指示器的数量。  
slide_indicator_set_size | 设置指示器的大小(默认为8)。  
slide_indicator_set_spacing | 设置指示器的间距(指示器有弧度时为角度值，否则为直线间距)。  
slide_indicator_set_transition | 设置是否启用过渡效果。  
slide_indicator_set_value | 设置当前页的序号。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
anchor_x | char* | 锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
anchor_y | char* | 锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
auto_hide | uint16_t | 自动隐藏。0表示禁止，非0表示无操作后延迟多久隐藏。  
default_paint | indicator_default_paint_t | 指示器的类型。  
indicated_target | char* | 指示器指示的目标控件的名称。  
margin | int32_t | 指示器与边缘的边距。  
max | uint32_t | 最大值(缺省为100)。  
size | uint32_t | 指示器的大小。  
spacing | float_t | 指示器的中心之间的间距（圆弧显示时，间距的单位为弧度，否则为像素）。  
transition | bool_t | 是否启用过渡效果。  
value | uint32_t | 值(缺省为0)。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(当前页的序号)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(当前页的序号)改变事件。  
EVT_PAGE_CHANGED | event_t | 页面改变事件。  
EVT_PAGE_CHANGING | event_t | 页面正在改变。  
  
#### slide_indicator_cast 函数

* * *

  * 函数功能：



> 转换为slide_indicator对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* slide_indicator_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | slide_indicator对象。  
widget | widget_t* | slide_indicator对象。  
  
#### slide_indicator_create 函数

* * *

  * 函数功能：



> 创建slide_indicator对象

  * 函数原型：


    
    
    widget_t* slide_indicator_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### slide_indicator_create_arc 函数

* * *

  * 函数功能：



> 创建slide_indicator对象（圆弧显示）

  * 函数原型：


    
    
    widget_t* slide_indicator_create_arc (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### slide_indicator_create_linear 函数

* * *

  * 函数功能：



> 创建slide_indicator对象（线性显示）

  * 函数原型：


    
    
    widget_t* slide_indicator_create_linear (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### slide_indicator_set_anchor 函数

* * *

  * 函数功能：



> 设置旋转锚点。

  * 函数原型：


    
    
    ret_t slide_indicator_set_anchor (widget_t* widget, const char* anchor_x, const char* anchor_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
anchor_x | const char* | 锚点坐标x。(后面加上px为像素点，不加px为相对百分比坐标)  
anchor_y | const char* | 锚点坐标y。(后面加上px为像素点，不加px为相对百分比坐标)  
  
#### slide_indicator_set_auto_hide 函数

* * *

  * 函数功能：



> 设置指示器是否自动隐藏。

  * 函数原型：


    
    
    ret_t slide_indicator_set_auto_hide (widget_t* widget, uint16_t auto_hide);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
auto_hide | uint16_t | 0表示禁止，非0表示无操作后延迟多久隐藏。  
  
#### slide_indicator_set_default_paint 函数

* * *

  * 函数功能：



> 设置指示器的默认绘制类型。

  * 函数原型：


    
    
    ret_t slide_indicator_set_default_paint (widget_t* widget, indicator_default_paint_t default_paint);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
default_paint | indicator_default_paint_t | 默认绘制类型。  
  
#### slide_indicator_set_indicated_target 函数

* * *

  * 函数功能：



> 设置指示器指示的目标。

  * 函数原型：


    
    
    ret_t slide_indicator_set_indicated_target (widget_t* widget, const char* target_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
target_name | const char* | 指示器指示的目标控件的名称  
  
#### slide_indicator_set_margin 函数

* * *

  * 函数功能：



> 设置指示器的边距(默认为10像素)。

  * 函数原型：


    
    
    ret_t slide_indicator_set_margin (widget_t* widget, int32_t margin);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
margin | int32_t | 指示器的边距。  
  
#### slide_indicator_set_max 函数

* * *

  * 函数功能：



> 设置指示器的数量。

  * 函数原型：


    
    
    ret_t slide_indicator_set_max (widget_t* widget, uint32_t max);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
max | uint32_t | 数量。  
  
#### slide_indicator_set_size 函数

* * *

  * 函数功能：



> 设置指示器的大小(默认为8)。

  * 函数原型：


    
    
    ret_t slide_indicator_set_size (widget_t* widget, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
size | uint32_t | 指示器的大小。  
  
#### slide_indicator_set_spacing 函数

* * *

  * 函数功能：



> 设置指示器的间距(指示器有弧度时为角度值，否则为直线间距)。

  * 函数原型：


    
    
    ret_t slide_indicator_set_spacing (widget_t* widget, float_t spacing);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
spacing | float_t | 指示器的间距。  
  
#### slide_indicator_set_transition 函数

* * *

  * 函数功能：



> 设置是否启用过渡效果。

  * 函数原型：


    
    
    ret_t slide_indicator_set_transition (widget_t* widget, bool_t transition);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
transition | bool_t | 是否启用过渡效果  
  
#### slide_indicator_set_value 函数

* * *

  * 函数功能：



> 设置当前页的序号。

  * 函数原型：


    
    
    ret_t slide_indicator_set_value (widget_t* widget, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_indicator对象。  
value | uint32_t | 当前项的序号。  
  
#### anchor_x 属性

* * *

> 锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### anchor_y 属性

* * *

> 锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### auto_hide 属性

* * *

> 自动隐藏。0表示禁止，非0表示无操作后延迟多久隐藏。

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
  
#### default_paint 属性

* * *

> 指示器的类型。

  * 类型：indicator_default_paint_t

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
  
#### indicated_target 属性

* * *

> 指示器指示的目标控件的名称。

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
  
#### margin 属性

* * *

> 指示器与边缘的边距。

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
  
#### max 属性

* * *

> 最大值(缺省为100)。

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
  
#### size 属性

* * *

> 指示器的大小。

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
  
#### spacing 属性

* * *

> 指示器的中心之间的间距（圆弧显示时，间距的单位为弧度，否则为像素）。

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
  
#### transition 属性

* * *

> 是否启用过渡效果。

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
  
#### value 属性

* * *

> 值(缺省为0)。

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
