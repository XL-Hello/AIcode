## input_method_t

### 概述

输入法接口。

常见的实现方式有以下几种：

  * 空实现。用于不需要输入法的嵌入式平台。

  * 缺省实现。用于需要输入法的嵌入式平台。

  * 基于SDL实现的平台原生输入法。用于桌面系统和手机系统。




![image](images/input_method_t_0.png)

## > 输入类型请参考：[input_type](input_type_t.html)

### 函数

函数名称 | 说明  
---|---  
input_method | 获取全局输入法对象。  
input_method_commit_text | 提交输入文本。  
input_method_commit_text_ex | 提交输入文本。  
input_method_create | 创建输入法对象。在具体实现中实现。  
input_method_destroy | 销毁输入法对象。在具体实现中实现。  
input_method_dispatch | 分发一个事件。  
input_method_dispatch_action | 软键盘上的action按钮被点击时，调用本函数分发EVT_IM_ACTION事件。  
input_method_dispatch_candidates | 请求显示候选字。  
input_method_dispatch_key | 提交按键。  
input_method_dispatch_keys | 提交按键。  
input_method_dispatch_pre_candidates | 请求显示预候选字。  
input_method_dispatch_preedit | 分发进入预编辑状态的事件。  
input_method_dispatch_preedit_abort | 分发取消预编辑状态的事件(提交预编辑内容，退出预编辑状态)。  
input_method_dispatch_preedit_confirm | 分发确认预编辑状态的事件(提交预编辑内容，退出预编辑状态)。  
input_method_dispatch_to_widget | 分发一个事件当前焦点控件。  
input_method_get_lang | 获取语言。  
input_method_is_native | 是否是平台原生输入法。  
input_method_off | 注销指定事件的处理函数。  
input_method_on | 注册指定事件的处理函数。  
input_method_request | 打开或关闭输入法。  
input_method_set | 设置全局输入法对象。  
input_method_set_lang | 设置语言。  
input_method_update_action_button_info | 设置软键盘上的action按钮的信息。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
action_button_enable | bool_t | 软键盘的上的action按钮是否可用。  
action_button_text | char* | 软键盘的上的action按钮文本。  
is_native | bool_t | 是否是原生输入法。  
keyboard_name | char* | 软键盘资源名称。  
  
#### input_method 函数

* * *

  * 函数功能：



> 获取全局输入法对象。

  * 函数原型：


    
    
    input_method_t* input_method ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | input_method_t* | 成功返回输入法对象，失败返回NULL。  
  
#### input_method_commit_text 函数

* * *

  * 函数功能：



