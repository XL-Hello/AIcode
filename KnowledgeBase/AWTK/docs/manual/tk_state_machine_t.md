## tk_state_machine_t

### 概述

## 状态机结构体

### 函数

函数名称 | 说明  
---|---  
tk_state_machine_current_get | 获取当前状态  
tk_state_machine_deinit | 反初始化  
tk_state_machine_handle | 事件处理  
tk_state_machine_init | 初始化  
tk_state_machine_previous_get | 获取上一个状态  
  
#### tk_state_machine_current_get 函数

* * *

  * 函数功能：



> 获取当前状态

  * 函数原型：


    
    
    const tk_sm_state_t* tk_state_machine_current_get (tk_state_machine_t* fsm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const tk_sm_state_t* | 返回 tk_sm_state_t 对象  
fsm | tk_state_machine_t* | 状态机地址  
  
#### tk_state_machine_deinit 函数

* * *

  * 函数功能：



> 反初始化

  * 函数原型：


    
    
    ret_t tk_state_machine_deinit (tk_state_machine_t* fsm, tk_sm_event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t 值  
fsm | tk_state_machine_t* | 状态机地址  
event | tk_sm_event_t* | 事件  
  
#### tk_state_machine_handle 函数

* * *

  * 函数功能：



> 事件处理

  * 函数原型：


    
    
    ret_t tk_state_machine_handle (tk_state_machine_t* fsm, tk_sm_event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t 值  
fsm | tk_state_machine_t* | 状态机地址  
event | tk_sm_event_t* | 事件  
  
#### tk_state_machine_init 函数

* * *

  * 函数功能：



> 初始化

  * 函数原型：


    
    
    ret_t tk_state_machine_init (tk_state_machine_t* fsm, const tk_sm_state_t* initial_state);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t 值  
fsm | tk_state_machine_t* | 状态机地址  
initial_state | const tk_sm_state_t* | 初始状态  
  
#### tk_state_machine_previous_get 函数

* * *

  * 函数功能：



> 获取上一个状态

  * 函数原型：


    
    
    const tk_sm_state_t* tk_state_machine_previous_get (tk_state_machine_t* fsm);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const tk_sm_state_t* | 返回 tk_sm_state_t 对象  
fsm | tk_state_machine_t* | 状态机地址
