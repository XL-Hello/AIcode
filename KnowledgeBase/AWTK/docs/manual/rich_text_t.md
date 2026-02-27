## rich_text_t

### 概述

![image](images/rich_text_t_0.png)

图文混排控件，实现简单的图文混排。

rich_text_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于rich_text_t控件。

在xml中使用”rich_text”标签创建图文混排控件。如：
    
    
    <rich_text x="0" y="0" w="100%" h="60"
    text="<image name=&quota;bricks&quota;/><font align_v=&quota;middle&quota;>hello awtk!</font>" />
    

> 更多用法请参考： [rich_text.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/rich_text.xml)

在c代码中使用函数rich_text_create创建图文混排控件。如：
    
    
    widget_t* rich_text = rich_text_create(win, 0, 0, 0, 0);
    widget_set_text_utf8(rich_text,
    "<image name=\"bricks\"/><font color=\"gold\" align_v=\"bottom\" "
    "size=\"24\">hello awtk!</font><font color=\"green\" size=\"20\">ProTip! The "
    "feed shows you events from people you follow and repositories you watch. "
    "nhello world. </font><font color=\"red\" "
    "size=\"20\">确定取消中文字符测试。确定。取消。中文字符测试。</font>");
    
    widget_set_self_layout_params(rich_text, "center", "middle", "100%", "100%");
    

> 完整示例请参考： [rich_text demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/rich_text.c)

可用通过style来设置控件的显示风格，如背景颜色等等。而字体的大小和颜色则由文本内部的属性决定。

目前支持image和font两个tag：

  * image 支持的属性有：
  * name 图片的名称。
  * w 图片的宽度。
  * h 图片的高度。

  * font 支持的属性有：

  * color 颜色。
  * size 大小。
  * align_v 垂直方向对齐的方式(top|middle|bottom)。
  * bold 粗体(暂不支持)
  * italic 斜体(暂不支持)
  * underline 下划线(暂不支持)



* * *

### 函数

函数名称 | 说明  
---|---  
rich_text_cast | 转换为rich_text对象(供脚本语言使用)。  
rich_text_create | 创建rich_text对象  
rich_text_get_widget_vtable | 获取 rich_text 虚表。  
rich_text_set_text | 设置文本。  
rich_text_set_yslidable | 设置是否允许y方向滑动。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
line_gap | uint32_t | 行间距。  
need_reset | bool_t | 标识控件是否需要重新绘图。  
yoffset | int32_t | y偏移。  
yslidable | bool_t | 标识控件是否允许上下拖动。  
  
#### rich_text_cast 函数

* * *

  * 函数功能：



> 转换为rich_text对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* rich_text_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | rich_text对象。  
widget | widget_t* | rich_text对象。  
  
#### rich_text_create 函数

* * *

  * 函数功能：



> 创建rich_text对象

  * 函数原型：


    
    
    widget_t* rich_text_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### rich_text_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 rich_text 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* rich_text_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 rich_text 虚表。  
  
#### rich_text_set_text 函数

* * *

  * 函数功能：



> 设置文本。

  * 函数原型：


    
    
    ret_t rich_text_set_text (widget_t* widget, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
text | const char* | 文本。  
  
#### rich_text_set_yslidable 函数

* * *

  * 函数功能：



> 设置是否允许y方向滑动。

  * 函数原型：


    
    
    ret_t rich_text_set_yslidable (widget_t* widget, bool_t yslidable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
yslidable | bool_t | 是否允许滑动。  
  
#### line_gap 属性

* * *

> 行间距。

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
  
#### need_reset 属性

* * *

> 标识控件是否需要重新绘图。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### yoffset 属性

* * *

> y偏移。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### yslidable 属性

* * *

> 标识控件是否允许上下拖动。

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
