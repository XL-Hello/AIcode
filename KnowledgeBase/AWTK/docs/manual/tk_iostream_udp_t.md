## tk_iostream_udp_t

### 概述

![image](images/tk_iostream_udp_t_0.png)

## 基于UDP实现的输入输出流。

### 函数

函数名称 | 说明  
---|---  
tk_iostream_udp_create | 创建iostream对象(客户端)。  
tk_iostream_udp_create_client | 创建iostream对象(客户端)。  
tk_iostream_udp_create_client_ex | 创建iostream对象(客户端)。  
  
#### tk_iostream_udp_create 函数

* * *

  * 函数功能：



> 创建iostream对象(客户端)。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_udp_create (int sock);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
sock | int | socket  
  
#### tk_iostream_udp_create_client 函数

* * *

  * 函数功能：



> 创建iostream对象(客户端)。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_udp_create_client (const char* host, int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
host | const char* | 服务器地址。  
port | int | 服务器端口。  
  
#### tk_iostream_udp_create_client_ex 函数

* * *

  * 函数功能：



> 创建iostream对象(客户端)。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_udp_create_client_ex (const char* host, int port, const char* local_ip, int local_port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
host | const char* | 服务器地址。  
port | int | 服务器端口。  
local_ip | const char* | 本地IP地址(为NULL时自动绑定)。  
local_port | int | 本地端口。