> 提交输入文本。

  * 函数原型：


    
    
    ret_t input_method_commit_text (input_method_t* im, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
text | const char* | 文本。  
  
#### input_method_commit_text_ex 函数

* * *

  * 函数功能：



> 提交输入文本。

  * 函数原型：


    
    
    ret_t input_method_commit_text_ex (input_method_t* im, bool_t replace, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
replace | bool_t | 是否替换原来的文本。  
text | const char* | 文本。  
  
#### input_method_create 函数

* * *

  * 函数功能：



> 创建输入法对象。在具体实现中实现。

  * 函数原型：


    
    
    input_method_t* input_method_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | input_method_t* | 成功返回输入法对象，失败返回NULL。  
  
#### input_method_destroy 函数

* * *

  * 函数功能：



> 销毁输入法对象。在具体实现中实现。

  * 函数原型：


    
    
    ret_t input_method_destroy (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
  
#### input_method_dispatch 函数

* * *

  * 函数功能：



> 分发一个事件。

  * 函数原型：


    
    
    ret_t input_method_dispatch (input_method_t* im, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 控件对象。  
e | event_t* | 事件。  
  
#### input_method_dispatch_action 函数

* * *

  * 函数功能：



> 软键盘上的action按钮被点击时，调用本函数分发EVT_IM_ACTION事件。

  * 函数原型：


    
    
    ret_t input_method_dispatch_action (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
  
#### input_method_dispatch_candidates 函数

* * *

  * 函数功能：



> 请求显示候选字。

  * 函数原型：


    
    
    ret_t input_method_dispatch_candidates (input_method_t* im, const char* strs, uint32_t nr, int32_t selected);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
strs | const char* | 候选字列表。  
nr | uint32_t | 候选字个数。  
selected | int32_t | 缺省选中候选字的序数。  
  
#### input_method_dispatch_key 函数

* * *

  * 函数功能：



> 提交按键。

  * 函数原型：


    
    
    ret_t input_method_dispatch_key (input_method_t* im, uint32_t key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
key | uint32_t | 键值。  
  
#### input_method_dispatch_keys 函数

* * *

  * 函数功能：



> 提交按键。

  * 函数原型：


    
    
    ret_t input_method_dispatch_keys (input_method_t* im, const char* keys);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
keys | const char* | 键值。  
  
#### input_method_dispatch_pre_candidates 函数

* * *

  * 函数功能：



> 请求显示预候选字。
> 
> 预候选字: 在有的输入法中，比如T9硬键盘输入时，按下12两个键时，预候选字会显示可用的拼音列表。 从预候选字列表中选择拼音，再查询拼音对应的候选字列表。

  * 函数原型：


    
    
    ret_t input_method_dispatch_pre_candidates (input_method_t* im, const char* strs, uint32_t nr, int32_t selected);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
strs | const char* | 候选字列表。  
nr | uint32_t | 候选字个数。  
selected | int32_t | 缺省选中候选字的序数。  
  
#### input_method_dispatch_preedit 函数

* * *

  * 函数功能：



> 分发进入预编辑状态的事件。

  * 函数原型：


    
    
    ret_t input_method_dispatch_preedit (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
  
#### input_method_dispatch_preedit_abort 函数

* * *

  * 函数功能：



> 分发取消预编辑状态的事件(提交预编辑内容，退出预编辑状态)。

  * 函数原型：


    
    
    ret_t input_method_dispatch_preedit_abort (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
  
#### input_method_dispatch_preedit_confirm 函数

* * *

  * 函数功能：



> 分发确认预编辑状态的事件(提交预编辑内容，退出预编辑状态)。

  * 函数原型：


    
    
    ret_t input_method_dispatch_preedit_confirm (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
  
#### input_method_dispatch_to_widget 函数

* * *

  * 函数功能：



> 分发一个事件当前焦点控件。

  * 函数原型：


    
    
    ret_t input_method_dispatch_to_widget (input_method_t* im, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 控件对象。  
e | event_t* | 事件。  
  
#### input_method_get_lang 函数

* * *

  * 函数功能：



> 获取语言。

  * 函数原型：


    
    
    const char* input_method_get_lang (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回语言。  
im | input_method_t* | 输入法对象。  
  
#### input_method_is_native 函数

* * *

  * 函数功能：



> 是否是平台原生输入法。

  * 函数原型：


    
    
    bool_t input_method_is_native (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是原生输入法，否则表示不是。  
im | input_method_t* | 输入法对象。  
  
#### input_method_off 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t input_method_off (input_method_t* im, uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
id | uint32_t | input_method_on返回的ID。  
  
#### input_method_on 函数

* * *

  * 函数功能：



> 注册指定事件的处理函数。

  * 函数原型：


    
    
    uint32_t input_method_on (input_method_t* im, event_type_t type, event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于input_method_off。  
im | input_method_t* | 输入法对象。  
type | event_type_t | 事件类型。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### input_method_request 函数

* * *

  * 函数功能：



> 打开或关闭输入法。

  * 函数原型：


    
    
    ret_t input_method_request (input_method_t* im, widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
widget | widget_t* | 焦点控件，为NULL时关闭输入法，非NULL时打开输入法。  
  
#### input_method_set 函数

* * *

  * 函数功能：



> 设置全局输入法对象。

  * 函数原型：


    
    
    ret_t input_method_set (input_method_t* im);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
  
#### input_method_set_lang 函数

* * *

  * 函数功能：



> 设置语言。
> 
> 有时在同一种语言环境下，也需要输入多种文字，典型的情况是同时输入中文和英文。 比如T9输入法，可以同时支持中文和英文输入，配合软键盘随时切换输入的语言。 数字、小写字母、大写字母和符合也可以视为输入的语言。 主要用于提示输入法引擎选择适当的输入方法。

  * 函数原型：


    
    
    ret_t input_method_set_lang (input_method_t* im, const char* lang);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
lang | const char* | 语言。格式为语言+国家/地区码。如：zh_cn和en_us等。  
  
#### input_method_update_action_button_info 函数

* * *

  * 函数功能：



> 设置软键盘上的action按钮的信息。

  * 函数原型：


    
    
    ret_t input_method_update_action_button_info (input_method_t* im, const char* text, bool_t enable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
im | input_method_t* | 输入法对象。  
text | const char* | 按钮的文本。  
enable | bool_t | 按钮的是否可用。  
  
#### action_button_enable 属性

* * *

> 软键盘的上的action按钮是否可用。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### action_button_text 属性

* * *

> 软键盘的上的action按钮文本。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### is_native 属性

* * *

> 是否是原生输入法。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### keyboard_name 属性

* * *

> 软键盘资源名称。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
