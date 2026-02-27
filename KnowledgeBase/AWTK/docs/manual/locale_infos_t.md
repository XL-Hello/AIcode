## locale_infos_t

### 概述

在某些情况下，需要多个资源管理器。比如在手表系统里，每个应用或表盘，可能放在独立的资源包中， 此时优先加载应用自己的资源，如果没有就加载系统的资源。

* * *

### 函数

函数名称 | 说明  
---|---  
locale_infos_change | 设置全部locale_info的当前国家和语言。  
locale_infos_off | 注销指定事件的处理函数。  
locale_infos_on | 注册指定事件的处理函数。  
locale_infos_ref | 获取指定小应用程序(applet)的locale_info。  
locale_infos_reload_all | 重新加载全部字符串资源。  
locale_infos_unref | 释放指定小应用程序(applet)的locale_info。  
  
#### locale_infos_change 函数

* * *

  * 函数功能：



> 设置全部locale_info的当前国家和语言。

  * 函数原型：


    
    
    ret_t locale_infos_change (const char* language, const char* country);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
language | const char* | 语言。  
country | const char* | 国家或地区。  
  
#### locale_infos_off 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t locale_infos_off (uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
id | uint32_t | locale_infos_on返回的ID。  
  
#### locale_infos_on 函数

* * *

  * 函数功能：



> 注册指定事件的处理函数。

  * 函数原型：


    
    
    uint32_t locale_infos_on (event_type_t type, event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于locale_infos_off。  
type | event_type_t | 事件类型，目前有EVT_LOCALE_INFOS_LOAD_INFO、EVT_LOCALE_INFOS_UNLOAD_INFO。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### locale_infos_ref 函数

* * *

  * 函数功能：



> 获取指定小应用程序(applet)的locale_info。

  * 函数原型：


    
    
    locale_info_t* locale_infos_ref (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | locale_info_t* | 返回locale_info对象。  
name | const char* | 小应用程序(applet)的名称。  
  
#### locale_infos_reload_all 函数

* * *

  * 函数功能：



> 重新加载全部字符串资源。

  * 函数原型：


    
    
    ret_t locale_infos_reload_all ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### locale_infos_unref 函数

* * *

  * 函数功能：



> 释放指定小应用程序(applet)的locale_info。

  * 函数原型：


    
    
    ret_t locale_infos_unref (locale_info_t* locale_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。
