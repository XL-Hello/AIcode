## shortcut_t

### 概述

## 快捷键。

### 函数

函数名称 | 说明  
---|---  
shortcut_equal | 比较两个快捷键对象。  
shortcut_init | 初始化快捷键对象。  
shortcut_init_with_str | 初始化快捷键对象。  
shortcut_match | 检查事件与快捷键是否匹配。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
alt | bool_t | alt键是否按下。  
cmd | bool_t | cmd/win键是否按下。  
ctrl | bool_t | ctrl键是否按下。  
is_valid | bool_t | 是否有效。  
key | uint32_t | 键值。  
lalt | bool_t | left alt键是否按下。  
lctrl | bool_t | left ctrl键是否按下。  
lshift | bool_t | left shift键是否按下。  
menu | bool_t | menu键是否按下。  
ralt | bool_t | right alt键是否按下。  
rctrl | bool_t | right ctrl键是否按下。  
rshift | bool_t | right shift键是否按下。  
shift | bool_t | shift键是否按下。  
  
#### shortcut_equal 函数

* * *

  * 函数功能：



> 比较两个快捷键对象。

  * 函数原型：


    
    
    bool_t shortcut_equal (shortcut_t* shortcut1, shortcut_t* shortcut2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示相同，否则表示不同。  
shortcut1 | shortcut_t* | 快捷键对象1。  
shortcut2 | shortcut_t* | 快捷键对象2。  
  
#### shortcut_init 函数

* * *

  * 函数功能：



> 初始化快捷键对象。

  * 函数原型：


    
    
    shortcut_t* shortcut_init (shortcut_t* shortcut, uint32_t key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | shortcut_t* | 返回快捷键对象。  
shortcut | shortcut_t* | 快捷键对象。  
key | uint32_t | 键值。  
  
#### shortcut_init_with_str 函数

* * *

  * 函数功能：



> 初始化快捷键对象。

  * 函数原型：


    
    
    shortcut_t* shortcut_init_with_str (shortcut_t* shortcut, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | shortcut_t* | 返回快捷键对象。  
shortcut | shortcut_t* | 快捷键对象。  
str | const char* | 快捷键。  
  
#### shortcut_match 函数

* * *

  * 函数功能：



> 检查事件与快捷键是否匹配。

  * 函数原型：


    
    
    bool_t shortcut_match (shortcut_t* filter, shortcut_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示匹配，否则表示不匹配。  
filter | shortcut_t* | 过滤器快捷键对象。  
event | shortcut_t* | 事件快捷键对象。  
  
#### alt 属性

* * *

> alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### cmd 属性

* * *

> cmd/win键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### ctrl 属性

* * *

> ctrl键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### is_valid 属性

* * *

> 是否有效。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### key 属性

* * *

> 键值。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lalt 属性

* * *

> left alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lctrl 属性

* * *

> left ctrl键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lshift 属性

* * *

> left shift键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### menu 属性

* * *

> menu键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### ralt 属性

* * *

> right alt键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### rctrl 属性

* * *

> right ctrl键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### rshift 属性

* * *

> right shift键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### shift 属性

* * *

> shift键是否按下。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
