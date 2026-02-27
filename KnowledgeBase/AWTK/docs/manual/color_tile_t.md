## color_tile_t

### 概述

![image](images/color_tile_t_0.png)

色块控件。

用来显示一个颜色块，它通过属性而不是窗体样式来设置颜色，方便在运行时动态改变颜色。

可以使用value属性访问背景颜色的颜色值。

color_tile_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于color_tile_t控件。

在xml中使用”color_tile”标签创建色块控件。如：
    
    
    <color_tile x="c" y="m" w="80" h="30" bg_color="green" />
    

> 更多用法请参考： [color_tile](https://github.com/zlgopen/awtk/blob/master/design/default/ui/color_picker_rgb.xml)

在c代码中使用函数color_tile_create创建色块控件。如：
    
    
    widget_t* color_tile = color_tile_create(win, 10, 10, 128, 30);
    color_tile_set_bg_color(color_tile, "red");
    

## > 创建之后，用color_tile_set_bg_color设置背景颜色。

### 函数

函数名称 | 说明  
---|---  
color_tile_cast | 转换为color_tile对象(供脚本语言使用)。  
color_tile_create | 创建color_tile对象  
color_tile_get_bg_color | 获取背景颜色。  
color_tile_get_border_color | 获取边框颜色。  
color_tile_get_widget_vtable | 获取 color_tile 虚表。  
color_tile_set_bg_color | 设置背景颜色。  
color_tile_set_border_color | 设置边框颜色。  
color_tile_set_value | 设置背景颜色。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
bg_color | char* | 背景颜色。  
border_color | char* | 边框颜色。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(颜色)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(颜色)改变事件。  
  
#### color_tile_cast 函数

* * *

  * 函数功能：



> 转换为color_tile对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* color_tile_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | color_tile对象。  
widget | widget_t* | color_tile对象。  
  
#### color_tile_create 函数

* * *

  * 函数功能：



> 创建color_tile对象

  * 函数原型：


    
    
    widget_t* color_tile_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### color_tile_get_bg_color 函数

* * *

  * 函数功能：



> 获取背景颜色。

  * 函数原型：


    
    
    const char* color_tile_get_bg_color (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回背景颜色。  
widget | widget_t* | 控件对象。  
  
#### color_tile_get_border_color 函数

* * *

  * 函数功能：



> 获取边框颜色。

  * 函数原型：


    
    
    const char* color_tile_get_border_color (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回边框颜色。  
widget | widget_t* | 控件对象。  
  
#### color_tile_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 color_tile 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* color_tile_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 color_tile 虚表。  
  
#### color_tile_set_bg_color 函数

* * *

  * 函数功能：



> 设置背景颜色。

  * 函数原型：


    
    
    ret_t color_tile_set_bg_color (widget_t* widget, const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
color | const char* | 背景颜色。  
  
#### color_tile_set_border_color 函数

* * *

  * 函数功能：



> 设置边框颜色。

  * 函数原型：


    
    
    ret_t color_tile_set_border_color (widget_t* widget, const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
color | const char* | 边框颜色。  
  
#### color_tile_set_value 函数

* * *

  * 函数功能：



> 设置背景颜色。

  * 函数原型：


    
    
    ret_t color_tile_set_value (widget_t* widget, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
color | color_t | 背景颜色。  
  
#### bg_color 属性

* * *

> 背景颜色。

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
  
#### border_color 属性

* * *

> 边框颜色。

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
