## log_t

### 概述

## log。

### 函数

函数名称 | 说明  
---|---  
log_debug | 输出调试信息。  
log_error | 输出错误信息。  
log_get_log_level | 获取log的级别。  
log_info | 输出参考信息。  
log_notify | 用于拦截日志，发送给客户端。  
log_set_hook | 设置钩子函数。  
log_set_log_level | 设置log的级别。  
log_warn | 输出警告信息。  
  
#### log_debug 函数

* * *

  * 函数功能：



> 输出调试信息。 变参函数。
    
    
    log_debug("debug message\n");
    

  * 函数原型：


    
    
    void log_debug (const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 无返回值。  
format | const char* | 格式或信息。  
  
#### log_error 函数

* * *

  * 函数功能：



> 输出错误信息。 变参函数。
    
    
    log_error("error message\n");
    

  * 函数原型：


    
    
    void log_error (const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 无返回值。  
format | const char* | 格式或信息。  
  
#### log_get_log_level 函数

* * *

  * 函数功能：



> 获取log的级别。

  * 函数原型：


    
    
    tk_log_level_t log_get_log_level ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_log_level_t | 返回log的级别。  
  
#### log_info 函数

* * *

  * 函数功能：



> 输出参考信息。 变参函数。
    
    
    log_info("info message\n");
    

  * 函数原型：


    
    
    void log_info (const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 无返回值。  
format | const char* | 格式或信息。  
  
#### log_notify 函数

* * *

  * 函数功能：



> 用于拦截日志，发送给客户端。 变参函数。

  * 函数原型：


    
    
    ret_t log_notify (tk_log_level_t level, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
level | tk_log_level_t | 级别。  
format | const char* | 格式或信息。  
  
#### log_set_hook 函数

* * *

  * 函数功能：



> 设置钩子函数。

  * 函数原型：


    
    
    ret_t log_set_hook (tk_log_hook_t log, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
log | tk_log_hook_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### log_set_log_level 函数

* * *

  * 函数功能：



> 设置log的级别。

  * 函数原型：


    
    
    ret_t log_set_log_level (tk_log_level_t log_level);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
log_level | tk_log_level_t | log的级别。  
  
#### log_warn 函数

* * *

  * 函数功能：



> 输出警告信息。 变参函数。
    
    
    log_warn("warn message\n");
    

  * 函数原型：


    
    
    void log_warn (const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 无返回值。  
format | const char* | 格式或信息。
