## app_bar_t

### 概述

![image](images/app_bar_t_0.png)

app_bar控件。

一个简单的容器控件，一般在窗口的顶部，用于显示本窗口的状态和信息。

它本身不提供布局功能，仅提供具有语义的标签，让xml更具有可读性。 子控件的布局可用layout_children属性指定。 请参考[布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)。

app_bar_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于app_bar_t控件。

在xml中使用”app_bar”标签创建app_bar。如：
    
    
    <app_bar x="0" y="0" w="100%" h="30" >
    <label x="0" y="0" w="100%" h="100%" text="Basic Controls" />
    </app_bar>
    

在c代码中使用函数app_bar_create创建app_bar。如：
    
    
    widget_t* app_bar = app_bar_create(win, 0, 0, 320, 30);
    

可用通过style来设置控件的显示风格，如背景颜色等。如：
    
    
    <style name="default" border_color="#a0a0a0">
    <normal     bg_color="#f0f0f0" />
    </style>
    

* * *

### 函数

函数名称 | 说明  
---|---  
app_bar_cast | 转换为app_bar对象(供脚本语言使用)。  
app_bar_create | 创建app_bar对象  
app_bar_get_widget_vtable | 获取 app_bar 虚表。  
  
#### app_bar_cast 函数

* * *

  * 函数功能：



> 转换为app_bar对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* app_bar_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | app_bar对象。  
widget | widget_t* | app_bar对象。  
  
#### app_bar_create 函数

* * *

  * 函数功能：



> 创建app_bar对象

  * 函数原型：


    
    
    widget_t* app_bar_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### app_bar_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 app_bar 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* app_bar_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 app_bar 虚表。
