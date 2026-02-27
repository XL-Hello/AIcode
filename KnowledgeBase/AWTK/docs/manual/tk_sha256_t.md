## tk_sha256_t

### 概述

## sha256

### 函数

函数名称 | 说明  
---|---  
tk_sha256 | 计算数据的sha256哈希值。  
tk_sha256_done | 完成计算。  
tk_sha256_file | 计算文件的sha256哈希值。  
tk_sha256_hash | 更新数据。  
tk_sha256_hash_from_str | 从字符串中提取哈希值。  
tk_sha256_hash_to_str | 哈希值转为字符串形式。  
tk_sha256_init | 初始化。  
  
#### tk_sha256 函数

* * *

  * 函数功能：



> 计算数据的sha256哈希值。

  * 函数原型：


    
    
    ret_t tk_sha256 (const void* data, uint32_t len, str_t* hash);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
data | const void* | 数据。  
len | uint32_t | 数据长度。  
hash | str_t* | 用于返回计算结果。  
  
#### tk_sha256_done 函数

* * *

  * 函数功能：



> 完成计算。

  * 函数原型：


    
    
    ret_t tk_sha256_done (tk_sha256_t* sha256, uint8_t* hash);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sha256 | tk_sha256_t* | sha256对象。  
hash | uint8_t* | 用于返回计算结果。  
  
#### tk_sha256_file 函数

* * *

  * 函数功能：



> 计算文件的sha256哈希值。

  * 函数原型：


    
    
    ret_t tk_sha256_file (const char* filename, uint32_t block_size, str_t* hash);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | const char* | 文件名。  
block_size | uint32_t | 数据块长度。  
hash | str_t* | 用于返回计算结果。  
  
#### tk_sha256_hash 函数

* * *

  * 函数功能：



> 更新数据。

  * 函数原型：


    
    
    ret_t tk_sha256_hash (tk_sha256_t* sha256, const uint8_t* data, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sha256 | tk_sha256_t* | sha256对象。  
data | const uint8_t* | 数据。  
len | uint32_t | 数据长度。  
  
#### tk_sha256_hash_from_str 函数

* * *

  * 函数功能：



> 从字符串中提取哈希值。

  * 函数原型：


    
    
    ret_t tk_sha256_hash_from_str (uint8_t* hash, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash | uint8_t* | 哈希值。  
str | const char* | 哈希值字符串形式。  
  
#### tk_sha256_hash_to_str 函数

* * *

  * 函数功能：



> 哈希值转为字符串形式。

  * 函数原型：


    
    
    ret_t tk_sha256_hash_to_str (uint8_t* hash, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash | uint8_t* | 哈希值。  
str | const char* | 哈希值字符串形式。  
  
#### tk_sha256_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    ret_t tk_sha256_init (tk_sha256_t* sha256);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
sha256 | tk_sha256_t* | sha256对象。
