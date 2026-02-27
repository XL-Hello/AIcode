## object_app_conf_t

### 概述

![image](images/object_app_conf_t_0.png)

  * 将用户配置和默认配置包装起来。
  * 优先读取用户配置。
  * 默认配置只读，用户配置可读写。



* * *

### 函数

函数名称 | 说明  
---|---  
object_app_conf_cast | 转换为object_app_conf对象。  
object_app_conf_create | 创建对象。  
  
#### object_app_conf_cast 函数

* * *

  * 函数功能：



> 转换为object_app_conf对象。

  * 函数原型：


    
    
    object_app_conf_t* object_app_conf_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_app_conf_t* | object_app_conf对象。  
obj | tk_object_t* | object_app_conf对象。  
  
#### object_app_conf_create 函数

* * *

  * 函数功能：



> 创建对象。

  * 函数原型：


    
    
    tk_object_t* object_app_conf_create (tk_object_t* user_obj, tk_object_t* default_obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
user_obj | tk_object_t* | 用户配置。  
default_obj | tk_object_t* | 默认配置。
