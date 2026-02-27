## slide_view_t

### 概述

![image](images/slide_view_t_0.png)

滑动视图。

滑动视图可以管理多个页面，并通过滑动来切换当前页面。也可以管理多张图片，让它们自动切换。

slide_view_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于slide_view_t控件。

在xml中使用”slide_view”标签创建滑动视图控件。如：
    
    
    <slide_view x="0" y="0" w="100%" h="100%" style="dot">
    <view x="0" y="0" w="100%" h="100%" children_layout="default(w=60,h=60,m=5,s=10)">
    ...
    </view>
    <view x="0" y="0" w="100%" h="100%" children_layout="default(w=60,h=60,m=5,s=10)">
    ...
    </view>
    </slide_view>
    

> 更多用法请参考：[slide_view.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/slide_view.xml)

在c代码中使用函数slide_view_create创建滑动视图控件。如：
    
    
    slide_view = slide_view_create(win, 0, 0, win->w, win->h);
    

> 完整示例请参考： [slide_view demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/slide_view.c)

可用通过style来设置控件的显示风格，如背景颜色和指示器的图标等等。如：
    
    
    <style name="dot">
    <normal  icon="dot" active_icon="active_dot"/>
    </style>
    

> 如果希望背景图片跟随滚动，请将背景图片设置到页面上，否则设置到slide_view上。
> 
> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L458)

* * *

### 函数

函数名称 | 说明  
---|---  
slide_view_cast | 转换为slide_view对象(供脚本语言使用)。  
slide_view_create | 创建slide_view对象  
slide_view_get_widget_vtable | 获取 slide_view 虚表。  
slide_view_remove_index | 删除指定序号页面。  
slide_view_set_active | 设置当前页的序号(默认启用动画)。  
slide_view_set_active_ex | 设置当前页的序号。  
slide_view_set_anim_hint | 设置页面切换动画。  
slide_view_set_animating_time | 设置动画时间(毫秒)。  
slide_view_set_auto_play | 设置为自动播放模式。  
slide_view_set_drag_threshold | 设置拖拽临界值。  
slide_view_set_loop | 设置循环切换模式。  
slide_view_set_vertical | 设置为上下滑动(缺省为左右滑动)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
anim_hint | char* | 页面切换效果。  
animating_time | uint32_t | 动画时间（单位：毫秒）。  
auto_play | uint16_t | 自动播放。0表示禁止自动播放，非0表示自动播放时每一页播放的时间(毫秒)。  
drag_threshold | uint32_t | 拖动临界值。  
loop | bool_t | 循环切换模式。  
vertical | bool_t | 是否为上下滑动模式。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(当前页)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(当前页)改变事件。  
EVT_PAGE_CHANGED | event_t | 页面改变事件。  
EVT_PAGE_CHANGING | event_t | 页面正在改变。  
  
#### slide_view_cast 函数

* * *

  * 函数功能：



> 转换为slide_view对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* slide_view_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | slide_view对象。  
widget | widget_t* | slide_view对象。  
  
#### slide_view_create 函数

* * *

  * 函数功能：



> 创建slide_view对象

  * 函数原型：


    
    
    widget_t* slide_view_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### slide_view_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 slide_view 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* slide_view_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 slide_view 虚表。  
  
#### slide_view_remove_index 函数

* * *

  * 函数功能：



> 删除指定序号页面。

  * 函数原型：


    
    
    ret_t slide_view_remove_index (widget_t* widget, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
index | uint32_t | 删除页面的序号。  
  
#### slide_view_set_active 函数

* * *

  * 函数功能：



> 设置当前页的序号(默认启用动画)。

  * 函数原型：


    
    
    ret_t slide_view_set_active (widget_t* widget, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
index | uint32_t | 当前页的序号。  
  
#### slide_view_set_active_ex 函数

* * *

  * 函数功能：



> 设置当前页的序号。

  * 函数原型：


    
    
    ret_t slide_view_set_active_ex (widget_t* widget, uint32_t index, bool_t animate);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
index | uint32_t | 当前页的序号。  
animate | bool_t | 是否启用动画。  
  
#### slide_view_set_anim_hint 函数

* * *

  * 函数功能：



> 设置页面切换动画。

anim_hint取值如下：

  * “translate”：平移。
  * “overlap”：覆盖。
  * “overlap_with_alpha”：覆盖并改变透明度。



> 使用”overlap”或”overlap_with_alpha”动画时，背景图片最好指定到page上。
> 
> 使用”overlap_with_alpha”动画时，slideview的背景设置为黑色， 或slideview的背景设置为透明，窗口的背景设置为黑色，以获得更好的视觉效果和性能。

  * 函数原型：


    
    
    ret_t slide_view_set_anim_hint (widget_t* widget, const char* anim_hint);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
anim_hint | const char* | 页面切换动画。  
  
#### slide_view_set_animating_time 函数

* * *

  * 函数功能：



> 设置动画时间(毫秒)。

  * 函数原型：


    
    
    ret_t slide_view_set_animating_time (widget_t* widget, uint32_t animating_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
animating_time | uint32_t | 动画时间(毫秒)。  
  
#### slide_view_set_auto_play 函数

* * *

  * 函数功能：



> 设置为自动播放模式。

  * 函数原型：


    
    
    ret_t slide_view_set_auto_play (widget_t* widget, uint16_t auto_play);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
auto_play | uint16_t | 0表示禁止自动播放，非0表示自动播放时每一页播放的时间(毫秒)。  
  
#### slide_view_set_drag_threshold 函数

* * *

  * 函数功能：



> 设置拖拽临界值。

  * 函数原型：


    
    
    ret_t slide_view_set_drag_threshold (widget_t* widget, uint32_t drag_threshold);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
drag_threshold | uint32_t | 拖动临界值。  
  
#### slide_view_set_loop 函数

* * *

  * 函数功能：



> 设置循环切换模式。

  * 函数原型：


    
    
    ret_t slide_view_set_loop (widget_t* widget, bool_t loop);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
loop | bool_t | 是否启用循环切换模式。  
  
#### slide_view_set_vertical 函数

* * *

  * 函数功能：



> 设置为上下滑动(缺省为左右滑动)。

  * 函数原型：


    
    
    ret_t slide_view_set_vertical (widget_t* widget, bool_t vertical);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | slide_view对象。  
vertical | bool_t | TRUE表示上下滑动，FALSE表示左右滑动。  
  
#### anim_hint 属性

* * *

> 页面切换效果。

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
  
#### animating_time 属性

* * *

> 动画时间（单位：毫秒）。

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
  
#### auto_play 属性

* * *

> 自动播放。0表示禁止自动播放，非0表示自动播放时每一页播放的时间(毫秒)。

  * 类型：uint16_t

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
  
#### drag_threshold 属性

* * *

> 拖动临界值。

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
  
#### loop 属性

* * *

> 循环切换模式。

向后切换：切换到最后一页时，再往后切换就到第一页。 向前切换：切换到第一页时，再往前切换就到最后一页。

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
  
#### vertical 属性

* * *

> 是否为上下滑动模式。

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
