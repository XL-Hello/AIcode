## tk_istream_udp_t

### 概述

![image](images/tk_istream_udp_t_0.png)

## 基于UDP实现的输入流。

### 函数

函数名称 | 说明  
---|---  
tk_istream_udp_create | 创建istream对象。  
tk_istream_udp_set_target_with_addr | 设置目标。  
tk_istream_udp_set_target_with_host | 设置目标。  
  
#### tk_istream_udp_create 函数

* * *

  * 函数功能：



> 创建istream对象。

  * 函数原型：


    
    
    tk_istream_t* tk_istream_udp_create (int sock);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_istream_t* | 返回istream对象。  
sock | int | socket。  
  
#### tk_istream_udp_set_target_with_addr 函数

* * *

  * 函数功能：



> 设置目标。

  * 函数原型：


    
    
    ret_t tk_istream_udp_set_target_with_addr (tk_istream_t* stream, struct sockaddr_in addr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
addr | struct sockaddr_in | 地址。  
  
#### tk_istream_udp_set_target_with_host 函数

* * *

  * 函数功能：



> 设置目标。

  * 函数原型：


    
    
    ret_t tk_istream_udp_set_target_with_host (tk_istream_t* stream, const char* host, int port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
stream | tk_istream_t* | istream对象。  
host | const char* | 主机或IP。  
port | int | 端口。
