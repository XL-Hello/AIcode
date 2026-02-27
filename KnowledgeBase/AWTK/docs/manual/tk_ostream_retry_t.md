## tk_ostream_retry_t

### 概述

![image](images/tk_ostream_retry_t_0.png)

如果写数据失败，将数据放入ring_buffer，后面再重试(flush)。

## 如果重试次数超出最大值，则丢掉数据。

### 函数

函数名称 | 说明  
---|---  
tk_ostream_retry_clear_buffer | 清除缓存的数据。  
tk_ostream_retry_create | 创建ostream对象。  
tk_ostream_retry_set_discard_policy | 设置数据丢弃策略。  
tk_ostream_retry_set_max_buffer_size | 设置最大缓存大小。  
tk_ostream_retry_set_max_retry_times | 设置最大尝试次数。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
discard_bytes | uint32_t | 总共丢弃数据的字节数。  
discard_packets | uint32_t | 总共丢弃数据包的个数。  
discard_policy | data_discard_policy_t | 缓存不够时，丢弃数据包的策略。  
max_retry_times | uint32_t | 尝试次数超过指定的值时丢弃该数据包。  
pending_bytes | uint32_t | 待重写的数据大小。  
pending_packets | uint32_t | 待重写的数据包的个数。  
timeout | uint32_t | 写超时时间(毫秒)。  
  
#### tk_ostream_retry_clear_buffer 函数

* * *

  * 函数功能：



> 清除缓存的数据。

  * 函数原型：


    
    
    ret_t tk_ostream_retry_clear_buffer (tk_ostream_t* ostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ostream | tk_ostream_t* | ostream对象。  
  
#### tk_ostream_retry_create 函数

* * *

  * 函数功能：



> 创建ostream对象。

本函数自动增加real_ostream的引用计数。

  * 函数原型：


    
    
    tk_ostream_t* tk_ostream_retry_create (tk_ostream_t* real_ostream);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_ostream_t* | 返回ostream对象。  
real_ostream | tk_ostream_t* | 实际的ostream对象。  
  
#### tk_ostream_retry_set_discard_policy 函数

* * *

  * 函数功能：



> 设置数据丢弃策略。

  * 函数原型：


    
    
    ret_t tk_ostream_retry_set_discard_policy (tk_ostream_t* ostream, data_discard_policy_t discard_policy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ostream | tk_ostream_t* | ostream对象。  
discard_policy | data_discard_policy_t | 丢弃策略。  
  
#### tk_ostream_retry_set_max_buffer_size 函数

* * *

  * 函数功能：



> 设置最大缓存大小。

  * 函数原型：


    
    
    ret_t tk_ostream_retry_set_max_buffer_size (tk_ostream_t* ostream, uint32_t max_buffer_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ostream | tk_ostream_t* | ostream对象。  
max_buffer_size | uint32_t | 缓存大小。  
  
#### tk_ostream_retry_set_max_retry_times 函数

* * *

  * 函数功能：



> 设置最大尝试次数。

  * 函数原型：


    
    
    ret_t tk_ostream_retry_set_max_retry_times (tk_ostream_t* ostream, uint32_t max_retry_times);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ostream | tk_ostream_t* | ostream对象。  
max_retry_times | uint32_t | 最大尝试次数。  
  
#### discard_bytes 属性

* * *

> 总共丢弃数据的字节数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### discard_packets 属性

* * *

> 总共丢弃数据包的个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### discard_policy 属性

* * *

> 缓存不够时，丢弃数据包的策略。

  * 类型：data_discard_policy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### max_retry_times 属性

* * *

> 尝试次数超过指定的值时丢弃该数据包。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### pending_bytes 属性

* * *

> 待重写的数据大小。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### pending_packets 属性

* * *

> 待重写的数据包的个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### timeout 属性

* * *

> 写超时时间(毫秒)。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
