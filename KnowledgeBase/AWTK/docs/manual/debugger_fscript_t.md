## debugger_fscript_t

### 概述

## fscript调试器

### 函数

函数名称 | 说明  
---|---  
debugger_fscript_cast | 类型转换。  
debugger_fscript_create | 创建调试器对象。  
debugger_fscript_get_start_line | 获取第一行被执行的代码的行号。  
debugger_fscript_set_code | 设置代码。  
debugger_fscript_set_fscript | 设置fscript对象。  
  
#### debugger_fscript_cast 函数

* * *

  * 函数功能：



> 类型转换。

  * 函数原型：


    
    
    debugger_fscript_t* debugger_fscript_cast (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_fscript_t* | 返回debugger对象。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_fscript_create 函数

* * *

  * 函数功能：



> 创建调试器对象。

  * 函数原型：


    
    
    debugger_t* debugger_fscript_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_t* | 返回debugger对象。  
  
#### debugger_fscript_get_start_line 函数

* * *

  * 函数功能：



> 获取第一行被执行的代码的行号。

  * 函数原型：


    
    
    int32_t debugger_fscript_get_start_line (fscript_t* fscript);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回行号。  
fscript | fscript_t* | fscript对象。  
  
#### debugger_fscript_set_code 函数

* * *

  * 函数功能：



> 设置代码。

  * 函数原型：


    
    
    ret_t debugger_fscript_set_code (debugger_t* debugger, const binary_data_t* code, bool_t changed);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
code | const binary_data_t* | 代码。  
changed | bool_t | 是否重新加载。  
  
#### debugger_fscript_set_fscript 函数

* * *

  * 函数功能：



> 设置fscript对象。

  * 函数原型：


    
    
    ret_t debugger_fscript_set_fscript (debugger_t* debugger, fscript_t* fscript);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
fscript | fscript_t* | 脚本对象。
