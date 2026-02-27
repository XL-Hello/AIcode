## remote_ui_service_t

### 概述

## remote ui服务端。

### 函数

函数名称 | 说明  
---|---  
remote_ui_service_create | 创建remote ui服务端。  
remote_ui_service_hook_log | 是否hook log。  
remote_ui_service_start_with_uart | 启动基于串口的Remote UI服务。  
  
#### remote_ui_service_create 函数

* * *

  * 函数功能：



> 创建remote ui服务端。

  * 函数原型：


    
    
    tk_service_t* remote_ui_service_create (tk_iostream_t* io, void* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_service_t* | 返回service对象。  
io | tk_iostream_t* | IO流(由service释放)。  
args | void* | 参数。  
  
#### remote_ui_service_hook_log 函数

* * *

  * 函数功能：



> 是否hook log。

  * 函数原型：


    
    
    ret_t remote_ui_service_hook_log (remote_ui_service_t* ui, bool_t hook);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui | remote_ui_service_t* | remote ui服务端。  
hook | bool_t | 是否hook log。  
  
#### remote_ui_service_start_with_uart 函数

* * *

  * 函数功能：



> 启动基于串口的Remote UI服务。 在很多RTOS上，没有select，所以通过timer定时检查串口是否有数据。

  * 函数原型：


    
    
    tk_service_t* remote_ui_service_start_with_uart (tk_iostream_t* io, void* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_service_t* | 返回service对象。  
io | tk_iostream_t* | IO流(由service释放)。  
args | void* | 参数。
