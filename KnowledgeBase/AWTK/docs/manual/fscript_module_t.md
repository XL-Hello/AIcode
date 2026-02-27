## fscript_module_t

### 概述

![image](images/fscript_module_t_0.png)

## 用require加载外部模块。

### 函数

函数名称 | 说明  
---|---  
fargs_get_data_and_size | 从参数中获取数据和长度。  
fscript_module_cast | 转换为fscript_module对象。  
fscript_module_create | 创建对象。  
fscript_module_register | 注册module函数。  
fscript_object_register | 注册object函数。  
fscript_ostream_register | 注册ostream相关函数。  
fscript_rbuffer_register | 注册rbuffer相关函数。  
fscript_typed_array_register | 注册typed array函数。  
fscript_wbuffer_register | 注册wbuffer相关函数。  
fscript_widget_register | 注册widget函数。  
  
#### fargs_get_data_and_size 函数

* * *

  * 函数功能：



> 从参数中获取数据和长度。

  * 函数原型：


    
    
    ret_t fargs_get_data_and_size (fscript_args_t* args, const uint8_t** ret_data, uint32_t* ret_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
args | fscript_args_t* | 参数。  
ret_data | const uint8_t** | 返回数据。  
ret_size | uint32_t* | 返回数据的长度。  
  
#### fscript_module_cast 函数

* * *

  * 函数功能：



> 转换为fscript_module对象。

  * 函数原型：


    
    
    fscript_module_t* fscript_module_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fscript_module_t* | fscript_module对象。  
obj | tk_object_t* | fscript_module对象。  
  
#### fscript_module_create 函数

* * *

  * 函数功能：



> 创建对象。

  * 函数原型：


    
    
    tk_object_t* fscript_module_create (const char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
url | const char* | URL(用于读取数据)  
  
#### fscript_module_register 函数

* * *

  * 函数功能：



> 注册module函数。

  * 函数原型：


    
    
    ret_t fscript_module_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_object_register 函数

* * *

  * 函数功能：



> 注册object函数。

  * 函数原型：


    
    
    ret_t fscript_object_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_ostream_register 函数

* * *

  * 函数功能：



> 注册ostream相关函数。

  * 函数原型：


    
    
    ret_t fscript_ostream_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_rbuffer_register 函数

* * *

  * 函数功能：



> 注册rbuffer相关函数。

  * 函数原型：


    
    
    ret_t fscript_rbuffer_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_typed_array_register 函数

* * *

  * 函数功能：



> 注册typed array函数。

  * 函数原型：


    
    
    ret_t fscript_typed_array_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_wbuffer_register 函数

* * *

  * 函数功能：



> 注册wbuffer相关函数。

  * 函数原型：


    
    
    ret_t fscript_wbuffer_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_widget_register 函数

* * *

  * 函数功能：



> 注册widget函数。

  * 函数原型：


    
    
    ret_t fscript_widget_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。
