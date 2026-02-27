## endian_t

### 概述

字节顺序转换相关函数。

示例
    
    
    uint16_t a = 0x1234;
    ENSURE(is_little_endian());
    ENSURE(int16_endian_invert(a) == 0x3412);
    ENSURE(int16_from_big_endian(a) == 0x3412);
    ENSURE(int16_to_big_endian(a) == 0x3412);
    
    int32_t b = 0x12345678;
    ENSURE(int32_endian_invert(b) == 0x78563412);
    ENSURE(int32_from_big_endian(b) == 0x78563412);
    ENSURE(int32_to_big_endian(b) == 0x78563412);
    
    int64_t c = 0x1234567890ABCDEF;
    ENSURE(int64_endian_invert(c) == 0xEFCDAB9078563412);
    ENSURE(int64_from_big_endian(c) == 0xEFCDAB9078563412);
    ENSURE(int64_to_big_endian(c) == 0xEFCDAB9078563412);
    
    float f1 = 1.23;
    float f2 = float_endian_invert(f1);
    ENSURE(float_from_big_endian(f2) == f1);
    float f3 = float_from_big_endian(f2);
    ENSURE(float_to_big_endian(f3) == f2);
    
    double d1 = 1.2345678;
    double d2 = double_endian_invert(d1);
    ENSURE(double_from_big_endian(d2) == d1);
    double d3 = double_from_big_endian(d2);
    ENSURE(double_to_big_endian(d3) == d2);
    

* * *

### 函数

函数名称 | 说明  
---|---  
double_endian_invert | double浮点数大小端模式转换。  
double_from_big_endian | double浮点数转换为小端模式。  
double_to_big_endian | double浮点数转换为大端模式。  
float_endian_invert | float浮点数大小端模式转换。  
float_from_big_endian | float浮点数转换为小端模式。  
float_to_big_endian | float浮点数转换为大端模式。  
int16_endian_invert | 16 整数大小端模式转换。  
int16_from_big_endian | 16 整数转换为小端模式。  
int16_to_big_endian | 16 整数转换为大端模式。  
int32_endian_invert | 32 整数大小端模式转换。  
int32_from_big_endian | 32 整数转换为小端模式。  
int32_to_big_endian | 32 整数转换为大端模式。  
int64_endian_invert | 64 整数大小端模式转换。  
int64_from_big_endian | 64 整数转换为小端模式。  
int64_to_big_endian | 64 整数转换为大端模式。  
is_little_endian | 检查当前系统是否是小端模式。  
uint16_endian_invert | 16 无符号整数大小端模式转换。  
uint16_from_big_endian | 16 无符号整数转换为小端模式。  
uint16_to_big_endian | 16 无符号整数转换为大端模式。  
uint32_endian_invert | 32 无符号整数大小端模式转换。  
uint32_from_big_endian | 32 无符号整数转换为小端模式。  
uint32_to_big_endian | 32 无符号整数转换为大端模式。  
uint64_endian_invert | 64 无符号整数大小端模式转换。  
uint64_from_big_endian | 64 无符号整数转换为小端模式。  
uint64_to_big_endian | 64 无符号整数转换为大端模式。  
  
#### double_endian_invert 函数

* * *

  * 函数功能：



