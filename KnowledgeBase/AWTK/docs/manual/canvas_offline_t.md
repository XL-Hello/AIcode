## canvas_offline_t

### 概述

## 离线画布 canvas。

### 函数

函数名称 | 说明  
---|---  
canvas_offline_begin_draw | 设置离线 canvas 开始绘图  
canvas_offline_bitmap_move_to_new_bitmap | 把离线 canvas 的离线 bitmap 移动赋值给新的 bitmap。  
canvas_offline_clear_canvas | 清除离线 canvas 所有数据，并把背景设置为全透明（注意：该离线 canvas 需要有透明通道）  
canvas_offline_create | 创建一个离线的 canvas  
canvas_offline_create_by_widget | 创建一个和控件大小一样的离线的 canvas  
canvas_offline_custom_begin_draw | 用户自定义 canvas_offline_custom_begin_draw  
canvas_offline_custom_bitmap_move_to_new_bitmap | 用户自定义 canvas_offline_custom_bitmap_move_to_new_bitmap  
canvas_offline_custom_clear_canvas | 用户自定义 canvas_offline_custom_clear_canvas  
canvas_offline_custom_create | 用户自定义 canvas_offline_create  
canvas_offline_custom_destroy | 用户自定义 canvas_offline_custom_destroy  
canvas_offline_custom_end_draw | 用户自定义 canvas_offline_custom_end_draw  
canvas_offline_custom_flush_bitmap | 用户自定义 canvas_offline_custom_flush_bitmap  
canvas_offline_custom_get_bitmap | 用户自定义 canvas_offline_custom_get_bitmap  
canvas_offline_destroy | 释放离线 canvas 和离线 bitmap  
canvas_offline_end_draw | 设置离线 canvas 结束绘图  
canvas_offline_flush_bitmap | 把离线 canvas 的数据放到绑定的 bitmap 中  
canvas_offline_get_bitmap | 获取离线 canvas 的离线 bitmap。  
canvas_offline_set_canvas_orientation | 设置离线画布旋转角度。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
bitmap | bitmap_t* | 绑定的离线 bitmap  
canvas_orientation | lcd_orientation_t | 快速的旋转角度（对应 WITH_FAST_LCD_PORTRAIT 宏的使用）  
  
#### canvas_offline_begin_draw 函数

* * *

  * 函数功能：



