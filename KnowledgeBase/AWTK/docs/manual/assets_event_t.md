## assets_event_t

### 概述

![image](images/assets_event_t_0.png)

## 资源事件，由资源管理器触发。

### 函数

函数名称 | 说明  
---|---  
assets_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
asset_info | asset_info_t* | 触发事件的资源对象  
type | asset_type_t | 触发事件的资源类型  
  
#### assets_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* assets_event_init (assets_event_t* event, assets_manager_t* am, uint32_t type, asset_type_t asset_type, asset_info_t* asset_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | assets_event_t* | event对象。  
am | assets_manager_t* | 事件目标资源管理器。  
type | uint32_t | 事件类型。  
asset_type | asset_type_t | 资源类型。  
asset_info | asset_info_t* | 资源对象。  
  
#### asset_info 属性

* * *

> 触发事件的资源对象

  * 类型：asset_info_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### type 属性

* * *

> 触发事件的资源类型

  * 类型：asset_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
