## touch_event_t

### 概述

![image](images/touch_event_t_0.png)

## 多点触摸事件(目前主要对接 SDL_TouchFingerEvent(SDL_FINGERMOTION/SDL_FINGERDOWN/SDL_FINGERUP))。

### 函数

函数名称 | 说明  
---|---  
touch_event_cast | 把event对象转touch_event_t对象。  
touch_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
finger_id | int64_t | 手指ID。  
pressure | float | 压力。  
touch_id | int64_t | 触摸ID。  
x | float | x坐标(在 0-1 之间，表示与屏幕宽度的比例）。  
y | float | y坐标(在 0-1 之间，表示与屏幕高度的比例）。  
  
#### touch_event_cast 函数

* * *

  * 函数功能：



> 把event对象转touch_event_t对象。

  * 函数原型：


    
    
    touch_event_t* touch_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | touch_event_t* | event 对象。  
event | event_t* | event对象。  
  
#### touch_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* touch_event_init (touch_event_t* event, uint32_t type, void* target, int64_t touch_id, int64_t finger_id, float x, float y, float pressure);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | touch_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
touch_id | int64_t | 触摸ID。  
finger_id | int64_t | 手指ID。  
x | float | x坐标。  
y | float | y坐标。  
pressure | float | 压力。  
  
#### finger_id 属性

* * *

> 手指ID。

  * 类型：int64_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### pressure 属性

* * *

> 压力。

  * 类型：float

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### touch_id 属性

* * *

> 触摸ID。

  * 类型：int64_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### x 属性

* * *

> x坐标(在 0-1 之间，表示与屏幕宽度的比例）。

  * 类型：float

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### y 属性

* * *

> y坐标(在 0-1 之间，表示与屏幕高度的比例）。

  * 类型：float

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
