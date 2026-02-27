## progress_event_t

### 概述

![image](images/progress_event_t_0.png)

## 进度变化事件。

### 函数

函数名称 | 说明  
---|---  
progress_event_cast | 把event对象转progress_event_t对象。  
progress_event_init | 初始progress event。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
percent | uint32_t | 进度百分比。  
  
#### progress_event_cast 函数

* * *

  * 函数功能：



> 把event对象转progress_event_t对象。

  * 函数原型：


    
    
    progress_event_t* progress_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | progress_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### progress_event_init 函数

* * *

  * 函数功能：



> 初始progress event。

  * 函数原型：


    
    
    event_t* progress_event_init (progress_event_t* event, uint32_t percent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | progress_event_t* | event对象。  
percent | uint32_t | 进度。  
  
#### percent 属性

* * *

> 进度百分比。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
