## timer_info_t

### 概述

![image](images/timer_info_t_0.png)

## 单个定时器的信息。

### 函数

函数名称 | 说明  
---|---  
timer_info_cast | 转换为timer_info对象(供脚本语言使用)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
ctx | void* | 定时器回调函数的上下文  
duration | uint32_t | 时间间隔(单位为毫秒)。  
extra_ctx | void* | 定时器回调函数的上下文  
id | uint32_t | 定时器的ID  
now | uint64_t | 当前时间(相对时间，单位为毫秒)。  
on_destroy | tk_destroy_t | 定时器销毁时的回调函数。  
on_destroy_ctx | void* | 定时器销毁时的回调函数上下文。  
on_timer | timer_func_t | 定时器回调函数。  
start | uint64_t | 起始时间(相对时间，单位为毫秒)。  
suspend | bool_t | 定时器是否为挂起状态。  
  
#### timer_info_cast 函数

* * *

  * 函数功能：



> 转换为timer_info对象(供脚本语言使用)。

  * 函数原型：


    
    
    timer_info_t* timer_info_cast (timer_info_t* timer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | timer_info_t* | timer_info对象。  
timer | timer_info_t* | timer_info对象。  
  
#### ctx 属性

* * *

> 定时器回调函数的上下文

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### duration 属性

* * *

> 时间间隔(单位为毫秒)。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### extra_ctx 属性

* * *

> 定时器回调函数的上下文

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### id 属性

* * *

> 定时器的ID
> 
> 为TK_INVALID_ID时表示无效定时器。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### now 属性

* * *

> 当前时间(相对时间，单位为毫秒)。

  * 类型：uint64_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### on_destroy 属性

* * *

> 定时器销毁时的回调函数。

  * 类型：tk_destroy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### on_destroy_ctx 属性

* * *

> 定时器销毁时的回调函数上下文。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### on_timer 属性

* * *

> 定时器回调函数。

  * 类型：timer_func_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### start 属性

* * *

> 起始时间(相对时间，单位为毫秒)。

  * 类型：uint64_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### suspend 属性

* * *

> 定时器是否为挂起状态。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
