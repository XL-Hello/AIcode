## lcd_type_t

### 概述

LCD类型常量定义。

### 常量

名称 | 说明  
---|---  
LCD_FRAMEBUFFER | 基于FrameBuffer的LCD。  
LCD_REGISTER | 基于寄存器的LCD。  
LCD_VGCANVAS | 基于VGCANVS的LCD。仅在支持OpenGL时，用nanovg实现。  
LCD_MONO | 单色LCD。  
LCD_CLUT | 颜色表 LCD。  
LCD_COMPOSITOR | 复合LCD。用于同时使用多个 LCD 的情况
