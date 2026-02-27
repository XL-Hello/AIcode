## bidi_t

### 概述

## Unicode Bidirectional Algorithm.

### 函数

函数名称 | 说明  
---|---  
bidi_deinit | 释放bidi对象相关资源。  
bidi_init | 初始化bidi对象。  
bidi_log2vis | 将字符串转成用于显示的字符串，输出结果放在bidi->vis_str中。  
bidi_type_from_name | 将bidi类型的名称转换成类型。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
positions_L_to_V | int32_t* | logical位置与visual位置的映射。  
positions_V_to_L | int32_t* | visual位置与logical位置的映射。  
request_type | bidi_type_t | 请求的类型。  
resolved_type | bidi_type_t | 实际的类型。  
vis_str | wchar_t* | 用于显示的字符串(存放log2vis的结果)。  
vis_str_size | uint32_t | 用于显示的字符串长度(存放log2vis的结果)。  
  
#### bidi_deinit 函数

* * *

  * 函数功能：



> 释放bidi对象相关资源。

  * 函数原型：


    
    
    ret_t bidi_deinit (bidi_t* bidi);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bidi | bidi_t* | bidi对象。  
  
#### bidi_init 函数

* * *

  * 函数功能：



> 初始化bidi对象。

  * 函数原型：


    
    
    bidi_t* bidi_init (bidi_t* bidi, bool_t alloc_l2v, bool_t alloc_v2l, bidi_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bidi_t* | 返回bidi对象。  
bidi | bidi_t* | bidi对象。  
alloc_l2v | bool_t | 是否为positions_L_to_V分配空间。  
alloc_v2l | bool_t | 是否为positions_V_to_L分配空间。  
type | bidi_type_t | 类型。  
  
#### bidi_log2vis 函数

* * *

  * 函数功能：



> 将字符串转成用于显示的字符串，输出结果放在bidi->vis_str中。

  * 函数原型：


    
    
    ret_t bidi_log2vis (bidi_t* bidi, const wchar_t* str, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bidi | bidi_t* | bidi对象。  
str | const wchar_t* | 字符串。  
size | uint32_t | 字符串的长度。  
  
#### bidi_type_from_name 函数

* * *

  * 函数功能：



> 将bidi类型的名称转换成类型。

  * 函数原型：


    
    
    bidi_type_t bidi_type_from_name (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bidi_type_t | 返回bidi对象。  
name | const char* | 类型名称(取值：rtl,ltr,auto,wrtl,wltr,lro,rlo)。  
  
#### positions_L_to_V 属性

* * *

> logical位置与visual位置的映射。

  * 类型：int32_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### positions_V_to_L 属性

* * *

> visual位置与logical位置的映射。

  * 类型：int32_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### request_type 属性

* * *

> 请求的类型。

  * 类型：bidi_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### resolved_type 属性

* * *

> 实际的类型。

  * 类型：bidi_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### vis_str 属性

* * *

> 用于显示的字符串(存放log2vis的结果)。

  * 类型：wchar_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### vis_str_size 属性

* * *

> 用于显示的字符串长度(存放log2vis的结果)。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
