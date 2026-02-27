## tk_socket_t

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
tk_socket_bind | 绑定到指定端口。  
tk_socket_bind_ex | 绑定到指定IP和端口。  
tk_socket_close | 关闭socket句柄。  
tk_socket_deinit | tcp/udp 平台~初始化。  
tk_socket_get_client_ip | 获取客户端IP。  
tk_socket_get_client_ip_str | 获取客户端IP。  
tk_socket_get_self_ip | 获取本地IP。  
tk_socket_get_self_ip_str | 获取本地IP。  
tk_socket_init | tcp/udp 平台初始化。  
tk_socket_last_io_has_error | 判断最后一次IO操作是否正常。  
tk_socket_recv | 接收数据。  
tk_socket_recvfrom | 从指定地址接收数据。  
tk_socket_resolve | 解析主机名，并初始化addr对象。  
tk_socket_send | 发送数据。  
tk_socket_sendto | 发送数据到指定地址。  
tk_socket_set_blocking | 设置为阻塞或非阻塞模式。  
tk_socket_wait_for_data | 等待数据。  
  
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
  
#### tk_socket_get_client_ip 函数

* * *

  * 函数功能：



> 获取客户端IP。

  * 函数原型：


    
    
    uint32_t tk_socket_get_client_ip (int sockfd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回客户端IP。  
sockfd | int | socket句柄。  
  
#### tk_socket_get_client_ip_str 函数

* * *

  * 函数功能：



> 获取客户端IP。

  * 函数原型：


    
    
    const char* tk_socket_get_client_ip_str (int sockfd, char* ip, int len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回IP地址。  
sockfd | int | socket句柄。  
ip | char* | 存放IP地址的内存。  
len | int | 存放IP地址的内存的长度。  
  
#### tk_socket_get_self_ip 函数

* * *

  * 函数功能：



> 获取本地IP。

  * 函数原型：


    
    
    uint32_t tk_socket_get_self_ip (int sockfd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回本地IP。  
sockfd | int | socket句柄。  
  
#### tk_socket_get_self_ip_str 函数

* * *

  * 函数功能：



> 获取本地IP。

  * 函数原型：


    
    
    const char* tk_socket_get_self_ip_str (int sockfd, char* ip, int len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回IP地址。  
sockfd | int | socket句柄。  
ip | char* | 存放IP地址的内存。  
len | int | 存放IP地址的内存的长度。  
  
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
  
#### tk_socket_last_io_has_error 函数

* * *

  * 函数功能：



> 判断最后一次IO操作是否正常。

  * 函数原型：


    
    
    bool_t tk_socket_last_io_has_error ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示有错误，否则表示正常。  
  
#### tk_socket_recv 函数

* * *

  * 函数功能：



> 接收数据。

  * 函数原型：


    
    
    int32_t tk_socket_recv (int sock, void* buffer, uint32_t size, int flags);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际接收的字节数。  
sock | int | socket句柄。  
buffer | void* | 用于返回数据的缓冲区。  
size | uint32_t | 缓冲区大小。  
flags | int | 标志。  
  
#### tk_socket_recvfrom 函数

* * *

  * 函数功能：



> 从指定地址接收数据。

  * 函数原型：


    
    
    int32_t tk_socket_recvfrom (int sock, void* buffer, uint32_t size, int flags, struct sockaddr* dest_addr, uint32_t* dest_len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际接收的字节数。  
sock | int | socket句柄。  
buffer | void* | 用于返回数据的缓冲区。  
size | uint32_t | 缓冲区大小。  
flags | int | 标志。  
dest_addr | struct sockaddr* | 目标地址。  
dest_len | uint32_t* | 目标地址长度。  
  
#### tk_socket_resolve 函数

* * *

  * 函数功能：



> 解析主机名，并初始化addr对象。

  * 函数原型：


    
    
    struct sockaddr* tk_socket_resolve (const char* host, int port, struct sockaddr_in* addr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | struct sockaddr* | 返回地址对象。  
host | const char* | 主机名。  
port | int | 端口号。  
addr | struct sockaddr_in* | 地址对象。  
  
#### tk_socket_send 函数

* * *

  * 函数功能：



> 发送数据。

  * 函数原型：


    
    
    int32_t tk_socket_send (int sock, const void* buffer, uint32_t size, int flags);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际发送的字节数。  
sock | int | socket句柄。  
buffer | const void* | 数据缓冲区。  
size | uint32_t | 数据长度。  
flags | int | 标志。  
  
#### tk_socket_sendto 函数

* * *

  * 函数功能：



> 发送数据到指定地址。

  * 函数原型：


    
    
    int32_t tk_socket_sendto (int sock, const void* buffer, uint32_t size, int flags, const struct sockaddr* dest_addr, uint32_t dest_len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际发送的字节数。  
sock | int | socket句柄。  
buffer | const void* | 数据缓冲区。  
size | uint32_t | 数据长度。  
flags | int | 标志。  
dest_addr | const struct sockaddr* | 目标地址。  
dest_len | uint32_t | 目标地址长度。  
  
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
timeout_ms | uint32_t | 等待时间(毫秒)。
