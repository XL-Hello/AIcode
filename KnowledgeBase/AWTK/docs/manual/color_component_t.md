## color_component_t

### 概述

![image](images/color_component_t_0.png)

颜色选择器的颜色分量。 控件的名称有严格规定： COLOR_PICKER_CHILD_SV: 水平为Value/Brightness(递增)，垂直为Saturation(递减)。 COLOR_PICKER_CHILD_H: 水平为同色，垂直为Hue(递减)。

* * *

### 函数

函数名称 | 说明  
---|---  
color_component_cast | 转换为color_component对象(供脚本语言使用)。  
color_component_create | 创建color_component对象  
color_component_get_h | 获取h分量。  
color_component_get_s | 获取s分量。  
color_component_get_v | 获取v分量。  
color_component_get_widget_vtable | 获取 color_component 虚表。  
color_component_set_color | 设置颜色。  
color_component_set_hsv | 设置颜色。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_CHANGING | value_change_event_t | 颜色正在改变事件。  
  
#### color_component_cast 函数

* * *

  * 函数功能：



> 转换为color_component对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* color_component_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | color_component对象。  
widget | widget_t* | color_component对象。  
  
#### color_component_create 函数

* * *

  * 函数功能：



> 创建color_component对象

  * 函数原型：


    
    
    widget_t* color_component_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### color_component_get_h 函数

* * *

  * 函数功能：



> 获取h分量。

  * 函数原型：


    
    
    float color_component_get_h (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 返回h分量。  
widget | widget_t* | color_component对象。  
  
#### color_component_get_s 函数

* * *

  * 函数功能：



> 获取s分量。

  * 函数原型：


    
    
    float color_component_get_s (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 返回s分量。  
widget | widget_t* | color_component对象。  
  
#### color_component_get_v 函数

* * *

  * 函数功能：



> 获取v分量。

  * 函数原型：


    
    
    float color_component_get_v (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 返回v分量。  
widget | widget_t* | color_component对象。  
  
#### color_component_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 color_component 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* color_component_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 color_component 虚表。  
  
#### color_component_set_color 函数

* * *

  * 函数功能：



> 设置颜色。

  * 函数原型：


    
    
    ret_t color_component_set_color (widget_t* widget, color_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | color_t | 颜色。  
  
#### color_component_set_hsv 函数

* * *

  * 函数功能：



> 设置颜色。

  * 函数原型：


    
    
    ret_t color_component_set_hsv (widget_t* widget, float h, float s, float v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
h | float | 色调。  
s | float | 饱和度。  
v | float | 明度。
