## bitmap_t

### 概述

## 位图。

### 函数

函数名称 | 说明  
---|---  
bitmap_clone | Clone图片。  
bitmap_create | 创建图片对象(一般供脚本语言中使用)。  
bitmap_create_ex | 创建图片对象。  
bitmap_create_ex2 | 创建图片对象。  
bitmap_create_ex3 | 创建图片对象。  
bitmap_deinit | 反初始化图片。  
bitmap_destroy | 销毁图片。  
bitmap_destroy_with_self | 销毁图片(for script only)。  
bitmap_get_bpp | 获取图片一个像素占用的字节数。  
bitmap_get_bpp_of_format | 获取位图格式对应的颜色位数。  
bitmap_get_line_length | 获取每一行占用内存的字节数。  
bitmap_get_physical_height | 获取图片真实物理的高度。  
bitmap_get_physical_line_length | 获取图片真实物理的每一行占用内存的字节数。  
bitmap_get_physical_width | 获取图片真实物理的宽度。  
bitmap_get_pixel | 获取图片指定像素的rgba颜色值(主要用于测试程序)。  
bitmap_init | 初始化图片。  
bitmap_init_ex | 初始化图片。  
bitmap_init_ex2 | 创建图片对象。  
bitmap_init_from_bgra | 初始化图片。  
bitmap_init_from_rgba | 初始化图片。  
bitmap_is_dirty | 获取图片是否脏。  
bitmap_lock_buffer_for_read | 为读取数据而锁定bitmap的图片缓冲区。  
bitmap_lock_buffer_for_write | 为修改数据而锁定bitmap的图片缓冲区。  
bitmap_mono_dump | dump mono bitmap。  
bitmap_save_png | 把bitmap保存为png。  
bitmap_set_dirty | 设置图片是否脏。  
bitmap_set_line_length | 设置line_length。  
bitmap_transform | 对图片每个像素进行变换。  
bitmap_unlock_buffer | 解锁图像缓冲区。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
buffer | graphic_buffer_t* | 图片数据。  
flags | uint16_t | 标志。请参考  
format | uint16_t | 格式。请参考  
h | wh_t | 高度。  
line_length | uint32_t | 每一行实际占用的内存(也称为stride或pitch)，一般情况下为w*bpp。  
name | const char* | 名称。  
orientation | lcd_orientation_t | 图片数据旋转。（修改了图片数据旋转后 flags 会带有 BITMAP_FLAG_LCD_ORIENTATION）  
w | wh_t | 宽度。  
  
#### bitmap_clone 函数

* * *

  * 函数功能：



