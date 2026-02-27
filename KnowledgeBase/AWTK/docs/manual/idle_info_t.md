## idle_info_t

### 概述

![image](images/idle_info_t_0.png)

## 单个idle的信息。

### 函数

函数名称 | 说明  
---|---  
idle_info_cast | 转换为idle_info对象(供脚本语言使用)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
ctx | void* | idle回调函数上下文。  
extra_ctx | void* | idle回调函数上下文。  
id | uint32_t | idle的ID  
on_destroy | tk_destroy_t | idle销毁时的回调函数。  
on_destroy_ctx | void* | idle销毁时的回调函数的上下文。  
on_idle | idle_func_t | idle回调函数。  
  
#### idle_info_cast 函数

* * *

  * 函数功能：



> 转换为idle_info对象(供脚本语言使用)。

  * 函数原型：


    
    
    idle_info_t* idle_info_cast (idle_info_t* idle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | idle_info_t* | idle_info对象。  
idle | idle_info_t* | idle_info对象。  
  
#### ctx 属性

* * *

> idle回调函数上下文。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### extra_ctx 属性

* * *

> idle回调函数上下文。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### id 属性

* * *

> idle的ID
> 
> 为TK_INVALID_ID时表示无效idle。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### on_destroy 属性

* * *

> idle销毁时的回调函数。

  * 类型：tk_destroy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### on_destroy_ctx 属性

* * *

> idle销毁时的回调函数的上下文。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### on_idle 属性

* * *

> idle回调函数。

  * 类型：idle_func_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
