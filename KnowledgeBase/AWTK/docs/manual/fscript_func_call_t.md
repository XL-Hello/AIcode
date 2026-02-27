## fscript_func_call_t

### 概述

## 函数描述。

### 函数

函数名称 | 说明  
---|---  
fscript_ensure_locals | export for debugger  
fscript_exec_func_default | 执行函数的默认实现。  
fscript_find_event | 查找事件。  
fscript_find_func | 查找函数。  
fscript_get_code_id | 获取code_id。  
fscript_set_hooks | 设置回调函数。  
fscript_set_self_hooks | 设置 fscript 对象的回调函数。  
fscript_set_var_default | 设置变量的默认实现。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
col | uint16_t | 对应源代码列号。  
ctx | void* | 函数需要的上下文。  
func | fscript_func_t | 函数指针。  
row | uint16_t | 对应源代码行号。  
  
#### fscript_ensure_locals 函数

* * *

  * 函数功能：



> export for debugger

  * 函数原型：


    
    
    ret_t fscript_ensure_locals (fscript_t* fscript);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
  
#### fscript_exec_func_default 函数

* * *

  * 函数功能：



> 执行函数的默认实现。

  * 函数原型：


    
    
    ret_t fscript_exec_func_default (fscript_t* fscript, fscript_func_call_t* iter, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
iter | fscript_func_call_t* | 当前函数。  
result | value_t* | 返回结果。  
  
#### fscript_find_event 函数

* * *

  * 函数功能：



> 查找事件。

  * 函数原型：


    
    
    uint32_t fscript_find_event (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回事件的值。  
name | const char* | 事件名。  
  
#### fscript_find_func 函数

* * *

  * 函数功能：



> 查找函数。

  * 函数原型：


    
    
    fscript_func_t fscript_find_func (fscript_t* fscript, const char* name, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fscript_func_t | 返回函数指针，NULL表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
name | const char* | 函数名。  
size | uint32_t | 函数名长度。  
  
#### fscript_get_code_id 函数

* * *

  * 函数功能：



> 获取code_id。

  * 函数原型：


    
    
    char* fscript_get_code_id (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回code_id，有调用者释放返回的字符串。  
str | const char* | 代码。  
  
#### fscript_set_hooks 函数

* * *

  * 函数功能：



> 设置回调函数。

  * 函数原型：


    
    
    ret_t fscript_set_hooks (const fscript_hooks_t* hooks);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hooks | const fscript_hooks_t* | 回调函数。  
  
#### fscript_set_self_hooks 函数

* * *

  * 函数功能：



> 设置 fscript 对象的回调函数。

  * 函数原型：


    
    
    ret_t fscript_set_self_hooks (fscript_t* fscript, const fscript_hooks_t* hooks);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | fscript 对象。  
hooks | const fscript_hooks_t* | 回调函数。  
  
#### fscript_set_var_default 函数

* * *

  * 函数功能：



> 设置变量的默认实现。

  * 函数原型：


    
    
    ret_t fscript_set_var_default (fscript_t* fscript, const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
name | const char* | 变量名。  
value | const value_t* | 值。  
  
#### col 属性

* * *

> 对应源代码列号。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### ctx 属性

* * *

> 函数需要的上下文。 目前主要保持自定义函数的实现。

  * 类型：void*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### func 属性

* * *

> 函数指针。

  * 类型：fscript_func_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### row 属性

* * *

> 对应源代码行号。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
