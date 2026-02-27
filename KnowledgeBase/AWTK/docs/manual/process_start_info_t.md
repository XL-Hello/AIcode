## process_start_info_t

### 概述

## 子程序启动配置结构体。

### 函数

函数名称 | 说明  
---|---  
process_create | 创建子进程。  
process_destroy | 释放子进程。  
process_handle_get_fd | 获取文件描述符。  
process_is_broken | 子进程是否断开  
process_kill | 杀死子进程  
process_read | 读子进程的数据（StdIntput 的方式）  
process_wait_for_data | 等待数据。  
process_write | 给子进程写数据（StdOutput 的方式）  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
work_dir | char* | 子进程当前工作目录。（如果 NULL 的话，就为父进程的工作目录）  
  
#### process_create 函数

* * *

  * 函数功能：



> 创建子进程。

  * 函数原型：


    
    
    process_handle_t process_create (const char* file_path, const char** args, uint32_t argc, const process_start_info_t* start_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | process_handle_t | 返回子进程句柄。  
file_path | const char* | 子进程程序路径。(如果为空的话，使用命令行来执行参数的内容)  
args | const char** | 子进程参数。  
argc | uint32_t | 子进程参数长度。  
start_info | const process_start_info_t* | 子进程启动信息。（如果 NULL，就使用默认是值）  
  
#### process_destroy 函数

* * *

  * 函数功能：



> 释放子进程。

  * 函数原型：


    
    
    ret_t process_destroy (process_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | process_handle_t | 子进程句柄。  
  
#### process_handle_get_fd 函数

* * *

  * 函数功能：



> 获取文件描述符。

  * 函数原型：


    
    
    int process_handle_get_fd (process_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回文件描述符。  
handle | process_handle_t | 子进程句柄。  
  
#### process_is_broken 函数

* * *

  * 函数功能：



> 子进程是否断开

  * 函数原型：


    
    
    bool_t process_is_broken (process_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 断开返回 true。  
handle | process_handle_t | 子进程句柄。  
  
#### process_kill 函数

* * *

  * 函数功能：



> 杀死子进程

  * 函数原型：


    
    
    ret_t process_kill (process_handle_t handle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | process_handle_t | 子进程句柄。  
  
#### process_read 函数

* * *

  * 函数功能：



> 读子进程的数据（StdIntput 的方式）

  * 函数原型：


    
    
    int32_t process_read (process_handle_t handle, uint8_t* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际读取的字节数。  
handle | process_handle_t | 子进程句柄。  
buff | uint8_t* | 数据缓冲区。  
max_size | uint32_t | 数据长度。  
  
#### process_wait_for_data 函数

* * *

  * 函数功能：



> 等待数据。

  * 函数原型：


    
    
    ret_t process_wait_for_data (process_handle_t handle, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
handle | process_handle_t | 子进程句柄。  
timeout_ms | uint32_t | 等待时间(毫秒)。  
  
#### process_write 函数

* * *

  * 函数功能：



> 给子进程写数据（StdOutput 的方式）

  * 函数原型：


    
    
    int32_t process_write (process_handle_t handle, const uint8_t* buff, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际写入的字节数。  
handle | process_handle_t | 子进程句柄。  
buff | const uint8_t* | 数据缓冲区。  
max_size | uint32_t | 数据长度。  
  
#### work_dir 属性

* * *

> 子进程当前工作目录。（如果 NULL 的话，就为父进程的工作目录）

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