> double浮点数大小端模式转换。

  * 函数原型：


    
    
    double double_endian_invert (double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回转换后的数据。  
value | double | 输入数据。  
  
#### double_from_big_endian 函数

* * *

  * 函数功能：



> double浮点数转换为小端模式。

  * 函数原型：


    
    
    double double_from_big_endian (double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回转换后的数据。  
value | double | 输入数据。  
  
#### double_to_big_endian 函数

* * *

  * 函数功能：



> double浮点数转换为大端模式。

  * 函数原型：


    
    
    double double_to_big_endian (double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回转换后的数据。  
value | double | 输入数据。  
  
#### float_endian_invert 函数

* * *

  * 函数功能：



> float浮点数大小端模式转换。

  * 函数原型：


    
    
    float float_endian_invert (float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 返回转换后的数据。  
value | float | 输入数据。  
  
#### float_from_big_endian 函数

* * *

  * 函数功能：



> float浮点数转换为小端模式。

  * 函数原型：


    
    
    float float_from_big_endian (float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 返回转换后的数据。  
value | float | 输入数据。  
  
#### float_to_big_endian 函数

* * *

  * 函数功能：



> float浮点数转换为大端模式。

  * 函数原型：


    
    
    float float_to_big_endian (float value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 返回转换后的数据。  
value | float | 输入数据。  
  
#### int16_endian_invert 函数

* * *

  * 函数功能：



> 16 整数大小端模式转换。

  * 函数原型：


    
    
    int16_t int16_endian_invert (int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int16_t | 返回转换后的数据。  
value | int16_t | 输入数据。  
  
#### int16_from_big_endian 函数

* * *

  * 函数功能：



> 16 整数转换为小端模式。

  * 函数原型：


    
    
    int16_t int16_from_big_endian (int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int16_t | 返回转换后的数据。  
value | int16_t | 输入数据。  
  
#### int16_to_big_endian 函数

* * *

  * 函数功能：



> 16 整数转换为大端模式。

  * 函数原型：


    
    
    int16_t int16_to_big_endian (int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int16_t | 返回转换后的数据。  
value | int16_t | 输入数据。  
  
#### int32_endian_invert 函数

* * *

  * 函数功能：



> 32 整数大小端模式转换。

  * 函数原型：


    
    
    int32_t int32_endian_invert (int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回转换后的数据。  
value | int32_t | 输入数据。  
  
#### int32_from_big_endian 函数

* * *

  * 函数功能：



> 32 整数转换为小端模式。

  * 函数原型：


    
    
    int32_t int32_from_big_endian (int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回转换后的数据。  
value | int32_t | 输入数据。  
  
#### int32_to_big_endian 函数

* * *

  * 函数功能：



> 32 整数转换为大端模式。

  * 函数原型：


    
    
    int32_t int32_to_big_endian (int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回转换后的数据。  
value | int32_t | 输入数据。  
  
#### int64_endian_invert 函数

* * *

  * 函数功能：



> 64 整数大小端模式转换。

  * 函数原型：


    
    
    int64_t int64_endian_invert (int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回转换后的数据。  
value | int64_t | 输入数据。  
  
#### int64_from_big_endian 函数

* * *

  * 函数功能：



> 64 整数转换为小端模式。

  * 函数原型：


    
    
    int64_t int64_from_big_endian (int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回转换后的数据。  
value | int64_t | 输入数据。  
  
#### int64_to_big_endian 函数

* * *

  * 函数功能：



> 64 整数转换为大端模式。

  * 函数原型：


    
    
    int64_t int64_to_big_endian (int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回转换后的数据。  
value | int64_t | 输入数据。  
  
#### is_little_endian 函数

* * *

  * 函数功能：



> 检查当前系统是否是小端模式。

  * 函数原型：


    
    
    bool_t is_little_endian ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示不是。  
  
#### uint16_endian_invert 函数

* * *

  * 函数功能：



> 16 无符号整数大小端模式转换。

  * 函数原型：


    
    
    uint16_t uint16_endian_invert (uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回转换后的数据。  
value | uint16_t | 输入数据。  
  
#### uint16_from_big_endian 函数

* * *

  * 函数功能：



> 16 无符号整数转换为小端模式。

  * 函数原型：


    
    
    uint16_t uint16_from_big_endian (uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回转换后的数据。  
value | uint16_t | 输入数据。  
  
#### uint16_to_big_endian 函数

* * *

  * 函数功能：



> 16 无符号整数转换为大端模式。

  * 函数原型：


    
    
    uint16_t uint16_to_big_endian (uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回转换后的数据。  
value | uint16_t | 输入数据。  
  
#### uint32_endian_invert 函数

* * *

  * 函数功能：



> 32 无符号整数大小端模式转换。

  * 函数原型：


    
    
    uint32_t uint32_endian_invert (uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回转换后的数据。  
value | uint32_t | 输入数据。  
  
#### uint32_from_big_endian 函数

* * *

  * 函数功能：



> 32 无符号整数转换为小端模式。

  * 函数原型：


    
    
    uint32_t uint32_from_big_endian (uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回转换后的数据。  
value | uint32_t | 输入数据。  
  
#### uint32_to_big_endian 函数

* * *

  * 函数功能：



> 32 无符号整数转换为大端模式。

  * 函数原型：


    
    
    uint32_t uint32_to_big_endian (uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回转换后的数据。  
value | uint32_t | 输入数据。  
  
#### uint64_endian_invert 函数

* * *

  * 函数功能：



> 64 无符号整数大小端模式转换。

  * 函数原型：


    
    
    uint64_t uint64_endian_invert (uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回转换后的数据。  
value | uint64_t | 输入数据。  
  
#### uint64_from_big_endian 函数

* * *

  * 函数功能：



> 64 无符号整数转换为小端模式。

  * 函数原型：


    
    
    uint64_t uint64_from_big_endian (uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回转换后的数据。  
value | uint64_t | 输入数据。  
  
#### uint64_to_big_endian 函数

* * *

  * 函数功能：



> 64 无符号整数转换为大端模式。

  * 函数原型：


    
    
    uint64_t uint64_to_big_endian (uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回转换后的数据。  
value | uint64_t | 输入数据。
