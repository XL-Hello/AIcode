## tokenizer_t

### 概述

从字符串中解析出一个一个的token。
    
    
    tokenizer_t tokenizer;
    tokenizer_t* t = tokenizer_init(&tokenizer, "20,111.2,22.3,333.3,44,555.5", 0xffffff, ",");
    
    while(tokenizer_has_more(t)) {
    double v = tokenizer_next_float(t, 0);
    log_debug("%lf\n", v);
    }
    
    tokenizer_deinit(t);
    

* * *

### 函数

函数名称 | 说明  
---|---  
tokenizer_deinit | 重置tokenizer。  
tokenizer_has_more | 是否还有下一个token。  
tokenizer_init | 初始化tokenizer对象。  
tokenizer_init_ex | 初始化tokenizer对象。  
tokenizer_next | 获取下一个token。  
tokenizer_next_expr_until | 获取下一个expr，该expr直到遇到指定的char。  
tokenizer_next_float | 获取下一个token，并转换成float。  
tokenizer_next_int | 获取下一个token，并转换成int。  
tokenizer_next_int64 | 获取下一个token，并转换成int64_t。  
tokenizer_next_str | 获取下一个字符串(允许使用英文单引号和双引号界定字符串)。  
tokenizer_next_str_until | 获取下一个str，该str直到遇到指定的char。  
tokenizer_next_until | 获取下一个token，该token直到遇到指定的char。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
cursor | uint32_t | 当前位置。  
separtor | const char* | 分隔字符串。  
single_char_token | const char* | 单字符的token。  
size | uint32_t | 字符串的长度。  
str | const char* | 字符串。  
  
#### tokenizer_deinit 函数

* * *

  * 函数功能：



> 重置tokenizer。

  * 函数原型：


    
    
    ret_t tokenizer_deinit (tokenizer_t* tokenizer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
tokenizer | tokenizer_t* | tokenizer对象。  
  
#### tokenizer_has_more 函数

* * *

  * 函数功能：



> 是否还有下一个token。

  * 函数原型：


    
    
    bool_t tokenizer_has_more (tokenizer_t* tokenizer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 还有下一个token返回TRUE，否则返回FALSE。  
tokenizer | tokenizer_t* | tokenizer对象。  
  
#### tokenizer_init 函数

* * *

  * 函数功能：



> 初始化tokenizer对象。

  * 函数原型：


    
    
    tokenizer_t* tokenizer_init (tokenizer_t* tokenizer, const char* str, uint32_t size, const char* separtor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tokenizer_t* | tokenizer对象本身。  
tokenizer | tokenizer_t* | tokenizer对象。  
str | const char* | 要解析的字符串。  
size | uint32_t | 字符串长度。  
separtor | const char* | 分隔字符。  
  
#### tokenizer_init_ex 函数

* * *

  * 函数功能：



> 初始化tokenizer对象。

  * 函数原型：


    
    
    tokenizer_t* tokenizer_init_ex (tokenizer_t* tokenizer, const char* str, uint32_t size, const char* separtor, const char* single_char_token);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tokenizer_t* | tokenizer对象本身。  
tokenizer | tokenizer_t* | tokenizer对象。  
str | const char* | 要解析的字符串。  
size | uint32_t | 字符串长度。  
separtor | const char* | 分隔字符。  
single_char_token | const char* | 单字符token。  
  
#### tokenizer_next 函数

* * *

  * 函数功能：



> 获取下一个token。

  * 函数原型：


    
    
    const char* tokenizer_next (tokenizer_t* tokenizer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 成功返回token，失败返回NULL。  
tokenizer | tokenizer_t* | tokenizer对象。  
  
#### tokenizer_next_expr_until 函数

* * *

  * 函数功能：



> 获取下一个expr，该expr直到遇到指定的char。

  * 函数原型：


    
    
    const char* tokenizer_next_expr_until (tokenizer_t* tokenizer, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 成功返回token，失败返回NULL。  
tokenizer | tokenizer_t* | tokenizer对象。  
str | const char* | 字符集。  
  
#### tokenizer_next_float 函数

* * *

  * 函数功能：



> 获取下一个token，并转换成float。

  * 函数原型：


    
    
    float tokenizer_next_float (tokenizer_t* tokenizer, float defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 成功返回token的float值，失败返回缺省值。  
tokenizer | tokenizer_t* | tokenizer对象。  
defval | float | 缺省值。  
  
#### tokenizer_next_int 函数

* * *

  * 函数功能：



> 获取下一个token，并转换成int。

  * 函数原型：


    
    
    int tokenizer_next_int (tokenizer_t* tokenizer, int defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 成功返回token的int值，失败返回缺省值。  
tokenizer | tokenizer_t* | tokenizer对象。  
defval | int | 缺省值。  
  
#### tokenizer_next_int64 函数

* * *

  * 函数功能：



> 获取下一个token，并转换成int64_t。

  * 函数原型：


    
    
    int64_t tokenizer_next_int64 (tokenizer_t* tokenizer, int64_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 成功返回token的int64_t值，失败返回缺省值。  
tokenizer | tokenizer_t* | tokenizer对象。  
defval | int64_t | 缺省值。  
  
#### tokenizer_next_str 函数

* * *

  * 函数功能：



> 获取下一个字符串(允许使用英文单引号和双引号界定字符串)。

  * 函数原型：


    
    
    const char* tokenizer_next_str (tokenizer_t* tokenizer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 成功返回字符串，失败返回NULL。  
tokenizer | tokenizer_t* | tokenizer对象。  
  
#### tokenizer_next_str_until 函数

* * *

  * 函数功能：



> 获取下一个str，该str直到遇到指定的char。

  * 函数原型：


    
    
    const char* tokenizer_next_str_until (tokenizer_t* tokenizer, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 成功返回token，失败返回NULL。  
tokenizer | tokenizer_t* | tokenizer对象。  
str | const char* | 字符集。  
  
#### tokenizer_next_until 函数

* * *

  * 函数功能：



> 获取下一个token，该token直到遇到指定的char。

  * 函数原型：


    
    
    const char* tokenizer_next_until (tokenizer_t* tokenizer, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 成功返回token，失败返回NULL。  
tokenizer | tokenizer_t* | tokenizer对象。  
str | const char* | 字符集。  
  
#### cursor 属性

* * *

> 当前位置。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### separtor 属性

* * *

> 分隔字符串。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### single_char_token 属性

* * *

> 单字符的token。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 字符串的长度。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### str 属性

* * *

> 字符串。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
