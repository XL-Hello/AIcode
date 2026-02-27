## rich_text_view_t

### 概述

![image](images/rich_text_view_t_0.png)

rich_text_view是一个专用容器，用来放rich text和 scroll bar，并在两者之间建立联系。

rich_text_view_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于rich_text_view_t控件。

在xml中使用”rich_text_view”标签创建rich_text_view。如：
    
    
    <rich_text_view x="0" y="10" w="100%" h="300">
    <rich_text line_gap="5" x="0" y="10" w="-12" h="100%" margin="10">
    ...
    </rich_text>
    <scroll_bar_d name="bar" x="right" y="0" w="12" h="100%" value="0"/>
    </rich_text_view>
    

可用通过style来设置控件的显示风格，如背景颜色等。如：
    
    
    <style name="default" border_color="#a0a0a0">
    <normal     bg_color="#f0f0f0" />
    </style>
    

* * *

### 函数

函数名称 | 说明  
---|---  
rich_text_view_cast | 转换为rich_text_view对象(供脚本语言使用)。  
rich_text_view_create | 创建rich_text_view对象  
  
#### rich_text_view_cast 函数

* * *

  * 函数功能：



> 转换为rich_text_view对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* rich_text_view_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | rich_text_view对象。  
widget | widget_t* | rich_text_view对象。  
  
#### rich_text_view_create 函数

* * *

  * 函数功能：



> 创建rich_text_view对象

  * 函数原型：


    
    
    widget_t* rich_text_view_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度
