## url_t

### 概述

## URL

### 函数

函数名称 | 说明  
---|---  
url_create | 创建URL对象。  
url_destroy | 销毁url对象。  
url_get_param | 获取参数。  
url_get_param_bool | 获取参数。  
url_get_param_int32 | 获取参数。  
url_set_host | 设置主机名。  
url_set_param | 设置参数。  
url_set_password | 设置密码。  
url_set_path | 设置路径。  
url_set_port | 设置端口。  
url_set_schema | 设置schema。  
url_set_user_name | 设置用户名。  
url_to_string | 格式化成字符串。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
host | char* | 主机名。  
params | tk_object_t* | 参数集合。  
password | char* | 密码。  
path | char* | 路径。  
port | int32_t | 端口。  
schema | char* | schema。  
user_name | char* | 用户名。  
  
#### url_create 函数

* * *

  * 函数功能：



> 创建URL对象。

  * 函数原型：


    
    
    url_t* url_create (const char* surl);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | url_t* | 返回URL对象。  
surl | const char* | 字符串格式的URL。  
  
#### url_destroy 函数

* * *

  * 函数功能：



> 销毁url对象。

  * 函数原型：


    
    
    ret_t url_destroy (url_t* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
  
#### url_get_param 函数

* * *

  * 函数功能：



> 获取参数。

  * 函数原型：


    
    
    const char* url_get_param (url_t* url, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回指定参数名的参数值。  
url | url_t* | url对象。  
name | const char* | 参数名。  
  
#### url_get_param_bool 函数

* * *

  * 函数功能：



> 获取参数。

  * 函数原型：


    
    
    bool_t url_get_param_bool (url_t* url, const char* name, bool_t defvalue);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回指定参数名的参数值。  
url | url_t* | url对象。  
name | const char* | 参数名。  
defvalue | bool_t | 默认值。  
  
#### url_get_param_int32 函数

* * *

  * 函数功能：



> 获取参数。

  * 函数原型：


    
    
    int32_t url_get_param_int32 (url_t* url, const char* name, int32_t defvalue);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回指定参数名的参数值。  
url | url_t* | url对象。  
name | const char* | 参数名。  
defvalue | int32_t | 默认值。  
  
#### url_set_host 函数

* * *

  * 函数功能：



> 设置主机名。

  * 函数原型：


    
    
    ret_t url_set_host (url_t* url, const char* host);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
host | const char* | 主机名。  
  
#### url_set_param 函数

* * *

  * 函数功能：



> 设置参数。

  * 函数原型：


    
    
    ret_t url_set_param (url_t* url, const char* name, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
name | const char* | 参数名。  
value | const char* | 参数值。  
  
#### url_set_password 函数

* * *

  * 函数功能：



> 设置密码。

  * 函数原型：


    
    
    ret_t url_set_password (url_t* url, const char* password);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
password | const char* | 密码。  
  
#### url_set_path 函数

* * *

  * 函数功能：



> 设置路径。

  * 函数原型：


    
    
    ret_t url_set_path (url_t* url, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
path | const char* | 路径。  
  
#### url_set_port 函数

* * *

  * 函数功能：



> 设置端口。

  * 函数原型：


    
    
    ret_t url_set_port (url_t* url, int32_t port);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
port | int32_t | 端口。  
  
#### url_set_schema 函数

* * *

  * 函数功能：



> 设置schema。

  * 函数原型：


    
    
    ret_t url_set_schema (url_t* url, const char* schema);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
schema | const char* | schema。  
  
#### url_set_user_name 函数

* * *

  * 函数功能：



> 设置用户名。

  * 函数原型：


    
    
    ret_t url_set_user_name (url_t* url, const char* user_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
url | url_t* | url对象。  
user_name | const char* | 用户名。  
  
#### url_to_string 函数

* * *

  * 函数功能：



> 格式化成字符串。
> 
> 返回的字符串在URL对象销毁或下一次调用本函数时失效。

  * 函数原型：


    
    
    const char* url_to_string (url_t* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回字符串格式的URL。  
url | url_t* | url对象。  
  
#### host 属性

* * *

> 主机名。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### params 属性

* * *

> 参数集合。

  * 类型：tk_object_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### password 属性

* * *

> 密码。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### path 属性

* * *

> 路径。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### port 属性

* * *

> 端口。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### schema 属性

* * *

> schema。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### user_name 属性

* * *

> 用户名。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
