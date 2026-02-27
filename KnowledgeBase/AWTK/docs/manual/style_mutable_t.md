## style_mutable_t

### 概述

![image](images/style_mutable_t_0.png)

可变的style(可实时修改并生效，主要用于在designer中被编辑的控件，或者一些特殊控件)。

## style_mutable也对style_const进行了包装，当用户没修改某个值时，便从style_const中获取。

### 函数

函数名称 | 说明  
---|---  
style_mutable_cast | 转换为style_mutable对象。  
style_mutable_copy | 将other对象的数据拷贝到s对象。  
style_mutable_create | 创建style_mutable对象。  
style_mutable_foreach | 遍历。对每项调用回调函数on_style_item。  
style_mutable_get_value | 获取指定名称的值。  
style_mutable_remove_value | 移除指定名称的值。  
style_mutable_reset | 清空s对象。  
style_mutable_set_color | 设置指定名称的颜色值。  
style_mutable_set_default_style | 设置 style_mutable 对象的 default_style 成员，并且释放原来的 default_style 成员对象  
style_mutable_set_int | 设置指定名称整数格式的值。  
style_mutable_set_name | 设置style的名称。  
style_mutable_set_str | 设置指定名称字符串的值。  
style_mutable_set_value | 设置指定名称的值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
name | char* | 名称。  
  
#### style_mutable_cast 函数

* * *

  * 函数功能：



> 转换为style_mutable对象。

  * 函数原型：


    
    
    style_t* style_mutable_cast (style_t* s);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | style_t* | style对象。  
s | style_t* | style对象。  
  
#### style_mutable_copy 函数

* * *

  * 函数功能：



> 将other对象的数据拷贝到s对象。

  * 函数原型：


    
    
    ret_t style_mutable_copy (style_t* s, style_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
other | style_t* | style对象。  
  
#### style_mutable_create 函数

* * *

  * 函数功能：



> 创建style_mutable对象。
> 
> 除了测试程序外不需要直接调用，widget会通过style_factory_create创建。

  * 函数原型：


    
    
    style_t* style_mutable_create (style_t* default_style);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | style_t* | style对象。  
default_style | style_t* | 缺省的style。  
  
#### style_mutable_foreach 函数

* * *

  * 函数功能：



> 遍历。对每项调用回调函数on_style_item。

  * 函数原型：


    
    
    ret_t style_mutable_foreach (style_t* s, tk_on_style_item_t on_style_item, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
on_style_item | tk_on_style_item_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### style_mutable_get_value 函数

* * *

  * 函数功能：



> 获取指定名称的值。

  * 函数原型：


    
    
    ret_t style_mutable_get_value (style_t* s, const char* state, const char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
state | const char* | 控件状态。  
name | const char* | 属性名。  
v | value_t* | 值。  
  
#### style_mutable_remove_value 函数

* * *

  * 函数功能：



> 移除指定名称的值。 备注： 如果 state 控件状态为 NULL，name 属性名为 NULL，就清除所有的 mutable 风格。 如果 state 控件状态为 NULL，name 属性名不为 NULL，清除 state 状态为 normal 的 name 属性。 如果 state 控件状态不为 NULL，name 属性名为 NULL，就清除所有的 state 状态的风格。

  * 函数原型：


    
    
    ret_t style_mutable_remove_value (style_t* s, const char* state, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
state | const char* | 控件状态。  
name | const char* | 属性名。  
  
#### style_mutable_reset 函数

* * *

  * 函数功能：



> 清空s对象。

  * 函数原型：


    
    
    ret_t style_mutable_reset (style_t* s);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
  
#### style_mutable_set_color 函数

* * *

  * 函数功能：



> 设置指定名称的颜色值。

  * 函数原型：


    
    
    ret_t style_mutable_set_color (style_t* s, const char* state, const char* name, color_t val);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
state | const char* | 控件状态。  
name | const char* | 属性名。  
val | color_t | 值。  
  
#### style_mutable_set_default_style 函数

* * *

  * 函数功能：



> 设置 style_mutable 对象的 default_style 成员，并且释放原来的 default_style 成员对象

  * 函数原型：


    
    
    ret_t style_mutable_set_default_style (style_t* s, style_t* default_style);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
default_style | style_t* | 缺省的style。  
  
#### style_mutable_set_int 函数

* * *

  * 函数功能：



> 设置指定名称整数格式的值。

  * 函数原型：


    
    
    ret_t style_mutable_set_int (style_t* s, const char* state, const char* name, uint32_t val);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
state | const char* | 控件状态。  
name | const char* | 属性名。  
val | uint32_t | 值。  
  
#### style_mutable_set_name 函数

* * *

  * 函数功能：



> 设置style的名称。

  * 函数原型：


    
    
    ret_t style_mutable_set_name (style_t* s, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
name | const char* | 名称。  
  
#### style_mutable_set_str 函数

* * *

  * 函数功能：



> 设置指定名称字符串的值。

  * 函数原型：


    
    
    ret_t style_mutable_set_str (style_t* s, const char* state, const char* name, const char* val);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
state | const char* | 控件状态。  
name | const char* | 属性名。  
val | const char* | 值。  
  
#### style_mutable_set_value 函数

* * *

  * 函数功能：



> 设置指定名称的值。

  * 函数原型：


    
    
    ret_t style_mutable_set_value (style_t* s, const char* state, const char* name, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
s | style_t* | style对象。  
state | const char* | 控件状态。  
name | const char* | 属性名。  
v | const value_t* | 值。  
  
#### name 属性

* * *

> 名称。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
