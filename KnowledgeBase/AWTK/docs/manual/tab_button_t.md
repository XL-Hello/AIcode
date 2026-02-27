## tab_button_t

### 概述

![image](images/tab_button_t_0.png)

标签按钮控件。

标签按钮有点类似单选按钮，但点击标签按钮之后会自动切换当前的标签页。

tab_button_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于tab_button_t控件。

在xml中使用”tab_button”标签创建标签按钮控件。如：
    
    
    <!-- tab_button_view_page1.xml -->
    <view w="100%" h="100%">
    <label x="c" y="m" w="100%" h="60" text="page1" />
    <button name="close" x="c" y="bottom:100" w="80" h="40" text="Close" />
    </view>
    
    
    
    <!-- tab_button dynamic load UI -->
    <pages name="pages" x="right" y="0" w="70%" h="100%">
    </pages>
    <list_view x="0" y="0" w="30%" h="100%" item_height="40" auto_hide_scroll_bar="true">
    <scroll_view name="view" x="0"  y="0" w="-12" h="100%">
    <tab_button text="page1" load_ui="tab_button_view_page1" value="true"/>
    <tab_button text="page2" load_ui="tab_button_view_page2" />
    <tab_button text="page3" load_ui="tab_button_view_page3" />
    <scroll_view />
    <scroll_bar_d name="bar" x="right" y="0" w="12" h="100%" value="0"/>
    </list_view>
    
    
    
    <!-- tab_button static load UI -->
    <tab_button_group x="c" y="bottom:10" w="90%" h="30" compact="true" >
    <tab_button text="General"/>
    <tab_button text="Network" value="true" />
    <tab_button text="Security"/>
    </tab_button_group>
    

标签按钮一般放在标签按钮分组中，布局由标签按钮分组控件决定，不需要指定自己的布局参数和坐标。

> 更多用法请参考： [tab control](https://github.com/zlgopen/awtk/blob/master/design/default/ui/)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <tab_button>
    <style name="default" border_color="#a0a0a0"  text_color="black">
    <normal     bg_color="#d0d0d0" />
    <pressed    bg_color="#f0f0f0" />
    <over       bg_color="#e0e0e0" />
    <normal_of_active     bg_color="#f0f0f0" />
    <pressed_of_active    bg_color="#f0f0f0" />
    <over_of_active       bg_color="#f0f0f0" />
    </style>
    </tab_button>
    

* * *

### 函数

函数名称 | 说明  
---|---  
tab_button_cast | 转换tab_button对象(供脚本语言使用)。  
tab_button_create | 创建tab_button对象  
tab_button_get_widget_vtable | 获取 tab_button 虚表。  
tab_button_restack | 调整控件在父控件中的位置序数。  
tab_button_set_active_icon | 设置控件的active图标。  
tab_button_set_icon | 设置控件的图标。  
tab_button_set_load_ui | 设置控件动态加载显示UI。  
tab_button_set_max_w | 设置控件的最大宽度。  
tab_button_set_value | 设置为当前标签。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
active_icon | char* | 当前项的图标的名称。  
icon | char* | 非当前项的图标的名称。  
load_ui | char* | 激活后加载的UI名字。  
max_w | int32_t | 最大宽度。（缺省值为-1，小于 0 则最大宽度无效）  
value | bool_t | 值。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(激活状态)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(激活状态)改变事件。  
EVT_CLICK | pointer_event_t | 点击事件。  
  
#### tab_button_cast 函数

* * *

  * 函数功能：



> 转换tab_button对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* tab_button_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | tab_button对象。  
widget | widget_t* | tab_button对象。  
  
#### tab_button_create 函数

* * *

  * 函数功能：



> 创建tab_button对象

  * 函数原型：


    
    
    widget_t* tab_button_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### tab_button_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 tab_button 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* tab_button_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 tab_button 虚表。  
  
#### tab_button_restack 函数

* * *

  * 函数功能：



> 调整控件在父控件中的位置序数。

  * 函数原型：


    
    
    ret_t tab_button_restack (widget_t* widget, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | tab_button对象。  
index | uint32_t | 位置序数(大于等于总个数，则放到最后)。  
  
#### tab_button_set_active_icon 函数

* * *

  * 函数功能：



> 设置控件的active图标。

  * 函数原型：


    
    
    ret_t tab_button_set_active_icon (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | tab_button对象。  
name | const char* | 当前项的图标。  
  
#### tab_button_set_icon 函数

* * *

  * 函数功能：



> 设置控件的图标。

  * 函数原型：


    
    
    ret_t tab_button_set_icon (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | tab_button对象。  
name | const char* | 当前项的图标。  
  
#### tab_button_set_load_ui 函数

* * *

  * 函数功能：



> 设置控件动态加载显示UI。

  * 函数原型：


    
    
    ret_t tab_button_set_load_ui (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | tab_button对象。  
name | const char* | 动态加载UI的资源名称。  
  
#### tab_button_set_max_w 函数

* * *

  * 函数功能：



> 设置控件的最大宽度。

  * 函数原型：


    
    
    ret_t tab_button_set_max_w (widget_t* widget, int32_t max_w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | tab_button对象。  
max_w | int32_t | 最大宽度。  
  
#### tab_button_set_value 函数

* * *

  * 函数功能：



> 设置为当前标签。

  * 函数原型：


    
    
    ret_t tab_button_set_value (widget_t* widget, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | tab_button对象。  
value | bool_t | 是否为当前标签。  
  
#### active_icon 属性

* * *

> 当前项的图标的名称。

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
  
#### icon 属性

* * *

> 非当前项的图标的名称。

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
  
#### load_ui 属性

* * *

> 激活后加载的UI名字。

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
  
#### max_w 属性

* * *

> 最大宽度。（缺省值为-1，小于 0 则最大宽度无效）

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
