## pointer_event_t

### 概述

![image](images/pointer_event_t_0.png)

## 指针事件。

### 函数

函数名称 | 说明  
---|---  
pointer_event_cast | 把event对象转pointer_event_t对象。  
pointer_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
alt | bool_t | alt键是否按下。  
button | xy_t | button。  
cmd | bool_t | cmd键是否按下。  
ctrl | bool_t | ctrl键是否按下。  
finger_id | int32_t | 触摸ID。  
menu | bool_t | menu键是否按下。  
pressed | bool_t | 指针是否按下。  
shift | bool_t | shift键是否按下。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### pointer_event_cast 函数

* * *

  * 函数功能：



> 把event对象转pointer_event_t对象。

  * 函数原型：


    
    
    pointer_event_t* pointer_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | pointer_event_t* | event对象。  
event | event_t* | event对象。  
  
#### pointer_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* pointer_event_init (pointer_event_t* event, uint32_t type, void* target, int32_t x, int32_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | pointer_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
x | int32_t | x的值。  
y | int32_t | y的值。  
  
#### alt 属性

* * *

> alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### button 属性

* * *

> button。 在不同的平台，该属性会发生变化， PC ：左键为 1，中键为 2，右键为 3 嵌入式：默认为 1

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### cmd 属性

* * *

> cmd键是否按下。

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
  
#### finger_id 属性

* * *

> 触摸ID。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### menu 属性

* * *

> menu键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### pressed 属性

* * *

> 指针是否按下。

  * 类型：bool_t

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
