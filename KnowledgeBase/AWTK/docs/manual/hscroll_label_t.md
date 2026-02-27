## hscroll_label_t

### 概述

![image](images/hscroll_label_t_0.png)

可水平滚动的文本控件，方便实现长文本滚动。

hscroll_label_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于hscroll_label_t控件。

> 更多用法请参考：[hscroll_label.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/hscroll_label.xml)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <style name="default" text_color="black">
    <normal   />
    <focused  />
    </style>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml)

* * *

### 函数

函数名称 | 说明  
---|---  
hscroll_label_cast | 转换为hscroll_label对象(供脚本语言使用)。  
hscroll_label_create | 创建hscroll_label对象  
hscroll_label_get_widget_vtable | 获取 hscroll_label 虚表。  
hscroll_label_set_delay | 设置开始延迟时间。  
hscroll_label_set_duration | 设置duration。  
hscroll_label_set_ellipses | 设置ellipses。  
hscroll_label_set_loop | 设置loop。  
hscroll_label_set_loop_interval_distance | 设置滚动文本结尾和文本开头间隔距离  
hscroll_label_set_lull | 设置lull。  
hscroll_label_set_only_focus | 设置only_focus。  
hscroll_label_set_only_parent_focus | 设置only_parent_focus。  
hscroll_label_set_speed | 设置speed（设置后 duration 不生效）。  
hscroll_label_set_stop_at_begin | 设置stop_at_begin。  
hscroll_label_set_xoffset | 设置x偏移(一般无需用户调用)。。  
hscroll_label_set_yoyo | 设置yoyo。  
hscroll_label_start | 启动(一般无需用户调用)。  
hscroll_label_stop | 停止(一般无需用户调用)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
delay | uint32_t | 延迟多久才开始滚动，缺省0ms。  
duration | int32_t | 滚动一次需要的时间(毫秒)，缺省5000ms。  
ellipses | bool_t | 文本显示不下时，在行尾显示省略号(缺省FALSE)。  
loop | bool_t | loop是否循环滚动(缺省FALSE)。  
loop_interval_distance | int32_t | 滚动文本结尾和文本开头间隔距离(缺省值为 -1，小于 0 视为使用控件宽度作为间隔距离)。  
lull | int32_t | 滚动之间的间歇时间(毫秒)，缺省3000ms。  
only_focus | bool_t | 只有处于focus时才滚动(缺省否)。  
only_parent_focus | bool_t | 只有父控件处于focus时才滚动(缺省否)。  
speed | float_t | 滚动速度(px/ms)（设置后 duration 不生效）。  
stop_at_begin | bool_t | 滚动完毕后停在文本开头(缺省FALSE)。  
text_w | int32_t | 文本的宽度。  
xoffset | int32_t | 偏移量。  
yoyo | bool_t | 是否往返滚动(缺省FALSE)。  
  
#### hscroll_label_cast 函数

* * *

  * 函数功能：



> 转换为hscroll_label对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* hscroll_label_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | hscroll_label对象。  
widget | widget_t* | hscroll_label对象。  
  
#### hscroll_label_create 函数

* * *

  * 函数功能：



> 创建hscroll_label对象

  * 函数原型：


    
    
    widget_t* hscroll_label_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### hscroll_label_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 hscroll_label 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* hscroll_label_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 hscroll_label 虚表。  
  
#### hscroll_label_set_delay 函数

* * *

  * 函数功能：



> 设置开始延迟时间。

  * 函数原型：


    
    
    ret_t hscroll_label_set_delay (widget_t* widget, uint32_t delay);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
delay | uint32_t | 开始延迟时间。  
  
#### hscroll_label_set_duration 函数

* * *

  * 函数功能：



