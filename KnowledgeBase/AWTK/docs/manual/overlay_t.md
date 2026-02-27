## overlay_t

### 概述

![image](images/overlay_t_0.png)

overlay窗口。

overlay窗口有点类似于非模态的dialog，但是它位置和大小是完全自由的，窗口管理器不会对它做任何限制。

如果overlay窗口有透明或半透效果，则不支持窗口动画，但可以通过移动窗口位置来实现类似动画的效果。

overlay_t是[window_base_t](window_base_t.html)的子类控件，window_base_t的函数均适用于overlay_t控件。

在xml中使用”overlay”标签创建窗口。需要指定坐标和大小，可以指定窗体样式和动画名称。如：
    
    
    <overlay theme="basic" x="100" y="100" w="200" h="300">
    ...
    </overlay>
    

> 更多用法请参考：[overlay.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/)

在c代码中使用函数overlay_create创建窗口。如：
    
    
    widget_t* overlay = overlay_create(NULL, 100, 100, 200, 300);
    

> 完整示例请参考：[overlay demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/)

可用通过style来设置窗口的风格，如背景颜色或图片等。如：
    
    
    <style name="bricks">
    <normal bg_image="bricks"  bg_image_draw_type="repeat"/>
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L0)

* * *

### 函数

函数名称 | 说明  
---|---  
overlay_cast | 转换为overlay对象(供脚本语言使用)。  
overlay_create | 创建overlay对象  
overlay_get_widget_vtable | 获取 overlay 虚表。  
overlay_set_always_on_top | 设置是否总是在最上面。  
overlay_set_click_through | 设置是否启用点击穿透。  
overlay_set_modeless | 设置是否非模态窗口模式。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
always_on_top | bool_t | 是否总在最上面。  
click_through | bool_t | 点击穿透。点击没有子控件的位置，是否穿透到底层窗口。  
modeless | bool_t | 非模态窗口。  
  
#### overlay_cast 函数

* * *

  * 函数功能：



> 转换为overlay对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* overlay_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | overlay对象。  
widget | widget_t* | overlay对象。  
  
#### overlay_create 函数

* * *

  * 函数功能：



> 创建overlay对象

  * 函数原型：


    
    
    widget_t* overlay_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### overlay_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 overlay 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* overlay_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 overlay 虚表。  
  
#### overlay_set_always_on_top 函数

* * *

  * 函数功能：



> 设置是否总是在最上面。

  * 函数原型：


    
    
    ret_t overlay_set_always_on_top (widget_t* widget, bool_t always_on_top);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
always_on_top | bool_t | 是否总是在最上面。  
  
#### overlay_set_click_through 函数

* * *

  * 函数功能：



> 设置是否启用点击穿透。

  * 函数原型：


    
    
    ret_t overlay_set_click_through (widget_t* widget, bool_t click_through);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
click_through | bool_t | 是否启用点击穿透。  
  
#### overlay_set_modeless 函数

* * *

  * 函数功能：



> 设置是否非模态窗口模式。

  * 函数原型：


    
    
    ret_t overlay_set_modeless (widget_t* widget, bool_t modeless);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
modeless | bool_t | 是否非模态窗口模式。  
  
#### always_on_top 属性

* * *

> 是否总在最上面。

缺省不启用。

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
  
#### click_through 属性

* * *

> 点击穿透。点击没有子控件的位置，是否穿透到底层窗口。

缺省不启用。

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
  
#### modeless 属性

* * *

> 非模态窗口。

缺省不启用。

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
