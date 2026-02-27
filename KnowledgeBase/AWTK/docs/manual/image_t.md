## image_t

### 概述

![image](images/image_t_0.png)

图片控件。

用来显示一张静态图片，目前支持bmp/png/jpg等格式。

如果要显示gif文件，请用[gif_image](gif_image_t.html)。

如果要显示svg文件，请用[svg_image](svg_image_t.html)。

如果需要支持勾选效果，请设置**selectable** 属性。

如果需要支持点击效果，请设置**clickable** 属性。

image_t是[image_base_t](image_base_t.html)的子类控件，image_base_t的函数均适用于image_t控件。

在xml中使用”image”标签创建图片控件。如：
    
    
    <image style="border" image="earth" draw_type="icon" />
    

> 更多用法请参考： [image.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/images.xml)

在c代码中使用函数image_create创建图片控件。如：
    
    
    widget_t* image = image_create(win, 10, 10, 128, 30);
    image_set_image(image, "earth");
    

> 创建之后:
> 
> 需要用widget_set_image设置图片名称。
> 
> 可以用image_set_draw_type设置图片的绘制方式。
> 
> 绘制方式请参考[image_draw_type_t](image_draw_type_t.html)
> 
> 绘制方式的属性值和枚举值: [image_draw_type_name_value](https://github.com/zlgopen/awtk/blob/master/src/base/enums.c#L98)
> 
> 完整示例请参考： [image demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/image.c)

可用通过style来设置控件的显示风格，如背景和边框等。如：
    
    
    <image>
    <style name="border">
    <normal border_color="#000000" bg_color="#e0e0e0" text_color="black"/>
    </style>
    </image>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L313)

* * *

### 函数

函数名称 | 说明  
---|---  
icon_create | 创建icon对象  
image_cast | 转换为image对象(供脚本语言使用)。  
image_create | 创建image对象  
image_get_widget_vtable | 获取 image 虚表。  
image_set_draw_type | 设置图片的绘制方式。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
draw_type | image_draw_type_t | 图片的绘制方式(仅在没有旋转和缩放时生效)。  
  
#### icon_create 函数

* * *

  * 函数功能：



> 创建icon对象

  * 函数原型：


    
    
    widget_t* icon_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### image_cast 函数

* * *

  * 函数功能：



> 转换为image对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* image_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | image对象。  
widget | widget_t* | image对象。  
  
#### image_create 函数

* * *

  * 函数功能：



> 创建image对象

  * 函数原型：


    
    
    widget_t* image_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### image_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 image 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* image_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 image 虚表。  
  
#### image_set_draw_type 函数

* * *

  * 函数功能：



> 设置图片的绘制方式。

  * 函数原型：


    
    
    ret_t image_set_draw_type (widget_t* widget, image_draw_type_t draw_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image对象。  
draw_type | image_draw_type_t | 绘制方式(仅在没有旋转和缩放时生效)。  
  
#### draw_type 属性

* * *

> 图片的绘制方式(仅在没有旋转和缩放时生效)。

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
