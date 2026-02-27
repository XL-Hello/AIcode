## timer_widget_t

### 概述

![image](images/timer_widget_t_0.png)

定时器。

> 主要目的是方便以拖拽的方式创建定时器，并用AWBlock编写简单的事件处理程序。 在xml中使用”timer”标签创建控件。如：
    
    
    <!-- ui -->
    <timer x="c" y="50" w="100" h="100" duration="1000"/>
    

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：

> 本控件默认不可见，无需指定style。
    
    
    <!-- style -->
    <timer>
    <style name="default" font_size="32">
    <normal text_color="black" />
    </style>
    </timer>
    

* * *

### 函数

函数名称 | 说明  
---|---  
timer_widget_cast | 转换为timer_widget对象(供脚本语言使用)。  
timer_widget_create | 创建timer_widget对象  
timer_widget_get_widget_vtable | 获取 timer_widget 虚表。  
timer_widget_set_duration | 设置 时长(毫秒)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
duration | uint32_t | 时长(毫秒)。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_TIMER | event_t | 定时器事件。  
  
#### timer_widget_cast 函数

* * *

  * 函数功能：



> 转换为timer_widget对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* timer_widget_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | timer_widget对象。  
widget | widget_t* | timer_widget对象。  
  
#### timer_widget_create 函数

* * *

  * 函数功能：



> 创建timer_widget对象

  * 函数原型：


    
    
    widget_t* timer_widget_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | timer_widget对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### timer_widget_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 timer_widget 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* timer_widget_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 timer_widget 虚表。  
  
#### timer_widget_set_duration 函数

* * *

  * 函数功能：



> 设置 时长(毫秒)。

  * 函数原型：


    
    
    ret_t timer_widget_set_duration (widget_t* widget, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
duration | uint32_t | 时长(毫秒)。  
  
#### duration 属性

* * *

> 时长(毫秒)。

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
