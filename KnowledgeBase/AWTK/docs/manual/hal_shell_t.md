## hal_shell_t

### 概述

## a shell to access network interface

### 函数

函数名称 | 说明  
---|---  
network_shell_run | 运行shell。  
  
#### network_shell_run 函数

* * *

  * 函数功能：



> 运行shell。

  * 函数原型：


    
    
    ret_t network_shell_run (network_interface_t* network_interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
network_interface | network_interface_t* | 网口对象。
