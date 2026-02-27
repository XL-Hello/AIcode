## tk_iostream_process_t

### 概述

![image](images/tk_iostream_process_t_0.png)

基于子程序实现的输入流。 备注：如果需要在 Windows 平台运行，请在应用程序初始化时，调用 tk_socket_init 函数初始化 socket。

* * *

### 函数

函数名称 | 说明  
---|---  
tk_iostream_process_create | 创建iostream对象。  
tk_iostream_process_kill | 杀死子进程流。  
tk_iostream_process_set_work_dir | 设置子进程流工作目录。  
tk_iostream_process_start | 启动子进程流。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
argc | uint32_t | 参数列表长度。  
args | const char** | 参数列表。  
file_path | char* | 子进程路径。  
  
#### tk_iostream_process_create 函数

* * *

  * 函数功能：



> 创建iostream对象。 备注：如果需要在 Windows 平台运行，请在应用程序初始化时，调用 tk_socket_init 函数初始化 socket。

  * 函数原型：


    
    
    tk_iostream_t* tk_iostream_process_create (const char* file_path, const char** args, uint32_t argc);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_iostream_t* | 返回iostream对象。  
file_path | const char* | 子进程程序路径。(如果为空的话，使用命令行来执行参数)  
args | const char** | 子进程参数。  
argc | uint32_t | 子进程参数长度。  
  
#### tk_iostream_process_kill 函数

* * *

  * 函数功能：



> 杀死子进程流。

  * 函数原型：


    
    
    ret_t tk_iostream_process_kill (tk_iostream_t* iostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
iostream | tk_iostream_t* | 子程序对象。  
  
#### tk_iostream_process_set_work_dir 函数

* * *

  * 函数功能：



> 设置子进程流工作目录。

  * 函数原型：


    
    
    ret_t tk_iostream_process_set_work_dir (tk_iostream_t* iostream, const char* work_dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
iostream | tk_iostream_t* | 子程序对象。  
work_dir | const char* | 工作目录。  
  
#### tk_iostream_process_start 函数

* * *

  * 函数功能：



> 启动子进程流。

  * 函数原型：


    
    
    ret_t tk_iostream_process_start (tk_iostream_t* iostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
iostream | tk_iostream_t* | 子程序对象。  
  
#### argc 属性

* * *

> 参数列表长度。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### args 属性

* * *

> 参数列表。

  * 类型：const char**

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### file_path 属性

* * *

> 子进程路径。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
