## slide_menu_t

### 概述

![image](images/slide_menu_t_0.png)

左右滑动菜单控件。

一般用一组按钮作为子控件，通过左右滑动改变当前的项。除了当菜单使用外，也可以用来切换页面。

slide_menu_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于slide_menu_t控件。

在xml中使用”slide_menu”标签创建左右滑动菜单控件。如：
    
    
    <slide_menu style="mask" align_v="top">
    <button style="slide_button" text="0"/>
    <button style="slide_button" text="1"/>
    <button style="slide_button" text="2"/>
    <button style="slide_button" text="3"/>
    <button style="slide_button" text="4"/>
    </slide_menu>
    

> 更多用法请参考：[slide_menu.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/slide_menu.xml)

在c代码中使用函数slide_menu_create创建左右滑动菜单控件。如：
    
    
    slide_menu = slide_menu_create(win, 10, 10, 300, 60);
    b = button_create(slide_menu, 0, 0, 0, 0);
    widget_set_text_utf8(b, "1");
    b = button_create(slide_menu, 0, 0, 0, 0);
    widget_set_text_utf8(b, "2");
    b = button_create(slide_menu, 0, 0, 0, 0);
    widget_set_text_utf8(b, "3");
    b = button_create(slide_menu, 0, 0, 0, 0);
    widget_set_text_utf8(b, "4");
    

可按下面的方法关注当前项改变的事件：
    
    
    widget_on(slide_menu, EVT_VALUE_CHANGED, on_current_changed, slide_menu);
    

可按下面的方法关注当前按钮被点击的事件：
    
    
    widget_on(b, EVT_CLICK, on_button_click, b);
    

> 完整示例请参考：[slide_menu demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/slide_menu.c)

可用通过style来设置控件的显示风格，如背景颜色和蒙版颜色等等。如：
    
    
    <style name="mask">
    <normal     bg_color="#f0f0f0" mask_color="#f0f0f0"/>
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L493)

* * *

### 函数

函数名称 | 说明  
---|---  
slide_menu_cast | 转换slide_menu对象(供脚本语言使用)。  
slide_menu_create | 创建slide_menu对象  
slide_menu_get_widget_vtable | 获取 slide_menu 虚表。  
slide_menu_scroll_to_next | 切换至下一项。  
slide_menu_scroll_to_prev | 切换至上一项。  
slide_menu_set_align_v | 设置垂直对齐方式。  
slide_menu_set_clip | 设置是否动态裁剪菜单项。  
slide_menu_set_menu_w | 设置菜单项的宽度。  
slide_menu_set_min_scale | 设置最小缩放比例。  
slide_menu_set_spacer | 设置菜单项之间的间距。  
slide_menu_set_value | 设置当前项。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
align_v | align_v_t | 垂直对齐方式。  
clip | bool_t | 是否动态裁剪菜单项(默认裁剪，不裁剪时，如果显示偶数项，左边会多一项)。  
menu_w | char* | 菜单项的宽度(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)(空字符串则使用控件高度)。  
min_scale | float_t | 最小缩放比例。  
spacer | int32_t | 菜单项之间的间距。  
value | int32_t | 值。代表当前选中项的索引。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(当前项)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(当前项)改变事件。  
  
#### slide_menu_cast 函数

* * *

  * 函数功能：



> 转换slide_menu对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* slide_menu_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | slide_menu对象。  
widget | widget_t* | slide_menu对象。  
  
#### slide_menu_create 函数

* * *

  * 函数功能：



> 创建slide_menu对象

  * 函数原型：


    
    
    widget_t* slide_menu_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### slide_menu_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 slide_menu 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* slide_menu_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 slide_menu 虚表。  
  
#### slide_menu_scroll_to_next 函数

* * *

  * 函数功能：



> 切换至下一项。

  * 函数原型：


    
    
    ret_t slide_menu_scroll_to_next (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
  
#### slide_menu_scroll_to_prev 函数

* * *

  * 函数功能：



> 切换至上一项。

  * 函数原型：


    
    
    ret_t slide_menu_scroll_to_prev (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
  
#### slide_menu_set_align_v 函数

* * *

  * 函数功能：



> 设置垂直对齐方式。

  * 函数原型：


    
    
    ret_t slide_menu_set_align_v (widget_t* widget, align_v_t align_v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
align_v | align_v_t | 对齐方式。  
  
#### slide_menu_set_clip 函数

* * *

  * 函数功能：



> 设置是否动态裁剪菜单项。

  * 函数原型：


    
    
    ret_t slide_menu_set_clip (widget_t* widget, bool_t clip);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
clip | bool_t | 是否动态裁剪菜单项。(关闭后，如果显示偶数项，左边会多一项)  
  
#### slide_menu_set_menu_w 函数

* * *

  * 函数功能：



> 设置菜单项的宽度。

  * 函数原型：


    
    
    ret_t slide_menu_set_menu_w (widget_t* widget, const char* menu_w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
menu_w | const char* | 菜单项的宽度。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)(空字符串则使用控件高度)  
  
#### slide_menu_set_min_scale 函数

* * *

  * 函数功能：



> 设置最小缩放比例。

  * 函数原型：


    
    
    ret_t slide_menu_set_min_scale (widget_t* widget, float_t min_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
min_scale | float_t | 最小缩放比例，范围[0.5-1]。  
  
#### slide_menu_set_spacer 函数

* * *

  * 函数功能：



> 设置菜单项之间的间距。

  * 函数原型：


    
    
    ret_t slide_menu_set_spacer (widget_t* widget, int32_t spacer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
spacer | int32_t | 菜单项之间的间距。  
  
#### slide_menu_set_value 函数

* * *

  * 函数功能：



> 设置当前项。

  * 函数原型：


    
    
    ret_t slide_menu_set_value (widget_t* widget, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_menu对象。  
value | uint32_t | 当前项的索引。  
  
#### align_v 属性

* * *

> 垂直对齐方式。

  * 类型：align_v_t

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
  
#### clip 属性

* * *

> 是否动态裁剪菜单项(默认裁剪，不裁剪时，如果显示偶数项，左边会多一项)。

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
  
#### menu_w 属性

* * *

> 菜单项的宽度(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)(空字符串则使用控件高度)。

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
  
#### min_scale 属性

* * *

> 最小缩放比例。

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
  
#### spacer 属性

* * *

> 菜单项之间的间距。

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
  
#### value 属性

* * *

> 值。代表当前选中项的索引。

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
