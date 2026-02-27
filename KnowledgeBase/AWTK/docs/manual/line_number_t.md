## line_number_t

### 概述

![image](images/line_number_t_0.png)

行号。多行编辑器的行号。

line_number_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于line_number_t控件。

在xml中使用”lin\e_number”标签创建行号控件，一般配合mledit使用。如：
    
    
    <mledit x="c" y="10" h="40%" w="90%" focus="true" left_margin="36" right_margin="16"
    wrap_word="true">
    <line_number x="0" y="0" w="32" h="100%" value="0"/>
    <scroll_bar_d x="right" y="0" w="14" h="100%" value="0"/>
    </mledit>
    

> 更多用法请参考：[mledit.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/mledit.xml)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <line_number>
    <style name="default">
    <normal text_color="black" bg_color="#d0d0d0" text_align_h="right"/>
    </style>
    </line_number>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L556)

* * *

### 函数

函数名称 | 说明  
---|---  
line_number_add_highlight_line | 增加高亮行。  
line_number_cast | 转换为line_number对象(供脚本语言使用)。  
line_number_clear_highlight | 清除高亮行。  
line_number_create | 创建line_number对象  
line_number_get_widget_vtable | 获取 line_number 虚表。  
line_number_is_highlight_line | 判断指定行是否是高亮行。  
line_number_set_active_line | 设置active行。  
line_number_set_bottom_margin | 设置顶部边距。  
line_number_set_line_height | 设置行高。  
line_number_set_lines_of_each_row | 设置每一个逻辑行(row)占几个物理行(line)。  
line_number_set_top_margin | 设置顶部边距。  
line_number_set_yoffset | 设置y偏移。  
  
#### line_number_add_highlight_line 函数

* * *

  * 函数功能：



> 增加高亮行。

  * 函数原型：


    
    
    ret_t line_number_add_highlight_line (widget_t* widget, int32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
line | int32_t | 行号。  
  
#### line_number_cast 函数

* * *

  * 函数功能：



> 转换为line_number对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* line_number_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | line_number对象。  
widget | widget_t* | line_number对象。  
  
#### line_number_clear_highlight 函数

* * *

  * 函数功能：



> 清除高亮行。

  * 函数原型：


    
    
    ret_t line_number_clear_highlight (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### line_number_create 函数

* * *

  * 函数功能：



> 创建line_number对象

  * 函数原型：


    
    
    widget_t* line_number_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### line_number_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 line_number 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* line_number_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 line_number 虚表。  
  
#### line_number_is_highlight_line 函数

* * *

  * 函数功能：



> 判断指定行是否是高亮行。

  * 函数原型：


    
    
    bool_t line_number_is_highlight_line (widget_t* widget, int32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则不是。  
widget | widget_t* | 控件对象。  
line | int32_t | 行号。  
  
#### line_number_set_active_line 函数

* * *

  * 函数功能：



> 设置active行。

  * 函数原型：


    
    
    ret_t line_number_set_active_line (widget_t* widget, int32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
line | int32_t | 行号。  
  
#### line_number_set_bottom_margin 函数

* * *

  * 函数功能：



> 设置顶部边距。

  * 函数原型：


    
    
    ret_t line_number_set_bottom_margin (widget_t* widget, int32_t bottom_margin);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
bottom_margin | int32_t | 顶部边距。  
  
#### line_number_set_line_height 函数

* * *

  * 函数功能：



> 设置行高。

  * 函数原型：


    
    
    ret_t line_number_set_line_height (widget_t* widget, int32_t line_height);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
line_height | int32_t | 行高。  
  
#### line_number_set_lines_of_each_row 函数

* * *

  * 函数功能：



> 设置每一个逻辑行(row)占几个物理行(line)。

  * 函数原型：


    
    
    ret_t line_number_set_lines_of_each_row (widget_t* widget, const uint32_t* lines_of_each_row, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
lines_of_each_row | const uint32_t* | 每一个逻辑行占几个物理行。  
len | uint32_t | 数组大小(逻辑行数)。  
  
#### line_number_set_top_margin 函数

* * *

  * 函数功能：



> 设置顶部边距。

  * 函数原型：


    
    
    ret_t line_number_set_top_margin (widget_t* widget, int32_t top_margin);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
top_margin | int32_t | 顶部边距。  
  
#### line_number_set_yoffset 函数

* * *

  * 函数功能：



> 设置y偏移。

  * 函数原型：


    
    
    ret_t line_number_set_yoffset (widget_t* widget, int32_t yoffset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
yoffset | int32_t | 行高。
