## event_t

### 概述

## 事件基类。

### 函数

函数名称 | 说明  
---|---  
event_cast | 转换为event对象。  
event_clone | clone事件对象。  
event_create | 创建event对象。  
event_destroy | 销毁事件对象。  
event_from_name | 将事件名转换成事件的类型。  
event_get_type | 获取event类型。  
event_init | 初始化事件。  
event_register_custom_name | 给事件注册名称。  
event_unregister_custom_name | 注销事件名称。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
native_window_handle | void* | 原生窗口句柄。  
size | uint32_t | 结构体的大小。  
target | void* | 事件发生的目标对象。  
time | uint64_t | 事件发生的时间点（该时间点并非真实时间）。  
type | uint32_t | 类型。  
  
#### event_cast 函数

* * *

  * 函数功能：



> 转换为event对象。
> 
> 供脚本语言使用

  * 函数原型：


    
    
    event_t* event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | event_t* | event对象。  
  
#### event_clone 函数

* * *

  * 函数功能：



> clone事件对象。

  * 函数原型：


    
    
    event_t* event_clone (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回事件对象。  
event | event_t* | event对象。  
  
#### event_create 函数

* * *

  * 函数功能：



> 创建event对象。

主要给脚本语言使用。

  * 函数原型：


    
    
    event_t* event_create (uint32_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回事件对象。  
type | uint32_t | 事件类型。  
  
#### event_destroy 函数

* * *

  * 函数功能：



> 销毁事件对象。

主要给脚本语言使用。

  * 函数原型：


    
    
    ret_t event_destroy (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
event | event_t* | event对象。  
  
#### event_from_name 函数

* * *

  * 函数功能：



> 将事件名转换成事件的类型。

  * 函数原型：


    
    
    int32_t event_from_name (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回事件的类型。  
name | const char* | 事件名。  
  
#### event_get_type 函数

* * *

  * 函数功能：



> 获取event类型。

  * 函数原型：


    
    
    uint32_t event_get_type (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回event类型。  
event | event_t* | event对象。  
  
#### event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t event_init (uint32_t type, void* target);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t | 事件对象。  
type | uint32_t | 事件类型。  
target | void* | 目标对象。  
  
#### event_register_custom_name 函数

* * *

  * 函数功能：



> 给事件注册名称。

  * 函数原型：


    
    
    ret_t event_register_custom_name (int32_t event_type, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
event_type | int32_t | 事件类型。  
name | const char* | 事件名。  
  
#### event_unregister_custom_name 函数

* * *

  * 函数功能：



> 注销事件名称。

  * 函数原型：


    
    
    ret_t event_unregister_custom_name (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 事件名。  
  
#### native_window_handle 属性

* * *

> 原生窗口句柄。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 结构体的大小。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### target 属性

* * *

> 事件发生的目标对象。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### time 属性

* * *

> 事件发生的时间点（该时间点并非真实时间）。

  * 类型：uint64_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### type 属性

* * *

> 类型。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
