## gauge_t

### 概述

![image](images/gauge_t_0.png)

表盘控件。

表盘控件就是一张图片。

gauge_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于gauge_t控件。

在xml中使用”gauge”标签创建表盘控件。如：
    
    
    <gauge x="c" y="10" w="240" h="240" image="gauge_bg" >
    

> 更多用法请参考： [gauge.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/gauge.xml)

在c代码中使用函数gauge_create创建表盘控件。如：
    
    
    widget_t* gauge = gauge_create(win, 10, 10, 200, 200);
    gauge_set_image(gauge, "gauge_bg");
    

可用通过style来设置控件的显示风格，如背景和边框等。如：
    
    
    <gauge>
    <style name="border">
    <normal border_color="#000000" bg_color="#e0e0e0" text_color="black"/>
    </style>
    </gauge>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml)

* * *

### 函数

函数名称 | 说明  
---|---  
gauge_cast | 转换为gauge对象(供脚本语言使用)。  
gauge_create | 创建gauge对象  
gauge_get_widget_vtable | 获取 gauge 虚表。  
gauge_set_draw_type | 设置图片的显示方式。  
gauge_set_image | 设置背景图片的名称。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
draw_type | image_draw_type_t | 图片的绘制方式。  
image | char* | 背景图片。  
  
#### gauge_cast 函数

* * *

  * 函数功能：



> 转换为gauge对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* gauge_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | gauge对象。  
widget | widget_t* | gauge对象。  
  
#### gauge_create 函数

* * *

  * 函数功能：



> 创建gauge对象

  * 函数原型：


    
    
    widget_t* gauge_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### gauge_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 gauge 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* gauge_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 gauge 虚表。  
  
#### gauge_set_draw_type 函数

* * *

  * 函数功能：



> 设置图片的显示方式。
> 
> 绘制方式的属性值和枚举值: [image_draw_type_name_value](https://github.com/zlgopen/awtk/blob/master/src/base/enums.c#L98)

  * 函数原型：


    
    
    ret_t gauge_set_draw_type (widget_t* widget, image_draw_type_t draw_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image对象。  
draw_type | image_draw_type_t | 显示方式。  
  
#### gauge_set_image 函数

* * *

  * 函数功能：



> 设置背景图片的名称。

  * 函数原型：


    
    
    ret_t gauge_set_image (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image对象。  
name | const char* | 图片名称，该图片必须存在于资源管理器。  
  
#### draw_type 属性

* * *

> 图片的绘制方式。

  * 类型：image_draw_type_t

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

> 背景图片。

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
