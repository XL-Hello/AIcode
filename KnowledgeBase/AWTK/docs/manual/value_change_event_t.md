## value_change_event_t

### 概述

![image](images/value_change_event_t_0.png)

## 值变化事件。

### 函数

函数名称 | 说明  
---|---  
value_change_event_cast | 把event对象转value_change_event_t对象。  
value_change_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
new_value | value_t | 新值。  
old_value | value_t | 旧值。  
  
#### value_change_event_cast 函数

* * *

  * 函数功能：



> 把event对象转value_change_event_t对象。

  * 函数原型：


    
    
    value_change_event_t* value_change_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_change_event_t* | event对象。  
event | event_t* | event对象。  
  
#### value_change_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* value_change_event_init (value_change_event_t* event, uint32_t type, void* target);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | value_change_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
  
#### new_value 属性

* * *

> 新值。

  * 类型：value_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### old_value 属性

* * *

> 旧值。

  * 类型：value_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
