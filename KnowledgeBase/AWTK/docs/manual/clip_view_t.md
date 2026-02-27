## clip_view_t

### 概述

![image](images/clip_view_t_0.png)

一个裁剪子控件的容器控件。

它本身不提供布局功能，仅提供具有语义的标签，让xml更具有可读性。 子控件的布局可用layout_children属性指定。 请参考[布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)。

clip_view_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于clip_view_t控件。

在xml中使用”clip_view”标签创建clip_view，在clip_view控件下的所有子控件都会被裁剪。如下button控件会被裁剪，无法画出clip_view控件 ：
    
    
    <clip_view x="0" y="0" w="100" h="100">
    <button x="50" y="10" w="100" h="50" />
    </clip_view>
    

备注：在clip_view控件下的所有子控件都会被裁剪，如果子控件本身会设置裁剪区的话，在子控件中计算裁剪区的交集，具体请参考scroll_view控件的scroll_view_on_paint_children函数。

可用通过style来设置控件的显示风格，如背景颜色等。如：
    
    
    <style name="default" border_color="#a0a0a0">
    <normal     bg_color="#f0f0f0" />
    </style>
    

* * *

### 函数

函数名称 | 说明  
---|---  
clip_view_cast | 转换为clip_view对象(供脚本语言使用)。  
clip_view_create | 创建clip_view对象  
  
#### clip_view_cast 函数

* * *

  * 函数功能：



> 转换为clip_view对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* clip_view_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | clip_view对象。  
widget | widget_t* | clip_view对象。  
  
#### clip_view_create 函数

* * *

  * 函数功能：



> 创建clip_view对象

  * 函数原型：


    
    
    widget_t* clip_view_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度
