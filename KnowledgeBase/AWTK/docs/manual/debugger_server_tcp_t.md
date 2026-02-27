## debugger_server_tcp_t

### 概述

## 调试器TCP服务端。

### 函数

函数名称 | 说明  
---|---  
debugger_server_tcp_deinit | 停止调试器服务。  
debugger_server_tcp_init | 初始化调试器服务。  
debugger_server_tcp_is_inited | 检查是否已经初始化。  
debugger_server_tcp_start | 启动调试器服务。  
debugger_server_tcp_start_async | 启动调试器服务。  
  
#### debugger_server_tcp_deinit 函数

* * *

  * 函数功能：



> 停止调试器服务。

  * 函数原型：


    
    
    ret_t debugger_server_tcp_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### debugger_server_tcp_init 函数

* * *

  * 函数功能：



> 初始化调试器服务。

  * 函数原型：


    
    
    ret_t debugger_server_tcp_init (uint32_t port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
port | uint32_t | 监听端口。  
  
#### debugger_server_tcp_is_inited 函数

* * *

  * 函数功能：



> 检查是否已经初始化。

  * 函数原型：


    
    
    bool_t debugger_server_tcp_is_inited ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示已经初始化，否则表示没有。  
  
#### debugger_server_tcp_start 函数

* * *

  * 函数功能：



> 启动调试器服务。 接收客户端请求，并启动服务。

  * 函数原型：


    
    
    ret_t debugger_server_tcp_start ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### debugger_server_tcp_start_async 函数

* * *

  * 函数功能：



> 启动调试器服务。 接收客户端请求，并启动服务。

  * 函数原型：


    
    
    ret_t debugger_server_tcp_start_async ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。
