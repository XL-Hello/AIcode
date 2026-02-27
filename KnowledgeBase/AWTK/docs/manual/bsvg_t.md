## bsvg_t

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
bsvg_draw | 绘制bsvg。  
bsvg_draw_path | 绘制bsvg路径。  
bsvg_init | 初始化bsvg对象。  
  
#### bsvg_draw 函数

* * *

  * 函数功能：



> 绘制bsvg。

  * 函数原型：


    
    
    ret_t bsvg_draw (bsvg_t* svg, vgcanvas_t* canvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
svg | bsvg_t* | SVG对象。  
canvas | vgcanvas_t* | vgcanvas对象。  
  
#### bsvg_draw_path 函数

* * *

  * 函数功能：



> 绘制bsvg路径。

  * 函数原型：


    
    
    ret_t bsvg_draw_path (bsvg_draw_ctx_t* ctx, const svg_path_t* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ctx | bsvg_draw_ctx_t* | 绘制上下文。  
path | const svg_path_t* | path对象。  
  
#### bsvg_init 函数

* * *

  * 函数功能：



> 初始化bsvg对象。

  * 函数原型：


    
    
    bsvg_t* bsvg_init (bsvg_t* svg, const uint32_t* data, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bsvg_t* | 返回解析后的svg。  
svg | bsvg_t* | svg对象。  
data | const uint32_t* | svg数据。  
size | uint32_t | data长度。
