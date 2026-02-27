## ring_buffer_t

### 概述

## 循环缓存区。

### 函数

函数名称 | 说明  
---|---  
ring_buffer_capacity | 获取容量。  
ring_buffer_create | 创建ring_buffer对象。  
ring_buffer_destroy | 销毁ring_buffer。  
ring_buffer_ensure_write_space | 扩展buffer。  
ring_buffer_free_size | 获取空闲空间的长度。  
ring_buffer_is_empty | 检查ring_buffer是否空。  
ring_buffer_is_full | 检查ring_buffer是否满。  
ring_buffer_peek | 读取数据(不修改读取位置)。  
ring_buffer_read | 读取数据。  
ring_buffer_read_len | 读取指定长度数据，要么成功要么失败。  
ring_buffer_reset | 重置ring_buffer为空。  
ring_buffer_set_read_cursor | 设置读取光标的位置。  
ring_buffer_set_read_cursor_delta | 设置读取光标的位置(delta)。  
ring_buffer_set_write_cursor | 设置写入光标的位置。  
ring_buffer_set_write_cursor_delta | 设置写入光标的位置(delta)。  
ring_buffer_size | 获取数据长度。  
ring_buffer_skip | 跳过指定长度数据，要么成功要么失败。  
ring_buffer_write | 写入数据。  
ring_buffer_write_len | 写入指定长度数据，要么成功要么失败。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
capacity | uint32_t | 当前容量。  
data | uint8_t* | 数据。  
full | bool_t | 是否满。  
max_capacity | uint32_t | 最大容量。  
r | uint32_t | 读取位置。  
w | uint32_t | 写入位置。  
  
#### ring_buffer_capacity 函数

* * *

  * 函数功能：



> 获取容量。

  * 函数原型：


    
    
    uint32_t ring_buffer_capacity (ring_buffer_t* ring_buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 容量。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
  
#### ring_buffer_create 函数

* * *

  * 函数功能：



> 创建ring_buffer对象。

  * 函数原型：


    
    
    ring_buffer_t* ring_buffer_create (uint32_t init_capacity, uint32_t max_capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ring_buffer_t* | ring_buffer对象。  
init_capacity | uint32_t | 初始容量。  
max_capacity | uint32_t | 最大容量。  
  
#### ring_buffer_destroy 函数

* * *

  * 函数功能：



> 销毁ring_buffer。

  * 函数原型：


    
    
    ret_t ring_buffer_destroy (ring_buffer_t* ring_buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
  
#### ring_buffer_ensure_write_space 函数

* * *

  * 函数功能：



> 扩展buffer。

  * 函数原型：


    
    
    ret_t ring_buffer_ensure_write_space (ring_buffer_t* ring_buffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
size | uint32_t | 需要的大小。  
  
#### ring_buffer_free_size 函数

* * *

  * 函数功能：



> 获取空闲空间的长度。

  * 函数原型：


    
    
    uint32_t ring_buffer_free_size (ring_buffer_t* ring_buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 空闲空间的长度。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
  
#### ring_buffer_is_empty 函数

* * *

  * 函数功能：



> 检查ring_buffer是否空。

  * 函数原型：


    
    
    bool_t ring_buffer_is_empty (ring_buffer_t* ring_buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 是否空。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
  
#### ring_buffer_is_full 函数

* * *

  * 函数功能：



> 检查ring_buffer是否满。

  * 函数原型：


    
    
    bool_t ring_buffer_is_full (ring_buffer_t* ring_buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 是否满。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
  
#### ring_buffer_peek 函数

* * *

  * 函数功能：



> 读取数据(不修改读取位置)。

  * 函数原型：


    
    
    uint32_t ring_buffer_peek (ring_buffer_t* ring_buffer, void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回实际读取数据的长度。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
buff | void* | 缓冲区。  
size | uint32_t | 最大长度。  
  
#### ring_buffer_read 函数

* * *

  * 函数功能：



> 读取数据。

  * 函数原型：


    
    
    uint32_t ring_buffer_read (ring_buffer_t* ring_buffer, void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回实际读取数据的长度。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
buff | void* | 缓冲区。  
size | uint32_t | 最大长度。  
  
#### ring_buffer_read_len 函数

* * *

  * 函数功能：



> 读取指定长度数据，要么成功要么失败。

  * 函数原型：


    
    
    ret_t ring_buffer_read_len (ring_buffer_t* ring_buffer, void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
buff | void* | 缓冲区。  
size | uint32_t | 最大长度。  
  
#### ring_buffer_reset 函数

* * *

  * 函数功能：



> 重置ring_buffer为空。

  * 函数原型：


    
    
    ret_t ring_buffer_reset (ring_buffer_t* ring_buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
  
#### ring_buffer_set_read_cursor 函数

* * *

  * 函数功能：



> 设置读取光标的位置。

  * 函数原型：


    
    
    ret_t ring_buffer_set_read_cursor (ring_buffer_t* ring_buffer, uint32_t r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
r | uint32_t | 读取光标的位置。  
  
#### ring_buffer_set_read_cursor_delta 函数

* * *

  * 函数功能：



> 设置读取光标的位置(delta)。

  * 函数原型：


    
    
    ret_t ring_buffer_set_read_cursor_delta (ring_buffer_t* ring_buffer, uint32_t r_delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
r_delta | uint32_t | 读取光标的位置(delta)。  
  
#### ring_buffer_set_write_cursor 函数

* * *

  * 函数功能：



> 设置写入光标的位置。

  * 函数原型：


    
    
    ret_t ring_buffer_set_write_cursor (ring_buffer_t* ring_buffer, uint32_t w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
w | uint32_t | 写入光标的位置。  
  
#### ring_buffer_set_write_cursor_delta 函数

* * *

  * 函数功能：



> 设置写入光标的位置(delta)。

  * 函数原型：


    
    
    ret_t ring_buffer_set_write_cursor_delta (ring_buffer_t* ring_buffer, uint32_t w_delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
w_delta | uint32_t | 写入光标的位置(delta)。  
  
#### ring_buffer_size 函数

* * *

  * 函数功能：



> 获取数据长度。

  * 函数原型：


    
    
    uint32_t ring_buffer_size (ring_buffer_t* ring_buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 数据长度。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
  
#### ring_buffer_skip 函数

* * *

  * 函数功能：



> 跳过指定长度数据，要么成功要么失败。

  * 函数原型：


    
    
    ret_t ring_buffer_skip (ring_buffer_t* ring_buffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
size | uint32_t | 长度。  
  
#### ring_buffer_write 函数

* * *

  * 函数功能：



> 写入数据。

  * 函数原型：


    
    
    uint32_t ring_buffer_write (ring_buffer_t* ring_buffer, const void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回实际写入数据的长度。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
buff | const void* | 缓冲区。  
size | uint32_t | 最大长度。  
  
#### ring_buffer_write_len 函数

* * *

  * 函数功能：



> 写入指定长度数据，要么成功要么失败。

  * 函数原型：


    
    
    ret_t ring_buffer_write_len (ring_buffer_t* ring_buffer, const void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ring_buffer | ring_buffer_t* | ring_buffer对象。  
buff | const void* | 缓冲区。  
size | uint32_t | 最大长度。  
  
#### capacity 属性

* * *

> 当前容量。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### data 属性

* * *

> 数据。

  * 类型：uint8_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### full 属性

* * *

> 是否满。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### max_capacity 属性

* * *

> 最大容量。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### r 属性

* * *

> 读取位置。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### w 属性

* * *

> 写入位置。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
