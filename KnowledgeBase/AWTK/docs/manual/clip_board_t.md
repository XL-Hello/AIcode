## clip_board_t

### 概述

## 剪切板接口。

### 函数

函数名称 | 说明  
---|---  
clip_board | 获取缺省的剪切板对象。  
clip_board_clear | 清空剪切板中的数据。  
clip_board_destroy | 销毁剪切板对象。  
clip_board_get_data | 从剪切板中获取数据。  
clip_board_get_text | 从剪切板中获取文本(UTF8)数据。  
clip_board_set | 设置缺省的剪切板对象。  
clip_board_set_data | 设置数据到剪切板中。  
clip_board_set_text | 设置文本(UTF8)数据到剪切板。  
  
#### clip_board 函数

* * *

  * 函数功能：



> 获取缺省的剪切板对象。

  * 函数原型：


    
    
    clip_board_t* clip_board ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | clip_board_t* | 返回缺省剪切板对象。  
  
#### clip_board_clear 函数

* * *

  * 函数功能：



> 清空剪切板中的数据。

  * 函数原型：


    
    
    ret_t clip_board_clear (clip_board_t* cl);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cl | clip_board_t* | 剪切板对象。  
  
#### clip_board_destroy 函数

* * *

  * 函数功能：



> 销毁剪切板对象。

  * 函数原型：


    
    
    ret_t clip_board_destroy (clip_board_t* cl);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cl | clip_board_t* | 剪切板对象。  
  
#### clip_board_get_data 函数

* * *

  * 函数功能：



> 从剪切板中获取数据。

  * 函数原型：


    
    
    ret_t clip_board_get_data (clip_board_t* cl, clip_board_data_type_t* type, const void** data, uint32_t* size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cl | clip_board_t* | 剪切板对象。  
type | clip_board_data_type_t* | 返回数据类型(可为NULL)。  
data | const void** | 返回数据(可为NULL)。  
size | uint32_t* | 返回数据长度(可为NULL)。  
  
#### clip_board_get_text 函数

* * *

  * 函数功能：



> 从剪切板中获取文本(UTF8)数据。

  * 函数原型：


    
    
    const char* clip_board_get_text ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回文本数据。  
  
#### clip_board_set 函数

* * *

  * 函数功能：



> 设置缺省的剪切板对象。

  * 函数原型：


    
    
    ret_t clip_board_set (clip_board_t* cl);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cl | clip_board_t* | 剪切板对象。  
  
#### clip_board_set_data 函数

* * *

  * 函数功能：



> 设置数据到剪切板中。

  * 函数原型：


    
    
    ret_t clip_board_set_data (clip_board_t* cl, clip_board_data_type_t type, const void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
cl | clip_board_t* | 剪切板对象。  
type | clip_board_data_type_t | 数据类型。  
data | const void* | 数据。  
size | uint32_t | 数据长度  
  
#### clip_board_set_text 函数

* * *

  * 函数功能：



> 设置文本(UTF8)数据到剪切板。

  * 函数原型：


    
    
    ret_t clip_board_set_text (const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text | const char* | 文本。
