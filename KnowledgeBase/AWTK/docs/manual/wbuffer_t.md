## wbuffer_t

### 概述

Write Buffer。用于数据打包。

示例：
    
    
    uint8_t buff[128];
    wbuffer_t wbuffer;
    rbuffer_t rbuffer;
    const char* str = NULL;
    wbuffer_init(&wbuffer, buff, sizeof(buff));
    
    wbuffer_write_string(&wbuffer, "hello awtk");
    
    rbuffer_init(&rbuffer, wbuffer.data, wbuffer.cursor);
    rbuffer_read_string(&rbuffer, &str);
    
    
    
    wbuffer_t wbuffer;
    wbuffer_init_extendable(&wbuffer);
    
    wbuffer_write_string(&wbuffer, "hello awtk");
    
    wbuffer_deinit(&wbuffer);
    

## > 如果初始化为extendable，则最后需要调用wbuffer_deinit释放资源。

### 函数

函数名称 | 说明  
---|---  
wbuffer_create | 创建wbuffer对象。  
wbuffer_create_extendable | 创建可自动扩展的wbuffer对象。  
wbuffer_deinit | 释放资源。  
wbuffer_destroy | 销毁wbuffer对象。  
wbuffer_extend_capacity | 扩展缓冲区至指定的大小。  
wbuffer_has_room | 是否还有空间。  
wbuffer_init | 初始wbuffer对象。  
wbuffer_init_extendable | 初始化可自动扩展的wbuffer对象。使用完成后需要调用wbuffer_deinit释放资源。  
wbuffer_rewind | 重置当前写入位置。  
wbuffer_skip | 跳过指定的长度。  
wbuffer_write_binary | 写入指定长度的二进制数据。  
wbuffer_write_double | 写入double数据。  
wbuffer_write_float | 写入float数据。  
wbuffer_write_int16 | 写入int16数据。  
wbuffer_write_int32 | 写入int32数据。  
wbuffer_write_int64 | 写入int64数据。  
wbuffer_write_int8 | 写入int8数据。  
wbuffer_write_string | 写入字符串。  
wbuffer_write_uint16 | 写入uint16数据。  
wbuffer_write_uint32 | 写入uint32数据。  
wbuffer_write_uint64 | 写入uint64数据。  
wbuffer_write_uint8 | 写入uint8数据。  
wbuffer_write_value | 写入value数据。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
capacity | uint32_t | 数据缓冲区最大容量。  
cursor | uint32_t | 当前写入位置。  
data | uint8_t* | 数据缓冲区。用于保存写入的数据。  
extendable | bool_t | 容量不够时是否支持自动扩展。  
  
#### wbuffer_create 函数

* * *

  * 函数功能：



