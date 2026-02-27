## input_engine_t

### 概述

输入法引擎接口。

常见的实现方式有以下几种：

  * 空实现。用于不需要输入法的嵌入式平台。

  * 拼音输入法实现。用于需要输入法的嵌入式平台。




![image](images/input_engine_t_0.png)

* * *

### 函数

函数名称 | 说明  
---|---  
input_engine_add_candidate | 给输入法引擎对象加入一个候选字。  
input_engine_add_candidates_from_char | 根据字符类型给输入法引擎对象加入所有符合的候选字。  
input_engine_add_candidates_from_string | 根据字符串给输入法引擎对象加入所有符合的候选字。  
input_engine_create | 创建输入法引擎对象。  
input_engine_deinit | 释放输入法引擎对象。  
input_engine_destroy | 销毁输入法引擎对象。  
input_engine_dispatch_candidates | 请求显示候选字。  
input_engine_get_lang | 获取语言。  
input_engine_init | 初始化输入法引擎对象。  
input_engine_input | 输入新的按键，并更新候选字。  
input_engine_reset_candidates | 重置输入法引擎对象。  
input_engine_reset_input | 清除所有输入的按键组合和候选字。  
input_engine_search | 根据按键组合，更新候选字，并通过输入法对象提交候选字和pre候选字。  
input_engine_set_lang | 设置语言。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
|  |   
  
#### input_engine_add_candidate 函数

* * *

  * 函数功能：



> 给输入法引擎对象加入一个候选字。

  * 函数原型：


    
    
    ret_t input_engine_add_candidate (input_engine_t* engine, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
str | const char* | 候选字。  
  
#### input_engine_add_candidates_from_char 函数

* * *

  * 函数功能：



> 根据字符类型给输入法引擎对象加入所有符合的候选字。 备注：搜索表是二维数组，需要通过参数 c 来确定使用具体行数。

  * 函数原型：


    
    
    ret_t input_engine_add_candidates_from_char (input_engine_t* engine, const wchar_t** table, char c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
table | const wchar_t** | 输入法搜索表。  
c | char | 需要显示查询的字符。  
  
#### input_engine_add_candidates_from_string 函数

* * *

  * 函数功能：



> 根据字符串给输入法引擎对象加入所有符合的候选字。

  * 函数原型：


    
    
    ret_t input_engine_add_candidates_from_string (input_engine_t* engine, const table_entry_t* items, uint32_t items_nr, const char* key, bool_t exact);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
items | const table_entry_t* | 输入法搜索表。  
items_nr | uint32_t | 输入法搜索表长度。  
key | const char* | 需要显示查询的字符。  
exact | bool_t | 是否只查询完全匹配的字符串。  
  
#### input_engine_create 函数

* * *

  * 函数功能：



> 创建输入法引擎对象。

  * 函数原型：


    
    
    input_engine_t* input_engine_create (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | input_engine_t* | 返回输入法引擎对象。  
im | input_method_t* | 输入法对象。  
  
#### input_engine_deinit 函数

* * *

  * 函数功能：



> 释放输入法引擎对象。

  * 函数原型：


    
    
    ret_t input_engine_deinit (input_engine_t* engine);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
  
#### input_engine_destroy 函数

* * *

  * 函数功能：



> 销毁输入法引擎对象。

  * 函数原型：


    
    
    ret_t input_engine_destroy (input_engine_t* engine);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
  
#### input_engine_dispatch_candidates 函数

* * *

  * 函数功能：



> 请求显示候选字。

  * 函数原型：


    
    
    ret_t input_engine_dispatch_candidates (input_engine_t* engine, int32_t selected);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
selected | int32_t | 缺省选中候选字的序数。  
  
#### input_engine_get_lang 函数

* * *

  * 函数功能：



> 获取语言。

  * 函数原型：


    
    
    const char* input_engine_get_lang (input_engine_t* engine);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回语言。  
engine | input_engine_t* | 输入法引擎对象。  
  
#### input_engine_init 函数

* * *

  * 函数功能：



> 初始化输入法引擎对象。

  * 函数原型：


    
    
    ret_t input_engine_init (input_engine_t* engine);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
  
#### input_engine_input 函数

* * *

  * 函数功能：



> 输入新的按键，并更新候选字。

  * 函数原型：


    
    
    ret_t input_engine_input (input_engine_t* engine, int key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
key | int | 键值。  
  
#### input_engine_reset_candidates 函数

* * *

  * 函数功能：



> 重置输入法引擎对象。

  * 函数原型：


    
    
    ret_t input_engine_reset_candidates (input_engine_t* engine);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
  
#### input_engine_reset_input 函数

* * *

  * 函数功能：



> 清除所有输入的按键组合和候选字。

  * 函数原型：


    
    
    ret_t input_engine_reset_input (input_engine_t* engine);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
  
#### input_engine_search 函数

* * *

  * 函数功能：



> 根据按键组合，更新候选字，并通过输入法对象提交候选字和pre候选字。

  * 函数原型：


    
    
    ret_t input_engine_search (input_engine_t* engine, const char* keys);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
keys | const char* | 按键组合。  
  
#### input_engine_set_lang 函数

* * *

  * 函数功能：



> 设置语言。 有时在同一种语言环境下，也需要输入多种文字，典型的情况是同时输入中文和英文。 比如T9输入法，可以同时支持中文和英文输入，配合软键盘随时切换输入的语言。 数字、小写字母、大写字母和符合也可以视为输入的语言。 主要用于提示输入法引擎选择适当的输入方法。

  * 函数原型：


    
    
    ret_t input_engine_set_lang (input_engine_t* engine, const char* lang);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
engine | input_engine_t* | 输入法引擎对象。  
lang | const char* | 语言。格式为语言+国家/地区码。如：zh_cn和en_us等。
