## global_t

### 概述

## TK全局对象。

### 函数

函数名称 | 说明  
---|---  
asset_loader_default_create | 创建缺省的资源加载器。  
asset_loader_zip_create | 创建zip资源加载器。  
asset_loader_zip_create_with_reader | 创建zip资源加载器。  
tk_deinit_internal | deinit。  
tk_enable_fast_lcd_portrait | 设置是否开启快速旋转功能。（开启这个功能需要定义 WITH_FAST_LCD_PORTRAIT 宏）  
tk_exit | public for web  
tk_get_pointer_x | 获取全局指针的X坐标。  
tk_get_pointer_y | 获取全局指针的Y坐标。  
tk_init | 初始化TK。  
tk_init_assets | 初始化资源。  
tk_init_internal | init。  
tk_is_pointer_pressed | 获取全局指针是否按下。  
tk_pre_init | 初始化基本功能。  
tk_quit | 退出TK事件主循环。  
tk_quit_ex | 退出TK事件主循环。  
tk_run | 进入TK事件主循环。  
tk_run_in_ui_thread | 后台线程在UI线程执行指定的函数。  
tk_set_lcd_orientation | 设置屏幕的旋转方向(XXX:目前仅支持0度,90度,180度和270度，旋转方向为逆时针方向)。  
  
#### asset_loader_default_create 函数

* * *

  * 函数功能：



> 创建缺省的资源加载器。

  * 函数原型：


    
    
    asset_loader_t* asset_loader_default_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | asset_loader_t* | 返回loader对象。  
  
#### asset_loader_zip_create 函数

* * *

  * 函数功能：



> 创建zip资源加载器。

  * 函数原型：


    
    
    asset_loader_t* asset_loader_zip_create (const char* zipfile);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | asset_loader_t* | 返回loader对象。  
zipfile | const char* | zip文件名。  
  
#### asset_loader_zip_create_with_reader 函数

* * *

  * 函数功能：



> 创建zip资源加载器。

  * 函数原型：


    
    
    asset_loader_t* asset_loader_zip_create_with_reader (data_reader_t* reader, bool_t own_the_reader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | asset_loader_t* | 返回loader对象。  
reader | data_reader_t* | reader对象。  
own_the_reader | bool_t | 如果希望销毁loader时销毁reader，请设置为TRUE。  
  
#### tk_deinit_internal 函数

* * *

  * 函数功能：



> deinit。 public for test program

  * 函数原型：


    
    
    ret_t tk_deinit_internal ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_enable_fast_lcd_portrait 函数

* * *

  * 函数功能：



> 设置是否开启快速旋转功能。（开启这个功能需要定义 WITH_FAST_LCD_PORTRAIT 宏） 备注：需要在 tk_set_lcd_orientation 函数之前调用

  * 函数原型：


    
    
    ret_t tk_enable_fast_lcd_portrait (bool_t enable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
enable | bool_t | 是否开启。  
  
#### tk_exit 函数

* * *

  * 函数功能：



> public for web

  * 函数原型：


    
    
    ret_t tk_exit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_get_pointer_x 函数

* * *

  * 函数功能：



> 获取全局指针的X坐标。

  * 函数原型：


    
    
    int32_t tk_get_pointer_x ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回全局指针的X坐标。  
  
#### tk_get_pointer_y 函数

* * *

  * 函数功能：



> 获取全局指针的Y坐标。

  * 函数原型：


    
    
    int32_t tk_get_pointer_y ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回全局指针的X坐标。  
  
#### tk_init 函数

* * *

  * 函数功能：



> 初始化TK。

  * 函数原型：


    
    
    ret_t tk_init (wh_t w, wh_t h, app_type_t app_type, const char* app_name, const char* app_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
w | wh_t | LCD宽度。  
h | wh_t | LCD高度。  
app_type | app_type_t | 应用程序的类型。  
app_name | const char* | 应用程序的名称(必须为常量字符串)。  
app_root | const char* | 应用程序的根目录，用于定位资源文件(必须为常量字符串)。  
  
#### tk_init_assets 函数

* * *

  * 函数功能：



> 初始化资源。

  * 函数原型：


    
    
    ret_t tk_init_assets ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_init_internal 函数

* * *

  * 函数功能：



> init。 public for test program

  * 函数原型：


    
    
    ret_t tk_init_internal ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_is_pointer_pressed 函数

* * *

  * 函数功能：



> 获取全局指针是否按下。

  * 函数原型：


    
    
    bool_t tk_is_pointer_pressed ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回全局指针是否按下。  
  
#### tk_pre_init 函数

* * *

  * 函数功能：



> 初始化基本功能。 在tk_init之前，应用程序可能需要加载配置文件， 为了保证这些功能正常工作，可以先调用tk_pre_init来初始化平台、内存和data reader等等。

  * 函数原型：


    
    
    ret_t tk_pre_init ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_quit 函数

* * *

  * 函数功能：



> 退出TK事件主循环。

  * 函数原型：


    
    
    ret_t tk_quit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_quit_ex 函数

* * *

  * 函数功能：



> 退出TK事件主循环。

  * 函数原型：


    
    
    ret_t tk_quit_ex (uint32_t delay);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
delay | uint32_t | 延迟退出的时间(毫秒)。  
  
#### tk_run 函数

* * *

  * 函数功能：



> 进入TK事件主循环。

  * 函数原型：


    
    
    ret_t tk_run ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### tk_run_in_ui_thread 函数

* * *

  * 函数功能：



> 后台线程在UI线程执行指定的函数。

  * 函数原型：


    
    
    ret_t tk_run_in_ui_thread (tk_callback_t func, void* ctx, bool_t wait_until_done);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
func | tk_callback_t | 函数。  
ctx | void* | 回调函数的上下文。  
wait_until_done | bool_t | 是否等待完成。  
  
#### tk_set_lcd_orientation 函数

* * *

  * 函数功能：



> 设置屏幕的旋转方向(XXX:目前仅支持0度,90度,180度和270度，旋转方向为逆时针方向)。

  * 函数原型：


    
    
    ret_t tk_set_lcd_orientation (lcd_orientation_t orientation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
orientation | lcd_orientation_t | 旋转方向。
