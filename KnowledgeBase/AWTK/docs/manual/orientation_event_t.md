## orientation_event_t

### 概述

![image](images/orientation_event_t_0.png)

## 滚轮事件。

### 函数

函数名称 | 说明  
---|---  
orientation_event_cast | 把event对象转orientation_event_t对象。  
orientation_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
old_orientation | lcd_orientation_t | 旧的屏幕方向。  
orientation | lcd_orientation_t | 屏幕方向。  
  
#### orientation_event_cast 函数

* * *

  * 函数功能：



> 把event对象转orientation_event_t对象。

  * 函数原型：


    
    
    orientation_event_t* orientation_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | orientation_event_t* | event对象。  
event | event_t* | event对象。  
  
#### orientation_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* orientation_event_init (orientation_event_t* event, uint32_t type, void* target, lcd_orientation_t old_orientation, lcd_orientation_t new_orientation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | orientation_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
old_orientation | lcd_orientation_t | 旧的屏幕方向。  
new_orientation | lcd_orientation_t | 新的屏幕方向。  
  
#### old_orientation 属性

* * *

> 旧的屏幕方向。

  * 类型：lcd_orientation_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### orientation 属性

* * *

> 屏幕方向。

  * 类型：lcd_orientation_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
