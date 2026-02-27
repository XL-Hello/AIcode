## system_bar_t

### 概述

![image](images/system_bar_t_0.png)

system_bar窗口。

system_bar窗口是一种特殊的窗口，独占LCD顶部区域，用来显示当前窗口的标题和关闭按钮等内容。

> system_bar窗口需要在打开第一个应用程序窗口之前打开。

system_bar对两个子控件会做特殊处理：

  * 1.名为”title”的label控件，自动显示当前主窗口的name或text。
  * 2.名为”close”的button控件，点击之后向当前主窗口发送EVT_REQUEST_CLOSE_WINDOW消息。



system_bar_t是[window_base_t](window_base_t.html)的子类控件， window_base_t的函数均适用于system_bar_t控件。

在xml中使用”system_bar”标签创建system_bar窗口。如：
    
    
    <system_bar h="30">
    <column x="0" y="0" w="-40" h="100%">
    <label style="title" x="10" y="m" w="55%" h="100%" name="title"/>
    <digit_clock style="time" x="r" y="m" w="40%" h="100%" format="hh:mm"/>
    </column>
    <button style="close" x="r:5" y="m" w="26" h="26" name="close" text="x"/>
    </system_bar>
    

> 更多用法请参考： [system_bar](https://github.com/zlgopen/awtk/blob/master/design/default/ui/system_bar.xml)

在c代码中使用函数system_bar_create创建system_bar窗口。如：
    
    
    widget_t* win = system_bar_create(NULL, 0, 0, 320, 30);
    

> 创建之后，和使用普通窗口是一样的。

可用通过style来设置控件的显示风格，如背景颜色等等。如：
    
    
    <system_bar>
    <style name="default">
    <normal bg_color="#a0a0a0"/>
    </style>
    </system_bar>
    

> 更多用法请参考： [system_bar.xml](https://github.com/zlgopen/awtk/blob/master/design/default/styles/system_bar.xml)

* * *

### 函数

函数名称 | 说明  
---|---  
system_bar_cast | 转换为system_bar对象(供脚本语言使用)。  
system_bar_create | 创建system_bar对象。  
system_bar_get_widget_vtable | 获取 system_bar 虚表。  
  
#### system_bar_cast 函数

* * *

  * 函数功能：



> 转换为system_bar对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* system_bar_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | system_bar对象。  
widget | widget_t* | system_bar对象。  
  
#### system_bar_create 函数

* * *

  * 函数功能：



> 创建system_bar对象。

  * 函数原型：


    
    
    widget_t* system_bar_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | system_bar对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### system_bar_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 system_bar 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* system_bar_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 system_bar 虚表。
