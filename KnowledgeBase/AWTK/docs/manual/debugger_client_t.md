## debugger_client_t

### 概述

## 调试器客户端。

### 函数

函数名称 | 说明  
---|---  
debugger_client_cast | 类型转换。  
debugger_client_create | 创建调试器对象。  
debugger_client_dispatch | 分发一个服务端推送的事件。  
debugger_client_wait_for_completed | 等待完成事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
io | tk_iostream_t* | 与服务器通信的stream对象。  
  
#### debugger_client_cast 函数

* * *

  * 函数功能：



> 类型转换。

  * 函数原型：


    
    
    debugger_client_t* debugger_client_cast (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_client_t* | 返回debugger对象。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_client_create 函数

* * *

  * 函数功能：



> 创建调试器对象。

  * 函数原型：


    
    
    debugger_t* debugger_client_create (tk_iostream_t* io);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_t* | 返回debugger对象。  
io | tk_iostream_t* | io对象。  
  
#### debugger_client_dispatch 函数

* * *

  * 函数功能：



> 分发一个服务端推送的事件。

  * 函数原型：


    
    
    ret_t debugger_client_dispatch (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_client_wait_for_completed 函数

* * *

  * 函数功能：



> 等待完成事件。

  * 函数原型：


    
    
    ret_t debugger_client_wait_for_completed (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### io 属性

* * *

> 与服务器通信的stream对象。

  * 类型：tk_iostream_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
