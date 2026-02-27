## rbuffer_t

### 概述

Read Buffer。用于数据解包。

示例：
    
    
    uint8_t buff[128];
    wbuffer_t wbuffer;
    rbuffer_t rbuffer;
    const char* str = NULL;
    wbuffer_init(&wbuffer, buff, sizeof(buff));
    
    wbuffer_write_string(&wbuffer, "hello awtk");
    
    rbuffer_init(&rbuffer, wbuffer.data, wbuffer.cursor);
    rbuffer_read_string(&rbuffer, &str);
    

* * *

### 函数

函数名称 | 说明  
---|---  
rbuffer_create | 创建rbuffer对象。  
rbuffer_deinit | 释放rbuffer资源。  
rbuffer_destroy | 销毁rbuffer对象。  
rbuffer_has_more | 判断是否还有数据可读。  
rbuffer_init | 初始rbuffer对象。  
rbuffer_peek_uint16 | 读取uint16数据，但不改变cursor的位置。  
rbuffer_peek_uint32 | 读取uint32数据，但不改变cursor的位置。  
rbuffer_peek_uint8 | 读取uint8数据，但不改变cursor的位置。  
rbuffer_read_binary | 读取指定长度的二进制数据。  
rbuffer_read_double | 读取double数据。  
rbuffer_read_float | 读取float数据。  
rbuffer_read_int16 | 读取int16数据。  
rbuffer_read_int32 | 读取int32数据。  
rbuffer_read_int64 | 读取int64数据。  
rbuffer_read_int8 | 读取int8数据。  
rbuffer_read_string | 读取字符串。  
rbuffer_read_uint16 | 读取uint16数据。  
rbuffer_read_uint32 | 读取uint32数据。  
rbuffer_read_uint64 | 读取uint64数据。  
rbuffer_read_uint8 | 读取uint8数据。  
rbuffer_read_value | 读取value数据。  
rbuffer_rewind | 重置当前读取位置。  
rbuffer_skip | 跳过指定的长度。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
capacity | uint32_t | 缓存区的容量。  
cursor | uint32_t | 当前读取位置。  
data | const uint8_t* | 数据缓冲区。  
  
#### rbuffer_create 函数

* * *

  * 函数功能：



