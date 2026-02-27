## widget_animator_event_t

### 概述

![image](images/widget_animator_event_t_0.png)

## 控件动画事件。

### 函数

函数名称 | 说明  
---|---  
widget_animator_event_cast | 把event对象转widget_animator_event_t对象。  
widget_animator_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
animator | void* | 控件动画句柄。  
widget | widget_t* | 控件对象。  
  
#### widget_animator_event_cast 函数

* * *

  * 函数功能：



> 把event对象转widget_animator_event_t对象。

  * 函数原型：


    
    
    widget_animator_event_t* widget_animator_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_event_t* | event对象。  
event | event_t* | event对象。  
  
#### widget_animator_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* widget_animator_event_init (widget_animator_event_t* event, uint32_t type, widget_t* widget, void* animator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | widget_animator_event_t* | event对象。  
type | uint32_t | 类型。  
widget | widget_t* | 控件对象。  
animator | void* | 控件动画句柄。  
  
#### animator 属性

* * *

> 控件动画句柄。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### widget 属性

* * *

> 控件对象。

  * 类型：widget_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
