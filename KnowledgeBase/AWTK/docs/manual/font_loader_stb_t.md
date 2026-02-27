## font_loader_stb_t

### 概述

![image](images/font_loader_stb_t_0.png)

stb字体加载器。

## stb主要用于加载矢量字体(如truetype)，它功能强大，体积小巧。

### 函数

函数名称 | 说明  
---|---  
font_loader_stb | 获取stb字体加载器对象。  
font_loader_stb_mono | 获取stb mono字体加载器对象。  
font_stb_create | 创建stb字体对象。  
font_stb_mono_create | 创建stb mono字体对象。  
fscript_app_conf_register | 注册app_conf函数。  
fscript_array_get_fscript_array_vt | 获取 fscript array 的虚表。  
fscript_array_register | 注册typed array函数。  
fscript_bits_register | 注册数学函数。  
fscript_crc_register | 注册crc16/crc32/cksum等函数。  
fscript_date_time_register | 注册date time函数。  
fscript_endian_register | 注册大端小断转换函数等函数。  
fscript_ext_init | 注册扩展函数。  
fscript_fs_register | 注册文件系统函数。  
fscript_iostream_file_register | 注册iostream_file相关函数。  
fscript_iostream_inet_register | 注册iostream_inet相关函数。  
fscript_iostream_register | 注册iostream相关函数。  
fscript_iostream_serial_register | 注册iostream_serial相关函数。  
fscript_istream_register | 注册istream相关等函数。  
fscript_json_register | 注册json函数。  
fscript_math_register | 注册数学函数。  
  
#### font_loader_stb 函数

* * *

  * 函数功能：



> 获取stb字体加载器对象。

  * 函数原型：


    
    
    font_loader_t* font_loader_stb ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_loader_t* | 返回字体加载器对象。  
  
#### font_loader_stb_mono 函数

* * *

  * 函数功能：



> 获取stb mono字体加载器对象。

  * 函数原型：


    
    
    font_loader_t* font_loader_stb_mono ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_loader_t* | 返回字体加载器对象。  
  
#### font_stb_create 函数

* * *

  * 函数功能：



> 创建stb字体对象。

  * 函数原型：


    
    
    font_t* font_stb_create (const char* name, const uint8_t* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_t* | 返回字体对象。  
name | const char* | 字体名称。  
buff | const uint8_t* | 字体数据。  
size | uint32_t | 字体数据长度。  
  
#### font_stb_mono_create 函数

* * *

  * 函数功能：



> 创建stb mono字体对象。

  * 函数原型：


    
    
    font_t* font_stb_mono_create (const char* name, const uint8_t* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_t* | 返回字体对象。  
name | const char* | 字体名称。  
buff | const uint8_t* | 字体数据。  
size | uint32_t | 字体数据长度。  
  
#### fscript_app_conf_register 函数

* * *

  * 函数功能：



> 注册app_conf函数。

  * 函数原型：


    
    
    ret_t fscript_app_conf_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_array_get_fscript_array_vt 函数

* * *

  * 函数功能：



> 获取 fscript array 的虚表。

  * 函数原型：


    
    
    const fscript_array_vtable_t* fscript_array_get_fscript_array_vt (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const fscript_array_vtable_t* | 成功返回虚表指针，失败返回 NULL。  
obj | tk_object_t* | obj对象。  
  
#### fscript_array_register 函数

* * *

  * 函数功能：



> 注册typed array函数。

  * 函数原型：


    
    
    ret_t fscript_array_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_bits_register 函数

* * *

  * 函数功能：



> 注册数学函数。

  * 函数原型：


    
    
    ret_t fscript_bits_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_crc_register 函数

* * *

  * 函数功能：



> 注册crc16/crc32/cksum等函数。

  * 函数原型：


    
    
    ret_t fscript_crc_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_date_time_register 函数

* * *

  * 函数功能：



> 注册date time函数。

  * 函数原型：


    
    
    ret_t fscript_date_time_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_endian_register 函数

* * *

  * 函数功能：



> 注册大端小断转换函数等函数。

  * 函数原型：


    
    
    ret_t fscript_endian_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_ext_init 函数

* * *

  * 函数功能：



> 注册扩展函数。

  * 函数原型：


    
    
    ret_t fscript_ext_init ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_fs_register 函数

* * *

  * 函数功能：



> 注册文件系统函数。

  * 函数原型：


    
    
    ret_t fscript_fs_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_iostream_file_register 函数

* * *

  * 函数功能：



> 注册iostream_file相关函数。

  * 函数原型：


    
    
    ret_t fscript_iostream_file_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_iostream_inet_register 函数

* * *

  * 函数功能：



> 注册iostream_inet相关函数。

  * 函数原型：


    
    
    ret_t fscript_iostream_inet_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_iostream_register 函数

* * *

  * 函数功能：



> 注册iostream相关函数。

  * 函数原型：


    
    
    ret_t fscript_iostream_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_iostream_serial_register 函数

* * *

  * 函数功能：



> 注册iostream_serial相关函数。

  * 函数原型：


    
    
    ret_t fscript_iostream_serial_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_istream_register 函数

* * *

  * 函数功能：



> 注册istream相关等函数。

  * 函数原型：


    
    
    ret_t fscript_istream_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_json_register 函数

* * *

  * 函数功能：



> 注册json函数。

  * 函数原型：


    
    
    ret_t fscript_json_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### fscript_math_register 函数

* * *

  * 函数功能：



> 注册数学函数。

  * 函数原型：


    
    
    ret_t fscript_math_register ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。
