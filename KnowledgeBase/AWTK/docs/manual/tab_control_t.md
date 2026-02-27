## tab_control_t

### 概述

![image](images/tab_control_t_0.png)

标签控件。

它本身不提供布局功能，仅提供具有语义的标签，让xml更具有可读性。

标签控件通常会包含一个pages控件和一个tab_button_group控件。

![image](images/tab_control_t_1.png)

tab_control_t是[widget_t](widget_t.html)的子类控件， widget_t的函数均适用于tab_control_t控件。

在xml中使用”tab_control”标签创建标签控件。如：
    
    
    <tab_control x="0" y="0" w="100%" h="100%" >
    <pages x="c" y="20" w="90%" h="-60" value="1">
    ...
    </pages>
    <tab_button_group>
    ...
    </tab_button_group>
    </tab_control>
    

> 更多用法请参考： [tab control](https://github.com/zlgopen/awtk/blob/master/design/default/ui/)

* * *

### 函数

函数名称 | 说明  
---|---  
tab_control_cast | 转换tab_control对象(供脚本语言使用)。  
tab_control_create | 创建tab_control对象  
tab_control_get_widget_vtable | 获取 tab_control 虚表。  
  
#### tab_control_cast 函数

* * *

  * 函数功能：



> 转换tab_control对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* tab_control_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | tab_control对象。  
widget | widget_t* | tab_control对象。  
  
#### tab_control_create 函数

* * *

  * 函数功能：



> 创建tab_control对象

  * 函数原型：


    
    
    widget_t* tab_control_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### tab_control_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 tab_control 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* tab_control_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 tab_control 虚表。