> 创建rbuffer对象。

  * 函数原型：


    
    
    rbuffer_t* rbuffer_create (const void* data, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rbuffer_t* | rbuffer对象本身。  
data | const void* | 缓冲区。  
capacity | uint32_t | 缓冲区的容量。  
  
#### rbuffer_deinit 函数

* * *

  * 函数功能：



> 释放rbuffer资源。

  * 函数原型：


    
    
    ret_t rbuffer_deinit (rbuffer_t* rbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
  
#### rbuffer_destroy 函数

* * *

  * 函数功能：



> 销毁rbuffer对象。

  * 函数原型：


    
    
    ret_t rbuffer_destroy (rbuffer_t* rbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
  
#### rbuffer_has_more 函数

* * *

  * 函数功能：



> 判断是否还有数据可读。

  * 函数原型：


    
    
    bool_t rbuffer_has_more (rbuffer_t* rbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示还有数据可读，否则表示无数据可读。  
rbuffer | rbuffer_t* | rbuffer对象。  
  
#### rbuffer_init 函数

* * *

  * 函数功能：



> 初始rbuffer对象。

  * 函数原型：


    
    
    rbuffer_t* rbuffer_init (rbuffer_t* rbuffer, const void* data, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rbuffer_t* | rbuffer对象本身。  
rbuffer | rbuffer_t* | rbuffer对象。  
data | const void* | 缓冲区。  
capacity | uint32_t | 缓冲区的容量。  
  
#### rbuffer_peek_uint16 函数

* * *

  * 函数功能：



> 读取uint16数据，但不改变cursor的位置。

  * 函数原型：


    
    
    ret_t rbuffer_peek_uint16 (rbuffer_t* rbuffer, uint16_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | uint16_t* | 返回读取的数据。  
  
#### rbuffer_peek_uint32 函数

* * *

  * 函数功能：



> 读取uint32数据，但不改变cursor的位置。

  * 函数原型：


    
    
    ret_t rbuffer_peek_uint32 (rbuffer_t* rbuffer, uint32_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | uint32_t* | 读取的数据。  
  
#### rbuffer_peek_uint8 函数

* * *

  * 函数功能：



> 读取uint8数据，但不改变cursor的位置。

  * 函数原型：


    
    
    ret_t rbuffer_peek_uint8 (rbuffer_t* rbuffer, uint8_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | uint8_t* | 返回读取的数据。  
  
#### rbuffer_read_binary 函数

* * *

  * 函数功能：



> 读取指定长度的二进制数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_binary (rbuffer_t* rbuffer, void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
data | void* | 返回读取的数据。  
size | uint32_t | 读取的数据长度。  
  
#### rbuffer_read_double 函数

* * *

  * 函数功能：



> 读取double数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_double (rbuffer_t* rbuffer, double* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | double* | 返回读取的数据。  
  
#### rbuffer_read_float 函数

* * *

  * 函数功能：



> 读取float数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_float (rbuffer_t* rbuffer, float* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | float* | 返回读取的数据。  
  
#### rbuffer_read_int16 函数

* * *

  * 函数功能：



> 读取int16数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_int16 (rbuffer_t* rbuffer, int16_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | int16_t* | 读取的数据。  
  
#### rbuffer_read_int32 函数

* * *

  * 函数功能：



> 读取int32数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_int32 (rbuffer_t* rbuffer, int32_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | int32_t* | 返回读取的数据。  
  
#### rbuffer_read_int64 函数

* * *

  * 函数功能：



> 读取int64数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_int64 (rbuffer_t* rbuffer, int64_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | int64_t* | 返回读取的数据。  
  
#### rbuffer_read_int8 函数

* * *

  * 函数功能：



> 读取int8数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_int8 (rbuffer_t* rbuffer, int8_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | int8_t* | 返回读取的数据。  
  
#### rbuffer_read_string 函数

* * *

  * 函数功能：



> 读取字符串。

  * 函数原型：


    
    
    ret_t rbuffer_read_string (rbuffer_t* rbuffer, const char** str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
str | const char** | 返回字符串。  
  
#### rbuffer_read_uint16 函数

* * *

  * 函数功能：



> 读取uint16数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_uint16 (rbuffer_t* rbuffer, uint16_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | uint16_t* | 读取的数据。  
  
#### rbuffer_read_uint32 函数

* * *

  * 函数功能：



> 读取uint32数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_uint32 (rbuffer_t* rbuffer, uint32_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | uint32_t* | 返回读取的数据。  
  
#### rbuffer_read_uint64 函数

* * *

  * 函数功能：



> 读取uint64数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_uint64 (rbuffer_t* rbuffer, uint64_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | uint64_t* | 返回读取的数据。  
  
#### rbuffer_read_uint8 函数

* * *

  * 函数功能：



> 读取uint8数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_uint8 (rbuffer_t* rbuffer, uint8_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
value | uint8_t* | 返回读取的数据。  
  
#### rbuffer_read_value 函数

* * *

  * 函数功能：



> 读取value数据。

  * 函数原型：


    
    
    ret_t rbuffer_read_value (rbuffer_t* rbuffer, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
v | value_t* | 返回读取的数据。  
  
#### rbuffer_rewind 函数

* * *

  * 函数功能：



> 重置当前读取位置。

  * 函数原型：


    
    
    ret_t rbuffer_rewind (rbuffer_t* rbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
  
#### rbuffer_skip 函数

* * *

  * 函数功能：



> 跳过指定的长度。

  * 函数原型：


    
    
    ret_t rbuffer_skip (rbuffer_t* rbuffer, int32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rbuffer | rbuffer_t* | rbuffer对象。  
offset | int32_t | 跳过的偏移量，正数往前负数往回跳。  
  
#### capacity 属性

* * *

> 缓存区的容量。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### cursor 属性

* * *

> 当前读取位置。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### data 属性

* * *

> 数据缓冲区。

  * 类型：const uint8_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
