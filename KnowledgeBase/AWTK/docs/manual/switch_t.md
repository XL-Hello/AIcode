## switch_t

### 概述

![image](images/switch_t_0.png)

开关控件。

switch_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于switch_t控件。

在xml中使用”switch”标签创建开关控件。如：
    
    
    <switch x="10" y="60" w="60" h="22" />
    

> 更多用法请参考：[switch.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/switch.xml)

在c代码中使用函数switch_create创建开关控件。如：
    
    
    widget_t* sw = switch_create(win, 10, 10, 80, 30);
    widget_on(sw, EVT_VALUE_CHANGED, on_changed, NULL);
    

> 完整示例请参考：[switch demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/switch.c)

可用通过style来设置控件的显示风格，如背景图片等。如：
    
    
    <style name="default">
    <normal  bg_image="switch" />
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L452)

* * *

### 函数

函数名称 | 说明  
---|---  
switch_cast | 转换switch对象(供脚本语言使用)。  
switch_create | 创建switch对象  
switch_get_widget_vtable | 获取 switch 虚表。  
switch_set_value | 设置控件的值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
max_xoffset_ratio | float_t | 当开关处于关闭时，图片偏移相对于图片宽度的比例(缺省为1/3)。  
value | bool_t | 值。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_CLICK | pointer_event_t | 点击事件。  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(开关状态)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(开关状态)改变事件。  
  
#### switch_cast 函数

* * *

  * 函数功能：



> 转换switch对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* switch_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | switch对象。  
widget | widget_t* | switch对象。  
  
#### switch_create 函数

* * *

  * 函数功能：



> 创建switch对象

  * 函数原型：


    
    
    widget_t* switch_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### switch_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 switch 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* switch_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 switch 虚表。  
  
#### switch_set_value 函数

* * *

  * 函数功能：



> 设置控件的值。

  * 函数原型：


    
    
    ret_t switch_set_value (widget_t* widget, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | switch对象。  
value | bool_t | 值  
  
#### max_xoffset_ratio 属性

* * *

> 当开关处于关闭时，图片偏移相对于图片宽度的比例(缺省为1/3)。

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
  
#### value 属性

* * *

> 值。

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
