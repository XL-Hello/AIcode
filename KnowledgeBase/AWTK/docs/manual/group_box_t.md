## group_box_t

### 概述

![image](images/group_box_t_0.png)

分组控件。

单选按钮在同一个父控件中是互斥的，所以通常将相关的单选按钮放在一个group_box中。

它本身不提供布局功能，仅提供具有语义的标签，让xml更具有可读性。 子控件的布局可用layout_children属性指定。 请参考[布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)。

group_box_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于group_box_t控件。

在xml中使用”group_box”标签创建group_box。如：
    
    
    <group_box x="20" y="230" w="50%" h="90" children_layout="default(r=3,c=1,ym=2,s=10)" >
    <radio_button name="r1" text="Book"/>
    <radio_button name="r2" text="Food"/>
    <radio_button name="r3" text="Pencil" value="true"/>
    </group_box>
    

可用通过style来设置控件的显示风格，如背景颜色等。如：
    
    
    <style name="default" border_color="#a0a0a0">
    <normal     bg_color="#f0f0f0" />
    </style>
    

* * *

### 函数

函数名称 | 说明  
---|---  
group_box_cast | 转换为group_box对象(供脚本语言使用)。  
group_box_create | 创建group_box对象  
group_box_get_widget_vtable | 获取 group_box 虚表。  
group_box_set_value | 设置选中的单选按钮的索引。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
value | uint32_t | 选中的单选按钮的索引。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(勾选状态)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(勾选状态)改变事件。  
  
#### group_box_cast 函数

* * *

  * 函数功能：



> 转换为group_box对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* group_box_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | group_box对象。  
widget | widget_t* | group_box对象。  
  
#### group_box_create 函数

* * *

  * 函数功能：



> 创建group_box对象

  * 函数原型：


    
    
    widget_t* group_box_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### group_box_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 group_box 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* group_box_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 group_box 虚表。  
  
#### group_box_set_value 函数

* * *

  * 函数功能：



> 设置选中的单选按钮的索引。

  * 函数原型：


    
    
    ret_t group_box_set_value (widget_t* widget, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | group_box对象。  
value | uint32_t | 选中的单选按钮的索引。  
  
#### value 属性

* * *

> 选中的单选按钮的索引。

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
