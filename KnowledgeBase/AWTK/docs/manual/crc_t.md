## crc_t

### 概述

## crc相关函数。

### 函数

函数名称 | 说明  
---|---  
tk_chksum | 计算检验和。  
tk_chksum_byte | 计算单子节的检验和。  
tk_crc16 | 计算crc16。  
tk_crc16_byte | 计算单子节的crc16。  
tk_crc16_modbus | 计算crc16(MODBUS)。  
tk_crc32 | 计算crc32。  
tk_crc32_byte | 计算单子节的crc32。  
tk_crc32_file | 计算文件的crc32哈希值。  
  
#### tk_chksum 函数

* * *

  * 函数功能：



> 计算检验和。

  * 函数原型：


    
    
    uint16_t tk_chksum (uint16_t sum, const void* data, int size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回计算结果。  
sum | uint16_t | 初始值(一般用INITCHECKSUM)  
data | const void* | 数据。  
size | int | 数据长度。  
  
#### tk_chksum_byte 函数

* * *

  * 函数功能：



> 计算单子节的检验和。

  * 函数原型：


    
    
    uint16_t tk_chksum_byte (uint16_t sum, uint8_t data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回计算结果。  
sum | uint16_t | 初始值(一般用0，或者之前的值)  
data | uint8_t | 数据。  
  
#### tk_crc16 函数

* * *

  * 函数功能：



> 计算crc16。

  * 函数原型：


    
    
    uint16_t tk_crc16 (uint16_t crc, const void* data, int size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回计算结果。  
crc | uint16_t | 初始值(一般用PPPINITFCS16)  
data | const void* | 数据。  
size | int | 数据长度。  
  
#### tk_crc16_byte 函数

* * *

  * 函数功能：



> 计算单子节的crc16。

  * 函数原型：


    
    
    uint16_t tk_crc16_byte (uint16_t crc, uint8_t data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回计算结果。  
crc | uint16_t | 初始值(一般用PPPINITFCS16，或者之前的值)  
data | uint8_t | 数据。  
  
#### tk_crc16_modbus 函数

* * *

  * 函数功能：



> 计算crc16(MODBUS)。

  * 函数原型：


    
    
    uint16_t tk_crc16_modbus (const void* data, int size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回计算结果。  
data | const void* | 数据。  
size | int | 数据长度。  
  
#### tk_crc32 函数

* * *

  * 函数功能：



> 计算crc32。

  * 函数原型：


    
    
    uint32_t tk_crc32 (uint32_t crc, const void* data, int size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回计算结果。  
crc | uint32_t | 初始值(一般用PPPINITFCS32)  
data | const void* | 数据。  
size | int | 数据长度。  
  
#### tk_crc32_byte 函数

* * *

  * 函数功能：



> 计算单子节的crc32。

  * 函数原型：


    
    
    uint32_t tk_crc32_byte (uint32_t crc, uint8_t data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回计算结果。  
crc | uint32_t | 初始值(一般用PPPINITFCS32，或者之前的值)  
data | uint8_t | 数据。  
  
#### tk_crc32_file 函数

* * *

  * 函数功能：



> 计算文件的crc32哈希值。

  * 函数原型：


    
    
    uint32_t tk_crc32_file (const char* filename, uint32_t block_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回计算结果。  
filename | const char* | 文件名。  
block_size | uint32_t | 数据块长度。
