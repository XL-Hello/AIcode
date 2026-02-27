## window_event_t

### 概述

![image](images/window_event_t_0.png)

## 窗口事件，由窗口管理器触发。

### 函数

函数名称 | 说明  
---|---  
pointer_event_rotate | 根据屏幕旋转方向修正pointer_event中的坐标。(旋转方向为逆时针)  
window_event_cast | 把event对象转window_event_t对象。  
window_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
window | widget_t* | canvas。  
  
#### pointer_event_rotate 函数

* * *

  * 函数功能：



> 根据屏幕旋转方向修正pointer_event中的坐标。(旋转方向为逆时针)

  * 函数原型：


    
    
    ret_t pointer_event_rotate (pointer_event_t* evt, system_info_t* info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
evt | pointer_event_t* | 指针事件对象。  
info | system_info_t* | 系统信息。  
  
#### window_event_cast 函数

* * *

  * 函数功能：



> 把event对象转window_event_t对象。

  * 函数原型：


    
    
    window_event_t* window_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | window_event_t* | 对象。  
event | event_t* | event对象。  
  
#### window_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* window_event_init (window_event_t* event, uint32_t type, void* target, widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | window_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
widget | widget_t* | window对象。  
  
#### window 属性

* * *

> canvas。

  * 类型：widget_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
