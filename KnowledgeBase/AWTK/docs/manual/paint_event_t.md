## paint_event_t

### 概述

![image](images/paint_event_t_0.png)

## 绘制事件。

### 函数

函数名称 | 说明  
---|---  
paint_event_cast | 把event对象转paint_event_t对象。  
paint_event_init | 初始化事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
c | canvas_t* | canvas。  
  
#### paint_event_cast 函数

* * *

  * 函数功能：



> 把event对象转paint_event_t对象。

  * 函数原型：


    
    
    paint_event_t* paint_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | paint_event_t* | event 对象。  
event | event_t* | event对象。  
  
#### paint_event_init 函数

* * *

  * 函数功能：



> 初始化事件。

  * 函数原型：


    
    
    event_t* paint_event_init (paint_event_t* event, uint32_t type, void* target, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | event对象。  
event | paint_event_t* | event对象。  
type | uint32_t | 事件类型。  
target | void* | 事件目标。  
c | canvas_t* | canvas对象。  
  
#### c 属性

* * *

> canvas。

  * 类型：canvas_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
