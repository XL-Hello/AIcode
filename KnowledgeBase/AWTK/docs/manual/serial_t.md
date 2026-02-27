## serial_t

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
serial_bytesize_from_str | 字符串转bytesize  
serial_close | 关闭串口  
serial_config | 配置串口  
serial_flowcontrol_from_str | 字符串转flowcontrol  
serial_handle_get_dev | 获取设备句柄。  
serial_handle_get_fd | 获取文件描述符。  
serial_iflush | 刷新input缓冲区。  
serial_oflush | 刷新output缓冲区。  
serial_open | 打开串口  
serial_parity_from_str | 字符串转parity  
serial_read | 串口读数据  
serial_stopbits_from_str | 字符串转stopbits  
serial_wait_for_data | 等待数据。  
serial_write | 串口写数据  
  
#### serial_bytesize_from_str 函数

* * *

  * 函数功能：



> 字符串转bytesize

  * 函数原型：


    
    
    bytesize_t serial_bytesize_from_str (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bytesize_t | 返回bytesize。  
str | const char* | 字符串。  
  
#### serial_close 函数

* * *

  * 函数功能：



> 关闭串口

  * 函数原型：


    
    
    ret_t serial_close (serial_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | serial_handle_t | 串口句柄。  
  
#### serial_config 函数

* * *

  * 函数功能：



> 配置串口

  * 函数原型：


    
    
    ret_t serial_config (serial_handle_t handle, uint32_t baudrate, bytesize_t bytesize, stopbits_t stopbits, flowcontrol_t flowcontrol, parity_t parity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | serial_handle_t | 串口句柄。  
baudrate | uint32_t | 波特率。  
bytesize | bytesize_t | 数据位。  
stopbits | stopbits_t | 停止位  
flowcontrol | flowcontrol_t | 流控。  
parity | parity_t | 校验位。  
  
#### serial_flowcontrol_from_str 函数

* * *

  * 函数功能：



> 字符串转flowcontrol

  * 函数原型：


    
    
    flowcontrol_t serial_flowcontrol_from_str (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | flowcontrol_t | 返回flowcontrol。  
str | const char* | 字符串。  
  
#### serial_handle_get_dev 函数

* * *

  * 函数功能：



> 获取设备句柄。

  * 函数原型：


    
    
    serial_dev_t serial_handle_get_dev (serial_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | serial_dev_t | 返回设备句柄。  
handle | serial_handle_t | 串口句柄。  
  
#### serial_handle_get_fd 函数

* * *

  * 函数功能：



> 获取文件描述符。

  * 函数原型：


    
    
    int serial_handle_get_fd (serial_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回文件描述符。  
handle | serial_handle_t | 串口句柄。  
  
#### serial_iflush 函数

* * *

  * 函数功能：



> 刷新input缓冲区。

  * 函数原型：


    
    
    ret_t serial_iflush (serial_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | serial_handle_t | 串口句柄。  
  
#### serial_oflush 函数

* * *

  * 函数功能：



> 刷新output缓冲区。

  * 函数原型：


    
    
    ret_t serial_oflush (serial_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | serial_handle_t | 串口句柄。  
  
#### serial_open 函数

* * *

  * 函数功能：



> 打开串口 Windows下，需要在应用程序初始化时，调用 tk_socket_init。

  * 函数原型：


    
    
    serial_handle_t serial_open (const char* port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | serial_handle_t | 失败返回NULL。  
port | const char* | 串口号。  
  
#### serial_parity_from_str 函数

* * *

  * 函数功能：



> 字符串转parity

  * 函数原型：


    
    
    parity_t serial_parity_from_str (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | parity_t | 返回parity。  
str | const char* | 字符串。  
  
#### serial_read 函数

* * *

  * 函数功能：



> 串口读数据

  * 函数原型：


    
    
    int32_t serial_read (serial_handle_t handle, uint8_t* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际读取的字节数。  
handle | serial_handle_t | 串口句柄。  
buff | uint8_t* | 数据缓冲区。  
max_size | uint32_t | 数据长度。  
  
#### serial_stopbits_from_str 函数

* * *

  * 函数功能：



> 字符串转stopbits

  * 函数原型：


    
    
    stopbits_t serial_stopbits_from_str (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | stopbits_t | 返回stopbits。  
str | const char* | 字符串。  
  
#### serial_wait_for_data 函数

* * *

  * 函数功能：



> 等待数据。

  * 函数原型：


    
    
    ret_t serial_wait_for_data (serial_handle_t handle, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | serial_handle_t | 串口句柄。  
timeout_ms | uint32_t | 等待时间(毫秒)。  
  
#### serial_write 函数

* * *

  * 函数功能：



> 串口写数据

  * 函数原型：


    
    
    int32_t serial_write (serial_handle_t handle, const uint8_t* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际写入的字节数。  
handle | serial_handle_t | 串口句柄。  
buff | const uint8_t* | 数据缓冲区。  
max_size | uint32_t | 数据长度。
