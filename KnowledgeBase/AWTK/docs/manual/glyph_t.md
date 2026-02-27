## glyph_t

### 概述

## 代表一个字符的字模。

### 函数

函数名称 | 说明  
---|---  
glyph_clone | 克隆glyph对象。  
glyph_create | 创建glyph对象。  
glyph_destroy | 销毁glyph对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
advance | uint16_t | 占位宽度。  
data | const uint8_t* | 数据。  
format | uint8_t | 格式。  
h | uint16_t | 高度。  
pitch | uint8_t | pitch。  
w | uint16_t | 宽度。  
x | int16_t | x坐标。  
y | int16_t | y坐标。  
  
#### glyph_clone 函数

* * *

  * 函数功能：



> 克隆glyph对象。

  * 函数原型：


    
    
    glyph_t* glyph_clone (glyph_t* g);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | glyph_t* | glyph对象。  
g | glyph_t* | glyph对象。  
  
#### glyph_create 函数

* * *

  * 函数功能：



> 创建glyph对象。

  * 函数原型：


    
    
    glyph_t* glyph_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | glyph_t* | glyph对象。  
  
#### glyph_destroy 函数

* * *

  * 函数功能：



> 销毁glyph对象。

  * 函数原型：


    
    
    ret_t glyph_destroy (glyph_t* g);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
g | glyph_t* | glyph对象。  
  
#### advance 属性

* * *

> 占位宽度。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### data 属性

* * *

> 数据。

  * 类型：const uint8_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### format 属性

* * *

> 格式。

  * 类型：uint8_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### h 属性

* * *

> 高度。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### pitch 属性

* * *

> pitch。

  * 类型：uint8_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### w 属性

* * *

> 宽度。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### x 属性

* * *

> x坐标。

  * 类型：int16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### y 属性

* * *

> y坐标。

  * 类型：int16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