> 创建wbuffer对象。

  * 函数原型：


    
    
    wbuffer_t* wbuffer_create (void* data, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wbuffer_t* | wbuffer对象本身。  
data | void* | 缓冲区。  
capacity | uint32_t | 缓冲区的容量。  
  
#### wbuffer_create_extendable 函数

* * *

  * 函数功能：



> 创建可自动扩展的wbuffer对象。

  * 函数原型：


    
    
    wbuffer_t* wbuffer_create_extendable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wbuffer_t* | wbuffer对象本身。  
  
#### wbuffer_deinit 函数

* * *

  * 函数功能：



> 释放资源。

  * 函数原型：


    
    
    ret_t wbuffer_deinit (wbuffer_t* wbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
  
#### wbuffer_destroy 函数

* * *

  * 函数功能：



> 销毁wbuffer对象。

  * 函数原型：


    
    
    ret_t wbuffer_destroy (wbuffer_t* wbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
  
#### wbuffer_extend_capacity 函数

* * *

  * 函数功能：



> 扩展缓冲区至指定的大小。

  * 函数原型：


    
    
    ret_t wbuffer_extend_capacity (wbuffer_t* wbuffer, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
capacity | uint32_t | 缓冲区的容量。  
  
#### wbuffer_has_room 函数

* * *

  * 函数功能：



> 是否还有空间。

  * 函数原型：


    
    
    bool_t wbuffer_has_room (wbuffer_t* wbuffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示无，否则表示有。  
wbuffer | wbuffer_t* | wbuffer对象。  
size | uint32_t | 空间大小。  
  
#### wbuffer_init 函数

* * *

  * 函数功能：



> 初始wbuffer对象。

  * 函数原型：


    
    
    wbuffer_t* wbuffer_init (wbuffer_t* wbuffer, void* data, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wbuffer_t* | wbuffer对象本身。  
wbuffer | wbuffer_t* | wbuffer对象。  
data | void* | 缓冲区。  
capacity | uint32_t | 缓冲区的容量。  
  
#### wbuffer_init_extendable 函数

* * *

  * 函数功能：



> 初始化可自动扩展的wbuffer对象。使用完成后需要调用wbuffer_deinit释放资源。

  * 函数原型：


    
    
    wbuffer_t* wbuffer_init_extendable (wbuffer_t* wbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wbuffer_t* | wbuffer对象本身。  
wbuffer | wbuffer_t* | wbuffer对象。  
  
#### wbuffer_rewind 函数

* * *

  * 函数功能：



> 重置当前写入位置。

  * 函数原型：


    
    
    ret_t wbuffer_rewind (wbuffer_t* wbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
  
#### wbuffer_skip 函数

* * *

  * 函数功能：



> 跳过指定的长度。

  * 函数原型：


    
    
    ret_t wbuffer_skip (wbuffer_t* wbuffer, int32_t delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
delta | int32_t | 跳过的偏移量，正数往前负数往回跳。  
  
#### wbuffer_write_binary 函数

* * *

  * 函数功能：



> 写入指定长度的二进制数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_binary (wbuffer_t* wbuffer, const void* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
data | const void* | 要写入的数据。  
size | uint32_t | 要写入的数据长度。  
  
#### wbuffer_write_double 函数

* * *

  * 函数功能：



> 写入double数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_double (wbuffer_t* wbuffer, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | double | 要写入的数据。  
  
#### wbuffer_write_float 函数

* * *

  * 函数功能：



> 写入float数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_float (wbuffer_t* wbuffer, float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | float | 要写入的数据。  
  
#### wbuffer_write_int16 函数

* * *

  * 函数功能：



> 写入int16数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_int16 (wbuffer_t* wbuffer, int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | int16_t | 要写入的数据。  
  
#### wbuffer_write_int32 函数

* * *

  * 函数功能：



> 写入int32数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_int32 (wbuffer_t* wbuffer, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | int32_t | 要写入的数据。  
  
#### wbuffer_write_int64 函数

* * *

  * 函数功能：



> 写入int64数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_int64 (wbuffer_t* wbuffer, int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | int64_t | 要写入的数据。  
  
#### wbuffer_write_int8 函数

* * *

  * 函数功能：



> 写入int8数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_int8 (wbuffer_t* wbuffer, int8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | int8_t | 要写入的数据。  
  
#### wbuffer_write_string 函数

* * *

  * 函数功能：



> 写入字符串。

  * 函数原型：


    
    
    ret_t wbuffer_write_string (wbuffer_t* wbuffer, const char* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
data | const char* | 要写入的字符串。  
  
#### wbuffer_write_uint16 函数

* * *

  * 函数功能：



> 写入uint16数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_uint16 (wbuffer_t* wbuffer, uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | uint16_t | 要写入的数据。  
  
#### wbuffer_write_uint32 函数

* * *

  * 函数功能：



> 写入uint32数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_uint32 (wbuffer_t* wbuffer, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | uint32_t | 要写入的数据。  
  
#### wbuffer_write_uint64 函数

* * *

  * 函数功能：



> 写入uint64数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_uint64 (wbuffer_t* wbuffer, uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | uint64_t | 要写入的数据。  
  
#### wbuffer_write_uint8 函数

* * *

  * 函数功能：



> 写入uint8数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_uint8 (wbuffer_t* wbuffer, uint8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
value | uint8_t | 要写入的数据。  
  
#### wbuffer_write_value 函数

* * *

  * 函数功能：



> 写入value数据。

  * 函数原型：


    
    
    ret_t wbuffer_write_value (wbuffer_t* wbuffer, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wbuffer | wbuffer_t* | wbuffer对象。  
v | const value_t* | 要写入的数据。  
  
#### capacity 属性

* * *

> 数据缓冲区最大容量。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### cursor 属性

* * *

> 当前写入位置。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### data 属性

* * *

> 数据缓冲区。用于保存写入的数据。

  * 类型：uint8_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### extendable 属性

* * *

> 容量不够时是否支持自动扩展。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
