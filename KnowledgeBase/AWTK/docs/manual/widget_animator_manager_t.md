## widget_animator_manager_t

### 概述

## 控件动画管理器。

### 函数

函数名称 | 说明  
---|---  
widget_animator_manager | 获取缺省的控件动画管理器。  
widget_animator_manager_add | 添加指定的动画，动画在创建时调用本函数。  
widget_animator_manager_count | 获取动画个数。  
widget_animator_manager_create | 创建控件动画管理器。  
widget_animator_manager_deinit | 析构控件动画管理器。  
widget_animator_manager_destroy | 析构并释放控件动画管理器。  
widget_animator_manager_find | 查找满足条件的动画。  
widget_animator_manager_init | 初始化控件动画管理器。  
widget_animator_manager_pause | 暂停满足条件的动画。  
widget_animator_manager_remove | 移出指定的动画，动画在销毁时调用本函数。。  
widget_animator_manager_remove_all | 销毁满足条件的动画。  
widget_animator_manager_set | 设置缺省的控件动画管理器。  
widget_animator_manager_set_time_scale | 设置时间倍率。  
widget_animator_manager_start | 播放满足条件的动画。  
widget_animator_manager_stop | 停止满足条件的动画。  
widget_animator_manager_time_elapse | 时间流失，调用本函数更新动画(public for test)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
time_scale | float_t | 时间倍率，可以让时间变快或变慢。  
  
#### widget_animator_manager 函数

* * *

  * 函数功能：



> 获取缺省的控件动画管理器。

  * 函数原型：


    
    
    widget_animator_manager_t* widget_animator_manager ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_manager_t* | 返回控件动画管理器。  
  
#### widget_animator_manager_add 函数

* * *

  * 函数功能：



> 添加指定的动画，动画在创建时调用本函数。

  * 函数原型：


    
    
    ret_t widget_animator_manager_add (widget_animator_manager_t* am, widget_animator_t* animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
animator | widget_animator_t* | 动画对象。  
  
#### widget_animator_manager_count 函数

* * *

  * 函数功能：



> 获取动画个数。

  * 函数原型：


    
    
    uint32_t widget_animator_manager_count (widget_animator_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回动画个数。  
am | widget_animator_manager_t* | 控件动画管理器。  
  
#### widget_animator_manager_create 函数

* * *

  * 函数功能：



> 创建控件动画管理器。

  * 函数原型：


    
    
    widget_animator_manager_t* widget_animator_manager_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_manager_t* | 返回控件动画管理器。  
  
#### widget_animator_manager_deinit 函数

* * *

  * 函数功能：



> 析构控件动画管理器。

  * 函数原型：


    
    
    ret_t widget_animator_manager_deinit (widget_animator_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
  
#### widget_animator_manager_destroy 函数

* * *

  * 函数功能：



> 析构并释放控件动画管理器。

  * 函数原型：


    
    
    ret_t widget_animator_manager_destroy (widget_animator_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
  
#### widget_animator_manager_find 函数

* * *

  * 函数功能：



> 查找满足条件的动画。

  * 函数原型：


    
    
    widget_animator_t* widget_animator_manager_find (widget_animator_manager_t* am, widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_t* | 成功返回动画对象，失败返回NULL。  
am | widget_animator_manager_t* | 控件动画管理器。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_animator_manager_init 函数

* * *

  * 函数功能：



> 初始化控件动画管理器。

  * 函数原型：


    
    
    widget_animator_manager_t* widget_animator_manager_init (widget_animator_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_manager_t* | 返回控件动画管理器。  
am | widget_animator_manager_t* | 控件动画管理器。  
  
#### widget_animator_manager_pause 函数

* * *

  * 函数功能：



> 暂停满足条件的动画。 1.widget为NULL时，暂停所有名称为name的动画。 2.name为NULL时，暂停所有widget相关的动画。 3.widget和name均为NULL，暂停所有动画。

  * 函数原型：


    
    
    ret_t widget_animator_manager_pause (widget_animator_manager_t* am, widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_animator_manager_remove 函数

* * *

  * 函数功能：



> 移出指定的动画，动画在销毁时调用本函数。。

  * 函数原型：


    
    
    ret_t widget_animator_manager_remove (widget_animator_manager_t* am, widget_animator_t* animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
animator | widget_animator_t* | 动画对象。  
  
#### widget_animator_manager_remove_all 函数

* * *

  * 函数功能：



> 销毁满足条件的动画。

  * 函数原型：


    
    
    ret_t widget_animator_manager_remove_all (widget_animator_manager_t* am, widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_animator_manager_set 函数

* * *

  * 函数功能：



> 设置缺省的控件动画管理器。

  * 函数原型：


    
    
    ret_t widget_animator_manager_set (widget_animator_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
  
#### widget_animator_manager_set_time_scale 函数

* * *

  * 函数功能：



> 设置时间倍率。 设置动画的时间倍率，<0: 时间倒退，<1: 时间变慢，>1 时间变快。

  * 函数原型：


    
    
    ret_t widget_animator_manager_set_time_scale (widget_animator_manager_t* am, widget_t* widget, const char* name, float_t time_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
time_scale | float_t | 时间倍率。  
  
#### widget_animator_manager_start 函数

* * *

  * 函数功能：



> 播放满足条件的动画。 1.widget为NULL时，播放所有名称为name的动画。 2.name为NULL时，播放所有widget相关的动画。 3.widget和name均为NULL，播放所有动画。

  * 函数原型：


    
    
    ret_t widget_animator_manager_start (widget_animator_manager_t* am, widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_animator_manager_stop 函数

* * *

  * 函数功能：



> 停止满足条件的动画。 1.widget为NULL时，停止所有名称为name的动画。 2.name为NULL时，停止所有widget相关的动画。 3.widget和name均为NULL，停止所有动画。

  * 函数原型：


    
    
    ret_t widget_animator_manager_stop (widget_animator_manager_t* am, widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_animator_manager_time_elapse 函数

* * *

  * 函数功能：



> 时间流失，调用本函数更新动画(public for test)。

  * 函数原型：


    
    
    ret_t widget_animator_manager_time_elapse (widget_animator_manager_t* am, uint32_t delta_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
am | widget_animator_manager_t* | 控件动画管理器。  
delta_time | uint32_t | 流失的时间(毫秒)。  
  
#### time_scale 属性

* * *

> 时间倍率，可以让时间变快或变慢。

  * 类型：float_t


