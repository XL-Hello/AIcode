## tk_service_t

### 概述

## 服务接口。

### 函数

函数名称 | 说明  
---|---  
tk_service_destroy | 销毁服务对象。  
tk_service_dispatch | 处理服务器请求。  
tk_service_download_file | 处理下载文件。  
tk_service_init | 初始化服务对象(仅供子类使用)。  
tk_service_lock | 加锁。  
tk_service_read_req | 服务端读取请求。  
tk_service_send_resp | 服务端发送响应。  
tk_service_set_retry_times | 设置重试次数。  
tk_service_start | 启动服务。  
tk_service_unlock | 解锁。  
tk_service_upload_file | 处理上传文件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
io | tk_iostream_t* | IO对象。  
wb | wbuffer_t | 用于接收/发送数据打包。  
  
#### tk_service_destroy 函数

* * *

  * 函数功能：



> 销毁服务对象。 服务负责销毁IO对象。

  * 函数原型：


    
    
    ret_t tk_service_destroy (tk_service_t* service);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | 服务对象。  
  
#### tk_service_dispatch 函数

* * *

  * 函数功能：



> 处理服务器请求。 返回非RET_OK，停止服务器，并销毁service对象。

  * 函数原型：


    
    
    ret_t tk_service_dispatch (tk_service_t* service);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | 服务对象。  
  
#### tk_service_download_file 函数

* * *

  * 函数功能：



> 处理下载文件。

  * 函数原型：


    
    
    ret_t tk_service_download_file (tk_service_t* service, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | service对象。  
filename | const char* | 文件名。  
  
#### tk_service_init 函数

* * *

  * 函数功能：



> 初始化服务对象(仅供子类使用)。

  * 函数原型：


    
    
    ret_t tk_service_init (tk_service_t* service, tk_iostream_t* io);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | 服务对象。  
io | tk_iostream_t* | IO对象。  
  
#### tk_service_lock 函数

* * *

  * 函数功能：



> 加锁。

  * 函数原型：


    
    
    ret_t tk_service_lock (tk_service_t* service);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | 服务对象。  
  
#### tk_service_read_req 函数

* * *

  * 函数功能：



> 服务端读取请求。

  * 函数原型：


    
    
    ret_t tk_service_read_req (tk_service_t* service, tk_msg_header_t* header, wbuffer_t* wb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | service对象。  
header | tk_msg_header_t* | 返回消息头。  
wb | wbuffer_t* | 返回对其的数据。  
  
#### tk_service_send_resp 函数

* * *

  * 函数功能：



> 服务端发送响应。

  * 函数原型：


    
    
    ret_t tk_service_send_resp (tk_service_t* service, uint32_t type, uint32_t data_type, uint32_t resp_code, wbuffer_t* wb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | service对象。  
type | uint32_t | 消息类型。  
data_type | uint32_t | 数据类型。  
resp_code | uint32_t | 响应码。  
wb | wbuffer_t* | 要发送的数据。  
  
#### tk_service_set_retry_times 函数

* * *

  * 函数功能：



> 设置重试次数。

  * 函数原型：


    
    
    ret_t tk_service_set_retry_times (tk_service_t* service, uint32_t retry_times);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | service对象。  
retry_times | uint32_t | 重试次数。  
  
#### tk_service_start 函数

* * *

  * 函数功能：



> 启动服务。

  * 函数原型：


    
    
    ret_t tk_service_start (event_source_manager_t* esm, const char* url, tk_service_create_t create, void* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
esm | event_source_manager_t* | 事件源管理器。  
url | const char* | 服务地址。  
create | tk_service_create_t | 创建服务对象的函数。  
args | void* | 参数(对于TCP服务，该参数必须持续有效，使用全局或静态变量)。  
  
#### tk_service_unlock 函数

* * *

  * 函数功能：



> 解锁。

  * 函数原型：


    
    
    ret_t tk_service_unlock (tk_service_t* service);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | 服务对象。  
  
#### tk_service_upload_file 函数

* * *

  * 函数功能：



> 处理上传文件。

  * 函数原型：


    
    
    ret_t tk_service_upload_file (tk_service_t* service, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
service | tk_service_t* | service对象。  
filename | const char* | 文件名。  
  
#### io 属性

* * *

> IO对象。

  * 类型：tk_iostream_t*



#### wb 属性

* * *

> 用于接收/发送数据打包。

  * 类型：wbuffer_t


