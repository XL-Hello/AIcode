## cmd_args_t

### 概述

## 命令行处理。

### 函数

函数名称 | 说明  
---|---  
cmd_args_init | 初始化。  
cmd_args_process | 处理。  
cmd_args_process_str | 处理。  
cmd_args_process_wstr | 处理。  
cmd_args_show_help | 显示帮助信息。  
  
#### cmd_args_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    cmd_args_t* cmd_args_init (cmd_args_t* args, const char* usage, const cmd_arg_desc_t* desc, uint32_t desc_nr, cmd_arg_on_arg_t on_arg, void* on_arg_ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | cmd_args_t* | 返回CMD_ARGS对象。  
args | cmd_args_t* | args对象。  
usage | const char* | 帮助信息。  
desc | const cmd_arg_desc_t* | 参数描述。  
desc_nr | uint32_t | 参数描述个数。  
on_arg | cmd_arg_on_arg_t | 参数处理回调函数。  
on_arg_ctx | void* | 参数处理回调函数的上下文。  
  
#### cmd_args_process 函数

* * *

  * 函数功能：



> 处理。

  * 函数原型：


    
    
    ret_t cmd_args_process (cmd_args_t* args, int argc, char** argv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
args | cmd_args_t* | args对象。  
argc | int | 参数个数。  
argv | char** | 参数数组。  
  
#### cmd_args_process_str 函数

* * *

  * 函数功能：



> 处理。

  * 函数原型：


    
    
    ret_t cmd_args_process_str (cmd_args_t* args, const char* cmd_line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
args | cmd_args_t* | args对象。  
cmd_line | const char* | 字符串格式的参数(适用于Windows)。  
  
#### cmd_args_process_wstr 函数

* * *

  * 函数功能：



> 处理。

  * 函数原型：


    
    
    ret_t cmd_args_process_wstr (cmd_args_t* args, int argc, wchar_t** argv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
args | cmd_args_t* | args对象。  
argc | int | 参数个数。  
argv | wchar_t** | 参数数组。  
  
#### cmd_args_show_help 函数

* * *

  * 函数功能：



> 显示帮助信息。

  * 函数原型：


    
    
    ret_t cmd_args_show_help (cmd_args_t* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
args | cmd_args_t* | args对象。
