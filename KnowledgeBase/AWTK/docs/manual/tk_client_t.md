## tk_client_t

### 概述

## 客户端接口。

### 函数

函数名称 | 说明  
---|---  
tk_client_deinit | 释放资源(仅供子类使用)。  
tk_client_download_file | 客户端下载文件。  
tk_client_init | 初始化(仅供子类使用)。  
tk_client_read_notify | 客户端读取通知。  
tk_client_read_resp | 客户端读取响应。  
tk_client_request | 客户端发送请求，并读取响应。  
tk_client_send_req | 客户端发送请求。  
tk_client_set_retry_times | 设置重试次数。  
tk_client_set_timeout_ms | 设置超时时间。  
tk_client_upload_file | 客户端上传文件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
io | tk_iostream_t* | IO对象。  
wb | wbuffer_t | 用于接收/发送数据打包。  
  
#### tk_client_deinit 函数

* * *

  * 函数功能：



> 释放资源(仅供子类使用)。

  * 函数原型：


    
    
    ret_t tk_client_deinit (tk_client_t* client);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | 服务对象。  
  
#### tk_client_download_file 函数

* * *

  * 函数功能：



> 客户端下载文件。

  * 函数原型：


    
    
    ret_t tk_client_download_file (tk_client_t* client, const char* remote_file, const char* local_file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
remote_file | const char* | 远程文件。  
local_file | const char* | 本地文件。  
  
#### tk_client_init 函数

* * *

  * 函数功能：



> 初始化(仅供子类使用)。

  * 函数原型：


    
    
    ret_t tk_client_init (tk_client_t* client, tk_iostream_t* io, tk_client_on_notify_t on_notify);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | 服务对象。  
io | tk_iostream_t* | io对象。  
on_notify | tk_client_on_notify_t | 通知回调。  
  
#### tk_client_read_notify 函数

* * *

  * 函数功能：



> 客户端读取通知。

  * 函数原型：


    
    
    ret_t tk_client_read_notify (tk_client_t* client, uint32_t timeout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
timeout | uint32_t | 超时时间(毫秒)。  
  
#### tk_client_read_resp 函数

* * *

  * 函数功能：



> 客户端读取响应。

  * 函数原型：


    
    
    ret_t tk_client_read_resp (tk_client_t* client, tk_msg_header_t* header, wbuffer_t* wb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
header | tk_msg_header_t* | 返回消息头。  
wb | wbuffer_t* | 返回读取的数据。  
  
#### tk_client_request 函数

* * *

  * 函数功能：



> 客户端发送请求，并读取响应。

  * 函数原型：


    
    
    ret_t tk_client_request (tk_client_t* client, uint32_t type, uint32_t data_type, wbuffer_t* wb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
type | uint32_t | 消息类型。  
data_type | uint32_t | 数据类型。  
wb | wbuffer_t* | 要发送的数据/返回读取的数据。  
  
#### tk_client_send_req 函数

* * *

  * 函数功能：



> 客户端发送请求。

  * 函数原型：


    
    
    ret_t tk_client_send_req (tk_client_t* client, uint32_t type, uint32_t data_type, wbuffer_t* wb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
type | uint32_t | 消息类型。  
data_type | uint32_t | 数据类型。  
wb | wbuffer_t* | 要发送的数据。  
  
#### tk_client_set_retry_times 函数

* * *

  * 函数功能：



> 设置重试次数。

  * 函数原型：


    
    
    ret_t tk_client_set_retry_times (tk_client_t* client, uint32_t retry_times);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
retry_times | uint32_t | 重试次数。  
  
#### tk_client_set_timeout_ms 函数

* * *

  * 函数功能：



> 设置超时时间。

  * 函数原型：


    
    
    ret_t tk_client_set_timeout_ms (tk_client_t* client, uint32_t wtimeout_ms, uint32_t rtimeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
wtimeout_ms | uint32_t | 读数据超时时间。  
rtimeout_ms | uint32_t | 写数据超时时间。  
  
#### tk_client_upload_file 函数

* * *

  * 函数功能：



> 客户端上传文件。

  * 函数原型：


    
    
    ret_t tk_client_upload_file (tk_client_t* client, const char* remote_file, const char* local_file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
client | tk_client_t* | client对象。  
remote_file | const char* | 远程文件。  
local_file | const char* | 本地文件。  
  
#### io 属性

* * *

> IO对象。

  * 类型：tk_iostream_t*



#### wb 属性

* * *

> 用于接收/发送数据打包。

  * 类型：wbuffer_t


