## check_button_t

### 概述

![image](images/check_button_t_0.png)

勾选按钮控件(单选/多选)。

check_button_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于check_button_t控件。

在xml中使用”check_button”标签创建多选按钮控件。如：
    
    
    <check_button name="c1" text="Book"/>
    

在xml中使用”radio_button”标签创建单选按钮控件。如：
    
    
    <radio_button name="r1" text="Book"/>
    

> 更多用法请参考： [button.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/basic.xml)

在c代码中使用函数check_button_create创建多选按钮控件。如：
    
    
    widget_t* button = check_button_create(win, x, y, w, h);
    widget_set_text(button, L"OK");
    widget_on(button, EVT_VALUE_CHANGED, on_changed, NULL);
    

在c代码中使用函数check_button_create_radio创建单选按钮控件。如：
    
    
    widget_t* button = check_button_create_radio(win, x, y, w, h);
    widget_set_text(button, L"OK");
    widget_on(button, EVT_VALUE_CHANGED, on_changed, NULL);
    

> 完整示例请参考： [button demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/check_button.c)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <style name="default" icon_at="left">
    <normal  icon="unchecked" />
    <pressed icon="unchecked" />
    <over    icon="unchecked" text_color="green"/>
    <normal_of_checked icon="checked" text_color="blue"/>
    <pressed_of_checked icon="checked" text_color="blue"/>
    <over_of_checked icon="checked" text_color="green"/>
    </style>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L227)

* * *

### 函数

函数名称 | 说明  
---|---  
check_button_cast | 转换check_button对象(供脚本语言使用)。  
check_button_create | 创建多选按钮对象  
check_button_create_ex | 创建check button对象  
check_button_create_radio | 创建单选按钮对象  
check_button_get_checked_button | 用于radio button获取同组中勾选的radio button。  
check_button_get_indeterminate | 获取控件的是否存于不确定状态。  
check_button_get_widget_vtable | 获取 check_button 虚表。  
check_button_set_indeterminate | 设置控件的不确定状态。  
check_button_set_value | 设置控件的值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
indeterminate | bool_t | 复选框是否是为不确定状态。（该值为TRUE的话，value 值存于不确定状态，该值为FALSE的话，value 值存于确定状态）  
radio | bool_t | 是否是单选按钮。  
value | bool_t | 值(勾选为TRUE，非勾选为FALSE)。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(勾选状态)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(勾选状态)改变事件。  
EVT_CLICK | pointer_event_t | 点击事件。  
  
#### check_button_cast 函数

* * *

  * 函数功能：



> 转换check_button对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* check_button_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | check_button对象。  
widget | widget_t* | check_button对象。  
  
#### check_button_create 函数

* * *

  * 函数功能：



> 创建多选按钮对象

  * 函数原型：


    
    
    widget_t* check_button_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | widget对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### check_button_create_ex 函数

* * *

  * 函数功能：



> 创建check button对象

  * 函数原型：


    
    
    widget_t* check_button_create_ex (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h, const char* type, bool_t radio);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | widget对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
type | const char* | 类型。  
radio | bool_t | 是否单选。  
  
#### check_button_create_radio 函数

* * *

  * 函数功能：



> 创建单选按钮对象

  * 函数原型：


    
    
    widget_t* check_button_create_radio (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | widget对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### check_button_get_checked_button 函数

* * *

  * 函数功能：



> 用于radio button获取同组中勾选的radio button。

  * 函数原型：


    
    
    widget_t* check_button_get_checked_button (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 同组中勾选的radio button对象。  
widget | widget_t* | radio_button对象。  
  
#### check_button_get_indeterminate 函数

* * *

  * 函数功能：



> 获取控件的是否存于不确定状态。

  * 函数原型：


    
    
    bool_t check_button_get_indeterminate (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回控件的是否存于不确定状态。  
widget | widget_t* | check_button对象。  
  
#### check_button_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 check_button 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* check_button_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 check_button 虚表。  
  
#### check_button_set_indeterminate 函数

* * *

  * 函数功能：



> 设置控件的不确定状态。

  * 函数原型：


    
    
    ret_t check_button_set_indeterminate (widget_t* widget, bool_t indeterminate);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | check_button对象。  
indeterminate | bool_t | 不确定状态。（该值为TRUE的话，value 值存于不确定状态，该值为FALSE的话，value 值存于确定状态）  
  
#### check_button_set_value 函数

* * *

  * 函数功能：



> 设置控件的值。

  * 函数原型：


    
    
    ret_t check_button_set_value (widget_t* widget, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | check_button对象。  
value | bool_t | 值(勾选为TRUE，非勾选为FALSE)。  
  
#### indeterminate 属性

* * *

> 复选框是否是为不确定状态。（该值为TRUE的话，value 值存于不确定状态，该值为FALSE的话，value 值存于确定状态）

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 否  
可直接修改 | 否  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### radio 属性

* * *

> 是否是单选按钮。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 否  
可直接修改 | 否  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### value 属性

* * *

> 值(勾选为TRUE，非勾选为FALSE)。

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
