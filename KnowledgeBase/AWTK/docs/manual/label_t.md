## label_t

### 概述

![image](images/label_t_0.png)

文本控件。用于显示一行或多行文本。

文本控件不会根据文本的长度自动换行，只有文本内容包含换行符时才会换行。

如需自动换行请使用[rich_text_t](rich_text_t.html)控件。

label_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于label_t控件。

在xml中使用”label”标签创建文本控件。如：
    
    
    <label style="center" text="center"/>
    

> 更多用法请参考：[label.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/label.xml)

在c代码中使用函数label_create创建文本控件。如：
    
    
    widget_t* label = label_create(win, 10, 10, 128, 30);
    widget_set_text(label, L"hello awtk!");
    

> 创建之后，需要用widget_set_text或widget_set_text_utf8设置文本内容。
> 
> 完整示例请参考：[label demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/label.c)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <style name="left">
    <normal text_color="red" text_align_h="left" border_color="#a0a0a0" margin="4" />
    </style>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L144)

* * *

### 函数

函数名称 | 说明  
---|---  
label_cast | 转换为label对象(供脚本语言使用)。  
label_create | 创建label对象  
label_get_widget_vtable | 获取 label 虚表。  
label_resize_to_content | 根据文本内容调节控件大小。  
label_set_ellipses | 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为…  
label_set_length | 设置显示字符的个数(小于0时全部显示)。  
label_set_line_wrap | 设置是否自动换行。  
label_set_max_w | 设置max_w。  
label_set_word_wrap | 设置是否允许整个单词换行。(需要开启自动换行才有效果)  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
ellipses | bool_t | 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为…  
length | int32_t | 显示字符的个数(小于0时全部显示)。  
line_wrap | bool_t | 是否自动换行(默认FALSE)。  
max_w | int32_t | 当auto_adjust_size为TRUE时，用于控制控件的最大宽度，超出该宽度后才自动换行。  
word_wrap | bool_t | 是否允许整个单词换行(默认FALSE)。  
  
#### label_cast 函数

* * *

  * 函数功能：



> 转换为label对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* label_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | label对象。  
widget | widget_t* | label对象。  
  
#### label_create 函数

* * *

  * 函数功能：



> 创建label对象

  * 函数原型：


    
    
    widget_t* label_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### label_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 label 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* label_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 label 虚表。  
  
#### label_resize_to_content 函数

* * *

  * 函数功能：



> 根据文本内容调节控件大小。

  * 函数原型：


    
    
    ret_t label_resize_to_content (widget_t* widget, uint32_t min_w, uint32_t max_w, uint32_t min_h, uint32_t max_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
min_w | uint32_t | 最小宽度。  
max_w | uint32_t | 最大宽度。  
min_h | uint32_t | 最小高度。  
max_h | uint32_t | 最大高度。  
  
#### label_set_ellipses 函数

* * *

  * 函数功能：



> 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为…

  * 函数原型：


    
    
    ret_t label_set_ellipses (widget_t* widget, bool_t ellipses);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
ellipses | bool_t | 是否开启缩写。  
  
#### label_set_length 函数

* * *

  * 函数功能：



> 设置显示字符的个数(小于0时全部显示)。

  * 函数原型：


    
    
    ret_t label_set_length (widget_t* widget, int32_t length);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
length | int32_t | 最大可显示字符个数。  
  
#### label_set_line_wrap 函数

* * *

  * 函数功能：



> 设置是否自动换行。

  * 函数原型：


    
    
    ret_t label_set_line_wrap (widget_t* widget, bool_t line_wrap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
line_wrap | bool_t | 是否自动换行。  
  
#### label_set_max_w 函数

* * *

  * 函数功能：



> 设置max_w。

  * 函数原型：


    
    
    ret_t label_set_max_w (widget_t* widget, int32_t max_w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
max_w | int32_t | 最大宽度。  
  
#### label_set_word_wrap 函数

* * *

  * 函数功能：



> 设置是否允许整个单词换行。(需要开启自动换行才有效果)

  * 函数原型：


    
    
    ret_t label_set_word_wrap (widget_t* widget, bool_t word_wrap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
word_wrap | bool_t | 是否允许整个单词换行。  
  
#### ellipses 属性

* * *

> 是否开启缩写，开启后，当文字长度操作控件长度后，自动变为… 和换行是冲突的，换行后，该属性不生效

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
  
#### length 属性

* * *

> 显示字符的个数(小于0时全部显示)。 主要用于动态改变显示字符的个数，来实现类似[拨号中…]的动画效果。

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
  
#### line_wrap 属性

* * *

> 是否自动换行(默认FALSE)。

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
  
#### max_w 属性

* * *

> 当auto_adjust_size为TRUE时，用于控制控件的最大宽度，超出该宽度后才自动换行。 为0表示忽略该参数。小于0时取父控件宽度加上max_w。

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
  
#### word_wrap 属性

* * *

> 是否允许整个单词换行(默认FALSE)。 需要开启自动换行才有效果

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
