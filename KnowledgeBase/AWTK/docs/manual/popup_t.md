## popup_t

### 概述

![image](images/popup_t_0.png)

弹出窗口。

弹出窗口是一种特殊的窗口，大小和位置可以自由设置，主要用来实现右键菜单和combo_box的下列列表等功能。

popup_t是[window_base_t](window_base_t.html)的子类控件，window_base_t的函数均适用于popup_t控件。

在xml中使用”popup”标签创建弹出窗口。如：
    
    
    <popup close_when_click_outside="true" x="c" y="m" w="80%" h="80" >
    <list_view x="0"  y="0" w="100%" h="100%" item_height="30">
    <scroll_view name="view" x="0"  y="0" w="-12" h="100%">
    <combo_box_item tr_text="english"/>
    <combo_box_item tr_text="chinese" />
    </scroll_view>
    <scroll_bar_d name="bar" x="right" y="0" w="12" h="100%" value="0"/>
    </list_view>
    </popup>
    

> 更多用法请参考：[popup](https://github.com/zlgopen/awtk/blob/master/design/default/ui/)

在c代码中使用函数popup_create创建弹出窗口。如：
    
    
    widget_t* win = popup_create(NULL, 0, 0, w, h);
    popup_set_close_when_click_outside(win, TRUE);
    

> 创建之后，和使用普通窗口是一样的。
> 
> 完整示例请参考：[combo_box.c](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/combo_box.c)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <popup>
    <style name="default" border_color="#a0a0a0">
    <normal bg_color="#f0f0f0"/>
    </style>
    </popup>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L324)

* * *

### 函数

函数名称 | 说明  
---|---  
popup_cast | 转换为popup对象(供脚本语言使用)。  
popup_create | 创建popup对象。  
popup_get_widget_vtable | 获取 popup 虚表。  
popup_set_close_when_click | 设置点击时是否关闭窗口。  
popup_set_close_when_click_outside | 设置点击窗口外部时是否关闭窗口。  
popup_set_close_when_timeout | 设置超时关闭时间(毫秒)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
close_when_click | bool_t | 点击时是否关闭窗口。  
close_when_click_outside | bool_t | 点击到窗口外时是否关闭窗口。  
close_when_timeout | uint32_t | 超时后自动关闭窗口(毫秒)。  
  
#### popup_cast 函数

* * *

  * 函数功能：



> 转换为popup对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* popup_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | popup对象。  
widget | widget_t* | popup对象。  
  
#### popup_create 函数

* * *

  * 函数功能：



> 创建popup对象。

  * 函数原型：


    
    
    widget_t* popup_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | popup对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### popup_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 popup 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* popup_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 popup 虚表。  
  
#### popup_set_close_when_click 函数

* * *

  * 函数功能：



> 设置点击时是否关闭窗口。

  * 函数原型：


    
    
    ret_t popup_set_close_when_click (widget_t* widget, bool_t close_when_click);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
close_when_click | bool_t | 点击时是否关闭窗口。  
  
#### popup_set_close_when_click_outside 函数

* * *

  * 函数功能：



> 设置点击窗口外部时是否关闭窗口。

  * 函数原型：


    
    
    ret_t popup_set_close_when_click_outside (widget_t* widget, bool_t close_when_click_outside);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
close_when_click_outside | bool_t | 点击窗口外部时是否关闭窗口。  
  
#### popup_set_close_when_timeout 函数

* * *

  * 函数功能：



> 设置超时关闭时间(毫秒)。

  * 函数原型：


    
    
    ret_t popup_set_close_when_timeout (widget_t* widget, uint32_t close_when_timeout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
close_when_timeout | uint32_t | 大于0时，为定时器时间(毫秒)，超时关闭窗口。  
  
#### close_when_click 属性

* * *

> 点击时是否关闭窗口。

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
  
#### close_when_click_outside 属性

* * *

> 点击到窗口外时是否关闭窗口。

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
  
#### close_when_timeout 属性

* * *

> 超时后自动关闭窗口(毫秒)。

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
