## debugger_global_t

### 概述

@annotaion [“fake”] 调试器全局函数。

* * *

### 函数

函数名称 | 说明  
---|---  
debugger_global_deinit | 禁用调试器。  
debugger_global_init | 启用调试器。  
  
#### debugger_global_deinit 函数

* * *

  * 函数功能：



> 禁用调试器。

  * 函数原型：


    
    
    ret_t debugger_global_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### debugger_global_init 函数

* * *

  * 函数功能：



> 启用调试器。

  * 函数原型：


    
    
    ret_t debugger_global_init ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。
