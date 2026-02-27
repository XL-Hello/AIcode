## bitmap_flag_t

### 概述

位图标志常量定义。

### 常量

名称 | 说明  
---|---  
BITMAP_FLAG_NONE | 无特殊标志。  
BITMAP_FLAG_OPAQUE | 不透明图片。  
BITMAP_FLAG_IMMUTABLE | 图片内容不会变化。  
BITMAP_FLAG_TEXTURE | OpenGL Texture, bitmap的id是有效的texture id。  
BITMAP_FLAG_CHANGED | 如果是MUTABLE的图片，更新时需要设置此标志，底层可能会做特殊处理，比如更新图片到GPU。  
BITMAP_FLAG_PREMULTI_ALPHA | 预乘alpha。  
BITMAP_FLAG_LCD_ORIENTATION | 位图数据已经处理了 lcd 旋转，同时说明 bitmap 的宽高和真实数据的宽高可能不一致  
BITMAP_FLAG_GPU_FBO_TEXTURE | 该位图为 GPU 的 fbo 数据。