> 设置离线 canvas 开始绘图

  * 函数原型：


    
    
    ret_t canvas_offline_begin_draw (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_bitmap_move_to_new_bitmap 函数

* * *

  * 函数功能：



> 把离线 canvas 的离线 bitmap 移动赋值给新的 bitmap。 移动赋值后原来的离线 canvas 的离线 bitmap 就会被置空。

  * 函数原型：


    
    
    ret_t canvas_offline_bitmap_move_to_new_bitmap (canvas_t* canvas, bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
bitmap | bitmap_t* | 新的 bitmap 对象。  
  
#### canvas_offline_clear_canvas 函数

* * *

  * 函数功能：



> 清除离线 canvas 所有数据，并把背景设置为全透明（注意：该离线 canvas 需要有透明通道） 该函数调用前必须要先 canvas_offline_begin_draw 函数。 该函数用来解决离线 canvas 多次绘图半透效果后导致半透效果无效的问题。

  * 函数原型：


    
    
    ret_t canvas_offline_clear_canvas (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_create 函数

* * *

  * 函数功能：



> 创建一个离线的 canvas 在 opengl 模式下 format 参数只能为 BITMAP_FMT_RGBA8888 在其他模式下，离线 canvas 格式可以为 rgba，bgar，bgr565和rgb565 旋转方向和 lcd 旋转方向保存一致，旋转方向不同可能会导致 bitmap 的逻辑宽高不同。

  * 函数原型：


    
    
    canvas_t* canvas_offline_create (uint32_t w, uint32_t h, bitmap_format_t format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | 成功返回 canvas ，失败返回 NULL。  
w | uint32_t | 离线 canvas 的物理宽。  
h | uint32_t | 离线 canvas 的物理高。  
format | bitmap_format_t | 离线 canvas 的格式。  
  
#### canvas_offline_create_by_widget 函数

* * *

  * 函数功能：



> 创建一个和控件大小一样的离线的 canvas

  * 函数原型：


    
    
    canvas_t* canvas_offline_create_by_widget (widget_t* widget, bitmap_format_t format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | 成功返回 canvas ，失败返回 NULL。  
widget | widget_t* | 控件。  
format | bitmap_format_t | 离线 canvas 的格式。  
  
#### canvas_offline_custom_begin_draw 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_custom_begin_draw

  * 函数原型：


    
    
    ret_t canvas_offline_custom_begin_draw (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_custom_bitmap_move_to_new_bitmap 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_custom_bitmap_move_to_new_bitmap

  * 函数原型：


    
    
    ret_t canvas_offline_custom_bitmap_move_to_new_bitmap (canvas_t* canvas, bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
bitmap | bitmap_t* | 新的 bitmap 对象。  
  
#### canvas_offline_custom_clear_canvas 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_custom_clear_canvas

  * 函数原型：


    
    
    ret_t canvas_offline_custom_clear_canvas (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_custom_create 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_create

  * 函数原型：


    
    
    canvas_t* canvas_offline_custom_create (uint32_t w, uint32_t h, bitmap_format_t format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | 成功返回 canvas ，失败返回 NULL。  
w | uint32_t | 离线 canvas 的宽。  
h | uint32_t | 离线 canvas 的高。  
format | bitmap_format_t | 离线 canvas 的格式。  
  
#### canvas_offline_custom_destroy 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_custom_destroy

  * 函数原型：


    
    
    ret_t canvas_offline_custom_destroy (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_custom_end_draw 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_custom_end_draw

  * 函数原型：


    
    
    ret_t canvas_offline_custom_end_draw (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_custom_flush_bitmap 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_custom_flush_bitmap

  * 函数原型：


    
    
    ret_t canvas_offline_custom_flush_bitmap (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_custom_get_bitmap 函数

* * *

  * 函数功能：



> 用户自定义 canvas_offline_custom_get_bitmap

  * 函数原型：


    
    
    bitmap_t* canvas_offline_custom_get_bitmap (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回 bitmap_t 对象表示成功，返回 NULL 表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_destroy 函数

* * *

  * 函数功能：



> 释放离线 canvas 和离线 bitmap

  * 函数原型：


    
    
    ret_t canvas_offline_destroy (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_end_draw 函数

* * *

  * 函数功能：



> 设置离线 canvas 结束绘图

  * 函数原型：


    
    
    ret_t canvas_offline_end_draw (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_flush_bitmap 函数

* * *

  * 函数功能：



> 把离线 canvas 的数据放到绑定的 bitmap 中 该函数只有在 opengl 模式才需要调用，是否把显存中的数据回传到内存中。

  * 函数原型：


    
    
    ret_t canvas_offline_flush_bitmap (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_get_bitmap 函数

* * *

  * 函数功能：



> 获取离线 canvas 的离线 bitmap。

  * 函数原型：


    
    
    bitmap_t* canvas_offline_get_bitmap (canvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回 bitmap_t 对象表示成功，返回 NULL 表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
  
#### canvas_offline_set_canvas_orientation 函数

* * *

  * 函数功能：



> 设置离线画布旋转角度。 备注：对应 WITH_FAST_LCD_PORTRAIT 宏的使用

  * 函数原型：


    
    
    ret_t canvas_offline_set_canvas_orientation (canvas_t* canvas, lcd_orientation_t canvas_orientation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | 离线 canvas 对象。  
canvas_orientation | lcd_orientation_t | 旋转角度。  
  
#### bitmap 属性

* * *

> 绑定的离线 bitmap

  * 类型：bitmap_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### canvas_orientation 属性

* * *

> 快速的旋转角度（对应 WITH_FAST_LCD_PORTRAIT 宏的使用）

  * 类型：lcd_orientation_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
