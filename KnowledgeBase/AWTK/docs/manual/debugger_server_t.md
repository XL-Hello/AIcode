## debugger_server_t

### 概述

@annotaion [“fake”] 调试器服务器。

* * *

### 函数

函数名称 | 说明  
---|---  
debugger_server_find_debugger | 查找调试器对象。  
debugger_server_is_running | 判断服务是否在运行。  
debugger_server_set_single_mode | 设置为单一debugger模式。  
debugger_server_set_single_mode_ex | 设置为单一debugger模式。  
debugger_server_start | 启用调试器服务。  
debugger_server_stop | 停用调试器服务。  
debugger_server_wait | 等待调试器服务退出。  
  
#### debugger_server_find_debugger 函数

* * *

  * 函数功能：



> 查找调试器对象。

  * 函数原型：


    
    
    debugger_t* debugger_server_find_debugger (const char* code_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_t* | 返回debugger对象或者NULL。  
code_id | const char* | 代码ID。  
  
#### debugger_server_is_running 函数

* * *

  * 函数功能：



> 判断服务是否在运行。

  * 函数原型：


    
    
    bool_t debugger_server_is_running ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示在运行，否则表示没有运行。  
  
#### debugger_server_set_single_mode 函数

* * *

  * 函数功能：



> 设置为单一debugger模式。

  * 函数原型：


    
    
    ret_t debugger_server_set_single_mode (bool_t single_mode);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
single_mode | bool_t | 单一debugger模式  
  
#### debugger_server_set_single_mode_ex 函数

* * *

  * 函数功能：



> 设置为单一debugger模式。

  * 函数原型：


    
    
    ret_t debugger_server_set_single_mode_ex (bool_t single_mode, const char* lang, const char* code_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
single_mode | bool_t | 单一debugger模式  
lang | const char* | 语言。  
code_id | const char* | 代码ID。  
  
#### debugger_server_start 函数

* * *

  * 函数功能：



> 启用调试器服务。

  * 函数原型：


    
    
    ret_t debugger_server_start (tk_iostream_t* io);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
io | tk_iostream_t* | IO对象，用于和客户端通信。  
  
#### debugger_server_stop 函数

* * *

  * 函数功能：



> 停用调试器服务。

  * 函数原型：


    
    
    ret_t debugger_server_stop ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### debugger_server_wait 函数

* * *

  * 函数功能：



> 等待调试器服务退出。

  * 函数原型：


    
    
    ret_t debugger_server_wait ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。
