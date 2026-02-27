## gauge_pointer_t

### 概述

![image](images/gauge_pointer_t_0.png)

仪表指针控件。

仪表指针就是一张旋转的图片，图片可以是普通图片也可以是SVG图片。

在嵌入式平台上，对于旋转的图片，SVG图片的效率比位图高数倍，所以推荐使用SVG图片。

gauge_pointer_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于gauge_pointer_t控件。

在xml中使用”gauge_pointer”标签创建仪表指针控件。如：
    
    
    <gauge_pointer x="c" y="50" w="24" h="140" value="-128" image="gauge_pointer" />
    

> 更多用法请参考： [gauge.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/gauge.xml)

在c代码中使用函数gauge_pointer_create创建仪表指针控件。如：
    
    
    widget_t* gauge_pointer = gauge_pointer_create(gauge, 10, 10, 100, 30);
    gauge_pointer_set_image(gauge_pointer, "gauge_pointer");
    

## > 创建之后，需要用gauge_pointer_set_image设置仪表指针图片。

### 函数

函数名称 | 说明  
---|---  
gauge_pointer_cast | 转换为gauge_pointer对象(供脚本语言使用)。  
gauge_pointer_create | 创建gauge_pointer对象  
gauge_pointer_get_widget_vtable | 获取 gauge_pointer 虚表。  
gauge_pointer_set_anchor | 设置指针的旋转锚点。  
gauge_pointer_set_angle | 设置指针角度。12点钟方向为0度，顺时钟方向为正，单位为度。  
gauge_pointer_set_image | 设置指针的图片。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
anchor_x | char* | 图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
anchor_y | char* | 图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
angle | float_t | 指针角度。12点钟方向为0度，顺时钟方向为正，单位为度。  
image | char* | 指针图片。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(角度)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(角度)改变事件。  
  
#### gauge_pointer_cast 函数

* * *

  * 函数功能：



> 转换为gauge_pointer对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* gauge_pointer_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | gauge_pointer对象。  
widget | widget_t* | gauge_pointer对象。  
  
#### gauge_pointer_create 函数

* * *

  * 函数功能：



> 创建gauge_pointer对象

  * 函数原型：


    
    
    widget_t* gauge_pointer_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### gauge_pointer_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 gauge_pointer 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* gauge_pointer_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 gauge_pointer 虚表。  
  
#### gauge_pointer_set_anchor 函数

* * *

  * 函数功能：



> 设置指针的旋转锚点。

  * 函数原型：


    
    
    ret_t gauge_pointer_set_anchor (widget_t* widget, const char* anchor_x, const char* anchor_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
anchor_x | const char* | 指针的锚点坐标x。(后面加上px为像素点，不加px为相对百分比坐标)  
anchor_y | const char* | 指针的锚点坐标y。(后面加上px为像素点，不加px为相对百分比坐标)  
  
#### gauge_pointer_set_angle 函数

* * *

  * 函数功能：



> 设置指针角度。12点钟方向为0度，顺时钟方向为正，单位为度。

  * 函数原型：


    
    
    ret_t gauge_pointer_set_angle (widget_t* widget, float_t angle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
angle | float_t | 指针角度。  
  
#### gauge_pointer_set_image 函数

* * *

  * 函数功能：



> 设置指针的图片。

  * 函数原型：


    
    
    ret_t gauge_pointer_set_image (widget_t* widget, const char* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
image | const char* | 指针的图片。  
  
#### anchor_x 属性

* * *

> 图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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

> 图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### angle 属性

* * *

> 指针角度。12点钟方向为0度，顺时钟方向为正，单位为度。

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
  
#### image 属性

* * *

> 指针图片。

图片须垂直向上，图片的中心点为旋转方向。

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
