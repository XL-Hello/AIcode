## model_event_t

### 概述

![image](images/model_event_t_0.png)

## model变化事件。

### 函数

函数名称 | 说明  
---|---  
model_event_cast | 把event对象转model_event_t对象。  
model_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
change_type | const char* | 变化类型(update/add/remove)。  
model | tk_object_t* | 模型。  
name | const char* | 模型名称。  
  
#### model_event_cast 函数

* * *

  * 函数功能：



> 把event对象转model_event_t对象。

  * 函数原型：


    
    
    model_event_t* model_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | model_event_t* | event对象。  
event | event_t* | event对象。  
  
#### model_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* model_event_init (model_event_t* event, const char* name, const char* change_type, tk_object_t* model);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | model_event_t* | event对象。  
name | const char* | 名称。  
change_type | const char* | 变化类型。  
model | tk_object_t* | 模型。  
  
#### change_type 属性

* * *

> 变化类型(update/add/remove)。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### model 属性

* * *

> 模型。

  * 类型：tk_object_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### name 属性

* * *

> 模型名称。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
