## lcd_mem_special_t

### 概述

![image](images/lcd_mem_special_t_0.png)

特殊的LCD。

通过重载flush函数来提交GUI绘制的结果到硬件。适用于：

  * lcd 硬件不支持framebuffer，如SPI接口的屏。
  * lcd 硬件支持framebuffer，但是其格式特殊，AWTK目前不支持。可以用flush进行格式转换。



* * *

### 函数

函数名称 | 说明  
---|---  
lcd_mem_deinit | 清除 lcd_mem 对象中的数据  
lcd_mem_get_next_fb | 获取 lcd_mem 对象中的 next_fb  
lcd_mem_get_offline_fb | 获取 lcd_mem 对象中的 offline_fb  
lcd_mem_get_online_fb | 获取 lcd_mem 对象中的 online_fb  
lcd_mem_set_next_fb | 设置 lcd_mem 对象中的 next_fb  
lcd_mem_set_offline_fb | 设置 lcd_mem 对象中的 offline_fb  
lcd_mem_set_online_fb | 设置 lcd_mem 对象中的 online_fb  
lcd_mem_set_wait_vbi | 设置等待VBI事件到来的回调函数。  
lcd_mem_special_create | 创建lcd对象。  
  
#### lcd_mem_deinit 函数

* * *

  * 函数功能：



> 清除 lcd_mem 对象中的数据

  * 函数原型：


    
    
    ret_t lcd_mem_deinit (lcd_mem_t* mem);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
mem | lcd_mem_t* | lcd_mem 对象。  
  
#### lcd_mem_get_next_fb 函数

* * *

  * 函数功能：



> 获取 lcd_mem 对象中的 next_fb

  * 函数原型：


    
    
    uint8_t* lcd_mem_get_next_fb (lcd_mem_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回 next_fb 地址。  
lcd | lcd_mem_t* | lcd_mem 对象。  
  
#### lcd_mem_get_offline_fb 函数

* * *

  * 函数功能：



> 获取 lcd_mem 对象中的 offline_fb

  * 函数原型：


    
    
    uint8_t* lcd_mem_get_offline_fb (lcd_mem_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回 offline_fb 地址。  
lcd | lcd_mem_t* | lcd_mem 对象。  
  
#### lcd_mem_get_online_fb 函数

* * *

  * 函数功能：



> 获取 lcd_mem 对象中的 online_fb

  * 函数原型：


    
    
    uint8_t* lcd_mem_get_online_fb (lcd_mem_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t* | 返回 online_fb 地址。  
lcd | lcd_mem_t* | lcd_mem 对象。  
  
#### lcd_mem_set_next_fb 函数

* * *

  * 函数功能：



> 设置 lcd_mem 对象中的 next_fb

  * 函数原型：


    
    
    ret_t lcd_mem_set_next_fb (lcd_mem_t* lcd, uint8_t* next_fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_mem_t* | lcd_mem 对象。  
next_fb | uint8_t* | next_fb 地址。  
  
#### lcd_mem_set_offline_fb 函数

* * *

  * 函数功能：



> 设置 lcd_mem 对象中的 offline_fb

  * 函数原型：


    
    
    ret_t lcd_mem_set_offline_fb (lcd_mem_t* lcd, uint8_t* offline_fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_mem_t* | lcd_mem 对象。  
offline_fb | uint8_t* | offline_fb 地址。  
  
#### lcd_mem_set_online_fb 函数

* * *

  * 函数功能：



> 设置 lcd_mem 对象中的 online_fb

  * 函数原型：


    
    
    ret_t lcd_mem_set_online_fb (lcd_mem_t* lcd, uint8_t* online_fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_mem_t* | lcd_mem 对象。  
online_fb | uint8_t* | online_fb 地址。  
  
#### lcd_mem_set_wait_vbi 函数

* * *

  * 函数功能：



> 设置等待VBI事件到来的回调函数。 VBI: vertical blank interrupt。用于2fb等待当前显示完成，以便把下一帧的数据从offline fb拷贝到online fb，从而避免因为同时访问online fb数据造成闪烁。

  * 函数原型：


    
    
    ret_t lcd_mem_set_wait_vbi (lcd_t* lcd, lcd_mem_wait_vbi_t wait_vbi, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
wait_vbi | lcd_mem_wait_vbi_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### lcd_mem_special_create 函数

* * *

  * 函数功能：



> 创建lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_special_create (wh_t w, wh_t h, bitmap_format_t fmt, lcd_flush_t on_flush, lcd_resize_t on_resize, lcd_destroy_t on_destroy, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
fmt | bitmap_format_t | 离线lcd的格式。一般用 BITMAP_FMT_BGR565 或 BITMAP_FMT_RGBA8888。  
on_flush | lcd_flush_t | 回调函数，用于刷新GUI数据到实际的LCD。  
on_resize | lcd_resize_t | 用于调整LCD的大小。一般用NULL即可。  
on_destroy | lcd_destroy_t | lcd销毁时的回调函数。  
ctx | void* | 回调函数的上下文。
