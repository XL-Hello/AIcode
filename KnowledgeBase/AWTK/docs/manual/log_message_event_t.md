## log_message_event_t

### 概述

![image](images/log_message_event_t_0.png)

## 日志事件。

### 函数

函数名称 | 说明  
---|---  
log_message_event_cast | 把event对象转log_message_event_t对象。  
log_message_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
level | tk_log_level_t | 级别。  
message | const char* | 日志。  
  
#### log_message_event_cast 函数

* * *

  * 函数功能：



> 把event对象转log_message_event_t对象。

  * 函数原型：


    
    
    log_message_event_t* log_message_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | log_message_event_t* | event对象。  
event | event_t* | event对象。  
  
#### log_message_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* log_message_event_init (log_message_event_t* event, tk_log_level_t level, const char* message);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | log_message_event_t* | event对象。  
level | tk_log_level_t | 级别。  
message | const char* | 日志。  
  
#### level 属性

* * *

> 级别。

  * 类型：tk_log_level_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### message 属性

* * *

> 日志。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
