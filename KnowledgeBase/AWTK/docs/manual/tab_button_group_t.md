## tab_button_group_t

### 概述

![image](images/tab_button_group_t_0.png)

标签按钮分组控件。

一个简单的容器，主要用于对标签按钮进行布局和管理。

tab_button_group_t是[widget_t](widget_t.html)的子类控件， widget_t的函数均适用于tab_button_group_t控件。

在xml中使用”tab_button_group”标签创建标签按钮分组控件。如：
    
    
    <tab_button_group x="c" y="bottom:10" w="90%" h="30" compact="true" >
    <tab_button text="General"/>
    <tab_button text="Network" value="true" />
    <tab_button text="Security"/>
    </tab_button_group>
    

> 更多用法请参考： [tab control](https://github.com/zlgopen/awtk/blob/master/design/default/ui/)

可用通过style来设置控件的显示风格，如颜色等等。如：
    
    
    <tab_button_group>
    <style name="default">
    <normal/>
    </style>
    </tab_button_group>
    

* * *

### 函数

函数名称 | 说明  
---|---  
tab_button_group_cast | 转换tab_button_group对象(供脚本语言使用)。  
tab_button_group_create | 创建tab_button_group对象  
tab_button_group_get_widget_vtable | 获取 tab_button_group 虚表。  
tab_button_group_remove_index | 设置删除 tab_button_group 控件中的 tab_button 控件和对应页。  
tab_button_group_set_compact | 设置compact。  
tab_button_group_set_drag_child | 设置拖拽 tab_button 控件位置。  
tab_button_group_set_scrollable | 设置scrollable。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
compact | bool_t | 紧凑型排版子控件(缺省FALSE)。  
drag_child | bool_t | 是否支持拖拽并且修改 tab_button 控件的位置(缺省FALSE)。  
enable_hscroll_animator | bool_t | 是否开启 tab_button 的左右滚动动画(缺省TRUE)。  
scrollable | bool_t | 是否支持滚动(缺省FALSE)。  
scrollable_mode | char* | 滚动模式 (缺省all) (all:鼠标滚轮+鼠标拖拽滚动，wheel:鼠标滚轮，dragged:鼠标拖拽滚动。  
  
#### tab_button_group_cast 函数

* * *

  * 函数功能：



> 转换tab_button_group对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* tab_button_group_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | tab_button_group对象。  
widget | widget_t* | tab_button_group对象。  
  
#### tab_button_group_create 函数

* * *

  * 函数功能：



> 创建tab_button_group对象

  * 函数原型：


    
    
    widget_t* tab_button_group_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### tab_button_group_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 tab_button_group 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* tab_button_group_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 tab_button_group 虚表。  
  
#### tab_button_group_remove_index 函数

* * *

  * 函数功能：



> 设置删除 tab_button_group 控件中的 tab_button 控件和对应页。

  * 函数原型：


    
    
    ret_t tab_button_group_remove_index (widget_t* widget, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
index | uint32_t | tab_button 的序号。  
  
#### tab_button_group_set_compact 函数

* * *

  * 函数功能：



> 设置compact。

  * 函数原型：


    
    
    ret_t tab_button_group_set_compact (widget_t* widget, bool_t compact);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
compact | bool_t | 是否使用紧凑布局(缺省FALSE)。  
  
#### tab_button_group_set_drag_child 函数

* * *

  * 函数功能：



> 设置拖拽 tab_button 控件位置。

  * 函数原型：


    
    
    ret_t tab_button_group_set_drag_child (widget_t* widget, bool_t drag_child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
drag_child | bool_t | 是否拖拽(缺省FALSE)。  
  
#### tab_button_group_set_scrollable 函数

* * *

  * 函数功能：



> 设置scrollable。

  * 函数原型：


    
    
    ret_t tab_button_group_set_scrollable (widget_t* widget, bool_t scrollable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
scrollable | bool_t | 是否允许滚动(缺省FALSE)。  
  
#### compact 属性

* * *

> 紧凑型排版子控件(缺省FALSE)。

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
  
#### drag_child 属性

* * *

> 是否支持拖拽并且修改 tab_button 控件的位置(缺省FALSE)。
> 
> 紧凑型排版子控件时才支持滚动，开启该功能后，就不能拖拽滚动了，只能鼠标滚轮滚动了。

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
  
#### enable_hscroll_animator 属性

* * *

> 是否开启 tab_button 的左右滚动动画(缺省TRUE)。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### scrollable 属性

* * *

> 是否支持滚动(缺省FALSE)。
> 
> 紧凑型排版子控件时才支持滚动。

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
  
#### scrollable_mode 属性

* * *

> 滚动模式 (缺省all) (all:鼠标滚轮+鼠标拖拽滚动，wheel:鼠标滚轮，dragged:鼠标拖拽滚动。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是
