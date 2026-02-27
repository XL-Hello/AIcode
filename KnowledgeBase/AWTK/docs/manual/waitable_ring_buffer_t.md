## waitable_ring_buffer_t

### 概述

## waitable ring buffer

### 函数

函数名称 | 说明  
---|---  
waitable_ring_buffer_create | 创建waitable_ring_buffer对象。  
waitable_ring_buffer_destroy | 销毁。  
waitable_ring_buffer_read | 读取数据。  
waitable_ring_buffer_write | 写入数据。  
  
#### waitable_ring_buffer_create 函数

* * *

  * 函数功能：



> 创建waitable_ring_buffer对象。

  * 函数原型：


    
    
    waitable_ring_buffer_t* waitable_ring_buffer_create (uint32_t capacity, uint32_t block_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | waitable_ring_buffer_t* | waitable_ring_buffer对象。  
capacity | uint32_t | 容量。  
block_size | uint32_t | 块的大小。  
  
#### waitable_ring_buffer_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t waitable_ring_buffer_destroy (waitable_ring_buffer_t* rb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rb | waitable_ring_buffer_t* | waitable_ring_buffer对象。  
  
#### waitable_ring_buffer_read 函数

* * *

  * 函数功能：



> 读取数据。

  * 函数原型：


    
    
    ret_t waitable_ring_buffer_read (waitable_ring_buffer_t* rb, void* buff, uint32_t size, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rb | waitable_ring_buffer_t* | waitable_ring_buffer对象。  
buff | void* | 接收数据的buff。  
size | uint32_t | 读取数据的长度(必须等于 block_size)。  
timeout_ms | uint32_t | 超时时间(毫秒)  
  
#### waitable_ring_buffer_write 函数

* * *

  * 函数功能：



> 写入数据。

  * 函数原型：


    
    
    ret_t waitable_ring_buffer_write (waitable_ring_buffer_t* rb, const void* buff, uint32_t size, uint32_t timeout_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
rb | waitable_ring_buffer_t* | waitable_ring_buffer对象。  
buff | const void* | 要写入的数据。  
size | uint32_t | 数据的长度(必须等于 block_size)。  
timeout_ms | uint32_t | 超时时间(毫秒)
