## gradient_t

### 概述

## 渐变。

### 函数

函数名称 | 说明  
---|---  
gradient_add_stop | 增加关键点。  
gradient_deinit | 释放gradient对象。  
gradient_get_color | 获取颜色。  
gradient_get_first_color | 获取开始的颜色。  
gradient_get_last_color | 获取结束的颜色。  
gradient_get_stop | 获取关键点。  
gradient_init | 初始化gradient对象。  
gradient_init_from_binary | 从二进制数据初始化gradient对象。  
gradient_init_from_str | 从字符串初始化gradient对象。  
gradient_init_simple | 初始化gradient对象。  
gradient_set_linear_degree | 设置线性渐变的角度。  
gradient_set_type | 设置类型。  
gradient_to_binary | 转成二进制格式。  
gradient_to_str | 转换成字符串格式。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
degree | uint32_t | 线性渐变的角度。  
nr | uint32_t | stop个数。  
type | gradient_type_t | 类型。  
  
#### gradient_add_stop 函数

* * *

  * 函数功能：



> 增加关键点。

  * 函数原型：


    
    
    ret_t gradient_add_stop (gradient_t* gradient, color_t color, float stop);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
gradient | gradient_t* | gradient对象。  
color | color_t | 颜色。  
stop | float | 位置。  
  
#### gradient_deinit 函数

* * *

  * 函数功能：



> 释放gradient对象。

  * 函数原型：


    
    
    ret_t gradient_deinit (gradient_t* gradient);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
gradient | gradient_t* | gradient对象。  
  
#### gradient_get_color 函数

* * *

  * 函数功能：



> 获取颜色。

  * 函数原型：


    
    
    color_t gradient_get_color (gradient_t* gradient, float offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t | 返回颜色。  
gradient | gradient_t* | gradient对象。  
offset | float | 偏移(0-1)。  
  
#### gradient_get_first_color 函数

* * *

  * 函数功能：



> 获取开始的颜色。

  * 函数原型：


    
    
    color_t gradient_get_first_color (const gradient_t* gradient);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t | 返回颜色。  
gradient | const gradient_t* | gradient对象。  
  
#### gradient_get_last_color 函数

* * *

  * 函数功能：



> 获取结束的颜色。

  * 函数原型：


    
    
    color_t gradient_get_last_color (const gradient_t* gradient);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t | 返回颜色。  
gradient | const gradient_t* | gradient对象。  
  
#### gradient_get_stop 函数

* * *

  * 函数功能：



> 获取关键点。

  * 函数原型：


    
    
    const gradient_stop_t* gradient_get_stop (const gradient_t* gradient, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const gradient_stop_t* | 返回index指定的关键点。  
gradient | const gradient_t* | gradient对象。  
index | uint32_t | 序数。  
  
#### gradient_init 函数

* * *

  * 函数功能：



> 初始化gradient对象。

  * 函数原型：


    
    
    gradient_t* gradient_init (gradient_t* gradient);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | gradient_t* | 返回gradient对象。  
gradient | gradient_t* | gradient对象。  
  
#### gradient_init_from_binary 函数

* * *

  * 函数功能：



> 从二进制数据初始化gradient对象。
> 
> 二进制数据必须由gradient_to_binary生成。

  * 函数原型：


    
    
    gradient_t* gradient_init_from_binary (gradient_t* gradient, const uint8_t* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | gradient_t* | 返回gradient对象。  
gradient | gradient_t* | gradient对象。  
data | const uint8_t* | 数据。  
size | uint32_t | 数据长度。  
  
#### gradient_init_from_str 函数

* * *

  * 函数功能：



> 从字符串初始化gradient对象。
> 
> 字符串的格式兼容CSS，请参考相关文档。

  * 函数原型：


    
    
    gradient_t* gradient_init_from_str (gradient_t* gradient, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | gradient_t* | 返回gradient对象。  
gradient | gradient_t* | gradient对象。  
str | const char* | 字符串。  
  
#### gradient_init_simple 函数

* * *

  * 函数功能：



> 初始化gradient对象。

  * 函数原型：


    
    
    gradient_t* gradient_init_simple (gradient_t* gradient, uint32_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | gradient_t* | 返回gradient对象。  
gradient | gradient_t* | gradient对象。  
color | uint32_t | 颜色。  
  
#### gradient_set_linear_degree 函数

* * *

  * 函数功能：



> 设置线性渐变的角度。

  * 函数原型：


    
    
    ret_t gradient_set_linear_degree (gradient_t* gradient, uint32_t degree);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
gradient | gradient_t* | gradient对象。  
degree | uint32_t | 角度。  
  
#### gradient_set_type 函数

* * *

  * 函数功能：



> 设置类型。

  * 函数原型：


    
    
    ret_t gradient_set_type (gradient_t* gradient, gradient_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
gradient | gradient_t* | gradient对象。  
type | gradient_type_t | 类型。  
  
#### gradient_to_binary 函数

* * *

  * 函数功能：



> 转成二进制格式。

  * 函数原型：


    
    
    ret_t gradient_to_binary (gradient_t* gradient, wbuffer_t* wb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
gradient | gradient_t* | gradient对象。  
wb | wbuffer_t* | 二进制数据。  
  
#### gradient_to_str 函数

* * *

  * 函数功能：



> 转换成字符串格式。

  * 函数原型：


    
    
    ret_t gradient_to_str (gradient_t* gradient, str_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
gradient | gradient_t* | gradient对象。  
str | str_t* | 字符串。  
  
#### degree 属性

* * *

> 线性渐变的角度。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### nr 属性

* * *

> stop个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### type 属性

* * *

> 类型。

  * 类型：gradient_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
