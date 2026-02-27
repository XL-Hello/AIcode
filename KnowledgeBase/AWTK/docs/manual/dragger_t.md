## dragger_t

### 概述

![image](images/dragger_t_0.png)

dragger控件。

## 目前主要用于scrollbar里的滑块。

### 函数

函数名称 | 说明  
---|---  
dragger_cast | 转换为dragger对象(供脚本语言使用)。  
dragger_create | 创建dragger对象。  
dragger_get_widget_vtable | 获取 dragger 虚表。  
dragger_set_range | 设置拖动的范围。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
x_max | xy_t | x坐标的最大值。  
x_min | xy_t | x坐标的最小值。  
y_max | xy_t | y坐标的最大值。  
y_min | xy_t | y坐标的最小值。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_DRAG_START | event_t | 开始拖动事件。  
EVT_DRAG | event_t | 拖动事件。  
EVT_DRAG_END | event_t | 结束拖动事件。  
  
#### dragger_cast 函数

* * *

  * 函数功能：



> 转换为dragger对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* dragger_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | dragger对象。  
widget | widget_t* | dragger对象。  
  
#### dragger_create 函数

* * *

  * 函数功能：



> 创建dragger对象。

  * 函数原型：


    
    
    widget_t* dragger_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### dragger_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 dragger 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* dragger_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 dragger 虚表。  
  
#### dragger_set_range 函数

* * *

  * 函数功能：



> 设置拖动的范围。

  * 函数原型：


    
    
    ret_t dragger_set_range (widget_t* widget, xy_t x_min, xy_t y_min, xy_t x_max, xy_t y_max);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | dragger控件。  
x_min | xy_t | x坐标最小值。  
y_min | xy_t | y坐标最小值。  
x_max | xy_t | x坐标最大值。  
y_max | xy_t | y坐标最大值。  
  
#### x_max 属性

* * *

> x坐标的最大值。

  * 类型：xy_t

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
  
#### x_min 属性

* * *

> x坐标的最小值。

  * 类型：xy_t

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
  
#### y_max 属性

* * *

> y坐标的最大值。

  * 类型：xy_t

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
  
#### y_min 属性

* * *

> y坐标的最小值。

  * 类型：xy_t

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
