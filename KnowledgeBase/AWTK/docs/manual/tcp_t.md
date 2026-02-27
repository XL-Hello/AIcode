## tcp_t

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
tk_socket_get_port | 获取当前 socket 的监听指定端口。  
tk_tcp_accept | 监听指定端口，成功返回sock句柄。  
tk_tcp_connect | 连接到指定服务器。  
tk_tcp_connect_ex | 连接到指定服务器。  
tk_tcp_is_port_in_use | 判断指定端口是否被占用。  
tk_tcp_listen | 监听指定端口，成功返回sock句柄。  
  
#### tk_socket_get_port 函数

* * *

  * 函数功能：



> 获取当前 socket 的监听指定端口。

  * 函数原型：


    
    
    int tk_socket_get_port (int sock);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 成功返回端口，失败返回 -1。  
sock | int | socket句柄。  
  
#### tk_tcp_accept 函数

* * *

  * 函数功能：



> 监听指定端口，成功返回sock句柄。

  * 函数原型：


    
    
    int tk_tcp_accept (int sock);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回sock句柄。  
sock | int | socket句柄。  
  
#### tk_tcp_connect 函数

* * *

  * 函数功能：



> 连接到指定服务器。

  * 函数原型：


    
    
    int tk_tcp_connect (const char* host, int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回sock句柄。  
host | const char* | 主机名或IP地址。  
port | int | 端口号。  
  
#### tk_tcp_connect_ex 函数

* * *

  * 函数功能：



> 连接到指定服务器。

  * 函数原型：


    
    
    int tk_tcp_connect_ex (const char* host, int port, int timeout, void* opts);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回sock句柄。  
host | const char* | 主机名或IP地址。  
port | int | 端口号。  
timeout | int | 连接超时（毫秒）设置，设置为0代表按系统默认超时。  
opts | void* | 保留参数设置，当前只接受NULL值。  
  
#### tk_tcp_is_port_in_use 函数

* * *

  * 函数功能：



> 判断指定端口是否被占用。

  * 函数原型：


    
    
    bool_t tk_tcp_is_port_in_use (int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示被占用，否则表示未被占用。  
port | int | 端口号。  
  
#### tk_tcp_listen 函数

* * *

  * 函数功能：



> 监听指定端口，成功返回sock句柄。

  * 函数原型：


    
    
    int tk_tcp_listen (int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回sock句柄。  
port | int | 端口号。
