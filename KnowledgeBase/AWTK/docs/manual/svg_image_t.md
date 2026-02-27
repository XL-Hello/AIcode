## svg_image_t

### 概述

![image](images/svg_image_t_0.png)

SVG图片控件。

svg_image_t是[image_base_t](image_base_t.html)的子类控件，image_base_t的函数均适用于svg_image_t控件。

在xml中使用”svg”标签创建SVG图片控件。如：
    
    
    <svg image="girl"/>
    

> 更多用法请参考：[svg image](https://github.com/zlgopen/awtk/blob/master/design/default/ui/svg_image.xml)

在c代码中使用函数svg_image_create创建SVG图片控件。如：
    
    
    widget_t* image = svg_image_create(win, 10, 10, 200, 200);
    image_set_image(image, "girl");
    

> 创建之后: 需要用widget_set_image设置图片名称。
> 
> 完整示例请参考：[svg image demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/svg_image.c)

可用通过style来设置控件的显示风格，如背景和边框等。如：
    
    
    <svg>
    <style name="default">
    <normal border_color="green" fg_color="red" />
    </style>
    </svg>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml)

* * *

### 函数

函数名称 | 说明  
---|---  
svg_image_cast | 转换为svg_image对象(供脚本语言使用)。  
svg_image_create | 创建svg_image对象  
svg_image_get_widget_vtable | 获取 svg_image 虚表。  
svg_image_set_cache_mode | 控件设置是否开启离线缓存渲染模式。  
svg_image_set_draw_type | 控件设置svg图片绘制模式。  
svg_image_set_image | 设置控件的图片名称。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
draw_type | image_draw_type_t | svg图片的绘制方式(支持旋转缩放, 目前仅支持scale、scale_auto模式)。  
is_cache_mode | bool_t | 离线缓存渲染模式。  
  
#### svg_image_cast 函数

* * *

  * 函数功能：



> 转换为svg_image对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* svg_image_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | svg_image对象。  
widget | widget_t* | svg_image对象。  
  
#### svg_image_create 函数

* * *

  * 函数功能：



> 创建svg_image对象

  * 函数原型：


    
    
    widget_t* svg_image_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### svg_image_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 svg_image 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* svg_image_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 svg_image 虚表。  
  
#### svg_image_set_cache_mode 函数

* * *

  * 函数功能：



> 控件设置是否开启离线缓存渲染模式。
> 
> 在确保svg图片不经常变化大小及状态的情况下，开启离线缓存渲染能够减少解析bsvg的开销，提高效率。

  * 函数原型：


    
    
    ret_t svg_image_set_cache_mode (widget_t* widget, bool_t is_cache_mode);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image对象。  
is_cache_mode | bool_t | 是否开启缓存模式。  
  
#### svg_image_set_draw_type 函数

* * *

  * 函数功能：



> 控件设置svg图片绘制模式。

  * 函数原型：


    
    
    ret_t svg_image_set_draw_type (widget_t* widget, image_draw_type_t draw_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image对象。  
draw_type | image_draw_type_t | 绘制模式。  
  
#### svg_image_set_image 函数

* * *

  * 函数功能：



> 设置控件的图片名称。
> 
> 如果需要显示文件系统中的图片，只需将图片名称换成实际的文件名，并加上”file://”前缀即可。

  * 函数原型：


    
    
    ret_t svg_image_set_image (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image对象。  
name | const char* | 图片名称，该图片必须存在于资源管理器。  
  
#### draw_type 属性

* * *

> svg图片的绘制方式(支持旋转缩放, 目前仅支持scale、scale_auto模式)。

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
  
#### is_cache_mode 属性

* * *

> 离线缓存渲染模式。

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
