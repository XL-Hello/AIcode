## theme_t

### 概述

## 窗体样式。

### 函数

函数名称 | 说明  
---|---  
theme | 获取缺省的窗体样式对象。  
theme_destroy | 析构并释放窗体样式对象。  
theme_find_style | 查找满足条件的style。  
theme_foreach | 遍历全部数据。  
theme_get_style_type | 获取窗体样式的风格类型。  
theme_load_from_asset | 加载窗体样式对象。  
theme_load_from_data | 加载窗体样式对象。  
theme_set | 设置缺省的窗体样式对象。  
theme_set_theme_data | 设置窗体样式的数据。  
  
#### theme 函数

* * *

  * 函数功能：



> 获取缺省的窗体样式对象。

  * 函数原型：


    
    
    theme_t* theme ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | theme_t* | 返回窗体样式对象。  
  
#### theme_destroy 函数

* * *

  * 函数功能：



> 析构并释放窗体样式对象。

  * 函数原型：


    
    
    ret_t theme_destroy (theme_t* theme);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
theme | theme_t* | 窗体样式对象。  
  
#### theme_find_style 函数

* * *

  * 函数功能：



> 查找满足条件的style。

  * 函数原型：


    
    
    const uint8_t* theme_find_style (theme_t* theme, const char* widget_type, const char* name, const char* widget_state);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const uint8_t* | 返回风格对象数据。  
theme | theme_t* | 窗体样式对象。  
widget_type | const char* | 控件的类型名。  
name | const char* | style的名称。  
widget_state | const char* | 控件的状态。  
  
#### theme_foreach 函数

* * *

  * 函数功能：



> 遍历全部数据。

  * 函数原型：


    
    
    ret_t theme_foreach (theme_t* theme, theme_on_data_t on_data, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
theme | theme_t* | 窗体样式对象。  
on_data | theme_on_data_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### theme_get_style_type 函数

* * *

  * 函数功能：



> 获取窗体样式的风格类型。

  * 函数原型：


    
    
    const char* theme_get_style_type (theme_t* theme);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回风格类型。  
theme | theme_t* | 窗体样式对象。  
  
#### theme_load_from_asset 函数

* * *

  * 函数功能：



> 加载窗体样式对象。

  * 函数原型：


    
    
    theme_t* theme_load_from_asset (asset_info_t* info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | theme_t* | 返回窗体样式对象。  
info | asset_info_t* | 资源对象。  
  
#### theme_load_from_data 函数

* * *

  * 函数功能：



> 加载窗体样式对象。

  * 函数原型：


    
    
    theme_t* theme_load_from_data (const char* name, const uint8_t* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | theme_t* | 返回窗体样式对象。  
name | const char* | 资源名。  
data | const uint8_t* | 窗体样式数据。  
size | uint32_t | 资源长度。  
  
#### theme_set 函数

* * *

  * 函数功能：



> 设置缺省的窗体样式对象。

  * 函数原型：


    
    
    ret_t theme_set (theme_t* theme);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
theme | theme_t* | 窗体样式对象。  
  
#### theme_set_theme_data 函数

* * *

  * 函数功能：



> 设置窗体样式的数据。

  * 函数原型：


    
    
    ret_t theme_set_theme_data (theme_t* theme, const uint8_t* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
theme | theme_t* | 窗体样式对象。  
data | const uint8_t* | 窗体样式数据。
