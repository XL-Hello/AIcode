## gif_image_t

### 概述

![image](images/gif_image_t_0.png)

GIF图片控件。

> 注意：GIF图片的尺寸大于控件大小时会自动缩小图片，但一般的嵌入式系统的硬件加速都不支持图片缩放， 所以缩放图片会导致性能明显下降。如果性能不满意时，请确认一下GIF图片的尺寸是否小于控件大小。

gif_image_t是[image_base_t](image_base_t.html)的子类控件，image_base_t的函数均适用于gif_image_t控件。

在xml中使用”gif”标签创建GIF图片控件。如：
    
    
    <gif image="bee"/>
    

> 更多用法请参考： [gif image](https://github.com/zlgopen/awtk/blob/master/design/default/ui/gif_image.xml)

在c代码中使用函数gif_image_create创建GIF图片控件。如：
    
    
    widget_t* image = gif_image_create(win, 10, 10, 200, 200);
    image_set_image(image, "bee");
    

> 创建之后:
> 
> 需要用widget_set_image设置图片名称。
> 
> 完整示例请参考：[gif image demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/gif_image.c)

可用通过style来设置控件的显示风格，如背景和边框等。如：
    
    
    <gif>
    <style name="border">
    <normal border_color="#000000" bg_color="#e0e0e0" text_color="black"/>
    </style>
    </gif>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml)

* * *

### 函数

函数名称 | 说明  
---|---  
gif_image_cast | 转换为gif_image对象(供脚本语言使用)。  
gif_image_create | 创建gif_image对象  
gif_image_get_widget_vtable | 获取 gif_image 虚表。  
gif_image_pause | 暂停。  
gif_image_play | 播放。  
gif_image_set_loop | 设置循环播放次数。  
gif_image_stop | 停止(并重置index为0)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
loop | uint32_t | 循环播放的次数。  
running | bool_t | 是否正在运行。  
  
#### gif_image_cast 函数

* * *

  * 函数功能：



> 转换为gif_image对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* gif_image_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | gif_image对象。  
widget | widget_t* | gif_image对象。  
  
#### gif_image_create 函数

* * *

  * 函数功能：



> 创建gif_image对象

  * 函数原型：


    
    
    widget_t* gif_image_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### gif_image_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 gif_image 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* gif_image_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 gif_image 虚表。  
  
#### gif_image_pause 函数

* * *

  * 函数功能：



> 暂停。

  * 函数原型：


    
    
    ret_t gif_image_pause (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | gif_image对象。  
  
#### gif_image_play 函数

* * *

  * 函数功能：



> 播放。

  * 函数原型：


    
    
    ret_t gif_image_play (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | gif_image对象。  
  
#### gif_image_set_loop 函数

* * *

  * 函数功能：



> 设置循环播放次数。

  * 函数原型：


    
    
    ret_t gif_image_set_loop (widget_t* widget, uint32_t loop);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
loop | uint32_t | 循环播放次数。  
  
#### gif_image_stop 函数

* * *

  * 函数功能：



> 停止(并重置index为0)。

  * 函数原型：


    
    
    ret_t gif_image_stop (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | gif_image对象。  
  
#### loop 属性

* * *

> 循环播放的次数。

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
  
#### running 属性

* * *

> 是否正在运行。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是
