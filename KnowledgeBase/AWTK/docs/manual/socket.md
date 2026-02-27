## socket

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
socket_last_io_has_error | 判断最后一次IO操作是否正常。  
socket_resolve | 解析主机名，并初始化addr对象。  
tk_socket_bind | 绑定到指定端口。  
tk_socket_bind_ex | 绑定到指定IP和端口。  
tk_socket_close | 关闭socket句柄。  
tk_socket_deinit | tcp/udp 平台~初始化。  
tk_socket_init | tcp/udp 平台初始化。  
tk_socket_set_blocking | 设置为阻塞或非阻塞模式。  
tk_socket_wait_for_data | 等待数据。  
  
#### socket_last_io_has_error 函数

* * *

  * 函数功能：



> 判断最后一次IO操作是否正常。

  * 函数原型：


    
    
    bool_t socket_last_io_has_error ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示有错误，否则表示正常。  
  
#### socket_resolve 函数

* * *

  * 函数功能：



> 解析主机名，并初始化addr对象。

  * 函数原型：


    
    
    struct sockaddr* socket_resolve (const char* host, int port, struct sockaddr_in* addr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | struct sockaddr* | 返回地址对象。  
host | const char* | 主机名。  
port | int | 端口号。  
addr | struct sockaddr_in* | 地址对象。  
  
#### tk_socket_bind 函数

* * *

  * 函数功能：



> 绑定到指定端口。

  * 函数原型：


    
    
    ret_t tk_socket_bind (int sock, int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sock | int | socket句柄。  
port | int | 端口号。  
  
#### tk_socket_bind_ex 函数

* * *

  * 函数功能：



> 绑定到指定IP和端口。

  * 函数原型：


    
    
    ret_t tk_socket_bind_ex (int sock, const char* ip, int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sock | int | socket句柄。  
ip | const char* | IP地址(可以为NULL)。  
port | int | 端口号。  
  
#### tk_socket_close 函数

* * *

  * 函数功能：



> 关闭socket句柄。

  * 函数原型：


    
    
    ret_t tk_socket_close (int sock);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sock | int | socket句柄。  
  
#### tk_socket_deinit 函数

* * *

  * 函数功能：



> tcp/udp 平台~初始化。

  * 函数原型：


    
    
    ret_t tk_socket_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_socket_init 函数

* * *

  * 函数功能：



> tcp/udp 平台初始化。

  * 函数原型：


    
    
    ret_t tk_socket_init ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_socket_set_blocking 函数

* * *

  * 函数功能：



> 设置为阻塞或非阻塞模式。

  * 函数原型：


    
    
    ret_t tk_socket_set_blocking (int sock, bool_t blocking);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sock | int | socket句柄。  
blocking | bool_t | 是否阻塞。  
  
#### tk_socket_wait_for_data 函数

* * *

  * 函数功能：



> 等待数据。

  * 函数原型：


    
    
    ret_t tk_socket_wait_for_data (int sock, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sock | int | socket句柄。  
timeout_ms | uint32_t | 等待时间(ms)。
