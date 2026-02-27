## vgcanvas_nanovg_gl_t

### 概述

## 主要用于导出vgcanvas_nanovg_glx函数。

### 函数

函数名称 | 说明  
---|---  
vgcanvas_create_gl2 | 创建一个基于nanovg的vgcanvas对象。  
vgcanvas_create_gl3 | 创建一个基于nanovg的vgcanvas对象。  
  
#### vgcanvas_create_gl2 函数

* * *

  * 函数功能：



> 创建一个基于nanovg的vgcanvas对象。

  * 函数原型：


    
    
    vgcanvas_t* vgcanvas_create_gl2 (uint32_t w, uint32_t h, uint32_t stride, bitmap_format_t format, void* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | vgcanvas_t* | 返回vgcanvas对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
stride | uint32_t | 跨度。  
format | bitmap_format_t | 格式。  
win | void* | 窗口句柄。  
  
#### vgcanvas_create_gl3 函数

* * *

  * 函数功能：



> 创建一个基于nanovg的vgcanvas对象。

  * 函数原型：


    
    
    vgcanvas_t* vgcanvas_create_gl3 (uint32_t w, uint32_t h, uint32_t stride, bitmap_format_t format, void* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | vgcanvas_t* | 返回vgcanvas对象。  
w | uint32_t | 宽度。  
h | uint32_t | 高度。  
stride | uint32_t | 跨度。  
format | bitmap_format_t | 格式。  
win | void* | 窗口句柄。
