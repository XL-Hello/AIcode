## named_value_hash_t

### 概述

![image](images/named_value_hash_t_0.png)

## 带有散列值的命名的值。

### 函数

函数名称 | 说明  
---|---  
named_value_hash_clone | 克隆named_value_hash对象。  
named_value_hash_compare | 比较。  
named_value_hash_compare_by_hash | 比较。  
named_value_hash_create | 创建named_value_hash对象。  
named_value_hash_create_ex | 创建named_value_hash对象。  
named_value_hash_deinit | 重置named_value_hash对象。  
named_value_hash_destroy | 销毁named_value_hash对象。  
named_value_hash_get_hash_from_str | 获取字符串散列值。  
named_value_hash_init | 初始化。  
named_value_hash_set_name | 设置散列值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
hash | uint64_t | 散列值。  
  
#### named_value_hash_clone 函数

* * *

  * 函数功能：



> 克隆named_value_hash对象。

  * 函数原型：


    
    
    named_value_hash_t* named_value_hash_clone (named_value_hash_t* nvh);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_hash_t* | 返回named_value_hash对象。  
nvh | named_value_hash_t* | named_value_hash对象。  
  
#### named_value_hash_compare 函数

* * *

  * 函数功能：



> 比较。

  * 函数原型：


    
    
    int32_t named_value_hash_compare (const named_value_hash_t* nvh, const named_value_hash_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回RET_OK表示成功，否则表示失败。  
nvh | const named_value_hash_t* | named_value_hash对象。  
other | const named_value_hash_t* | named_value_hash对象。  
  
#### named_value_hash_compare_by_hash 函数

* * *

  * 函数功能：



> 比较。

  * 函数原型：


    
    
    int32_t named_value_hash_compare_by_hash (const named_value_hash_t* nvh, uint64_t hash);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回RET_OK表示成功，否则表示失败。  
nvh | const named_value_hash_t* | named_value_hash对象。  
hash | uint64_t | 散列值。  
  
#### named_value_hash_create 函数

* * *

  * 函数功能：



> 创建named_value_hash对象。

  * 函数原型：


    
    
    named_value_hash_t* named_value_hash_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_hash_t* | 返回named_value_hash对象。  
  
#### named_value_hash_create_ex 函数

* * *

  * 函数功能：



> 创建named_value_hash对象。

  * 函数原型：


    
    
    named_value_hash_t* named_value_hash_create_ex (const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_hash_t* | 返回named_value_hash对象。  
name | const char* | 名称。  
value | const value_t* | 值。  
  
#### named_value_hash_deinit 函数

* * *

  * 函数功能：



> 重置named_value_hash对象。

  * 函数原型：


    
    
    ret_t named_value_hash_deinit (named_value_hash_t* nvh);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
nvh | named_value_hash_t* | named_value_hash对象。  
  
#### named_value_hash_destroy 函数

* * *

  * 函数功能：



> 销毁named_value_hash对象。

  * 函数原型：


    
    
    ret_t named_value_hash_destroy (named_value_hash_t* nvh);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
nvh | named_value_hash_t* | named_value_hash对象。  
  
#### named_value_hash_get_hash_from_str 函数

* * *

  * 函数功能：



> 获取字符串散列值。

  * 函数原型：


    
    
    uint64_t named_value_hash_get_hash_from_str (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回散列值。  
str | const char* | 字符串。  
  
#### named_value_hash_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    named_value_hash_t* named_value_hash_init (named_value_hash_t* nvh, const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | named_value_hash_t* | 返回named_value_hash对象。  
nvh | named_value_hash_t* | named_value_hash对象。  
name | const char* | 名称。  
value | const value_t* | 值。  
  
#### named_value_hash_set_name 函数

* * *

  * 函数功能：



> 设置散列值。

  * 函数原型：


    
    
    ret_t named_value_hash_set_name (named_value_hash_t* nvh, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
nvh | named_value_hash_t* | named_value_hash对象。  
name | const char* | 名称。  
  
#### hash 属性

* * *

> 散列值。

  * 类型：uint64_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
