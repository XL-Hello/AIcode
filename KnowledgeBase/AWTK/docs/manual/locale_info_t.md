## locale_info_t

### 概述

## 本地化信息。提供字符串翻译数据管理，当前语言改变的事件通知等等。

### 函数

函数名称 | 说明  
---|---  
locale_info | 获取缺省locale_info。  
locale_info_change | 设置当前的国家和语言。  
locale_info_create | 创建locale_info。  
locale_info_create_ex | 创建locale_info。  
locale_info_destroy | 释放全部资源并销毁locale_info对象。  
locale_info_off | 注销指定事件的处理函数。  
locale_info_on | 注册指定事件的处理函数。  
locale_info_reload | 重新加载字符串资源。  
locale_info_set | 设置缺省locale_info。  
locale_info_set_assets_manager | 设置资源管理器对象。  
locale_info_set_custom_tr | 设置自定义的候补翻译函数。  
locale_info_set_fallback_tr | 设置候补翻译函数。  
locale_info_set_fallback_tr2 | 设置候补翻译函数。  
locale_info_tr | 翻译字符串。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
country | char* | 国家或地区。如：CN  
language | char* | 语言。如：zh  
  
#### locale_info 函数

* * *

  * 函数功能：



> 获取缺省locale_info。

  * 函数原型：


    
    
    locale_info_t* locale_info ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | locale_info_t* | 返回locale_info对象。  
  
#### locale_info_change 函数

* * *

  * 函数功能：



> 设置当前的国家和语言。

  * 函数原型：


    
    
    ret_t locale_info_change (locale_info_t* locale_info, const char* language, const char* country);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
language | const char* | 语言。  
country | const char* | 国家或地区。  
  
#### locale_info_create 函数

* * *

  * 函数功能：



> 创建locale_info。

  * 函数原型：


    
    
    locale_info_t* locale_info_create (const char* language, const char* country);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | locale_info_t* | 返回locale_info对象。  
language | const char* | 语言。  
country | const char* | 国家或地区。  
  
#### locale_info_create_ex 函数

* * *

  * 函数功能：



> 创建locale_info。

  * 函数原型：


    
    
    locale_info_t* locale_info_create_ex (const char* language, const char* country, assets_manager_t* am);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | locale_info_t* | 返回locale_info对象。  
language | const char* | 语言。  
country | const char* | 国家或地区。  
am | assets_manager_t* | 资源管理器。  
  
#### locale_info_destroy 函数

* * *

  * 函数功能：



> 释放全部资源并销毁locale_info对象。

  * 函数原型：


    
    
    ret_t locale_info_destroy (locale_info_t* locale_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
  
#### locale_info_off 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t locale_info_off (locale_info_t* locale_info, uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
id | uint32_t | locale_info_on返回的ID。  
  
#### locale_info_on 函数

* * *

  * 函数功能：



> 注册指定事件的处理函数。

  * 函数原型：


    
    
    uint32_t locale_info_on (locale_info_t* locale_info, event_type_t type, event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于locale_info_off。  
locale_info | locale_info_t* | locale_info对象。  
type | event_type_t | 事件类型，目前固定为EVT_LOCALE_CHANGED。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### locale_info_reload 函数

* * *

  * 函数功能：



> 重新加载字符串资源。

  * 函数原型：


    
    
    ret_t locale_info_reload (locale_info_t* locale_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
  
#### locale_info_set 函数

* * *

  * 函数功能：



> 设置缺省locale_info。

  * 函数原型：


    
    
    ret_t locale_info_set (locale_info_t* locale_info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
  
#### locale_info_set_assets_manager 函数

* * *

  * 函数功能：



> 设置资源管理器对象。

  * 函数原型：


    
    
    ret_t locale_info_set_assets_manager (locale_info_t* locale_info, assets_manager_t* assets_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
assets_manager | assets_manager_t* | 资源管理器。  
  
#### locale_info_set_custom_tr 函数

* * *

  * 函数功能：



> 设置自定义的候补翻译函数。 有时我们需要优先加载用户自定义的翻译，加载失败才加载系统缺省的，可用设置一个函数去实现这类功能。

  * 函数原型：


    
    
    ret_t locale_info_set_custom_tr (locale_info_t* locale_info, locale_info_tr_with_context_t tr, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
tr | locale_info_tr_with_context_t | 自定义的翻译函数。  
ctx | void* | 翻译函数的上下文。  
  
#### locale_info_set_fallback_tr 函数

* * *

  * 函数功能：



> 设置候补翻译函数。

  * 函数原型：


    
    
    ret_t locale_info_set_fallback_tr (locale_info_t* locale_info, locale_info_tr_t tr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
tr | locale_info_tr_t | fallback翻译函数。  
  
#### locale_info_set_fallback_tr2 函数

* * *

  * 函数功能：



> 设置候补翻译函数。

  * 函数原型：


    
    
    ret_t locale_info_set_fallback_tr2 (locale_info_t* locale_info, locale_info_tr_with_context_t tr, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
locale_info | locale_info_t* | locale_info对象。  
tr | locale_info_tr_with_context_t | fallback翻译函数。  
ctx | void* | 翻译函数的上下文。  
  
#### locale_info_tr 函数

* * *

  * 函数功能：



> 翻译字符串。

  * 函数原型：


    
    
    const char* locale_info_tr (locale_info_t* locale_info, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回翻译之后的字符串。  
locale_info | locale_info_t* | locale_info对象。  
text | const char* | 待翻译的文本。  
  
#### country 属性

* * *

> 国家或地区。如：CN

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### language 属性

* * *

> 语言。如：zh

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
