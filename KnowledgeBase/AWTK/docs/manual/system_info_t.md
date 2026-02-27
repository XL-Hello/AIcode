## system_info_t

### 概述

![image](images/system_info_t_0.png)

## 当前系统的信息。

### 函数

函数名称 | 说明  
---|---  
system_info | 获取system_info对象。  
system_info_create | 创建system_info对象。  
system_info_deinit | 释放system_info对象。  
system_info_fix_font_name | 修正字体名称，如果为NULL，返回缺省字体。  
system_info_init | 初始化system_info对象。  
system_info_set_app_name | 设置应用程序的名称。  
system_info_set_app_root | 设置app root。  
system_info_set_default_font | 设置缺省字体。  
system_info_set_device_pixel_ratio | 设置LCD密度。  
system_info_set_font_scale | 设置字体缩放比例。  
system_info_set_keyboard_type | 设置键盘类型。  
system_info_set_lcd_h | 设置LCD高度。  
system_info_set_lcd_orientation | 设置LCD的旋转角度。  
system_info_set_lcd_type | 设置LCD类型。  
system_info_set_lcd_w | 设置LCD宽度。  
tk_is_swap_size_by_orientation | 根据旧的和新的方向判断是否需要交换宽度和高度。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
app_name | const char* | 应用程序的名称。  
app_root | char* | 应用程序的根目录，用于定位资源文件。  
app_type | app_type_t | 应用程序的类型。  
country | const char* | locale中的国家。  
default_font | const char* | 缺省字体。  
device_orientation | const char* | 显示屏的方向名称，可选值：”portrait”表示竖屏，”landscape”表示横屏。  
device_pixel_ratio | float_t | 显示屏的密度。  
flags | uint32_t | 标志。请参考  
font_scale | float_t | 字体缩放比例，用于实现字体整体放大。  
keyboard_type | keyboard_type_t | 键盘类型。  
language | const char* | locale中的语言。  
lcd_h | uint32_t | 显示屏的高度。  
lcd_orientation | lcd_orientation_t | 显示屏的旋转角度。  
lcd_type | lcd_type_t | 显示屏的类型。  
lcd_w | uint32_t | 显示屏的宽度。  
  
#### system_info 函数

* * *

  * 函数功能：



> 获取system_info对象。

  * 函数原型：


    
    
    system_info_t* system_info ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | system_info_t* | 返回system_info对象。  
  
#### system_info_create 函数

* * *

  * 函数功能：



