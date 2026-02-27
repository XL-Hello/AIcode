## image_value_t

### 概述

![image](images/image_value_t_0.png)

图片值控件。

可以用图片来表示如电池电量、WIFI信号强度和其它各种数值的值。

其原理如下：

  * 1.把value以format为格式转换成字符串。
  * 2.把每个字符与image(图片文件名前缀)映射成一个图片名。
  * 3.最后把这些图片显示出来。



如果设置click_add_delta为非0，那么点击时自动增加指定的增量，值超过最大值时回到最小值, 或者值超过最小值时回到最大值。

image_value_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于image_value_t控件。

在xml中使用”image_value”标签创建图片值控件。如：
    
    
    <image_value  value="0" image="num_" />
    

> 更多用法请参考： [image_value](https://github.com/zlgopen/awtk/blob/master/design/default/ui/image_value.xml)

在c代码中使用函数image_value_create创建图片值控件。如：
    
    
    image_value = image_value_create(win, 10, 10, 200, 200);
    image_value_set_image(image_value, "num_");
    image_value_set_value(image_value, 100);
    

> 完整示例请参考： [image_value demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/image_value.c)

## 可用通过style来设置控件的显示风格，如背景颜色和边框等等，不过一般情况并不需要。

### 函数

函数名称 | 说明  
---|---  
image_value_cast | 转换为image_value对象(供脚本语言使用)。  
image_value_create | 创建image_value对象  
image_value_get_widget_vtable | 获取 image_value 虚表。  
image_value_set_click_add_delta | 设置点击时加上的增量。  
image_value_set_format | 设置格式。  
image_value_set_image | 设置图片前缀。  
image_value_set_max | 设置最大值。  
image_value_set_min | 设置最小值。  
image_value_set_value | 设置值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
click_add_delta | double | 点击时加上一个增量。  
format | char* | 数值到字符串转换时的格式，缺省为”%d”。  
image | char* | 图片名称的前缀。  
max | double | 最大值(如果设置了click_add_delta，到达最大值后回到最小值)。  
min | double | 最小值(如果设置了click_add_delta，到达最小值后回到最大值)。  
value | double | 值。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值即将改变事件(click_add_delta为非0时，点击触发)。  
EVT_VALUE_CHANGED | value_change_event_t | 值改变事件(click_add_delta为非0时，点击触发)。  
  
#### image_value_cast 函数

* * *

  * 函数功能：



> 转换为image_value对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* image_value_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | image_value对象。  
widget | widget_t* | image_value对象。  
  
#### image_value_create 函数

* * *

  * 函数功能：



> 创建image_value对象

  * 函数原型：


    
    
    widget_t* image_value_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### image_value_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 image_value 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* image_value_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 image_value 虚表。  
  
#### image_value_set_click_add_delta 函数

* * *

  * 函数功能：



> 设置点击时加上的增量。

  * 函数原型：


    
    
    ret_t image_value_set_click_add_delta (widget_t* widget, double click_add_delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_value对象。  
click_add_delta | double | 增量。  
  
#### image_value_set_format 函数

* * *

  * 函数功能：



> 设置格式。

  * 函数原型：


    
    
    ret_t image_value_set_format (widget_t* widget, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_value对象。  
format | const char* | 格式。  
  
#### image_value_set_image 函数

* * *

  * 函数功能：



> 设置图片前缀。

  * 函数原型：


    
    
    ret_t image_value_set_image (widget_t* widget, const char* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_value对象。  
image | const char* | 图片前缀。  
  
#### image_value_set_max 函数

* * *

  * 函数功能：



> 设置最大值。

  * 函数原型：


    
    
    ret_t image_value_set_max (widget_t* widget, double max);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_max对象。  
max | double | 最大值。  
  
#### image_value_set_min 函数

* * *

  * 函数功能：



> 设置最小值。

  * 函数原型：


    
    
    ret_t image_value_set_min (widget_t* widget, double min);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_min对象。  
min | double | 最小值。  
  
#### image_value_set_value 函数

* * *

  * 函数功能：



> 设置值。

  * 函数原型：


    
    
    ret_t image_value_set_value (widget_t* widget, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_value对象。  
value | double | 值。  
  
#### click_add_delta 属性

* * *

> 点击时加上一个增量。

  * 类型：double

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
  
#### format 属性

* * *

> 数值到字符串转换时的格式，缺省为”%d”。

  * 类型：char*

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
  
#### image 属性

* * *

> 图片名称的前缀。

  * 类型：char*

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
  
#### max 属性

* * *

> 最大值(如果设置了click_add_delta，到达最大值后回到最小值)。

  * 类型：double

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
  
#### min 属性

* * *

> 最小值(如果设置了click_add_delta，到达最小值后回到最大值)。

  * 类型：double

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
  
#### value 属性

* * *

> 值。

  * 类型：double

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
