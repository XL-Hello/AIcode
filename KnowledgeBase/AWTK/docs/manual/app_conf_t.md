## app_conf_t

### 概述

应用程序的配置信息。

底层实现可以是任何格式，比如INI，XML，JSON和UBJSON。

对于树状的文档，key可以是多级的，用.分隔。如network.ip。

conf-io是可选组件，需要自己包含头文件，否则64位数据类型会被截断成32位的数据。
    
    
    #include "conf_io/app_conf.h"
    

* * *

### 函数

函数名称 | 说明  
---|---  
app_conf_deinit | 释放conf对象。  
app_conf_exist | 检查配置项是否存在。  
app_conf_get | 获取配置项的值。  
app_conf_get_bool | 获取bool类型配置项的值。  
app_conf_get_double | 获取单精度浮点数类型配置项的值。  
app_conf_get_instance | 获取app_conf实例。  
app_conf_get_int | 获取整数类型配置项的值。  
app_conf_get_int64 | 获取64位整数类型配置项的值。  
app_conf_get_str | 获取字符串类型配置项的值。  
app_conf_get_wstr | 获取宽字符串类型配置项的值。  
app_conf_off_changed | 注销配置变化事件。  
app_conf_off_changed_by_ctx | 注销配置变化事件。  
app_conf_on_changed | 注册配置变化事件。  
app_conf_reload | 重新加载配置(内存中的配置丢失)。  
app_conf_remove | 删除配置项。  
app_conf_save | 持久保存配置。  
app_conf_set | 设置配置项的值。  
app_conf_set_bool | 设置bool类型配置项的值。  
app_conf_set_double | 设置双精度类型配置项的值。  
app_conf_set_instance | 设置app_conf实例。  
app_conf_set_int | 设置整数类型配置项的值。  
app_conf_set_int64 | 设置64位整数类型配置项的值。  
app_conf_set_str | 设置字符串类型配置项的值。  
app_conf_set_wstr | 设置宽字符串类型配置项的值。  
  
#### app_conf_deinit 函数

* * *

  * 函数功能：



> 释放conf对象。

  * 函数原型：


    
    
    ret_t app_conf_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### app_conf_exist 函数

* * *

  * 函数功能：



> 检查配置项是否存在。

  * 函数原型：


    
    
    bool_t app_conf_exist (const char* key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，FALSE表示不存在。  
key | const char* | 配置项的名称。  
  
#### app_conf_get 函数

* * *

  * 函数功能：



> 获取配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_get (const char* key, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | value_t* | 配置项的值(用于返回)。  
  
#### app_conf_get_bool 函数

* * *

  * 函数功能：



> 获取bool类型配置项的值。

  * 函数原型：


    
    
    bool_t app_conf_get_bool (const char* key, bool_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回配置项的值（如果不存在返回缺省值）。  
key | const char* | 配置项的名称。  
defval | bool_t | 缺省值。  
  
#### app_conf_get_double 函数

* * *

  * 函数功能：



> 获取单精度浮点数类型配置项的值。

  * 函数原型：


    
    
    double app_conf_get_double (const char* key, double defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回配置项的值（如果不存在返回缺省值）。  
key | const char* | 配置项的名称。  
defval | double | 缺省值。  
  
#### app_conf_get_instance 函数

* * *

  * 函数功能：



> 获取app_conf实例。

  * 函数原型：


    
    
    tk_object_t* app_conf_get_instance ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回app_conf实例。  
  
#### app_conf_get_int 函数

* * *

  * 函数功能：



> 获取整数类型配置项的值。

  * 函数原型：


    
    
    int32_t app_conf_get_int (const char* key, int32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回配置项的值（如果不存在返回缺省值）。  
key | const char* | 配置项的名称。  
defval | int32_t | 缺省值。  
  
#### app_conf_get_int64 函数

* * *

  * 函数功能：



> 获取64位整数类型配置项的值。

  * 函数原型：


    
    
    int64_t app_conf_get_int64 (const char* key, int64_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回配置项的值（如果不存在返回缺省值）。  
key | const char* | 配置项的名称。  
defval | int64_t | 缺省值。  
  
#### app_conf_get_str 函数

* * *

  * 函数功能：



> 获取字符串类型配置项的值。

  * 函数原型：


    
    
    const char* app_conf_get_str (const char* key, const char* defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回配置项的值（如果不存在返回缺省值）。  
key | const char* | 配置项的名称。  
defval | const char* | 缺省值。  
  
#### app_conf_get_wstr 函数

* * *

  * 函数功能：



> 获取宽字符串类型配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_get_wstr (const char* key, wchar_t* str, uint32_t max_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
str | wchar_t* | 返回值。  
max_size | uint32_t | 最大长度(字符数)。  
  
#### app_conf_off_changed 函数

* * *

  * 函数功能：



> 注销配置变化事件。

  * 函数原型：


    
    
    ret_t app_conf_off_changed (uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
id | uint32_t | app_conf_on_changed返回的ID。  
  
#### app_conf_off_changed_by_ctx 函数

* * *

  * 函数功能：



> 注销配置变化事件。

  * 函数原型：


    
    
    ret_t app_conf_off_changed_by_ctx (void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ctx | void* | 事件处理函数上下文。  
  
#### app_conf_on_changed 函数

* * *

  * 函数功能：



> 注册配置变化事件。

  * 函数原型：


    
    
    uint32_t app_conf_on_changed (event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于app_conf_off_changed。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### app_conf_reload 函数

* * *

  * 函数功能：



> 重新加载配置(内存中的配置丢失)。

  * 函数原型：


    
    
    ret_t app_conf_reload ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### app_conf_remove 函数

* * *

  * 函数功能：



> 删除配置项。

  * 函数原型：


    
    
    ret_t app_conf_remove (const char* key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
  
#### app_conf_save 函数

* * *

  * 函数功能：



> 持久保存配置。

  * 函数原型：


    
    
    ret_t app_conf_save ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### app_conf_set 函数

* * *

  * 函数功能：



> 设置配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_set (const char* key, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | const value_t* | 配置项的值。  
  
#### app_conf_set_bool 函数

* * *

  * 函数功能：



> 设置bool类型配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_set_bool (const char* key, bool_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | bool_t | 配置项的值。  
  
#### app_conf_set_double 函数

* * *

  * 函数功能：



> 设置双精度类型配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_set_double (const char* key, double v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | double | 配置项的值。  
  
#### app_conf_set_instance 函数

* * *

  * 函数功能：



> 设置app_conf实例。

  * 函数原型：


    
    
    ret_t app_conf_set_instance (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 配置对象。由app_conf_deinit释放。  
  
#### app_conf_set_int 函数

* * *

  * 函数功能：



> 设置整数类型配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_set_int (const char* key, int32_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | int32_t | 配置项的值。  
  
#### app_conf_set_int64 函数

* * *

  * 函数功能：



> 设置64位整数类型配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_set_int64 (const char* key, int64_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | int64_t | 配置项的值。  
  
#### app_conf_set_str 函数

* * *

  * 函数功能：



> 设置字符串类型配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_set_str (const char* key, const char* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | const char* | 配置项的值。  
  
#### app_conf_set_wstr 函数

* * *

  * 函数功能：



> 设置宽字符串类型配置项的值。

  * 函数原型：


    
    
    ret_t app_conf_set_wstr (const char* key, const wchar_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
key | const char* | 配置项的名称。  
v | const wchar_t* | 配置项的值。
