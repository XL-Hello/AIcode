## named_value_t

### 概述

![image](images/named_value_t_0.png)

## 命名的值。

### 函数

函数名称 | 说明  
---|---  
named_value_cast | 转换为named_value对象(供脚本语言使用)。  
named_value_compare | 比较。  
named_value_compare_by_name | 比较。  
named_value_create | 创建named_value对象。  
named_value_create_ex | 创建named_value对象。  
named_value_deinit | 重置named_value对象。  
named_value_destroy | 销毁named_value对象。  
named_value_get_value | 获取值对象(主要给脚本语言使用)。  
named_value_icompare | 大小写不敏感比较。  
named_value_icompare_by_name | 大小写不敏感比较。  
named_value_init | 初始化。  
named_value_set_name | 设置名称。  
named_value_set_value | 设置值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
name | char* | 名称。  
value | value_t | 值。  
  
#### named_value_cast 函数

* * *

  * 函数功能：



> 转换为named_value对象(供脚本语言使用)。

  * 函数原型：


    
    
    named_value_t* named_value_cast (named_value_t* nv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_t* | 返回named_value对象。  
nv | named_value_t* | named_value对象。  
  
#### named_value_compare 函数

* * *

  * 函数功能：



> 比较。

  * 函数原型：


    
    
    int32_t named_value_compare (named_value_t* nv, const named_value_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
other | const named_value_t* | named_value对象。  
  
#### named_value_compare_by_name 函数

* * *

  * 函数功能：



> 比较。

  * 函数原型：


    
    
    int32_t named_value_compare_by_name (named_value_t* nv, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
name | const char* | 名称。  
  
#### named_value_create 函数

* * *

  * 函数功能：



> 创建named_value对象。

  * 函数原型：


    
    
    named_value_t* named_value_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_t* | 返回named_value对象。  
  
#### named_value_create_ex 函数

* * *

  * 函数功能：



> 创建named_value对象。

  * 函数原型：


    
    
    named_value_t* named_value_create_ex (const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_t* | 返回named_value对象。  
name | const char* | 名称。  
value | const value_t* | 值。  
  
#### named_value_deinit 函数

* * *

  * 函数功能：



> 重置named_value对象。

  * 函数原型：


    
    
    ret_t named_value_deinit (named_value_t* nv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
  
#### named_value_destroy 函数

* * *

  * 函数功能：



> 销毁named_value对象。

  * 函数原型：


    
    
    ret_t named_value_destroy (named_value_t* nv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
  
#### named_value_get_value 函数

* * *

  * 函数功能：



> 获取值对象(主要给脚本语言使用)。

  * 函数原型：


    
    
    value_t* named_value_get_value (named_value_t* nv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | 返回值对象。  
nv | named_value_t* | named_value对象。  
  
#### named_value_icompare 函数

* * *

  * 函数功能：



> 大小写不敏感比较。

  * 函数原型：


    
    
    int32_t named_value_icompare (named_value_t* nv, const named_value_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
other | const named_value_t* | named_value对象。  
  
#### named_value_icompare_by_name 函数

* * *

  * 函数功能：



> 大小写不敏感比较。

  * 函数原型：


    
    
    int32_t named_value_icompare_by_name (named_value_t* nv, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
name | const char* | 名称。  
  
#### named_value_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    named_value_t* named_value_init (named_value_t* nv, const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_t* | 返回named_value对象。  
nv | named_value_t* | named_value对象。  
name | const char* | 名称。  
value | const value_t* | 值。  
  
#### named_value_set_name 函数

* * *

  * 函数功能：



> 设置名称。

  * 函数原型：


    
    
    ret_t named_value_set_name (named_value_t* nv, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
name | const char* | 名称。  
  
#### named_value_set_value 函数

* * *

  * 函数功能：



> 设置值。

  * 函数原型：


    
    
    ret_t named_value_set_value (named_value_t* nv, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
nv | named_value_t* | named_value对象。  
value | const value_t* | 值。  
  
#### name 属性

* * *

> 名称。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### value 属性

* * *

> 值。

  * 类型：value_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
