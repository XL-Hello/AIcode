## cmd_exec_event_t

### 概述

![image](images/cmd_exec_event_t_0.png)

## 对象执行命令的事件。

### 函数

函数名称 | 说明  
---|---  
cmd_exec_event_cast | 把event对象转cmd_exec_event_t对象。  
cmd_exec_event_init | 初始命令执行事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
args | const char* | 命令的参数。  
can_exec | bool_t | 标识命令是否可以执行(适用于CAN_EXEC)。  
name | const char* | 命令的名称。  
result | ret_t | 执行结果(适用于EXECED)。  
  
#### cmd_exec_event_cast 函数

* * *

  * 函数功能：



> 把event对象转cmd_exec_event_t对象。

  * 函数原型：


    
    
    cmd_exec_event_t* cmd_exec_event_cast (event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | cmd_exec_event_t* | 返回event对象。  
event | event_t* | event对象。  
  
#### cmd_exec_event_init 函数

* * *

  * 函数功能：



> 初始命令执行事件。

  * 函数原型：


    
    
    event_t* cmd_exec_event_init (cmd_exec_event_t* event, uint32_t type, const char* name, const char* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回event对象。  
event | cmd_exec_event_t* | event对象。  
type | uint32_t | 事件类型。  
name | const char* | 命令名。  
args | const char* | 命令参数。  
  
#### args 属性

* * *

> 命令的参数。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### can_exec 属性

* * *

> 标识命令是否可以执行(适用于CAN_EXEC)。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### name 属性

* * *

> 命令的名称。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### result 属性

* * *

> 执行结果(适用于EXECED)。

  * 类型：ret_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
