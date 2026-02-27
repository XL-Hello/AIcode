## remote_ui_service_args_t

### 概述

## remote ui服务端启动参数。

### 属性

属性名称 | 类型 | 说明  
---|---|---  
auth | tk_service_auth_t | 登陆认证函数。  
find_target | remote_ui_service_find_target_t | 查找target的函数。  
logout | tk_service_logout_t | 登出函数。  
  
#### auth 属性

* * *

> 登陆认证函数。

  * 类型：tk_service_auth_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### find_target 属性

* * *

> 查找target的函数。

  * 类型：remote_ui_service_find_target_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### logout 属性

* * *

> 登出函数。

  * 类型：tk_service_logout_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
