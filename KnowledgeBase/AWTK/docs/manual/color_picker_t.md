## color_picker_t

### 概述

![image](images/color_picker_t_0.png)

颜色选择器。

color_picker_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于color_picker_t控件。

在xml中使用”color_picker”标签创建颜色选择器控件。如：
    
    
    <color_picker x="0" y="0" w="100%" h="100%" value="orange">
    <color_component x="0" y="0" w="200" h="200" name="sv"/>
    <color_component x="210" y="0" w="20" h="200" name="h"/>
    <color_tile x="0" y="210" w="50%" h="20" name="new" bg_color="green"/>
    <color_tile x="right" y="210" w="50%" h="20" name="old" bg_color="blue"/>
    </color_picker>
    

> 更多用法请参考： [color_picker](https://github.com/zlgopen/awtk/blob/master/design/default/ui/color_picker.xml)

其中的子控件必须按下列规则命名：

  * r 红色分量。可以是spin_box、edit和slider。
  * g 绿色分量。可以是spin_box、edit和slider。
  * b 蓝色分量。可以是spin_box、edit和slider。
  * h Hue分量。可以是spin_box、edit、slider和color_component。
  * s Saturation分量。可以是spin_box、edit和slider。
  * v Value/Brightness分量。可以是spin_box、edit和slider。
  * sv Saturation和Value/Brightness分量。可以是color_component。
  * old 旧的值。可以是spin_box、edit和color_tile。
  * new 新的值。可以是spin_box、edit和color_tile。



* * *

### 函数

函数名称 | 说明  
---|---  
color_picker_cast | 转换为color_picker对象(供脚本语言使用)。  
color_picker_create | 创建color_picker对象  
color_picker_get_widget_vtable | 获取 color_picker 虚表。  
color_picker_set_color | 设置颜色。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
value | char* | 颜色。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(颜色)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(颜色)改变事件。  
  
#### color_picker_cast 函数

* * *

  * 函数功能：



> 转换为color_picker对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* color_picker_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | color_picker对象。  
widget | widget_t* | color_picker对象。  
  
#### color_picker_create 函数

* * *

  * 函数功能：



> 创建color_picker对象

  * 函数原型：


    
    
    widget_t* color_picker_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### color_picker_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 color_picker 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* color_picker_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 color_picker 虚表。  
  
#### color_picker_set_color 函数

* * *

  * 函数功能：



> 设置颜色。

  * 函数原型：


    
    
    ret_t color_picker_set_color (widget_t* widget, const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
color | const char* | 颜色。  
  
#### value 属性

* * *

> 颜色。

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
