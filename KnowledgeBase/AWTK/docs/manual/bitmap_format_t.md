## bitmap_format_t

### 概述

位图格式常量定义。

### 常量

名称 | 说明  
---|---  
BITMAP_FMT_NONE | 无效格式。  
BITMAP_FMT_RGBA8888 | 一个像素占用4个字节，RGBA占一个字节，按内存地址递增。  
BITMAP_FMT_ABGR8888 | 一个像素占用4个字节，ABGR占一个字节，按内存地址递增。  
BITMAP_FMT_BGRA8888 | 一个像素占用4个字节，BGRA占一个字节，按内存地址递增。  
BITMAP_FMT_ARGB8888 | 一个像素占用4个字节，ARGB占一个字节，按内存地址递增。  
BITMAP_FMT_RGB565 | 一个像素占用2个字节，RGB分别占用5,6,5位, 按内存地址递增。  
BITMAP_FMT_BGR565 | 一个像素占用2个字节，BGR分别占用5,6,5位, 按内存地址递增。  
BITMAP_FMT_RGB888 | 一个像素占用3个字节，RGB占一个字节，按内存地址递增。  
BITMAP_FMT_BGR888 | 一个像素占用3个字节，RGB占一个字节，按内存地址递增。  
BITMAP_FMT_GRAY | 一个像素占用1个字节。  
BITMAP_FMT_MONO | 一个像素占用1比特。
