## wheel_event_t

### 概述

![image](images/wheel_event_t_0.png)

## 滚轮事件。

### 函数

函数名称 | 说明  
---|---  
wheel_event_cast | 把event对象转wheel_event_t对象。  
wheel_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
alt | bool_t | alt键是否按下。  
ctrl | bool_t | ctrl键是否按下。  
dy | int32_t | 滚轮的y值。  
shift | bool_t | shift键是否按下。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### wheel_event_cast 函数

* * *

  * 函数功能：



> 把event对象转wheel_event_t对象。

  * 函数原型：


    
    
    wheel_event_t* wheel_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wheel_event_t* | event对象。  
event | event_t* | event对象。  
  
#### wheel_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* wheel_event_init (wheel_event_t* event, uint32_t type, void* target, int32_t dy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | wheel_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
dy | int32_t | 滚轮的y值。  
  
#### alt 属性

* * *

> alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### ctrl 属性

* * *

> ctrl键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### dy 属性

* * *

> 滚轮的y值。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### shift 属性

* * *

> shift键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### x 属性

* * *

> x坐标。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### y 属性

* * *

> y坐标。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
