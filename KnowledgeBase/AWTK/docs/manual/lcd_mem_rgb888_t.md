## lcd_mem_rgb888_t

### 概述

![image](images/lcd_mem_rgb888_t_0.png)

* * *

### 函数

函数名称 | 说明  
---|---  
lcd_mem_rgb888_create | 创建lcd对象。  
lcd_mem_rgb888_create_double_fb | 创建double fb lcd对象。  
lcd_mem_rgb888_create_double_fb_bitmap | 创建double fb lcd对象。  
lcd_mem_rgb888_create_single_fb | 创建single fb lcd对象。  
lcd_mem_rgb888_create_single_fb_bitmap | 创建single fb lcd对象。  
lcd_mem_rgb888_create_three_fb | 创建three fb lcd对象。  
lcd_mem_rgb888_create_three_fb_bitmap | 创建three fb lcd对象。  
lcd_mem_rgb888_init | 创建lcd对象。  
  
#### lcd_mem_rgb888_create 函数

* * *

  * 函数功能：



> 创建lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_create (wh_t w, wh_t h, bool_t alloc);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
alloc | bool_t | 是否分配内存。  
  
#### lcd_mem_rgb888_create_double_fb 函数

* * *

  * 函数功能：



> 创建double fb lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_create_double_fb (wh_t w, wh_t h, uint8_t* online_fb, uint8_t* offline_fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
online_fb | uint8_t* | 在线帧率缓冲区。  
offline_fb | uint8_t* | 离线帧率缓冲区。  
  
#### lcd_mem_rgb888_create_double_fb_bitmap 函数

* * *

  * 函数功能：



> 创建double fb lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_create_double_fb_bitmap (bitmap_t* online_fb_bitmap, bitmap_t* offline_fb_bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
online_fb_bitmap | bitmap_t* | 在线帧率缓冲区。  
offline_fb_bitmap | bitmap_t* | 离线帧率缓冲区。  
  
#### lcd_mem_rgb888_create_single_fb 函数

* * *

  * 函数功能：



> 创建single fb lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_create_single_fb (wh_t w, wh_t h, uint8_t* fbuff);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
fbuff | uint8_t* | 帧率缓冲区。  
  
#### lcd_mem_rgb888_create_single_fb_bitmap 函数

* * *

  * 函数功能：



> 创建single fb lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_create_single_fb_bitmap (bitmap_t* offline_fb_bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
offline_fb_bitmap | bitmap_t* | 帧率缓冲区。  
  
#### lcd_mem_rgb888_create_three_fb 函数

* * *

  * 函数功能：



> 创建three fb lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_create_three_fb (wh_t w, wh_t h, uint8_t* online_fb, uint8_t* offline_fb, uint8_t* next_fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
online_fb | uint8_t* | 在线帧率缓冲区。  
offline_fb | uint8_t* | 离线帧率缓冲区。  
next_fb | uint8_t* | 待显示的帧率缓冲区。  
  
#### lcd_mem_rgb888_create_three_fb_bitmap 函数

* * *

  * 函数功能：



> 创建three fb lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_create_three_fb_bitmap (bitmap_t* online_fb_bitmap, bitmap_t* offline_fb_bitmap, bitmap_t* next_fb_bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
online_fb_bitmap | bitmap_t* | 在线帧率缓冲区。  
offline_fb_bitmap | bitmap_t* | 离线帧率缓冲区。  
next_fb_bitmap | bitmap_t* | 待显示的帧率缓冲区。  
  
#### lcd_mem_rgb888_init 函数

* * *

  * 函数功能：



> 创建lcd对象。

  * 函数原型：


    
    
    lcd_t* lcd_mem_rgb888_init (lcd_mem_t* lcd, wh_t w, wh_t h, bool_t alloc);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_t* | 返回lcd对象。  
lcd | lcd_mem_t* | 对象。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
alloc | bool_t | 是否分配内存。
