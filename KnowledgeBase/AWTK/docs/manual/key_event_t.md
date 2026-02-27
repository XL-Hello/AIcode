## key_event_t

### 概述

![image](images/key_event_t_0.png)

## 按键事件。

### 函数

函数名称 | 说明  
---|---  
key_event_cast | 把event对象转key_event_t对象。  
key_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
alt | bool_t | alt键是否按下。  
capslock | bool_t | capslock键是否按下。  
cmd | bool_t | cmd/win键是否按下。  
ctrl | bool_t | ctrl键是否按下。  
key | uint32_t | 键值。  
lalt | bool_t | left alt键是否按下。  
lctrl | bool_t | left ctrl键是否按下。  
lshift | bool_t | left shift键是否按下。  
menu | bool_t | menu键是否按下。  
numlock | bool_t | numlock键是否按下。  
ralt | bool_t | right alt键是否按下。  
rctrl | bool_t | right ctrl键是否按下。  
rshift | bool_t | right shift键是否按下。  
shift | bool_t | shift键是否按下。  
  
#### key_event_cast 函数

* * *

  * 函数功能：



> 把event对象转key_event_t对象。

  * 函数原型：


    
    
    key_event_t* key_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | key_event_t* | event对象。  
event | event_t* | event对象。  
  
#### key_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* key_event_init (key_event_t* event, uint32_t type, void* target, int32_t key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | key_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
key | int32_t | key的值。  
  
#### alt 属性

* * *

> alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### capslock 属性

* * *

> capslock键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### cmd 属性

* * *

> cmd/win键是否按下。

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
  
#### key 属性

* * *

> 键值。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### lalt 属性

* * *

> left alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### lctrl 属性

* * *

> left ctrl键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### lshift 属性

* * *

> left shift键是否按下。

  * 类型：bool_t

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
  
#### numlock 属性

* * *

> numlock键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### ralt 属性

* * *

> right alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### rctrl 属性

* * *

> right ctrl键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### rshift 属性

* * *

> right shift键是否按下。

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
