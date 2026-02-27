## tk_iostream_mbedtls_t

### 概述

![image](images/tk_iostream_mbedtls_t_0.png)

## 基于MBEDTLS实现的输入输出流。

### 函数

函数名称 | 说明  
---|---  
tk_iostream_mbedtls_create | 创建iostream对象。  
tk_iostream_mbedtls_create_client | 创建iostream对象。  
  
#### tk_iostream_mbedtls_create 函数

* * *

  * 函数功能：



> 创建iostream对象。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_mbedtls_create (mbedtls_conn_t* conn);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
conn | mbedtls_conn_t* | ssl连接。  
  
#### tk_iostream_mbedtls_create_client 函数

* * *

  * 函数功能：



> 创建iostream对象。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_mbedtls_create_client (const char* host, uint16_t port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
host | const char* | 主机地址。  
port | uint16_t | 端口号。
