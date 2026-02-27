## font_loader_t

### 概述

## 字体加载接口。

### 函数

函数名称 | 说明  
---|---  
font_loader_load | 加载字体。  
  
#### font_loader_load 函数

* * *

  * 函数功能：



> 加载字体。

  * 函数原型：


    
    
    font_t* font_loader_load (font_loader_t* loader, const char* name, const uint8_t* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_t* | 成功返回font，失败返回NULL。  
loader | font_loader_t* | loader对象。  
name | const char* | 字体名字。  
buff | const uint8_t* | 字体数据。  
size | uint32_t | 字体数据长度。
