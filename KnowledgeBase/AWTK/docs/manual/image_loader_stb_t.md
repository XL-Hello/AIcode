## image_loader_stb_t

### 概述

![image](images/image_loader_stb_t_0.png)

stb图片加载器。

## stb主要用于加载jpg/png/gif等格式的图片，它功能强大，体积小巧。

### 函数

函数名称 | 说明  
---|---  
image_loader_stb | 获取stb图片加载器对象。  
stb_load_image | 加载图片。  
  
#### image_loader_stb 函数

* * *

  * 函数功能：



> 获取stb图片加载器对象。

  * 函数原型：


    
    
    image_loader_t* image_loader_stb ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | image_loader_t* | 返回图片加载器对象。  
  
#### stb_load_image 函数

* * *

  * 函数功能：



> 加载图片。

  * 函数原型：


    
    
    ret_t stb_load_image (int32_t subtype, const uint8_t* buff, uint32_t buff_size, bitmap_t* image, bitmap_format_t transparent_bitmap_format, bitmap_format_t opaque_bitmap_format, lcd_orientation_t o);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
subtype | int32_t | 资源类型。  
buff | const uint8_t* | 资源数据。  
buff_size | uint32_t | 资源数据长度。  
image | bitmap_t* | image 对象。  
transparent_bitmap_format | bitmap_format_t | 带透明通道的位图格式（只能 BITMAP_FMT_RGBA8888 和 BITMAP_FMT_RGBA8888 二选一，其他类型默认都为 BITMAP_FMT_RGBA8888）  
opaque_bitmap_format | bitmap_format_t | 不透明位图格式（暂时支持 BITMAP_FMT_RGBA8888，BITMAP_FMT_RGBA8888，16 位色和 24 位色以及 mono 格式）  
o | lcd_orientation_t | 旋转方向
