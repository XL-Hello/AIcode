## color_t

### 概述

## 颜色。

### 函数

函数名称 | 说明  
---|---  
color_a | 获取alpha通道的值。  
color_b | 获取蓝色通道的值。  
color_cast | 转换为color对象。  
color_create | 创建color对象。  
color_destroy | 销毁color对象。  
color_from_str | 创建color对象。  
color_g | 获取绿色通道的值。  
color_get_color | 获取颜色值。  
color_hex_str | 获取16进制格式表示的颜色  
color_init | 初始化颜色对象。  
color_r | 获取红色通道的值。  
color_rgba_str | 获取rgba格式表示的颜色  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
color | uint32_t | 颜色的数值。  
rgba | rgba_t | 颜色的RGBA值。  
  
#### color_a 函数

* * *

  * 函数功能：



> 获取alpha通道的值。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    uint8_t color_a (color_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t | 返回alpha通道的值。  
c | color_t* | color对象。  
  
#### color_b 函数

* * *

  * 函数功能：



> 获取蓝色通道的值。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    uint8_t color_b (color_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t | 返回蓝色通道的值。  
c | color_t* | color对象。  
  
#### color_cast 函数

* * *

  * 函数功能：



> 转换为color对象。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    color_t* color_cast (color_t* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t* | color对象。  
color | color_t* | color对象。  
  
#### color_create 函数

* * *

  * 函数功能：



> 创建color对象。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    color_t* color_create (uint8_t r, uint8_t g, uint8_t b, uint8_t a);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t* | color对象。  
r | uint8_t | 红色通道。  
g | uint8_t | 绿色通道。  
b | uint8_t | 蓝色通道。  
a | uint8_t | alpha通道。  
  
#### color_destroy 函数

* * *

  * 函数功能：



> 销毁color对象。 主要供脚本语言使用。

  * 函数原型：


    
    
    ret_t color_destroy (color_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | color_t* | color对象。  
  
#### color_from_str 函数

* * *

  * 函数功能：



> 创建color对象。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    color_t* color_from_str (color_t* c, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t* | color对象。  
c | color_t* | color对象。  
str | const char* | css类似的颜色值。  
  
#### color_g 函数

* * *

  * 函数功能：



> 获取绿色通道的值。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    uint8_t color_g (color_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t | 返回绿色通道的值。  
c | color_t* | color对象。  
  
#### color_get_color 函数

* * *

  * 函数功能：



> 获取颜色值。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    uint32_t color_get_color (color_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回颜色值。  
c | color_t* | color对象。  
  
#### color_hex_str 函数

* * *

  * 函数功能：



> 获取16进制格式表示的颜色

  * 函数原型：


    
    
    const char* color_hex_str (color_t c, char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 获取16进制字符串表示的颜色。  
c | color_t | color对象。  
str | char* | 内存。  
  
#### color_init 函数

* * *

  * 函数功能：



> 初始化颜色对象。

  * 函数原型：


    
    
    color_t color_init (uint8_t r, uint8_t g, uint8_t b, uint8_t a);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t | 颜色对象。  
r | uint8_t | 红色。  
g | uint8_t | 绿色。  
b | uint8_t | 蓝色。  
a | uint8_t | alpha。  
  
#### color_r 函数

* * *

  * 函数功能：



> 获取红色通道的值。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    uint8_t color_r (color_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t | 返回红色通道的值。  
c | color_t* | color对象。  
  
#### color_rgba_str 函数

* * *

  * 函数功能：



> 获取rgba格式表示的颜色

  * 函数原型：


    
    
    const char* color_rgba_str (color_t c, char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 获取rgba格式表示的颜色。  
c | color_t | color对象。  
str | char* | 内存。  
  
#### color 属性

* * *

> 颜色的数值。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 是  
可脚本化 | 是  
  
#### rgba 属性

* * *

> 颜色的RGBA值。

  * 类型：rgba_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 是
