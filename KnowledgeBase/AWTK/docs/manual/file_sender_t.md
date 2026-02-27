## file_sender_t

### 概述

文件发送方。

## > 可用注册EVT_PROGRESS事件，以获取传输的进度状态。

### 函数

函数名称 | 说明  
---|---  
file_sender_create | 创建sender对象。  
file_sender_destroy | 销毁sender对象。  
file_sender_run | 开始传输文件。  
  
#### file_sender_create 函数

* * *

  * 函数功能：



> 创建sender对象。

  * 函数原型：


    
    
    file_sender_t* file_sender_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | file_sender_t* | 返回sender对象。  
  
#### file_sender_destroy 函数

* * *

  * 函数功能：



> 销毁sender对象。

  * 函数原型：


    
    
    ret_t file_sender_destroy (file_sender_t* sender);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sender | file_sender_t* | sender对象。  
  
#### file_sender_run 函数

* * *

  * 函数功能：



> 开始传输文件。

  * 函数原型：


    
    
    ret_t file_sender_run (file_sender_t* sender, tk_iostream_t* io, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sender | file_sender_t* | sender对象。  
io | tk_iostream_t* | 数据传输流。  
filename | const char* | 文件名。
