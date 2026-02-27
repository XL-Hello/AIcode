## fscript_parser_error_t

### 概述

## 解析错误信息。

### 函数

函数名称 | 说明  
---|---  
fscript_parser_error_deinit | 释放error对象中的资源。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
col | int | 出现错误的代码列。  
message | char* | 错误信息。  
offset | int | 出现错误的代码偏移。  
row | int | 出现错误的代码行。  
token | char* | 当前的token。  
  
#### fscript_parser_error_deinit 函数

* * *

  * 函数功能：



> 释放error对象中的资源。

  * 函数原型：


    
    
    ret_t fscript_parser_error_deinit (fscript_parser_error_t* error);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
error | fscript_parser_error_t* | 解析错误信息。  
  
#### col 属性

* * *

> 出现错误的代码列。

  * 类型：int

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### message 属性

* * *

> 错误信息。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### offset 属性

* * *

> 出现错误的代码偏移。

  * 类型：int

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### row 属性

* * *

> 出现错误的代码行。

  * 类型：int

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### token 属性

* * *

> 当前的token。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
