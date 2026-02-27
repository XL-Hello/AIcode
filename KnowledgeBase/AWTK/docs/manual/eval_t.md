## eval_t

### 概述

## 表达式。

### 函数

函数名称 | 说明  
---|---  
eval_default_hooks | 获取内置函数。  
eval_execute | 计算表达式的值。  
eval_result_to_string | 将错误码转换成字符串。  
expr_value_clear | 清除值。  
expr_value_get_number | 获取浮点数值。  
expr_value_get_string | 获取字符串。  
expr_value_init | 初始化值。  
expr_value_set_number | 设置浮点数值。  
expr_value_set_string | 设置字符串。  
tk_expr_eval | 计算表达式返回浮点数。  
tk_expr_eval_str | 计算表达式返回字符串。  
  
#### eval_default_hooks 函数

* * *

  * 函数功能：



> 获取内置函数。

  * 函数原型：


    
    
    const EvalHooks* eval_default_hooks ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const EvalHooks* | 回调函数列表。  
  
#### eval_execute 函数

* * *

  * 函数功能：



> 计算表达式的值。

  * 函数原型：


    
    
    EvalResult eval_execute (const char* expr, const EvalHooks* hooks, void* ctx, ExprValue* output);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | EvalResult | 返回EVAL_RESULT_OK表示成功，否则表示失败。  
expr | const char* | 表达式  
hooks | const EvalHooks* | 回调函数。  
ctx | void* | 回调函数的上下文。  
output | ExprValue* | 计算结果。  
  
#### eval_result_to_string 函数

* * *

  * 函数功能：



> 将错误码转换成字符串。

  * 函数原型：


    
    
    const char* eval_result_to_string (EvalResult result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回对应的字符串。  
result | EvalResult | 值。  
  
#### expr_value_clear 函数

* * *

  * 函数功能：



> 清除值。

  * 函数原型：


    
    
    void expr_value_clear (ExprValue* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回void。  
v | ExprValue* | 值对象。  
  
#### expr_value_get_number 函数

* * *

  * 函数功能：



> 获取浮点数值。

  * 函数原型：


    
    
    double expr_value_get_number (const ExprValue* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回浮点数值。  
v | const ExprValue* | 值对象。  
  
#### expr_value_get_string 函数

* * *

  * 函数功能：



> 获取字符串。

  * 函数原型：


    
    
    const char* expr_value_get_string (const ExprValue* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回字符串。  
v | const ExprValue* | 值对象。  
  
#### expr_value_init 函数

* * *

  * 函数功能：



> 初始化值。

  * 函数原型：


    
    
    void expr_value_init (ExprValue* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 返回void。  
v | ExprValue* | 值对象。  
  
#### expr_value_set_number 函数

* * *

  * 函数功能：



> 设置浮点数值。

  * 函数原型：


    
    
    EvalResult expr_value_set_number (ExprValue* v, double val);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | EvalResult | 返回EVAL_RESULT_OK表示成功，否则表示失败。  
v | ExprValue* | 值对象。  
val | double | 浮点数的值。  
  
#### expr_value_set_string 函数

* * *

  * 函数功能：



> 设置字符串。

  * 函数原型：


    
    
    EvalResult expr_value_set_string (ExprValue* v, const char* str, size_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | EvalResult | 返回EVAL_RESULT_OK表示成功，否则表示失败。  
v | ExprValue* | 值对象。  
str | const char* | 字符串。  
len | size_t | 字符串长度。  
  
#### tk_expr_eval 函数

* * *

  * 函数功能：



> 计算表达式返回浮点数。

  * 函数原型：


    
    
    double tk_expr_eval (const char* expor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回结果。  
expor | const char* | 表达式  
  
#### tk_expr_eval_str 函数

* * *

  * 函数功能：



> 计算表达式返回字符串。

  * 函数原型：


    
    
    const char* tk_expr_eval_str (const char* expor, char* result, uint32_t );
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回结果。  
expor | const char* | 表达式  
result | char* | 结果字符串  
| uint32_t | 。
