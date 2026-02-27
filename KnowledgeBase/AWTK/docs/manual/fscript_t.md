## fscript_t

### 概述

一个简易的函数式脚本引擎。 用法请参考：https://github.com/zlgopen/awtk/blob/master/docs/fscript.md

* * *

### 函数

函数名称 | 说明  
---|---  
fscript_clean | 使用lua或其它脚本来运行fscript时，本函数用于清理不必要的数据结构。  
fscript_create | 创建引擎对象，并解析代码。  
fscript_create_ex | 创建引擎对象，并解析代码。  
fscript_deinit | 清除引擎对象的数据。  
fscript_destroy | 销毁引擎对象。  
fscript_eval | 执行一段脚本。  
fscript_exec | 执行解析后的代码。  
fscript_get_global_object | 获取fscript的全局对象。  
fscript_global_deinit | 全局释放。  
fscript_global_init | 全局初始化。  
fscript_init | 初始化引擎对象，并解析代码。  
fscript_register_const_double | 注册浮点数常量。  
fscript_register_const_int | 注册整数常量。  
fscript_register_const_value | 注册常量。  
fscript_register_event | 注册自定义事件。  
fscript_register_func | 注册全局自定义函数。  
fscript_register_funcs | 注册全局自定义函数。  
fscript_reload | 重新加载代码。  
fscript_set_error | 用于扩展函数设置遇到的错误。  
fscript_set_global_object | 用于替换默认的全局对象。  
fscript_set_on_error | 设置错误处理函数。  
fscript_set_print_func | 设置打印日志的函数。  
fscript_syntax_check | 解析代码，分析是否有语法错误。  
tk_expr_eval | 对fscript的简单包装。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
error_code | ret_t | 运行时错误码。  
error_col | int32_t | 运行时错误的列号。  
error_message | char* | 运行时错误信息。  
error_row | int32_t | 运行时错误的行号。  
lines | uint16_t | 代码总行数。  
obj | tk_object_t* | 脚本执行上下文。  
str | str_t | C语言实现函数可以使用这个变量，可以有效避免内存分配。  
  
#### fscript_clean 函数

* * *

  * 函数功能：



> 使用lua或其它脚本来运行fscript时，本函数用于清理不必要的数据结构。

  * 函数原型：


    
    
    ret_t fscript_clean (fscript_t* fscript);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
  
#### fscript_create 函数

* * *

  * 函数功能：



> 创建引擎对象，并解析代码。

  * 函数原型：


    
    
    fscript_t* fscript_create (tk_object_t* obj, const char* script);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fscript_t* | 返回fscript对象。  
obj | tk_object_t* | 脚本执行上下文。  
script | const char* | 脚本代码。  
  
#### fscript_create_ex 函数

* * *

  * 函数功能：