> 设置duration。

  * 函数原型：


    
    
    ret_t hscroll_label_set_duration (widget_t* widget, int32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
duration | int32_t | 滚动时间(毫秒)。  
  
#### hscroll_label_set_ellipses 函数

* * *

  * 函数功能：



> 设置ellipses。

  * 函数原型：


    
    
    ret_t hscroll_label_set_ellipses (widget_t* widget, bool_t ellipses);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
ellipses | bool_t | 是否在文本超长时在行尾显示”…”。  
  
#### hscroll_label_set_loop 函数

* * *

  * 函数功能：



> 设置loop。

  * 函数原型：


    
    
    ret_t hscroll_label_set_loop (widget_t* widget, bool_t loop);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
loop | bool_t | 是否循环滚动。  
  
#### hscroll_label_set_loop_interval_distance 函数

* * *

  * 函数功能：



> 设置滚动文本结尾和文本开头间隔距离

  * 函数原型：


    
    
    ret_t hscroll_label_set_loop_interval_distance (widget_t* widget, int32_t loop_interval_distance);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
loop_interval_distance | int32_t | 间隔距离。  
  
#### hscroll_label_set_lull 函数

* * *

  * 函数功能：



> 设置lull。

  * 函数原型：


    
    
    ret_t hscroll_label_set_lull (widget_t* widget, int32_t lull);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
lull | int32_t | 间歇时间(毫秒)。  
  
#### hscroll_label_set_only_focus 函数

* * *

  * 函数功能：



> 设置only_focus。

  * 函数原型：


    
    
    ret_t hscroll_label_set_only_focus (widget_t* widget, bool_t only_focus);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
only_focus | bool_t | 是否只有处于focus时才滚动。  
  
#### hscroll_label_set_only_parent_focus 函数

* * *

  * 函数功能：



> 设置only_parent_focus。

  * 函数原型：


    
    
    ret_t hscroll_label_set_only_parent_focus (widget_t* widget, bool_t only_parent_focus);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
only_parent_focus | bool_t | 是否只有处于focus时才滚动。  
  
#### hscroll_label_set_speed 函数

* * *

  * 函数功能：



> 设置speed（设置后 duration 不生效）。

  * 函数原型：


    
    
    ret_t hscroll_label_set_speed (widget_t* widget, float_t speed);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
speed | float_t | 滚动速度(px/ms)。  
  
#### hscroll_label_set_stop_at_begin 函数

* * *

  * 函数功能：



> 设置stop_at_begin。

  * 函数原型：


    
    
    ret_t hscroll_label_set_stop_at_begin (widget_t* widget, bool_t stop_at_begin);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
stop_at_begin | bool_t | 是否在滚动完毕后停在文本结尾。  
  
#### hscroll_label_set_xoffset 函数

* * *

  * 函数功能：



> 设置x偏移(一般无需用户调用)。。

  * 函数原型：


    
    
    ret_t hscroll_label_set_xoffset (widget_t* widget, int32_t xoffset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
xoffset | int32_t | x偏移。  
  
#### hscroll_label_set_yoyo 函数

* * *

  * 函数功能：



> 设置yoyo。

  * 函数原型：


    
    
    ret_t hscroll_label_set_yoyo (widget_t* widget, bool_t yoyo);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
yoyo | bool_t | 是否往返滚动。  
  
#### hscroll_label_start 函数

* * *

  * 函数功能：



> 启动(一般无需用户调用)。

  * 函数原型：


    
    
    ret_t hscroll_label_start (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### hscroll_label_stop 函数

* * *

  * 函数功能：



> 停止(一般无需用户调用)。

  * 函数原型：


    
    
    ret_t hscroll_label_stop (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### delay 属性

* * *

> 延迟多久才开始滚动，缺省0ms。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### duration 属性

* * *

> 滚动一次需要的时间(毫秒)，缺省5000ms。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### ellipses 属性

* * *

> 文本显示不下时，在行尾显示省略号(缺省FALSE)。

  * 类型：bool_t

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
  
#### loop 属性

* * *

> loop是否循环滚动(缺省FALSE)。

  * 类型：bool_t

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
  
#### loop_interval_distance 属性

* * *

> 滚动文本结尾和文本开头间隔距离(缺省值为 -1，小于 0 视为使用控件宽度作为间隔距离)。

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
  
#### lull 属性

* * *

> 滚动之间的间歇时间(毫秒)，缺省3000ms。

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
  
#### only_focus 属性

* * *

> 只有处于focus时才滚动(缺省否)。

  * 类型：bool_t

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
  
#### only_parent_focus 属性

* * *

> 只有父控件处于focus时才滚动(缺省否)。

  * 类型：bool_t

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
  
#### speed 属性

* * *

> 滚动速度(px/ms)（设置后 duration 不生效）。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### stop_at_begin 属性

* * *

> 滚动完毕后停在文本开头(缺省FALSE)。 注：yoyo 为 TRUE 时，该功能失效。

  * 类型：bool_t

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
  
#### text_w 属性

* * *

> 文本的宽度。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### xoffset 属性

* * *

> 偏移量。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### yoyo 属性

* * *

> 是否往返滚动(缺省FALSE)。

  * 类型：bool_t

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
