## dirty_rects_t

### 概述

支持多个脏矩形。

> 在通常情况下，脏矩形的个数并不多，而且一般都是不重叠的， 所以为了降低计算开销、避免内存分配和简化实现。这里采用下列措施：

  * 如果新的脏矩形是独立的，直接加入进来。
  * 如果新的脏矩形与某个脏矩形有重叠，则合并到该脏矩形。
  * 如果脏矩形的个数超出最大个数则进行合并。



* * *

### 函数

函数名称 | 说明  
---|---  
dirty_rects_add | 增加脏矩形。  
dirty_rects_deinit | 释放dirty_rects对象。  
dirty_rects_fix | 脏矩形之间可能重叠，合并重叠的脏矩形。  
dirty_rects_init | 初始化dirty_rects对象。  
dirty_rects_remove | 删除指定序数的矩形。  
dirty_rects_reset | 重置dirty_rects对象。  
dirty_rects_set_debug | 设置是否开启调试模式。  
dirty_rects_set_disable_multiple | 设置是否关闭多脏矩形模式(方便对比测试和调试)。  
dirty_rects_set_profile | 设置是否开启profile模式。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
max | rect_t | 最大脏矩形。  
nr | uint32_t | 个数。  
rects | rect_t* | 脏矩形。  
  
#### dirty_rects_add 函数

* * *

  * 函数功能：



> 增加脏矩形。

  * 函数原型：


    
    
    ret_t dirty_rects_add (dirty_rects_t* dirty_rects, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
r | const rect_t* | 脏矩形。  
  
#### dirty_rects_deinit 函数

* * *

  * 函数功能：



> 释放dirty_rects对象。

  * 函数原型：


    
    
    ret_t dirty_rects_deinit (dirty_rects_t* dirty_rects);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
  
#### dirty_rects_fix 函数

* * *

  * 函数功能：



> 脏矩形之间可能重叠，合并重叠的脏矩形。

  * 函数原型：


    
    
    ret_t dirty_rects_fix (dirty_rects_t* dirty_rects);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
  
#### dirty_rects_init 函数

* * *

  * 函数功能：



> 初始化dirty_rects对象。

  * 函数原型：


    
    
    ret_t dirty_rects_init (dirty_rects_t* dirty_rects);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
  
#### dirty_rects_remove 函数

* * *

  * 函数功能：



> 删除指定序数的矩形。

  * 函数原型：


    
    
    ret_t dirty_rects_remove (dirty_rects_t* dirty_rects, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
index | uint32_t | 序数。  
  
#### dirty_rects_reset 函数

* * *

  * 函数功能：



> 重置dirty_rects对象。

  * 函数原型：


    
    
    ret_t dirty_rects_reset (dirty_rects_t* dirty_rects);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
  
#### dirty_rects_set_debug 函数

* * *

  * 函数功能：



> 设置是否开启调试模式。

  * 函数原型：


    
    
    ret_t dirty_rects_set_debug (dirty_rects_t* dirty_rects, bool_t debug);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
debug | bool_t | 是否开启调试模式。  
  
#### dirty_rects_set_disable_multiple 函数

* * *

  * 函数功能：



> 设置是否关闭多脏矩形模式(方便对比测试和调试)。

  * 函数原型：


    
    
    ret_t dirty_rects_set_disable_multiple (dirty_rects_t* dirty_rects, bool_t disable_multiple);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
disable_multiple | bool_t | 是否关闭多脏矩形模式。  
  
#### dirty_rects_set_profile 函数

* * *

  * 函数功能：



> 设置是否开启profile模式。

  * 函数原型：


    
    
    ret_t dirty_rects_set_profile (dirty_rects_t* dirty_rects, bool_t profile);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dirty_rects | dirty_rects_t* | dirty_rects对象。  
profile | bool_t | 是否开启profile模式。  
  
#### max 属性

* * *

> 最大脏矩形。

  * 类型：rect_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### nr 属性

* * *

> 个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### rects 属性

* * *

> 脏矩形。

  * 类型：rect_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
