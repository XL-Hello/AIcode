## time_clock_t

### 概述

![image](images/time_clock_t_0.png)

模拟时钟控件。

time_clock_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于time_clock_t控件。

在xml中使用”time_clock”标签创建模拟时钟控件。如：
    
    
    <time_clock x="c" y="m" w="300" h="300" bg_image="clock_bg" image="clock"
    hour_image="clock_hour" minute_image="clock_minute" second_image="clock_second"/>
    

> 更多用法请参考：[time_clock.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/time_clock.xml)

在c代码中使用函数time_clock_create创建模拟时钟控件。如：
    
    
    widget_t* tc = time_clock_create(win, 10, 10, 240, 240);
    time_clock_set_image(tc, "clock");
    time_clock_set_bg_image(tc, "clock_bg");
    time_clock_set_hour_image(tc, "clock_hour");
    time_clock_set_minute_image(tc, "clock_minute");
    time_clock_set_second_image(tc, "clock_second");
    

> 完整示例请参考：[time_clock demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/time_clock.c)

## time_clock一般不需要设置style。

### 函数

函数名称 | 说明  
---|---  
time_clock_cast | 转换为time_clock对象(供脚本语言使用)。  
time_clock_create | 创建time_clock对象  
time_clock_get_widget_vtable | 获取 time_clock 虚表。  
time_clock_set_bg_image | 设置背景图片。  
time_clock_set_hour | 设置小时的值。  
time_clock_set_hour_anchor | 设置小时指针的旋转锚点。  
time_clock_set_hour_image | 设置小时的图片。  
time_clock_set_image | 设置中心图片。  
time_clock_set_minute | 设置分钟的值。  
time_clock_set_minute_anchor | 设置分钟指针的旋转锚点。  
time_clock_set_minute_image | 设置分钟的图片。  
time_clock_set_second | 设置秒的值。  
time_clock_set_second_anchor | 设置秒钟指针的旋转锚点。  
time_clock_set_second_image | 设置秒的图片。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
bg_image | char* | 背景图片。  
hour | int32_t | 小时。  
hour_anchor_x | char* | 时针图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
hour_anchor_y | char* | 时针图片旋转锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
hour_image | char* | 时针图片。  
image | char* | 中心图片。  
minute | int32_t | 分钟。  
minute_anchor_x | char* | 分针图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
minute_anchor_y | char* | 分针图片旋转锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
minute_image | char* | 分针图片。  
second | int32_t | 秒。  
second_anchor_x | char* | 秒针图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
second_anchor_y | char* | 秒针图片旋转锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)  
second_image | char* | 秒针图片。  
  
#### time_clock_cast 函数

* * *

  * 函数功能：



> 转换为time_clock对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* time_clock_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | time_clock对象。  
widget | widget_t* | time_clock对象。  
  
#### time_clock_create 函数

* * *

  * 函数功能：



> 创建time_clock对象

  * 函数原型：


    
    
    widget_t* time_clock_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### time_clock_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 time_clock 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* time_clock_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 time_clock 虚表。  
  
#### time_clock_set_bg_image 函数

* * *

  * 函数功能：



> 设置背景图片。

  * 函数原型：


    
    
    ret_t time_clock_set_bg_image (widget_t* widget, const char* bg_image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
bg_image | const char* | 背景图片。  
  
#### time_clock_set_hour 函数

* * *

  * 函数功能：



> 设置小时的值。

  * 函数原型：


    
    
    ret_t time_clock_set_hour (widget_t* widget, int32_t hour);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
hour | int32_t | 小时的值。  
  
#### time_clock_set_hour_anchor 函数

* * *

  * 函数功能：



> 设置小时指针的旋转锚点。 后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f

  * 函数原型：


    
    
    ret_t time_clock_set_hour_anchor (widget_t* widget, const char* anchor_x, const char* anchor_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
anchor_x | const char* | 指针的锚点坐标x。  
anchor_y | const char* | 指针的锚点坐标y。  
  
#### time_clock_set_hour_image 函数

* * *

  * 函数功能：



> 设置小时的图片。

  * 函数原型：


    
    
    ret_t time_clock_set_hour_image (widget_t* widget, const char* hour);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
hour | const char* | 小时的图片。  
  
#### time_clock_set_image 函数

* * *

  * 函数功能：



> 设置中心图片。

  * 函数原型：


    
    
    ret_t time_clock_set_image (widget_t* widget, const char* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
image | const char* | 图片。  
  
#### time_clock_set_minute 函数

* * *

  * 函数功能：



> 设置分钟的值。

  * 函数原型：


    
    
    ret_t time_clock_set_minute (widget_t* widget, int32_t minute);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
minute | int32_t | 分钟的值。  
  
#### time_clock_set_minute_anchor 函数

* * *

  * 函数功能：



> 设置分钟指针的旋转锚点。 后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f

  * 函数原型：


    
    
    ret_t time_clock_set_minute_anchor (widget_t* widget, const char* anchor_x, const char* anchor_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
anchor_x | const char* | 指针的锚点坐标x。  
anchor_y | const char* | 指针的锚点坐标y。  
  
#### time_clock_set_minute_image 函数

* * *

  * 函数功能：



> 设置分钟的图片。

  * 函数原型：


    
    
    ret_t time_clock_set_minute_image (widget_t* widget, const char* minute_image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
minute_image | const char* | 分钟的图片。  
  
#### time_clock_set_second 函数

* * *

  * 函数功能：



> 设置秒的值。

  * 函数原型：


    
    
    ret_t time_clock_set_second (widget_t* widget, int32_t second);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
second | int32_t | 秒的值。  
  
#### time_clock_set_second_anchor 函数

* * *

  * 函数功能：



> 设置秒钟指针的旋转锚点。 后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f

  * 函数原型：


    
    
    ret_t time_clock_set_second_anchor (widget_t* widget, const char* anchor_x, const char* anchor_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
anchor_x | const char* | 指针的锚点坐标x。  
anchor_y | const char* | 指针的锚点坐标y。  
  
#### time_clock_set_second_image 函数

* * *

  * 函数功能：



> 设置秒的图片。

  * 函数原型：


    
    
    ret_t time_clock_set_second_image (widget_t* widget, const char* second_image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
second_image | const char* | 秒的图片。  
  
#### bg_image 属性

* * *

> 背景图片。

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
  
#### hour 属性

* * *

> 小时。

  * 类型：int32_t

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
  
#### hour_anchor_x 属性

* * *

> 时针图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### hour_anchor_y 属性

* * *

> 时针图片旋转锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### hour_image 属性

* * *

> 时针图片。

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

> 中心图片。

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
  
#### minute 属性

* * *

> 分钟。

  * 类型：int32_t

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
  
#### minute_anchor_x 属性

* * *

> 分针图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### minute_anchor_y 属性

* * *

> 分针图片旋转锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### minute_image 属性

* * *

> 分针图片。

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
  
#### second 属性

* * *

> 秒。

  * 类型：int32_t

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
  
#### second_anchor_x 属性

* * *

> 秒针图片旋转锚点x坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### second_anchor_y 属性

* * *

> 秒针图片旋转锚点y坐标。(后面加上px为像素点，不加px为相对百分比坐标0.0f到1.0f)

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
  
#### second_image 属性

* * *

> 秒针图片。

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
