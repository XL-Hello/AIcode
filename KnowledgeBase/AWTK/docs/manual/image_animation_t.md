## image_animation_t

### 概述

![image](images/image_animation_t_0.png)

图片动画控件，指定一个图片前缀，依次显示指定序列的图片，从而形成动画效果。

图片序列可以用sequence指定，也可以用start_index和end_index指定一个范围。

image_animation_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于image_animation_t控件。

在xml中使用”image_animation”标签创建图片动画控件。如：
    
    
    <image_animation image="ani" start_index="1" end_index="9" auto_play="true" interval="50"
    delay="100"/>
    

> 更多用法请参考： [image_animation.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/image_animation.xml)

在c代码中使用函数image_animation_create创建图片动画控件。如：
    
    
    image_animation = image_animation_create(win, 10, 10, 200, 200);
    image_animation_set_image(image_animation, "ani");
    image_animation_set_interval(image_animation, 50);
    image_animation_set_range_sequence(image_animation, 1, 9);
    image_animation_play(image_animation);
    

> 完整示例请参考： [image_animation demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/image_animation.c)

## 可用通过style来设置控件的显示风格，如背景颜色和边框等等，不过一般情况并不需要。

### 函数

函数名称 | 说明  
---|---  
image_animation_cast | 转换为image_animation对象(供脚本语言使用)。  
image_animation_create | 创建image_animation对象  
image_animation_get_widget_vtable | 获取 image_animation 虚表。  
image_animation_is_playing | 判断是否在播放。  
image_animation_next | 手动切换到下一张图片。  
image_animation_pause | 暂停。  
image_animation_play | 播放。  
image_animation_set_auto_play | 设置是否自动播放。  
image_animation_set_delay | 设置延迟播放时间(仅适用于自动播放)。  
image_animation_set_format | 设置生成图片名的格式。  
image_animation_set_image | 设置图片前缀。  
image_animation_set_interval | 设置播放间隔时间(毫秒)。  
image_animation_set_loop | 设置是否循环播放。  
image_animation_set_range_sequence | 设置播放序列。比如image为”fire”，start_index为0, end_index为99, 将依次播放”fire0”, …,  
image_animation_set_reverse | 设置是否倒序播放。  
image_animation_set_sequence | 设置播放序列。比如image为”fire”，sequence为”12223”, 将依次播放”fire1”, “fire2”, “fire2”, “fire2”,  
image_animation_set_show_when_done | 设置结束播放后是否保持显示最后一帧。  
image_animation_set_unload_after_paint | 设置绘制完成后unload图片，以释放内存空间。  
image_animation_stop | 停止(并重置index为-1)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
auto_play | bool_t | 是否自动播放。  
delay | uint32_t | 自动播放时延迟播放的时间(毫秒)。  
end_index | uint32_t | 图片结束序数。  
format | char* | 索引到图片名转换时的格式，缺省为”%s%d”。  
image | char* | 图片名称的前缀。  
interval | uint32_t | 每张图片播放的时间(毫秒)。  
loop | bool_t | 是否循环播放。  
reverse | bool_t | 是否倒序播放。  
sequence | char* | 播放的序列，字符可选值为数字和英文大小写字母，字符可以重复。如：0123456789或者123123abcd。  
show_when_done | bool_t | 结束后是否继续显示最后一帧。  
start_index | uint32_t | 图片起始序数。  
unload_after_paint | bool_t | 绘制完成后unload图片，以释放内存空间。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_ANIM_ONCE | event_t | 使能循环播放时，控件动画完成一次事件。  
EVT_ANIM_END | event_t | 控件动画完成事件。  
  
#### image_animation_cast 函数

* * *

  * 函数功能：



> 转换为image_animation对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* image_animation_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | image_animation对象。  
widget | widget_t* | image_animation对象。  
  
#### image_animation_create 函数

* * *

  * 函数功能：



> 创建image_animation对象

  * 函数原型：


    
    
    widget_t* image_animation_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### image_animation_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 image_animation 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* image_animation_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 image_animation 虚表。  
  
#### image_animation_is_playing 函数

* * *

  * 函数功能：