> 创建引擎对象，并解析代码。

  * 函数原型：


    
    
    fscript_t* fscript_create_ex (tk_object_t* obj, const char* script, bool_t keep_func_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fscript_t* | 返回fscript对象。  
obj | tk_object_t* | 脚本执行上下文。  
script | const char* | 脚本代码。  
keep_func_name | bool_t | 是否在func_call结构后保存函数名。  
  
#### fscript_deinit 函数

* * *

  * 函数功能：



> 清除引擎对象的数据。

  * 函数原型：


    
    
    ret_t fscript_deinit (fscript_t* fscript);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
  
#### fscript_destroy 函数

* * *

  * 函数功能：



> 销毁引擎对象。

  * 函数原型：


    
    
    ret_t fscript_destroy (fscript_t* fscript);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
  
#### fscript_eval 函数

* * *

  * 函数功能：



> 执行一段脚本。

  * 函数原型：


    
    
    ret_t fscript_eval (tk_object_t* obj, const char* script, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 脚本执行上下文。  
script | const char* | 脚本代码。  
result | value_t* | 执行结果(调用者需要用value_reset函数清除result)。  
  
#### fscript_exec 函数

* * *

  * 函数功能：



> 执行解析后的代码。

  * 函数原型：


    
    
    ret_t fscript_exec (fscript_t* fscript, value_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
result | value_t* | 执行结果(调用者需要用value_reset函数清除result)。  
  
#### fscript_get_global_object 函数

* * *

  * 函数功能：



> 获取fscript的全局对象。

  * 函数原型：


    
    
    tk_object_t* fscript_get_global_object ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回fscript的全局对象。  
  
#### fscript_global_deinit 函数

* * *

  * 函数功能：



> 全局释放。

  * 函数原型：


    
    
    ret_t fscript_global_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_global_init 函数

* * *

  * 函数功能：



> 全局初始化。

  * 函数原型：


    
    
    ret_t fscript_global_init ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_init 函数

* * *

  * 函数功能：



> 初始化引擎对象，并解析代码。

  * 函数原型：


    
    
    fscript_t* fscript_init (fscript_t* fscript, tk_object_t* obj, const char* script, const char* first_call_name, bool_t keep_func_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fscript_t* | 返回fscript对象。  
fscript | fscript_t* | 初始化 fscript 对象。  
obj | tk_object_t* | 脚本执行上下文。  
script | const char* | 脚本代码。  
first_call_name | const char* | 第一个函数的名字。  
keep_func_name | bool_t | 是否在func_call结构后保存函数名。  
  
#### fscript_register_const_double 函数

* * *

  * 函数功能：



> 注册浮点数常量。

  * 函数原型：


    
    
    ret_t fscript_register_const_double (const char* name, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 常量名。  
value | double | 数据。  
  
#### fscript_register_const_int 函数

* * *

  * 函数功能：



> 注册整数常量。

  * 函数原型：


    
    
    ret_t fscript_register_const_int (const char* name, int value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 常量名。  
value | int | 数据。  
  
#### fscript_register_const_value 函数

* * *

  * 函数功能：



> 注册常量。

  * 函数原型：


    
    
    ret_t fscript_register_const_value (const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 常量名。  
value | const value_t* | 数据。  
  
#### fscript_register_event 函数

* * *

  * 函数功能：



> 注册自定义事件。

  * 函数原型：


    
    
    ret_t fscript_register_event (const char* name, uint32_t etype);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 事件名。  
etype | uint32_t | 事件的值。  
  
#### fscript_register_func 函数

* * *

  * 函数功能：



> 注册全局自定义函数。

  * 函数原型：


    
    
    ret_t fscript_register_func (const char* name, fscript_func_t func);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 函数名(无需加函数前缀)。  
func | fscript_func_t | 函数指针。  
  
#### fscript_register_funcs 函数

* * *

  * 函数功能：



> 注册全局自定义函数。

  * 函数原型：


    
    
    ret_t fscript_register_funcs (const general_factory_table_t* table);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
table | const general_factory_table_t* | 函数表。  
  
#### fscript_reload 函数

* * *

  * 函数功能：



> 重新加载代码。

  * 函数原型：


    
    
    ret_t fscript_reload (fscript_t* fscript, const char* script);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
script | const char* | 脚本代码。  
  
#### fscript_set_error 函数

* * *

  * 函数功能：



> 用于扩展函数设置遇到的错误。

  * 函数原型：


    
    
    ret_t fscript_set_error (fscript_t* fscript, ret_t code, const char* func, const char* message);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
code | ret_t | 错误码。  
func | const char* | 函数名。  
message | const char* | 错误消息。  
  
#### fscript_set_global_object 函数

* * *

  * 函数功能：



> 用于替换默认的全局对象。 仅限于在系统初始化时调用。

  * 函数原型：


    
    
    ret_t fscript_set_global_object (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 全局对象。  
  
#### fscript_set_on_error 函数

* * *

  * 函数功能：



> 设置错误处理函数。

  * 函数原型：


    
    
    ret_t fscript_set_on_error (fscript_t* fscript, fscript_on_error_t on_error, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
on_error | fscript_on_error_t | 错误处理函数。  
ctx | void* | 错误处理函数的上下文。  
  
#### fscript_set_print_func 函数

* * *

  * 函数功能：



> 设置打印日志的函数。

  * 函数原型：


    
    
    ret_t fscript_set_print_func (fscript_t* fscript, fscript_func_t print);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fscript | fscript_t* | 脚本引擎对象。  
print | fscript_func_t | 打印日志的函数。  
  
#### fscript_syntax_check 函数

* * *

  * 函数功能：



> 解析代码，分析是否有语法错误。

示例：
    
    
    fscript_parser_error_t error;
    fscript_syntax_check(obj, "1+1", &error);
    fscript_parser_error_deinit(&error);
    

  * 函数原型：


    
    
    ret_t fscript_syntax_check (tk_object_t* obj, const char* script, fscript_parser_error_t* error);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 脚本执行上下文。  
script | const char* | 脚本代码。  
error | fscript_parser_error_t* | 用于返回错误信息。  
  
#### tk_expr_eval 函数

* * *

  * 函数功能：



> 对fscript的简单包装。

  * 函数原型：


    
    
    double tk_expr_eval (const char* expr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回表达式的值。  
expr | const char* | 表达式。  
  
#### error_code 属性

* * *

> 运行时错误码。

  * 类型：ret_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### error_col 属性

* * *

> 运行时错误的列号。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### error_message 属性

* * *

> 运行时错误信息。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### error_row 属性

* * *

> 运行时错误的行号。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lines 属性

* * *

> 代码总行数。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### obj 属性

* * *

> 脚本执行上下文。

  * 类型：tk_object_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### str 属性

* * *

> C语言实现函数可以使用这个变量，可以有效避免内存分配。

  * 类型：str_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
