## done_event_t

### 概述

![image](images/done_event_t_0.png)

## 执行完成事件。

### 函数

函数名称 | 说明  
---|---  
done_event_cast | 把event对象转done_event_t对象。  
done_event_init | 初始done event。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
result | ret_t | 执行结果。  
  
#### done_event_cast 函数

* * *

  * 函数功能：



> 把event对象转done_event_t对象。

  * 函数原型：


    
    
    done_event_t* done_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | done_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### done_event_init 函数

* * *

  * 函数功能：



> 初始done event。

  * 函数原型：


    
    
    event_t* done_event_init (done_event_t* event, ret_t result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | done_event_t* | event对象。  
result | ret_t | 结果。  
  
#### result 属性

* * *

> 执行结果。

  * 类型：ret_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
