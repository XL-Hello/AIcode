## scroll_view_t

### 概述

![image](images/scroll_view_t_0.png)

滚动视图。

scroll_view_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于scroll_view_t控件。

在xml中使用”scroll_view”标签创建滚动视图控件。如：
    
    
    <list_view x="0"  y="30" w="100%" h="-80" item_height="60">
    <scroll_view name="view" x="0"  y="0" w="100%" h="100%">
    <list_item style="odd" children_layout="default(rows=1,cols=0)">
    <image draw_type="icon" w="30" image="earth"/>
    <label w="-30" text="1.Hello AWTK !">
    <switch x="r:10" y="m" w="60" h="20"/>
    </label>
    </list_item>
    ...
    </scroll_view>
    </list_view>
    

> 滚动视图一般作为列表视图的子控件使用。
> 
> 更多用法请参考：[list_view_m.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/list_view_m.xml)

在c代码中使用函数scroll_view_create创建列表视图控件。如：
    
    
    widget_t* scroll_view = scroll_view_create(win, 0, 0, 0, 0);
    

## 可用通过style来设置控件的显示风格，如背景颜色和边框颜色等(一般情况不需要)。

### 函数

函数名称 | 说明  
---|---  
scroll_view_cast | 转换为scroll_view对象(供脚本语言使用)。  
scroll_view_create | 创建scroll_view对象  
scroll_view_get_widget_vtable | 获取 scroll_view 虚表。  
scroll_view_scroll_delta_to | 滚动到指定的偏移量。  
scroll_view_scroll_to | 滚动到指定的偏移量。  
scroll_view_set_move_to_page | 设置滚动时是否每次翻一页  
scroll_view_set_offset | 设置偏移量。  
scroll_view_set_recursive | 设置是否递归查找全部子控件。  
scroll_view_set_recursive_only | 设置是否递归查找全部子控件。(不触发repaint和relayout)。  
scroll_view_set_slide_limit_ratio | 设置滑动到极限时可继续滑动区域的占比。  
scroll_view_set_snap_to_page | 设置滚动时offset是否按页面对齐。  
scroll_view_set_speed_scale | 设置偏移速度比例。  
scroll_view_set_virtual_h | 设置虚拟高度。  
scroll_view_set_virtual_w | 设置虚拟宽度。  
scroll_view_set_xslidable | 设置是否允许x方向滑动。  
scroll_view_set_yslidable | 设置是否允许y方向滑动。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
move_to_page | bool_t | 是否每次翻一页（当 move_to_page 为ture 的时候才有效果，主要用于区分一次翻一页还是一次翻多页）。  
recursive | bool_t | 是否递归查找全部子控件。  
slide_limit_ratio | float_t | 滑动到极限时可继续滑动区域的占比。  
snap_to_page | bool_t | 滚动时offset是否按页面对齐。  
virtual_h | wh_t | 虚拟高度。  
virtual_w | wh_t | 虚拟宽度。  
xoffset | int32_t | x偏移量。  
xslidable | bool_t | 是否允许x方向滑动。  
xspeed_scale | float_t | x偏移速度比例。  
yoffset | int32_t | y偏移量。  
yslidable | bool_t | 是否允许y方向滑动。  
yspeed_scale | float_t | y偏移速度比例。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_SCROLL_START | event_t | 开始滚动事件。  
EVT_SCROLL_END | event_t | 结束滚动事件。  
EVT_SCROLL | event_t | 滚动事件。  
EVT_PAGE_CHANGED | event_t | 页面改变事件。  
EVT_PAGE_CHANGING | event_t | 页面正在改变。  
  
#### scroll_view_cast 函数

* * *

  * 函数功能：



> 转换为scroll_view对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* scroll_view_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | scroll_view对象。  
widget | widget_t* | scroll_view对象。  
  
#### scroll_view_create 函数

* * *

  * 函数功能：



> 创建scroll_view对象

  * 函数原型：


    
    
    widget_t* scroll_view_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### scroll_view_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 scroll_view 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* scroll_view_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 scroll_view 虚表。  
  
#### scroll_view_scroll_delta_to 函数

* * *

  * 函数功能：



