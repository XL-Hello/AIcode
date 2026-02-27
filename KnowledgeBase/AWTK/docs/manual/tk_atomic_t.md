## tk_atomic_t

### 概述

@export none 原子操作类。

* * *

### 函数

函数名称 | 说明  
---|---  
tk_atomic_compare_exchange_strong | 原子比较交换操作(Compare And Swap)。  
tk_atomic_compare_exchange_weak | 原子比较交换操作(Compare And Swap)。  
tk_atomic_create | 创建原子操作类对象。  
tk_atomic_deinit | 释放原子操作类对象。  
tk_atomic_destroy | 销毁原子操作类对象。  
tk_atomic_exchange | 原子交换操作。  
tk_atomic_fetch_add | 原子加操作。  
tk_atomic_fetch_sub | 原子减操作。  
tk_atomic_init | 初始化原子操作类对象。  
tk_atomic_load | 原子读操作。  
tk_atomic_store | 原子写操作。  
tk_atomic_support_value_type | 判断原子操作是否支持该类型。  
  
#### tk_atomic_compare_exchange_strong 函数

* * *

  * 函数功能：



> 原子比较交换操作(Compare And Swap)。 如果 atomic 等于 expect，则将 atomic 改为 desire, 否则将 expect 改为 atomic。

  * 函数原型：


    
    
    bool_t tk_atomic_compare_exchange_strong (tk_atomic_t* atomic, value_t* expect, value_t* desire);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
expect | value_t* | 期望值。  
desire | value_t* | 设定值。  
  
#### tk_atomic_compare_exchange_weak 函数

* * *

  * 函数功能：



> 原子比较交换操作(Compare And Swap)。 如果 atomic 等于 expect，则将 atomic 改为 desire, 否则将 expect 改为 atomic。

weak版本的CAS允许偶然出乎意料的返回（比如在字段值和期待值一样的时候却返回了FALSE）， 不过在一些循环算法中，这是可以接受的。通常它比起strong有更高的性能。

  * 函数原型：


    
    
    bool_t tk_atomic_compare_exchange_weak (tk_atomic_t* atomic, value_t* expect, value_t* desire);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
expect | value_t* | 期望值。  
desire | value_t* | 设定值。  
  
#### tk_atomic_create 函数

* * *

  * 函数功能：



> 创建原子操作类对象。

  * 函数原型：


    
    
    tk_atomic_t* tk_atomic_create (const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_atomic_t* | 返回原子操作类对象。  
v | const value_t* | 值。  
  
#### tk_atomic_deinit 函数

* * *

  * 函数功能：



> 释放原子操作类对象。

  * 函数原型：


    
    
    ret_t tk_atomic_deinit (tk_atomic_t* atomic);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
  
#### tk_atomic_destroy 函数

* * *

  * 函数功能：



> 销毁原子操作类对象。

  * 函数原型：


    
    
    ret_t tk_atomic_destroy (tk_atomic_t* atomic);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
  
#### tk_atomic_exchange 函数

* * *

  * 函数功能：



> 原子交换操作。

  * 函数原型：


    
    
    ret_t tk_atomic_exchange (tk_atomic_t* atomic, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
v | value_t* | 交换值。  
  
#### tk_atomic_fetch_add 函数

* * *

  * 函数功能：



> 原子加操作。

  * 函数原型：


    
    
    ret_t tk_atomic_fetch_add (tk_atomic_t* atomic, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
v | value_t* | 值。  
  
#### tk_atomic_fetch_sub 函数

* * *

  * 函数功能：



> 原子减操作。

  * 函数原型：


    
    
    ret_t tk_atomic_fetch_sub (tk_atomic_t* atomic, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
v | value_t* | 值。  
  
#### tk_atomic_init 函数

* * *

  * 函数功能：



> 初始化原子操作类对象。

  * 函数原型：


    
    
    ret_t tk_atomic_init (tk_atomic_t* atomic, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
v | const value_t* | 值。  
  
#### tk_atomic_load 函数

* * *

  * 函数功能：



> 原子读操作。

  * 函数原型：


    
    
    ret_t tk_atomic_load (const tk_atomic_t* atomic, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | const tk_atomic_t* | 原子操作类对象。  
v | value_t* | 用于返回读取值。  
  
#### tk_atomic_store 函数

* * *

  * 函数功能：



> 原子写操作。

  * 函数原型：


    
    
    ret_t tk_atomic_store (tk_atomic_t* atomic, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
atomic | tk_atomic_t* | 原子操作类对象。  
v | const value_t* | 写入值。  
  
#### tk_atomic_support_value_type 函数

* * *

  * 函数功能：



> 判断原子操作是否支持该类型。

  * 函数原型：


    
    
    bool_t tk_atomic_support_value_type (value_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回 TRUE 表示支持，FALSE 表示不支持。  
type | value_type_t | 类型。