> 判断是否在播放。

  * 函数原型：


    
    
    bool_t image_animation_is_playing (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示否。  
widget | widget_t* | image_animation对象。  
  
#### image_animation_next 函数

* * *

  * 函数功能：



> 手动切换到下一张图片。

  * 函数原型：


    
    
    ret_t image_animation_next (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
  
#### image_animation_pause 函数

* * *

  * 函数功能：



> 暂停。

  * 函数原型：


    
    
    ret_t image_animation_pause (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
  
#### image_animation_play 函数

* * *

  * 函数功能：



> 播放。

  * 函数原型：


    
    
    ret_t image_animation_play (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
  
#### image_animation_set_auto_play 函数

* * *

  * 函数功能：



> 设置是否自动播放。

  * 函数原型：


    
    
    ret_t image_animation_set_auto_play (widget_t* widget, bool_t auto_play);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
auto_play | bool_t | 是否自动播放。  
  
#### image_animation_set_delay 函数

* * *

  * 函数功能：



> 设置延迟播放时间(仅适用于自动播放)。

  * 函数原型：


    
    
    ret_t image_animation_set_delay (widget_t* widget, uint32_t delay);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
delay | uint32_t | 延迟播放时间(毫秒)。  
  
#### image_animation_set_format 函数

* * *

  * 函数功能：



> 设置生成图片名的格式。

XXX:生成图片名时，第一个参数是图片名前缀，第二个是序数，只能在此前提下设置格式。
    
    
    const char* format = image_animation->format ? image_animation->format : "%s%d";
    tk_snprintf(name, TK_NAME_LEN, format, image_animation->image, image_animation->index);
    

  * 函数原型：


    
    
    ret_t image_animation_set_format (widget_t* widget, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
format | const char* | 格式。  
  
#### image_animation_set_image 函数

* * *

  * 函数功能：



> 设置图片前缀。

  * 函数原型：


    
    
    ret_t image_animation_set_image (widget_t* widget, const char* image);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
image | const char* | 图片前缀。  
  
#### image_animation_set_interval 函数

* * *

  * 函数功能：



> 设置播放间隔时间(毫秒)。

  * 函数原型：


    
    
    ret_t image_animation_set_interval (widget_t* widget, uint32_t interval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
interval | uint32_t | 间隔时间(毫秒)。  
  
#### image_animation_set_loop 函数

* * *

  * 函数功能：



> 设置是否循环播放。

  * 函数原型：


    
    
    ret_t image_animation_set_loop (widget_t* widget, bool_t loop);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
loop | bool_t | 是否循环播放。  
  
#### image_animation_set_range_sequence 函数

* * *

  * 函数功能：



> 设置播放序列。比如image为”fire”，start_index为0, end_index为99, 将依次播放”fire0”, …, “fire99”。

若指定的图片不存在，则重复上一张图片。

  * 函数原型：


    
    
    ret_t image_animation_set_range_sequence (widget_t* widget, uint32_t start_index, uint32_t end_index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
start_index | uint32_t | 图片起始序数。  
end_index | uint32_t | 图片结束序数。  
  
#### image_animation_set_reverse 函数

* * *

  * 函数功能：



> 设置是否倒序播放。

  * 函数原型：


    
    
    ret_t image_animation_set_reverse (widget_t* widget, bool_t reverse);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
reverse | bool_t | 是否倒序播放。  
  
#### image_animation_set_sequence 函数

* * *

  * 函数功能：



> 设置播放序列。比如image为”fire”，sequence为”12223”, 将依次播放”fire1”, “fire2”, “fire2”, “fire2”, “fire3”。

  * 函数原型：


    
    
    ret_t image_animation_set_sequence (widget_t* widget, const char* sequence);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
sequence | const char* | 播放序列。  
  
#### image_animation_set_show_when_done 函数

* * *

  * 函数功能：



> 设置结束播放后是否保持显示最后一帧。

  * 函数原型：


    
    
    ret_t image_animation_set_show_when_done (widget_t* widget, bool_t show_when_done);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
show_when_done | bool_t | 是否继续显示最后一帧。  
  
#### image_animation_set_unload_after_paint 函数

* * *

  * 函数功能：



> 设置绘制完成后unload图片，以释放内存空间。

  * 函数原型：


    
    
    ret_t image_animation_set_unload_after_paint (widget_t* widget, bool_t unload_after_paint);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
unload_after_paint | bool_t | 是否绘制完成后unload图片。  
  
#### image_animation_stop 函数

* * *

  * 函数功能：



> 停止(并重置index为-1)。

  * 函数原型：


    
    
    ret_t image_animation_stop (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image_animation对象。  
  
#### auto_play 属性

* * *

> 是否自动播放。

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
  
#### delay 属性

* * *

> 自动播放时延迟播放的时间(毫秒)。

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
  
#### end_index 属性

* * *

> 图片结束序数。

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
  
#### format 属性

* * *

> 索引到图片名转换时的格式，缺省为”%s%d”。

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
  
#### interval 属性

* * *

> 每张图片播放的时间(毫秒)。

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
  
#### loop 属性

* * *

> 是否循环播放。

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
  
#### reverse 属性

* * *

> 是否倒序播放。

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
  
#### sequence 属性

* * *

> 播放的序列，字符可选值为数字和英文大小写字母，字符可以重复。如：0123456789或者123123abcd。

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
  
#### show_when_done 属性

* * *

> 结束后是否继续显示最后一帧。

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
  
#### start_index 属性

* * *

> 图片起始序数。

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
  
#### unload_after_paint 属性

* * *

> 绘制完成后unload图片，以释放内存空间。

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
