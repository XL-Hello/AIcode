## enum_helper

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
asset_type_find_by_value | 获取资源类型枚值和名称的对应关系。  
find_item | 获取特定枚值和名称的对应关系。  
find_item_by_value | 获取特定枚值和名称的对应关系。  
input_type_find | 获取输入类型值和名称的对应关系。  
keys_type_find | 获取按键值和名称的对应关系。  
keys_type_find_by_value | 获取按键值和名称的对应关系。  
keys_type_set_custom_keys | 设置自定义键值表。  
  
#### asset_type_find_by_value 函数

* * *

  * 函数功能：



> 获取资源类型枚值和名称的对应关系。

  * 函数原型：


    
    
    const key_type_value_t* asset_type_find_by_value (uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const key_type_value_t* | 返回资源类型枚值和名称的对应关系。  
value | uint32_t | 资源的类型。  
  
#### find_item 函数

* * *

  * 函数功能：



> 获取特定枚值和名称的对应关系。

  * 函数原型：


    
    
    const key_type_value_t* find_item (const key_type_value_t* items, uint32_t nr, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const key_type_value_t* | 返回资源类型枚值和名称的对应关系。  
items | const key_type_value_t* | 特定枚举值对应列表。  
nr | uint32_t | 列表长度。  
name | const char* | 名称。  
  
#### find_item_by_value 函数

* * *

  * 函数功能：



> 获取特定枚值和名称的对应关系。

  * 函数原型：


    
    
    const key_type_value_t* find_item_by_value (const key_type_value_t* items, uint32_t nr, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const key_type_value_t* | 返回资源类型枚值和名称的对应关系。  
items | const key_type_value_t* | 特定枚举值对应列表。  
nr | uint32_t | 列表长度。  
value | uint32_t | 资源的类型。  
  
#### input_type_find 函数

* * *

  * 函数功能：



> 获取输入类型值和名称的对应关系。

  * 函数原型：


    
    
    const key_type_value_t* input_type_find (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const key_type_value_t* | 返回输入类型值和名称的对应关系。  
name | const char* | 输入类型名。  
  
#### keys_type_find 函数

* * *

  * 函数功能：



> 获取按键值和名称的对应关系。

  * 函数原型：


    
    
    const key_type_value_t* keys_type_find (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const key_type_value_t* | 返回按键值和名称的对应关系。  
name | const char* | 按键名。  
  
#### keys_type_find_by_value 函数

* * *

  * 函数功能：



> 获取按键值和名称的对应关系。

  * 函数原型：


    
    
    const key_type_value_t* keys_type_find_by_value (uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const key_type_value_t* | 返回按键值和名称的对应关系。  
value | uint32_t | 按键值。  
  
#### keys_type_set_custom_keys 函数

* * *

  * 函数功能：



> 设置自定义键值表。 请确保键值表的生命周期在程序运行期一直存在，不要传入局部变量。

  * 函数原型：


    
    
    ret_t keys_type_set_custom_keys (const key_type_value_t* table, uint32_t nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
table | const key_type_value_t* | 键值表(NULL清除之前的设置)。  
nr | uint32_t | 键值表的长度。
