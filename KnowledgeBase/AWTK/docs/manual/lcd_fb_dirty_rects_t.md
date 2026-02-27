## lcd_fb_dirty_rects_t

### 概述

## lcd fb脏矩形。

### 函数

函数名称 | 说明  
---|---  
lcd_fb_dirty_rects_add_fb_info | 添加新的 fb 信息  
lcd_fb_dirty_rects_deinit | 清除 lcd_fb_dirty_rects_t 对象数据  
lcd_fb_dirty_rects_get_dirty_rects_by_fb | 根据 fb 来获取脏矩形对象  
lcd_fb_dirty_rects_init | 初始化 lcd_fb_dirty_rects_t 对象  
lcd_fb_dirty_rects_reinit | 修改 lcd_fb_dirty_rects_t 对象的宽高  
lcd_fb_dirty_rects_reset_dirty_rects_by_fb | 清除对应 fb 的脏矩形列表。  
lcd_fb_dirty_rects_update_all_fb_dirty_rect | 把当前脏矩形合并到所有 fb 的脏矩形中。  
lcd_fb_dirty_rects_update_all_fb_dirty_rects | 把当前脏矩形列表合并到所有 fb 的脏矩形中。  
  
#### lcd_fb_dirty_rects_add_fb_info 函数

* * *

  * 函数功能：



> 添加新的 fb 信息 如果已经存在的话，就不会重新添加

  * 函数原型：


    
    
    ret_t lcd_fb_dirty_rects_add_fb_info (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects, uint8_t* fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
fb | uint8_t* | fb 地址。  
  
#### lcd_fb_dirty_rects_deinit 函数

* * *

  * 函数功能：



> 清除 lcd_fb_dirty_rects_t 对象数据

  * 函数原型：


    
    
    ret_t lcd_fb_dirty_rects_deinit (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
  
#### lcd_fb_dirty_rects_get_dirty_rects_by_fb 函数

* * *

  * 函数功能：



> 根据 fb 来获取脏矩形对象

  * 函数原型：


    
    
    const dirty_rects_t* lcd_fb_dirty_rects_get_dirty_rects_by_fb (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects, uint8_t* fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const dirty_rects_t* | 成功返回脏矩形对象，失败返回 NULL。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
fb | uint8_t* | fb 地址。  
  
#### lcd_fb_dirty_rects_init 函数

* * *

  * 函数功能：



> 初始化 lcd_fb_dirty_rects_t 对象

  * 函数原型：


    
    
    ret_t lcd_fb_dirty_rects_init (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects, wh_t lcd_w, wh_t lcd_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
lcd_w | wh_t | lcd 的宽。  
lcd_h | wh_t | lcd 的高。  
  
#### lcd_fb_dirty_rects_reinit 函数

* * *

  * 函数功能：



> 修改 lcd_fb_dirty_rects_t 对象的宽高

  * 函数原型：


    
    
    ret_t lcd_fb_dirty_rects_reinit (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects, wh_t lcd_w, wh_t lcd_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
lcd_w | wh_t | lcd 的宽。  
lcd_h | wh_t | lcd 的高。  
  
#### lcd_fb_dirty_rects_reset_dirty_rects_by_fb 函数

* * *

  * 函数功能：



> 清除对应 fb 的脏矩形列表。

  * 函数原型：


    
    
    ret_t lcd_fb_dirty_rects_reset_dirty_rects_by_fb (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects, uint8_t* fb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
fb | uint8_t* | fb 地址。  
  
#### lcd_fb_dirty_rects_update_all_fb_dirty_rect 函数

* * *

  * 函数功能：



> 把当前脏矩形合并到所有 fb 的脏矩形中。

  * 函数原型：


    
    
    ret_t lcd_fb_dirty_rects_update_all_fb_dirty_rect (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects, const rect_t* dirty_rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
dirty_rect | const rect_t* | 当前脏矩形。  
  
#### lcd_fb_dirty_rects_update_all_fb_dirty_rects 函数

* * *

  * 函数功能：



> 把当前脏矩形列表合并到所有 fb 的脏矩形中。

  * 函数原型：


    
    
    ret_t lcd_fb_dirty_rects_update_all_fb_dirty_rects (lcd_fb_dirty_rects_t* lcd_fb_dirty_rects, const dirty_rects_t* dirty_rects);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd_fb_dirty_rects | lcd_fb_dirty_rects_t* | lcd_fb_dirty_rects_t对象。  
dirty_rects | const dirty_rects_t* | 当前脏矩形列表。
