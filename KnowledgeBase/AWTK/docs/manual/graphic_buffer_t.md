## graphic_buffer_t

### 概述

## graphic_buffer。

### 函数

函数名称 | 说明  
---|---  
graphic_buffer_attach | 附件到指定的内存。  
graphic_buffer_create_for_bitmap | 为位图创建缓冲区。  
graphic_buffer_create_with_data | 创建缓冲区。  
graphic_buffer_create_with_data_ex | 创建缓冲区。  
graphic_buffer_destroy | 销毁缓冲区。  
graphic_buffer_get_physical_height | 获取 graphic_buffer 真实物理的的高度  
graphic_buffer_get_physical_line_length | 获取 graphic_buffer 真实物理的的行长度  
graphic_buffer_get_physical_width | 获取 graphic_buffer 真实物理的的宽度  
graphic_buffer_is_valid_for | 用于检查graphic buffer的有效性。  
graphic_buffer_lock_for_read | 为读取数据而锁定缓冲区。  
graphic_buffer_lock_for_write | 为修改数据而锁定缓冲区。  
graphic_buffer_set_physical_height | 设置 graphic_buffer 真实物理的的高度  
graphic_buffer_set_physical_line_length | 设置 graphic_buffer 真实物理的的行长度  
graphic_buffer_set_physical_width | 设置 graphic_buffer 真实物理的的宽度  
graphic_buffer_unlock | 解锁缓冲区。  
  
#### graphic_buffer_attach 函数

* * *

  * 函数功能：



> 附件到指定的内存。

  * 函数原型：


    
    
    ret_t graphic_buffer_attach (graphic_buffer_t* buffer, void* data, uint32_t w, uint32_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
data | void* | 内存数据。  
w | uint32_t | 宽度。  
h | uint32_t | 宽度。  
  
#### graphic_buffer_create_for_bitmap 函数

* * *

  * 函数功能：



> 为位图创建缓冲区。

  * 函数原型：


    
    
    ret_t graphic_buffer_create_for_bitmap (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | 位图对象。  
  
#### graphic_buffer_create_with_data 函数

* * *

  * 函数功能：



> 创建缓冲区。
> 
> 为了兼容raw图像。

  * 函数原型：


    
    
    graphic_buffer_t* graphic_buffer_create_with_data (const uint8_t* data, uint32_t w, uint32_t h, bitmap_format_t format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | graphic_buffer_t* | 返回缓存区。  
data | const uint8_t* | 数据。  
w | uint32_t | 宽度。  
h | uint32_t | 宽度。  
format | bitmap_format_t | 格式。  
  
#### graphic_buffer_create_with_data_ex 函数

* * *

  * 函数功能：



> 创建缓冲区。
> 
> 为了兼容raw图像。

  * 函数原型：


    
    
    graphic_buffer_t* graphic_buffer_create_with_data_ex (const uint8_t* virtual_data, const uint8_t* physical_data, uint32_t w, uint32_t h, uint32_t line_length, bitmap_format_t format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | graphic_buffer_t* | 返回缓存区。  
virtual_data | const uint8_t* | 数据虚拟地址。  
physical_data | const uint8_t* | 数据物理地址。  
w | uint32_t | 宽度。  
h | uint32_t | 宽度。  
line_length | uint32_t | 每行宽度(字节数)  
format | bitmap_format_t | 格式。  
  
#### graphic_buffer_destroy 函数

* * *

  * 函数功能：



> 销毁缓冲区。

  * 函数原型：


    
    
    ret_t graphic_buffer_destroy (graphic_buffer_t* buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
  
#### graphic_buffer_get_physical_height 函数

* * *

  * 函数功能：



> 获取 graphic_buffer 真实物理的的高度

  * 函数原型：


    
    
    uint32_t graphic_buffer_get_physical_height (graphic_buffer_t* buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回高度。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
  
#### graphic_buffer_get_physical_line_length 函数

* * *

  * 函数功能：



> 获取 graphic_buffer 真实物理的的行长度

  * 函数原型：


    
    
    uint32_t graphic_buffer_get_physical_line_length (graphic_buffer_t* buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回行长度。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
  
#### graphic_buffer_get_physical_width 函数

* * *

  * 函数功能：



> 获取 graphic_buffer 真实物理的的宽度

  * 函数原型：


    
    
    uint32_t graphic_buffer_get_physical_width (graphic_buffer_t* buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回宽度。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
  
#### graphic_buffer_is_valid_for 函数

* * *

  * 函数功能：



> 用于检查graphic buffer的有效性。

  * 函数原型：


    
    
    bool_t graphic_buffer_is_valid_for (graphic_buffer_t* buffer, bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示有效，否则表示无效。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
bitmap | bitmap_t* | 位图对象。  
  
#### graphic_buffer_lock_for_read 函数

* * *

  * 函数功能：



> 为读取数据而锁定缓冲区。

  * 函数原型：


    
    
    uint8_t* graphic_buffer_lock_for_read (graphic_buffer_t* buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回缓存区的首地址。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
  
#### graphic_buffer_lock_for_write 函数

* * *

  * 函数功能：



> 为修改数据而锁定缓冲区。

  * 函数原型：


    
    
    uint8_t* graphic_buffer_lock_for_write (graphic_buffer_t* buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回缓存区的首地址。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
  
#### graphic_buffer_set_physical_height 函数

* * *

  * 函数功能：



> 设置 graphic_buffer 真实物理的的高度

  * 函数原型：


    
    
    ret_t graphic_buffer_set_physical_height (graphic_buffer_t* buffer, uint32_t height);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
height | uint32_t | 真实物理的的高度。  
  
#### graphic_buffer_set_physical_line_length 函数

* * *

  * 函数功能：



> 设置 graphic_buffer 真实物理的的行长度

  * 函数原型：


    
    
    ret_t graphic_buffer_set_physical_line_length (graphic_buffer_t* buffer, uint32_t line_length);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
line_length | uint32_t | 真实物理的的行长度。  
  
#### graphic_buffer_set_physical_width 函数

* * *

  * 函数功能：



> 设置 graphic_buffer 真实物理的的宽度

  * 函数原型：


    
    
    ret_t graphic_buffer_set_physical_width (graphic_buffer_t* buffer, uint32_t width);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | graphic_buffer_t* | 图像缓冲区对象。  
width | uint32_t | 真实物理的的宽度。  
  
#### graphic_buffer_unlock 函数

* * *

  * 函数功能：



> 解锁缓冲区。

  * 函数原型：


    
    
    ret_t graphic_buffer_unlock (graphic_buffer_t* buffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | graphic_buffer_t* | 图像缓冲区对象。
