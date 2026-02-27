## widget_animator_t

### 概述

## 控件动画接口。

### 函数

函数名称 | 说明  
---|---  
widget_animator_destroy | 销毁animator对象。  
widget_animator_init | 初始化。仅供子类内部使用。  
widget_animator_off | 注销指定事件的处理函数。  
widget_animator_on | 注册指定事件的处理函数。  
widget_animator_pause | 暂停动画。  
widget_animator_set_destroy_when_done | 设置完成时是否自动销毁动画对象(缺省销毁)。  
widget_animator_set_name | 设置名称。  
widget_animator_set_relayout | 设置每帧是否重新布局。  
widget_animator_set_repeat | 设置为重复模式。  
widget_animator_set_reversed | 设置为逆向模式。  
widget_animator_set_time_scale | 设置时间倍率，用于实现时间加速减速和停滞的功能。  
widget_animator_set_yoyo | 设置为yoyo模式。  
widget_animator_start | 启动动画。  
widget_animator_stop | 停止动画。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
name | char* | 名称。  
  
#### widget_animator_destroy 函数

* * *

  * 函数功能：



> 销毁animator对象。

  * 函数原型：


    
    
    ret_t widget_animator_destroy (widget_animator_t* animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
  
#### widget_animator_init 函数

* * *

  * 函数功能：



> 初始化。仅供子类内部使用。

  * 函数原型：


    
    
    ret_t widget_animator_init (widget_animator_t* animator, widget_t* widget, uint32_t duration, uint32_t delay, easing_func_t easing);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
widget | widget_t* | 控件对象。  
duration | uint32_t | 动画持续时间(毫秒)。  
delay | uint32_t | 动画执行时间(毫秒)。  
easing | easing_func_t | 插值函数。  
  
#### widget_animator_off 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t widget_animator_off (widget_animator_t* animator, uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
id | uint32_t | widget_animator_on返回的ID。  
  
#### widget_animator_on 函数

* * *

  * 函数功能：



> 注册指定事件的处理函数。

  * 函数原型：


    
    
    uint32_t widget_animator_on (widget_animator_t* animator, event_type_t type, event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于widget_animator_off。  
animator | widget_animator_t* | 动画对象。  
type | event_type_t | 事件类型。目前支持：EVT_ANIM_START,EVT_ANIM_STOP,EVT_ANIM_PAUSE,EVT_ANIM_ONCE和EVT_ANIM_END。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### widget_animator_pause 函数

* * *

  * 函数功能：



> 暂停动画。

  * 函数原型：


    
    
    ret_t widget_animator_pause (widget_animator_t* animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
  
#### widget_animator_set_destroy_when_done 函数

* * *

  * 函数功能：



> 设置完成时是否自动销毁动画对象(缺省销毁)。

  * 函数原型：


    
    
    ret_t widget_animator_set_destroy_when_done (widget_animator_t* animator, bool_t destroy_when_done);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
destroy_when_done | bool_t | 完成时是否自动销毁动画对象。  
  
#### widget_animator_set_name 函数

* * *

  * 函数功能：



> 设置名称。

  * 函数原型：


    
    
    ret_t widget_animator_set_name (widget_animator_t* animator, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
name | const char* | 名称。  
  
#### widget_animator_set_relayout 函数

* * *

  * 函数功能：



> 设置每帧是否重新布局。

  * 函数原型：


    
    
    ret_t widget_animator_set_relayout (widget_animator_t* animator, bool_t relayout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
relayout | bool_t | 是否重新布局。  
  
#### widget_animator_set_repeat 函数

* * *

  * 函数功能：



> 设置为重复模式。

  * 函数原型：


    
    
    ret_t widget_animator_set_repeat (widget_animator_t* animator, uint32_t repeat_times);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
repeat_times | uint32_t | 重复的次数。  
  
#### widget_animator_set_reversed 函数

* * *

  * 函数功能：



> 设置为逆向模式。

  * 函数原型：


    
    
    ret_t widget_animator_set_reversed (widget_animator_t* animator, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
value | bool_t | 是否为逆向模式。  
  
#### widget_animator_set_time_scale 函数

* * *

  * 函数功能：



> 设置时间倍率，用于实现时间加速减速和停滞的功能。

  * 函数原型：


    
    
    ret_t widget_animator_set_time_scale (widget_animator_t* animator, float_t time_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
time_scale | float_t | 时间倍率。  
  
#### widget_animator_set_yoyo 函数

* * *

  * 函数功能：



> 设置为yoyo模式。

  * 函数原型：


    
    
    ret_t widget_animator_set_yoyo (widget_animator_t* animator, uint32_t yoyo_times);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
yoyo_times | uint32_t | yoyo的次数，往返视为两次。  
  
#### widget_animator_start 函数

* * *

  * 函数功能：



> 启动动画。

  * 函数原型：


    
    
    ret_t widget_animator_start (widget_animator_t* animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
  
#### widget_animator_stop 函数

* * *

  * 函数功能：



> 停止动画。

  * 函数原型：


    
    
    ret_t widget_animator_stop (widget_animator_t* animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象。  
  
#### name 属性

* * *

> 名称。

  * 类型：char*


