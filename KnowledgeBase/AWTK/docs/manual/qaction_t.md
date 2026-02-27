## qaction_t

### 概述

## 代表一个action，放在action queue中。

### 函数

函数名称 | 说明  
---|---  
qaction_create | 创建action对象。  
qaction_destroy | 销毁。  
qaction_exec | 执行。  
qaction_notify | 事件通知。  
qaction_set_on_event | 设置事件处理函数(回调函数在后台线程执行)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
args | uint64_t* | exec的参数(视具体的action而不同)。  
exec | qaction_exec_t | 执行函数。  
on_event | qaction_on_event_t | 事件处理函数。如进度、错误和完成等。  
  
#### qaction_create 函数

* * *

  * 函数功能：



> 创建action对象。

  * 函数原型：


    
    
    qaction_t* qaction_create (qaction_exec_t exec, void* args, uint32_t args_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | qaction_t* | 返回action对象。  
exec | qaction_exec_t | 执行函数。  
args | void* | 参数。  
args_size | uint32_t | 参数长度。  
  
#### qaction_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t qaction_destroy (qaction_t* q);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
q | qaction_t* | qaction对象。  
  
#### qaction_exec 函数

* * *

  * 函数功能：



> 执行。

  * 函数原型：


    
    
    ret_t qaction_exec (qaction_t* action);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
action | qaction_t* | action对象。  
  
#### qaction_notify 函数

* * *

  * 函数功能：



> 事件通知。

  * 函数原型：


    
    
    ret_t qaction_notify (qaction_t* action, event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
action | qaction_t* | action对象。  
event | event_t* | event对象。  
  
#### qaction_set_on_event 函数

* * *

  * 函数功能：



> 设置事件处理函数(回调函数在后台线程执行)。
> 
> exec执行完成后，会触发EVT_DONE事件，一般在EVT_DONE事件中调用qaction_destroy函数销毁action。

  * 函数原型：


    
    
    ret_t qaction_set_on_event (qaction_t* action, qaction_on_event_t on_event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
action | qaction_t* | action对象。  
on_event | qaction_on_event_t | 事件处理函数。  
  
#### args 属性

* * *

> exec的参数(视具体的action而不同)。

  * 类型：uint64_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### exec 属性

* * *

> 执行函数。

  * 类型：qaction_exec_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### on_event 属性

* * *

> 事件处理函数。如进度、错误和完成等。

  * 类型：qaction_on_event_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
