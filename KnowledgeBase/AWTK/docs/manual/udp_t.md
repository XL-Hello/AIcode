## udp_t

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
tk_udp_connect | 连接到指定服务器。  
tk_udp_listen | 监听指定端口，成功返回sock句柄。  
tk_udp_socket | 创建UDP socket。  
  
#### tk_udp_connect 函数

* * *

  * 函数功能：



> 连接到指定服务器。

  * 函数原型：


    
    
    int tk_udp_connect (const char* host, int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回sock句柄。  
host | const char* | 主机名或IP地址。  
port | int | 端口号。  
  
#### tk_udp_listen 函数

* * *

  * 函数功能：



> 监听指定端口，成功返回sock句柄。

  * 函数原型：


    
    
    int tk_udp_listen (int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回sock句柄。  
port | int | 端口号。  
  
#### tk_udp_socket 函数

* * *

  * 函数功能：



> 创建UDP socket。

  * 函数原型：


    
    
    int tk_udp_socket ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回sock句柄。