> 创建system_info对象。

  * 函数原型：


    
    
    system_info_t* system_info_create (app_type_t app_type, const char* app_name, const char* app_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | system_info_t* | 返回创建的对象指针。  
app_type | app_type_t | 应用程序的类型。  
app_name | const char* | 应用程序的名称。  
app_root | const char* | 应用程序的根目录，用于定位资源文件。  
  
#### system_info_deinit 函数

* * *

  * 函数功能：



> 释放system_info对象。

  * 函数原型：


    
    
    ret_t system_info_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### system_info_fix_font_name 函数

* * *

  * 函数功能：



> 修正字体名称，如果为NULL，返回缺省字体。

  * 函数原型：


    
    
    const char* system_info_fix_font_name (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回有效的字体名称。  
name | const char* | 字体名称。  
  
#### system_info_init 函数

* * *

  * 函数功能：



> 初始化system_info对象。

  * 函数原型：


    
    
    ret_t system_info_init (app_type_t app_type, const char* app_name, const char* app_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
app_type | app_type_t | 应用程序的类型。  
app_name | const char* | 应用程序的名称。  
app_root | const char* | 应用程序的根目录，用于定位资源文件。  
  
#### system_info_set_app_name 函数

* * *

  * 函数功能：



> 设置应用程序的名称。

  * 函数原型：


    
    
    ret_t system_info_set_app_name (system_info_t* info, const char* app_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
app_name | const char* | 应用程序的名称。  
  
#### system_info_set_app_root 函数

* * *

  * 函数功能：



> 设置app root。

  * 函数原型：


    
    
    ret_t system_info_set_app_root (system_info_t* info, const char* app_root);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
app_root | const char* | app root。  
  
#### system_info_set_default_font 函数

* * *

  * 函数功能：



> 设置缺省字体。

  * 函数原型：


    
    
    ret_t system_info_set_default_font (system_info_t* info, const char* default_font);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
default_font | const char* | 缺省字体。  
  
#### system_info_set_device_pixel_ratio 函数

* * *

  * 函数功能：



> 设置LCD密度。

  * 函数原型：


    
    
    ret_t system_info_set_device_pixel_ratio (system_info_t* info, float_t device_pixel_ratio);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
device_pixel_ratio | float_t | 设置LCD密度。  
  
#### system_info_set_font_scale 函数

* * *

  * 函数功能：



> 设置字体缩放比例。

  * 函数原型：


    
    
    ret_t system_info_set_font_scale (system_info_t* info, float_t font_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
font_scale | float_t | 字体缩放比例。  
  
#### system_info_set_keyboard_type 函数

* * *

  * 函数功能：



> 设置键盘类型。

  * 函数原型：


    
    
    ret_t system_info_set_keyboard_type (system_info_t* info, keyboard_type_t keyboard_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
keyboard_type | keyboard_type_t | 键盘类型。  
  
#### system_info_set_lcd_h 函数

* * *

  * 函数功能：



> 设置LCD高度。

  * 函数原型：


    
    
    ret_t system_info_set_lcd_h (system_info_t* info, uint32_t lcd_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
lcd_h | uint32_t | 设置LCD高度。  
  
#### system_info_set_lcd_orientation 函数

* * *

  * 函数功能：



> 设置LCD的旋转角度。

  * 函数原型：


    
    
    ret_t system_info_set_lcd_orientation (system_info_t* info, lcd_orientation_t lcd_orientation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
lcd_orientation | lcd_orientation_t | 设置LCD的旋转角度。  
  
#### system_info_set_lcd_type 函数

* * *

  * 函数功能：



> 设置LCD类型。

  * 函数原型：


    
    
    ret_t system_info_set_lcd_type (system_info_t* info, lcd_type_t lcd_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
lcd_type | lcd_type_t | 设置LCD类型。  
  
#### system_info_set_lcd_w 函数

* * *

  * 函数功能：



> 设置LCD宽度。

  * 函数原型：


    
    
    ret_t system_info_set_lcd_w (system_info_t* info, uint32_t lcd_w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
info | system_info_t* | system_info对象。  
lcd_w | uint32_t | 设置LCD宽度。  
  
#### tk_is_swap_size_by_orientation 函数

* * *

  * 函数功能：



> 根据旧的和新的方向判断是否需要交换宽度和高度。

  * 函数原型：


    
    
    bool_t tk_is_swap_size_by_orientation (lcd_orientation_t old_orientation, lcd_orientation_t new_orientation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回是否需要交换宽度和高度。  
old_orientation | lcd_orientation_t | 旧的方向。  
new_orientation | lcd_orientation_t | 新的方向。  
  
#### app_name 属性

* * *

> 应用程序的名称。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### app_root 属性

* * *

> 应用程序的根目录，用于定位资源文件。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### app_type 属性

* * *

> 应用程序的类型。

  * 类型：app_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### country 属性

* * *

> locale中的国家。
> 
> 只能通过object_get_prop函数访问。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### default_font 属性

* * *

> 缺省字体。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### device_orientation 属性

* * *

> 显示屏的方向名称，可选值：”portrait”表示竖屏，”landscape”表示横屏。
> 
> 只能通过object_get_prop函数访问。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### device_pixel_ratio 属性

* * *

> 显示屏的密度。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### flags 属性

* * *

> 标志。请参考{system_info_flag_t}。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### font_scale 属性

* * *

> 字体缩放比例，用于实现字体整体放大。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### keyboard_type 属性

* * *

> 键盘类型。

  * 类型：keyboard_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### language 属性

* * *

> locale中的语言。
> 
> 只能通过object_get_prop函数访问。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lcd_h 属性

* * *

> 显示屏的高度。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lcd_orientation 属性

* * *

> 显示屏的旋转角度。

  * 类型：lcd_orientation_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lcd_type 属性

* * *

> 显示屏的类型。

  * 类型：lcd_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### lcd_w 属性

* * *

> 显示屏的宽度。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
