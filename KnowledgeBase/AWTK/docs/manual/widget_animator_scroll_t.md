## widget_animator_scroll_t

### 概述

滚动控件的动画。 本动画也可以用widget_animator_prop2实现，但滚动控件需要访问内部数据结构，出于可读性考虑保留独立实现。

* * *

### 函数

函数名称 | 说明  
---|---  
widget_animator_scroll_create | 创建动画对象。  
widget_animator_scroll_set_params | 设置动画对象的参数。  
  
#### widget_animator_scroll_create 函数

* * *

  * 函数功能：



> 创建动画对象。

  * 函数原型：


    
    
    widget_animator_t* widget_animator_scroll_create (widget_t* widget, uint32_t duration, uint32_t delay, easing_type_t easing);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_t* | 成功返回动画对象，失败返回NULL。  
widget | widget_t* | 控件对象。  
duration | uint32_t | 动画持续时间(毫秒)。  
delay | uint32_t | 动画执行时间(毫秒)。  
easing | easing_type_t | 插值函数类型。  
  
#### widget_animator_scroll_set_params 函数

* * *

  * 函数功能：



> 设置动画对象的参数。

  * 函数原型：


    
    
    ret_t widget_animator_scroll_set_params (widget_animator_t* animator, xy_t x_from, xy_t y_from, xy_t x_to, xy_t y_to);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象本身。  
x_from | xy_t | x起点值。  
y_from | xy_t | y起点值。  
x_to | xy_t | x终点值。  
y_to | xy_t | y终点值。
