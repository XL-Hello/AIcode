## prop_change_event_t

### 概述

![image](images/prop_change_event_t_0.png)

## 对象属性变化事件。

### 函数

函数名称 | 说明  
---|---  
prop_change_event_cast | 把event对象转prop_change_event_t对象。  
prop_change_event_init | 初始prop change event。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
name | const char* | 属性的名称。  
value | const value_t* | 属性的值。  
  
#### prop_change_event_cast 函数

* * *

  * 函数功能：



> 把event对象转prop_change_event_t对象。

  * 函数原型：


    
    
    prop_change_event_t* prop_change_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | prop_change_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### prop_change_event_init 函数

* * *

  * 函数功能：



> 初始prop change event。

  * 函数原型：


    
    
    event_t* prop_change_event_init (prop_change_event_t* event, uint32_t type, const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | prop_change_event_t* | event对象。  
type | uint32_t | 事件类型。  
name | const char* | 属性名。  
value | const value_t* | 属性的值。  
  
#### name 属性

* * *

> 属性的名称。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### value 属性

* * *

> 属性的值。

  * 类型：const value_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