> 滚动到指定的偏移量。

  * 函数原型：


    
    
    ret_t scroll_view_scroll_delta_to (widget_t* widget, int32_t xoffset_delta, int32_t yoffset_delta, int32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
xoffset_delta | int32_t | x偏移量。  
yoffset_delta | int32_t | y偏移量。  
duration | int32_t | 时间(毫秒)。  
  
#### scroll_view_scroll_to 函数

* * *

  * 函数功能：



> 滚动到指定的偏移量。

  * 函数原型：


    
    
    ret_t scroll_view_scroll_to (widget_t* widget, int32_t xoffset_end, int32_t yoffset_end, int32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
xoffset_end | int32_t | x偏移量。  
yoffset_end | int32_t | y偏移量。  
duration | int32_t | 时间(毫秒)。  
  
#### scroll_view_set_move_to_page 函数

* * *

  * 函数功能：



> 设置滚动时是否每次翻一页 备注：当 snap_to_page 为ture 的时候才有效果，主要用于区分一次翻一页还是一次翻多页。

  * 函数原型：


    
    
    ret_t scroll_view_set_move_to_page (widget_t* widget, bool_t move_to_page);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
move_to_page | bool_t | 是否每次翻一页。  
  
#### scroll_view_set_offset 函数

* * *

  * 函数功能：



> 设置偏移量。

  * 函数原型：


    
    
    ret_t scroll_view_set_offset (widget_t* widget, int32_t xoffset, int32_t yoffset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
xoffset | int32_t | x偏移量。  
yoffset | int32_t | y偏移量。  
  
#### scroll_view_set_recursive 函数

* * *

  * 函数功能：



> 设置是否递归查找全部子控件。

  * 函数原型：


    
    
    ret_t scroll_view_set_recursive (widget_t* widget, bool_t recursive);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
recursive | bool_t | 是否递归查找全部子控件。  
  
#### scroll_view_set_recursive_only 函数

* * *

  * 函数功能：



> 设置是否递归查找全部子控件。(不触发repaint和relayout)。

  * 函数原型：


    
    
    ret_t scroll_view_set_recursive_only (widget_t* widget, bool_t recursive);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
recursive | bool_t | 是否递归查找全部子控件。  
  
#### scroll_view_set_slide_limit_ratio 函数

* * *

  * 函数功能：



> 设置滑动到极限时可继续滑动区域的占比。

  * 函数原型：


    
    
    ret_t scroll_view_set_slide_limit_ratio (widget_t* widget, float_t slide_limit_ratio);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
slide_limit_ratio | float_t | 滑动到极限时可继续滑动区域的占比。  
  
#### scroll_view_set_snap_to_page 函数

* * *

  * 函数功能：



> 设置滚动时offset是否按页面对齐。

  * 函数原型：


    
    
    ret_t scroll_view_set_snap_to_page (widget_t* widget, bool_t snap_to_page);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
snap_to_page | bool_t | 是否按页面对齐。  
  
#### scroll_view_set_speed_scale 函数

* * *

  * 函数功能：



> 设置偏移速度比例。

  * 函数原型：


    
    
    ret_t scroll_view_set_speed_scale (widget_t* widget, float_t xspeed_scale, float_t yspeed_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
xspeed_scale | float_t | x偏移速度比例。  
yspeed_scale | float_t | y偏移速度比例。  
  
#### scroll_view_set_virtual_h 函数

* * *

  * 函数功能：



> 设置虚拟高度。

  * 函数原型：


    
    
    ret_t scroll_view_set_virtual_h (widget_t* widget, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
h | wh_t | 虚拟高度。  
  
#### scroll_view_set_virtual_w 函数

* * *

  * 函数功能：



> 设置虚拟宽度。

  * 函数原型：


    
    
    ret_t scroll_view_set_virtual_w (widget_t* widget, wh_t w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
w | wh_t | 虚拟宽度。  
  
#### scroll_view_set_xslidable 函数

* * *

  * 函数功能：



> 设置是否允许x方向滑动。

  * 函数原型：


    
    
    ret_t scroll_view_set_xslidable (widget_t* widget, bool_t xslidable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
xslidable | bool_t | 是否允许滑动。  
  
#### scroll_view_set_yslidable 函数

* * *

  * 函数功能：



> 设置是否允许y方向滑动。

  * 函数原型：


    
    
    ret_t scroll_view_set_yslidable (widget_t* widget, bool_t yslidable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
yslidable | bool_t | 是否允许滑动。  
  
#### move_to_page 属性

* * *

> 是否每次翻一页（当 move_to_page 为ture 的时候才有效果，主要用于区分一次翻一页还是一次翻多页）。

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
  
#### recursive 属性

* * *

> 是否递归查找全部子控件。

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
  
#### slide_limit_ratio 属性

* * *

> 滑动到极限时可继续滑动区域的占比。

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
  
#### snap_to_page 属性

* * *

> 滚动时offset是否按页面对齐。

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
  
#### virtual_h 属性

* * *

> 虚拟高度。

  * 类型：wh_t

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
  
#### virtual_w 属性

* * *

> 虚拟宽度。

  * 类型：wh_t

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
  
#### xoffset 属性

* * *

> x偏移量。

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
  
#### xslidable 属性

* * *

> 是否允许x方向滑动。

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
  
#### xspeed_scale 属性

* * *

> x偏移速度比例。

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
  
#### yoffset 属性

* * *

> y偏移量。

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
  
#### yslidable 属性

* * *

> 是否允许y方向滑动。

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
  
#### yspeed_scale 属性

* * *

> y偏移速度比例。

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