> Clone图片。

  * 函数原型：


    
    
    bitmap_t* bitmap_clone (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回新的bitmap对象。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_create 函数

* * *

  * 函数功能：



> 创建图片对象(一般供脚本语言中使用)。

  * 函数原型：


    
    
    bitmap_t* bitmap_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回bitmap对象。  
  
#### bitmap_create_ex 函数

* * *

  * 函数功能：



> 创建图片对象。

  * 函数原型：


    
    
    bitmap_t* bitmap_create_ex (uint32_t w, uint32_t h, uint32_t line_length, bitmap_format_t format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
line_length | uint32_t | line_length。  
format | bitmap_format_t | 格式。  
  
#### bitmap_create_ex2 函数

* * *

  * 函数功能：



> 创建图片对象。

  * 函数原型：


    
    
    bitmap_t* bitmap_create_ex2 (uint32_t w, uint32_t h, uint32_t line_length, bitmap_format_t format, uint8_t* data, bool_t should_free_data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
line_length | uint32_t | line_length。  
format | bitmap_format_t | 格式。  
data | uint8_t* | 图像数据。  
should_free_data | bool_t | 是否释放数据。  
  
#### bitmap_create_ex3 函数

* * *

  * 函数功能：



> 创建图片对象。

  * 函数原型：


    
    
    bitmap_t* bitmap_create_ex3 (uint32_t w, uint32_t h, uint32_t line_length, bitmap_format_t format, uint8_t* data, uint8_t* physical_data_addr, bool_t should_free_data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
line_length | uint32_t | line_length。  
format | bitmap_format_t | 格式。  
data | uint8_t* | 图像数据。  
physical_data_addr | uint8_t* | 物理地址(部分硬件加速需要)。  
should_free_data | bool_t | 是否释放数据。  
  
#### bitmap_deinit 函数

* * *

  * 函数功能：



> 反初始化图片。

  * 函数原型：


    
    
    ret_t bitmap_deinit (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_destroy 函数

* * *

  * 函数功能：



> 销毁图片。

  * 函数原型：


    
    
    ret_t bitmap_destroy (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_destroy_with_self 函数

* * *

  * 函数功能：



> 销毁图片(for script only)。

  * 函数原型：


    
    
    ret_t bitmap_destroy_with_self (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_get_bpp 函数

* * *

  * 函数功能：



> 获取图片一个像素占用的字节数。

  * 函数原型：


    
    
    uint32_t bitmap_get_bpp (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回一个像素占用的字节数。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_get_bpp_of_format 函数

* * *

  * 函数功能：



> 获取位图格式对应的颜色位数。

  * 函数原型：


    
    
    uint32_t bitmap_get_bpp_of_format (bitmap_format_t format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 成功返回颜色位数，失败返回0。  
format | bitmap_format_t | 位图格式。  
  
#### bitmap_get_line_length 函数

* * *

  * 函数功能：



> 获取每一行占用内存的字节数。

  * 函数原型：


    
    
    uint32_t bitmap_get_line_length (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回每一行占用内存的字节数。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_get_physical_height 函数

* * *

  * 函数功能：



> 获取图片真实物理的高度。

  * 函数原型：


    
    
    uint32_t bitmap_get_physical_height (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回图片高度。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_get_physical_line_length 函数

* * *

  * 函数功能：



> 获取图片真实物理的每一行占用内存的字节数。

  * 函数原型：


    
    
    uint32_t bitmap_get_physical_line_length (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回每一行占用内存的字节数。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_get_physical_width 函数

* * *

  * 函数功能：



> 获取图片真实物理的宽度。

  * 函数原型：


    
    
    uint32_t bitmap_get_physical_width (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回图片宽度。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_get_pixel 函数

* * *

  * 函数功能：



> 获取图片指定像素的rgba颜色值(主要用于测试程序)。

  * 函数原型：


    
    
    ret_t bitmap_get_pixel (bitmap_t* bitmap, uint32_t x, uint32_t y, rgba_t* rgba);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
x | uint32_t | x坐标。  
y | uint32_t | y坐标。  
rgba | rgba_t* | 返回颜色值。  
  
#### bitmap_init 函数

* * *

  * 函数功能：



> 初始化图片。

  * 函数原型：


    
    
    ret_t bitmap_init (bitmap_t* bitmap, uint32_t w, uint32_t h, bitmap_format_t format, uint8_t* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
format | bitmap_format_t | 格式。  
data | uint8_t* | 数据，直接引用，但不负责释放。如果为空，由内部自动分配和释放。  
  
#### bitmap_init_ex 函数

* * *

  * 函数功能：



> 初始化图片。

  * 函数原型：


    
    
    ret_t bitmap_init_ex (bitmap_t* bitmap, uint32_t w, uint32_t h, uint32_t line_length, bitmap_format_t format, uint8_t* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
line_length | uint32_t | 行长。  
format | bitmap_format_t | 格式。  
data | uint8_t* | 数据，直接引用，但不负责释放。如果为空，由内部自动分配和释放。  
  
#### bitmap_init_ex2 函数

* * *

  * 函数功能：



> 创建图片对象。

  * 函数原型：


    
    
    ret_t bitmap_init_ex2 (bitmap_t* bitmap, uint32_t w, uint32_t h, uint32_t line_length, bitmap_format_t format, uint8_t* data, uint8_t* physical_data_addr, bool_t should_free_data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
line_length | uint32_t | line_length。  
format | bitmap_format_t | 格式。  
data | uint8_t* | 图像数据。  
physical_data_addr | uint8_t* | 物理地址(部分硬件加速需要)。  
should_free_data | bool_t | 是否释放数据。  
  
#### bitmap_init_from_bgra 函数

* * *

  * 函数功能：



> 初始化图片。

  * 函数原型：


    
    
    ret_t bitmap_init_from_bgra (bitmap_t* bitmap, uint32_t w, uint32_t h, bitmap_format_t format, const uint8_t* data, uint32_t comp, lcd_orientation_t o);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
format | bitmap_format_t | 格式。  
data | const uint8_t* | 数据。3通道时为BGR888格式，4通道时为BGRA888格式(内部拷贝该数据，不会引用，调用者自行释放)。  
comp | uint32_t | 颜色通道数(目前支持3(bgr)和4(bgra))。  
o | lcd_orientation_t | 旋转方向。  
  
#### bitmap_init_from_rgba 函数

* * *

  * 函数功能：



> 初始化图片。

  * 函数原型：


    
    
    ret_t bitmap_init_from_rgba (bitmap_t* bitmap, uint32_t w, uint32_t h, bitmap_format_t format, const uint8_t* data, uint32_t comp, lcd_orientation_t o);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
format | bitmap_format_t | 格式。  
data | const uint8_t* | 数据。3通道时为RGB888格式，4通道时为RGBA888格式(内部拷贝该数据，不会引用，调用者自行释放)。  
comp | uint32_t | 颜色通道数(目前支持3(rgb)和4(rgba))。  
o | lcd_orientation_t | 旋转方向。  
  
#### bitmap_is_dirty 函数

* * *

  * 函数功能：



> 获取图片是否脏。

  * 函数原型：


    
    
    bool_t bitmap_is_dirty (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示脏，FALSE表示不脏。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_lock_buffer_for_read 函数

* * *

  * 函数功能：



> 为读取数据而锁定bitmap的图片缓冲区。

  * 函数原型：


    
    
    uint8_t* bitmap_lock_buffer_for_read (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回缓存区的首地址。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_lock_buffer_for_write 函数

* * *

  * 函数功能：



> 为修改数据而锁定bitmap的图片缓冲区。

  * 函数原型：


    
    
    uint8_t* bitmap_lock_buffer_for_write (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回缓存区的首地址。  
bitmap | bitmap_t* | bitmap对象。  
  
#### bitmap_mono_dump 函数

* * *

  * 函数功能：



> dump mono bitmap。

  * 函数原型：


    
    
    ret_t bitmap_mono_dump (const uint8_t* buff, uint32_t w, uint32_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buff | const uint8_t* | 数据。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
  
#### bitmap_save_png 函数

* * *

  * 函数功能：



> 把bitmap保存为png。

  * 函数原型：


    
    
    bool_t bitmap_save_png (bitmap_t* bitmap, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示成功，FALSE表示失败。  
bitmap | bitmap_t* | bitmap对象。  
filename | const char* | 文件名。  
  
#### bitmap_set_dirty 函数

* * *

  * 函数功能：



> 设置图片是否脏。

  * 函数原型：


    
    
    ret_t bitmap_set_dirty (bitmap_t* bitmap, bool_t dirty);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
dirty | bool_t | 是否脏。  
  
#### bitmap_set_line_length 函数

* * *

  * 函数功能：



> 设置line_length。

  * 函数原型：


    
    
    ret_t bitmap_set_line_length (bitmap_t* bitmap, uint32_t line_length);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
line_length | uint32_t | line_length。  
  
#### bitmap_transform 函数

* * *

  * 函数功能：



> 对图片每个像素进行变换。

  * 函数原型：


    
    
    ret_t bitmap_transform (bitmap_t* bitmap, bitmap_transform_t transform, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
transform | bitmap_transform_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### bitmap_unlock_buffer 函数

* * *

  * 函数功能：



> 解锁图像缓冲区。

  * 函数原型：


    
    
    ret_t bitmap_unlock_buffer (bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bitmap | bitmap_t* | bitmap对象。  
  
#### buffer 属性

* * *

> 图片数据。

  * 类型：graphic_buffer_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### flags 属性

* * *

> 标志。请参考{bitmap_flag_t}。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### format 属性

* * *

> 格式。请参考{bitmap_format_t}。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### h 属性

* * *

> 高度。

  * 类型：wh_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### line_length 属性

* * *

> 每一行实际占用的内存(也称为stride或pitch)，一般情况下为w*bpp。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### name 属性

* * *

> 名称。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### orientation 属性

* * *

> 图片数据旋转。（修改了图片数据旋转后 flags 会带有 BITMAP_FLAG_LCD_ORIENTATION）

  * 类型：lcd_orientation_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### w 属性

* * *

> 宽度。

  * 类型：wh_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
