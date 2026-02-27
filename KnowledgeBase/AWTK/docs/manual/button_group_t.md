## button_group_t

### 概述

![image](images/button_group_t_0.png)

Button Group控件。一个简单的容器控件，用于容纳一组按钮控件。

它本身不提供布局功能，仅提供具有语义的标签，让xml更具有可读性。 子控件的布局可用layout_children属性指定。 请参考[布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)。

button_group_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于button_group_t控件。

在xml中使用”button_group”标签创建button_group。如：
    
    
    <button_group x="0" y="m" w="100%" h="40" children_layout="default(c=4,r=1,s=5,m=5)">
    <button name="open:basic" text="Basic"/>
    <button name="open:button" text="Buttons"/>
    <button name="open:edit" text="Edits"/>
    <button name="open:keyboard" text="KeyBoard"/>
    </button_group>
    

可用通过style来设置控件的显示风格，如背景颜色等。如：
    
    
    <style name="default" border_color="#a0a0a0">
    <normal     bg_color="#f0f0f0" />
    </style>
    

* * *

### 函数

函数名称 | 说明  
---|---  
button_group_cast | 转换为button_group对象(供脚本语言使用)。  
button_group_create | 创建button_group对象  
button_group_get_widget_vtable | 获取 button_group 虚表。  
  
#### button_group_cast 函数

* * *

  * 函数功能：



> 转换为button_group对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* button_group_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | button_group对象。  
widget | widget_t* | button_group对象。  
  
#### button_group_create 函数

* * *

  * 函数功能：



> 创建button_group对象

  * 函数原型：


    
    
    widget_t* button_group_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### button_group_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 button_group 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* button_group_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 button_group 虚表。
