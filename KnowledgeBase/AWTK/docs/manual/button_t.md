## button_t

### 概述

![image](images/button_t_0.png)

按钮控件。

点击按钮之后会触发EVT_CLICK事件，注册EVT_CLICK事件以执行特定操作。

按钮控件也可以作为容器使用，使用图片和文本作为其子控件，可以实现很多有趣的效果。

button_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于button_t控件。

在xml中使用”button”标签创建按钮控件。如：
    
    
    <button x="c" y="m" w="80" h="30" text="OK"/>
    

> 更多用法请参考： [button.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/button.xml)

在c代码中使用函数button_create创建按钮控件。如：
    
    
    widget_t* button = button_create(win, 10, 10, 128, 30);
    widget_set_text(button, L"OK");
    widget_on(button, EVT_CLICK, on_click, NULL);
    

> 创建之后，需要用widget_set_text或widget_set_text_utf8设置文本内容。
> 
> 完整示例请参考： [button demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/button.c)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <style name="default" border_color="#a0a0a0"  text_color="black">
    <normal     bg_color="#f0f0f0" />
    <pressed    bg_color="#c0c0c0" x_offset="1" y_offset="1"/>
    <over       bg_color="#e0e0e0" />
    <disable    bg_color="gray" text_color="#d0d0d0" />
    </style>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L31)

* * *

### 函数

函数名称 | 说明  
---|---  
button_cast | 转换为button对象(供脚本语言使用)。  
button_create | 创建button对象  
button_get_widget_vtable | 获取 button 虚表。  
button_set_enable_long_press | 设置是否启用长按事件。  
button_set_enable_preview | 设置是否启用预览。  
button_set_long_press_time | 设置触发长按事件的时间(毫秒)。  
button_set_repeat | 设置触发EVT_CLICK事件的时间间隔。为0则不重复触发EVT_CLICK事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
enable_long_press | bool_t | 是否启用长按事件，为true时才触发长按事件。  
enable_preview | bool_t | 是否启用预览(主要用于软键盘)。  
long_press_time | uint32_t | 触发长按事件的时间(毫秒)  
pressed | bool_t | 当前是否按下。  
repeat | int32_t | 重复触发EVT_CLICK事件的时间间隔。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_CLICK | pointer_event_t | 点击事件。  
EVT_LONG_PRESS | pointer_event_t | 长按事件。  
  
#### button_cast 函数

* * *

  * 函数功能：



> 转换为button对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* button_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | button对象。  
widget | widget_t* | button对象。  
  
#### button_create 函数

* * *

  * 函数功能：



> 创建button对象

  * 函数原型：


    
    
    widget_t* button_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### button_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 button 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* button_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 button 虚表。  
  
#### button_set_enable_long_press 函数

* * *

  * 函数功能：



> 设置是否启用长按事件。

  * 函数原型：


    
    
    ret_t button_set_enable_long_press (widget_t* widget, bool_t enable_long_press);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
enable_long_press | bool_t | 是否启用长按事件。  
  
#### button_set_enable_preview 函数

* * *

  * 函数功能：



> 设置是否启用预览。

  * 函数原型：


    
    
    ret_t button_set_enable_preview (widget_t* widget, bool_t enable_preview);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
enable_preview | bool_t | 是否启用预览。  
  
#### button_set_long_press_time 函数

* * *

  * 函数功能：



> 设置触发长按事件的时间(毫秒)。

  * 函数原型：


    
    
    ret_t button_set_long_press_time (widget_t* widget, uint32_t long_press_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
long_press_time | uint32_t | 触发长按事件的时间(毫秒)。  
  
#### button_set_repeat 函数

* * *

  * 函数功能：



> 设置触发EVT_CLICK事件的时间间隔。为0则不重复触发EVT_CLICK事件。

  * 函数原型：


    
    
    ret_t button_set_repeat (widget_t* widget, int32_t repeat);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
repeat | int32_t | 触发EVT_CLICK事件的时间间隔(毫秒)。  
  
#### enable_long_press 属性

* * *

> 是否启用长按事件，为true时才触发长按事件。

触发长按事件后不再触发点击事件。 缺省不启用。

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
  
#### enable_preview 属性

* * *

> 是否启用预览(主要用于软键盘)。

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
  
#### long_press_time 属性

* * *

> 触发长按事件的时间(毫秒)

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
  
#### pressed 属性

* * *

> 当前是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### repeat 属性

* * *

> 重复触发EVT_CLICK事件的时间间隔。

为0则不重复触发EVT_CLICK事件。

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
