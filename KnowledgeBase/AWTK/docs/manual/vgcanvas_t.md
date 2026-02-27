## vgcanvas_t

### 概述

矢量图画布抽象基类。

具体实现时可以使用agg，nanovg, cairo和skia等方式。

cairo和skia体积太大，不适合嵌入式平台，但在PC平台也是一种选择。

目前我们只提供了基于nanovg的实现，支持软件渲染和硬件渲染。

我们对nanovg进行了一些改进:

  * 可以用agg/agge实现软件渲染(暂时不支持文本绘制)。

  * 可以用bgfx使用DirectX(Windows平台)和Metal(iOS)平台硬件加速。




![image](images/vgcanvas_t_0.png)

示例：
    
    
    vgcanvas_t* vg = canvas_get_vgcanvas(c);
    vgcanvas_save(vg);
    vgcanvas_translate(vg, 0, 100);
    
    vgcanvas_set_line_width(vg, 1);
    vgcanvas_set_fill_color(vg, color_init(0xff, 0, 0, 0xff));
    vgcanvas_rect(vg, 5, 5, 100, 100);
    vgcanvas_fill(vg);
    vgcanvas_restore(vg);
    

## >请参考：https://www.w3schools.com/tags/ref_canvas.asp

### 函数

函数名称 | 说明  
---|---  
vgcanvas_arc | 生成一条圆弧。  
vgcanvas_arc_to | 生成一条圆弧路径到指定点。  
vgcanvas_begin_frame | 开始绘制，系统内部调用。  
vgcanvas_begin_path | 清除之前的路径，并重新开始一条路径。  
vgcanvas_bezier_to | 生成一条三次贝塞尔曲线。  
vgcanvas_bind_fbo | 绑定 fbo 对象。  
vgcanvas_cast | 转换为vgcanvas对象(供脚本语言使用)。  
vgcanvas_clear_cache | 释放vgcanvas对象的缓冲数据。  
vgcanvas_clear_rect | 用颜色清除指定矩形区域。  
vgcanvas_clip_path | 使用当前的path裁剪。  
vgcanvas_clip_rect | 矩形裁剪。  
vgcanvas_close_path | 闭合路径。  
vgcanvas_create | 创建vgcanvas。  
vgcanvas_create_fbo | 创建 fbo 对象。  
vgcanvas_destroy | 销毁vgcanvas对象。  
vgcanvas_destroy_fbo | 销毁 fbo 对象。  
vgcanvas_draw_circle | 画圆。  
vgcanvas_draw_icon | 绘制图标。  
vgcanvas_draw_image | 绘制图片。  
vgcanvas_draw_image_repeat | 绘制图片。  
vgcanvas_ellipse | 生成一个椭圆路径。  
vgcanvas_end_frame | 结束绘制。系统内部调用。  
vgcanvas_fbo_to_bitmap | 把 fbo 对象的数据拷贝到 bitmap 中。  
vgcanvas_fill | 填充多边形。  
vgcanvas_fill_text | 绘制文本。  
vgcanvas_flush | flush  
vgcanvas_get_canvas | 获取 canvas 对象。  
vgcanvas_get_clip_rect | 获取矩形裁剪。  
vgcanvas_get_height | 获取高度。  
vgcanvas_get_text_metrics | 获取当前字体的度量信息。  
vgcanvas_get_width | 获取宽度。  
vgcanvas_intersect_clip_rect | 设置一个与前一个裁剪区做交集的矩形裁剪区。  
vgcanvas_is_point_in_path | 检查点是否在当前路径中。  
vgcanvas_is_rectf_in_clip_rect | 矩形区域是否在矩形裁剪中。  
vgcanvas_line_to | 生成一条线段(从当前点到目标点)。  
vgcanvas_measure_text | 测量文本的宽度。  
vgcanvas_move_to | 移动当前点到指定点。  
vgcanvas_paint | 用图片填充/画多边形(可能存在可移植性问题，除非必要请勿使用)。  
vgcanvas_path_winding | 设置路径填充实心与否。  
vgcanvas_quad_to | 生成一条二次贝塞尔曲线。  
vgcanvas_rect | 生成一个矩形路径。  
vgcanvas_reinit | 重新初始化，系统内部调用。  
vgcanvas_reset | 重置所有状态。  
vgcanvas_reset_curr_state | 重置当前状态。  
vgcanvas_restore | 恢复上次save的状态。  
vgcanvas_rotate | 旋转。  
vgcanvas_rounded_rect | 生成一个圆角矩形路径。  
vgcanvas_save | 保存当前的状态。如颜色和矩阵等信息。  
vgcanvas_scale | 缩放。  
vgcanvas_set_antialias | 设置是否启用反走样。  
vgcanvas_set_fill_color | 设置填充颜色。  
vgcanvas_set_fill_color_str | 设置填充颜色。  
vgcanvas_set_fill_gradient | 设置填充颜色为渐变色。  
vgcanvas_set_fill_linear_gradient | 设置填充颜色为线性渐变色。  
vgcanvas_set_fill_radial_gradient | 设置填充颜色为径向渐变色。  
vgcanvas_set_font | 设置字体的名称。  
vgcanvas_set_font_size | 设置字体的大小。  
vgcanvas_set_global_alpha | 设置全局透明度。  
vgcanvas_set_line_cap | 设置line cap。  
vgcanvas_set_line_join | 设置line join。  
vgcanvas_set_line_width | 设置线条的宽度。  
vgcanvas_set_miter_limit | 设置miter limit。  
vgcanvas_set_stroke_color | 设置线条颜色。  
vgcanvas_set_stroke_color_str | 设置线条颜色。  
vgcanvas_set_stroke_gradient | 设置线条颜色为渐变色。  
vgcanvas_set_stroke_linear_gradient | 设置线条颜色为线性渐变色。  
vgcanvas_set_stroke_radial_gradient | 设置线条颜色为径向渐变色。  
vgcanvas_set_text_align | 设置文本水平对齐的方式。  
vgcanvas_set_text_baseline | 设置文本垂直对齐的方式。  
vgcanvas_set_transform | 设置变换矩阵。  
vgcanvas_stroke | 画线。  
vgcanvas_transform | 变换矩阵。  
vgcanvas_translate | 平移。  
vgcanvas_unbind_fbo | 解开绑定 fbo 对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
anti_alias | bool_t | 是否启用反走样功能。  
fill_color | color_t | 填充颜色  
font | char* | 字体。  
font_size | float_t | 字体大小。  
global_alpha | float_t | 全局alpha。  
h | uint32_t | canvas的高度  
line_cap | const char* | line_cap。  
line_join | const char* | line_join。  
line_width | float_t | 线宽。  
miter_limit | float_t | miter_limit。  
ratio | float_t | 显示比例。  
stride | uint32_t | 一行占的字节  
stroke_color | color_t | 线条颜色  
text_align | char* | 文本对齐方式。  
text_baseline | char* | 文本基线。  
w | uint32_t | canvas的宽度  
  
#### vgcanvas_arc 函数

* * *

  * 函数功能：



> 生成一条圆弧。

  * 函数原型：


    
    
    ret_t vgcanvas_arc (vgcanvas_t* vg, float_t x, float_t y, float_t r, float_t start_angle, float_t end_angle, bool_t ccw);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | 原点x坐标。  
y | float_t | 原点y坐标。  
r | float_t | 半径。  
start_angle | float_t | 起始角度（单位：弧度）。  
end_angle | float_t | 结束角度（单位：弧度）。  
ccw | bool_t | 是否逆时针。  
  
#### vgcanvas_arc_to 函数

* * *

  * 函数功能：



> 生成一条圆弧路径到指定点。

  * 函数原型：


    
    
    ret_t vgcanvas_arc_to (vgcanvas_t* vg, float_t x1, float_t y1, float_t x2, float_t y2, float_t r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x1 | float_t | 起始点x坐标。  
y1 | float_t | 起始点y坐标。  
x2 | float_t | 结束点x坐标。  
y2 | float_t | 结束点y坐标。  
r | float_t | 半径。  
  
#### vgcanvas_begin_frame 函数

* * *

  * 函数功能：



> 开始绘制，系统内部调用。

  * 函数原型：


    
    
    ret_t vgcanvas_begin_frame (vgcanvas_t* vg, const dirty_rects_t* dirty_rects);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
dirty_rects | const dirty_rects_t* | 需要绘制的区域。  
  
#### vgcanvas_begin_path 函数

* * *

  * 函数功能：



> 清除之前的路径，并重新开始一条路径。

  * 函数原型：


    
    
    ret_t vgcanvas_begin_path (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_bezier_to 函数

* * *

  * 函数功能：



> 生成一条三次贝塞尔曲线。

  * 函数原型：


    
    
    ret_t vgcanvas_bezier_to (vgcanvas_t* vg, float_t cp1x, float_t cp1y, float_t cp2x, float_t cp2y, float_t x, float_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
cp1x | float_t | 控制点1x坐标。  
cp1y | float_t | 控制点1y坐标。  
cp2x | float_t | 控制点2x坐标。  
cp2y | float_t | 控制点2y坐标。  
x | float_t | x坐标。  
y | float_t | y坐标。  
  
#### vgcanvas_bind_fbo 函数

* * *

  * 函数功能：



> 绑定 fbo 对象。

  * 函数原型：


    
    
    ret_t vgcanvas_bind_fbo (vgcanvas_t* vg, framebuffer_object_t* fbo);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
fbo | framebuffer_object_t* | 需要创建 fbo 的对象。  
  
#### vgcanvas_cast 函数

* * *

  * 函数功能：



> 转换为vgcanvas对象(供脚本语言使用)。

  * 函数原型：


    
    
    vgcanvas_t* vgcanvas_cast (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | vgcanvas_t* | vgcanvas对象。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_clear_cache 函数

* * *

  * 函数功能：



> 释放vgcanvas对象的缓冲数据。

  * 函数原型：


    
    
    ret_t vgcanvas_clear_cache (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_clear_rect 函数

* * *

  * 函数功能：



> 用颜色清除指定矩形区域。

  * 函数原型：


    
    
    ret_t vgcanvas_clear_rect (vgcanvas_t* vg, float_t x, float_t y, float_t w, float_t h, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
w | float_t | 宽度。  
h | float_t | 高度。  
color | color_t | 颜色。  
  
#### vgcanvas_clip_path 函数

* * *

  * 函数功能：



> 使用当前的path裁剪。 目前只有部分backend支持(如cairo)。

  * 函数原型：


    
    
    ret_t vgcanvas_clip_path (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_clip_rect 函数

* * *

  * 函数功能：



> 矩形裁剪。

  * 函数原型：


    
    
    ret_t vgcanvas_clip_rect (vgcanvas_t* vg, float_t x, float_t y, float_t w, float_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
w | float_t | 宽度。  
h | float_t | 高度。  
  
#### vgcanvas_close_path 函数

* * *

  * 函数功能：



> 闭合路径。
> 
> 闭合路径是指把起点和终点连接起来，形成一个封闭的多边形。

  * 函数原型：


    
    
    ret_t vgcanvas_close_path (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_create 函数

* * *

  * 函数功能：



> 创建vgcanvas。

  * 函数原型：


    
    
    vgcanvas_t* vgcanvas_create (uint32_t w, uint32_t h, uint32_t stride, bitmap_format_t format, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | vgcanvas_t* | 返回vgcanvas对象。  
w | uint32_t | 宽度  
h | uint32_t | 高度  
stride | uint32_t | 一行占用的字节数。  
format | bitmap_format_t | 如果data是framebuffer，format指定data的格式。  
data | void* | framebuffer或其它ctx。  
  
#### vgcanvas_create_fbo 函数

* * *

  * 函数功能：



> 创建 fbo 对象。

  * 函数原型：


    
    
    ret_t vgcanvas_create_fbo (vgcanvas_t* vg, uint32_t w, uint32_t h, bool_t custom_draw_model, framebuffer_object_t* fbo);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
w | uint32_t | fbo 对象的宽。  
h | uint32_t | fbo 对象的高。  
custom_draw_model | bool_t | 是否脱离 awtk 默认的 OpenGL 绘图方法。  
fbo | framebuffer_object_t* | 需要创建 fbo 的对象。  
  
#### vgcanvas_destroy 函数

* * *

  * 函数功能：



> 销毁vgcanvas对象。

  * 函数原型：


    
    
    ret_t vgcanvas_destroy (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_destroy_fbo 函数

* * *

  * 函数功能：



> 销毁 fbo 对象。

  * 函数原型：


    
    
    ret_t vgcanvas_destroy_fbo (vgcanvas_t* vg, framebuffer_object_t* fbo);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
fbo | framebuffer_object_t* | 需要创建 fbo 的对象。  
  
#### vgcanvas_draw_circle 函数

* * *

  * 函数功能：



> 画圆。

  * 函数原型：


    
    
    ret_t vgcanvas_draw_circle (vgcanvas_t* vg, double x, double y, double r, color_t color, bool_t fill, bool_t stroke);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | double | x坐标。  
y | double | y坐标。  
r | double | 半径。  
color | color_t | 颜色。  
fill | bool_t | 是否填充。  
stroke | bool_t | 是否画线。  
  
#### vgcanvas_draw_icon 函数

* * *

  * 函数功能：



> 绘制图标。

绘制图标时会根据屏幕密度进行自动缩放，而绘制普通图片时不会。

  * 函数原型：


    
    
    ret_t vgcanvas_draw_icon (vgcanvas_t* vg, bitmap_t* img, float_t sx, float_t sy, float_t sw, float_t sh, float_t dx, float_t dy, float_t dw, float_t dh);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
img | bitmap_t* | 图片。  
sx | float_t | sx  
sy | float_t | sy  
sw | float_t | sw  
sh | float_t | sh  
dx | float_t | dx  
dy | float_t | dy  
dw | float_t | dw  
dh | float_t | dh  
  
#### vgcanvas_draw_image 函数

* * *

  * 函数功能：



> 绘制图片。

  * 函数原型：


    
    
    ret_t vgcanvas_draw_image (vgcanvas_t* vg, bitmap_t* img, float_t sx, float_t sy, float_t sw, float_t sh, float_t dx, float_t dy, float_t dw, float_t dh);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
img | bitmap_t* | 图片。  
sx | float_t | sx  
sy | float_t | sy  
sw | float_t | sw  
sh | float_t | sh  
dx | float_t | dx  
dy | float_t | dy  
dw | float_t | dw  
dh | float_t | dh  
  
#### vgcanvas_draw_image_repeat 函数

* * *

  * 函数功能：



> 绘制图片。

备注： 当绘制区域大于原图区域时，多余的绘制区域会重复绘制原图区域的东西。（绘制图区按照绘制图片的宽高来绘制的） 当绘制图片的宽高和原图的不同，在重复绘制的同时加入缩放。

  * 函数原型：


    
    
    ret_t vgcanvas_draw_image_repeat (vgcanvas_t* vg, bitmap_t* img, float_t sx, float_t sy, float_t sw, float_t sh, float_t dx, float_t dy, float_t dw, float_t dh, float_t dst_w, float_t dst_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
img | bitmap_t* | 图片。  
sx | float_t | 原图区域的 x  
sy | float_t | 原图区域的 y  
sw | float_t | 原图区域的 w  
sh | float_t | 原图区域的 h  
dx | float_t | 绘制区域的 x  
dy | float_t | 绘制区域的 y  
dw | float_t | 绘制区域的 w  
dh | float_t | 绘制区域的 h  
dst_w | float_t | 绘制图片的宽  
dst_h | float_t | 绘制图片的高  
  
#### vgcanvas_ellipse 函数

* * *

  * 函数功能：



> 生成一个椭圆路径。

  * 函数原型：


    
    
    ret_t vgcanvas_ellipse (vgcanvas_t* vg, float_t x, float_t y, float_t rx, float_t ry);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
rx | float_t | 圆角半径。  
ry | float_t | 圆角半径。  
  
#### vgcanvas_end_frame 函数

* * *

  * 函数功能：



> 结束绘制。系统内部调用。

  * 函数原型：


    
    
    ret_t vgcanvas_end_frame (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_fbo_to_bitmap 函数

* * *

  * 函数功能：



> 把 fbo 对象的数据拷贝到 bitmap 中。

  * 函数原型：


    
    
    ret_t vgcanvas_fbo_to_bitmap (vgcanvas_t* vg, framebuffer_object_t* fbo, bitmap_t* img, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
fbo | framebuffer_object_t* | 需要创建 fbo 的对象。  
img | bitmap_t* | 输出的 bitmap 的对象。  
r | const rect_t* | 需要拷贝的区域。  
  
#### vgcanvas_fill 函数

* * *

  * 函数功能：



> 填充多边形。

  * 函数原型：


    
    
    ret_t vgcanvas_fill (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_fill_text 函数

* * *

  * 函数功能：



> 绘制文本。

  * 函数原型：


    
    
    ret_t vgcanvas_fill_text (vgcanvas_t* vg, const char* text, float_t x, float_t y, float_t max_width);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
text | const char* | text  
x | float_t | x坐标。  
y | float_t | y坐标。  
max_width | float_t | 最大宽度。  
  
#### vgcanvas_flush 函数

* * *

  * 函数功能：



> flush

  * 函数原型：


    
    
    ret_t vgcanvas_flush (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_get_canvas 函数

* * *

  * 函数功能：



> 获取 canvas 对象。

  * 函数原型：


    
    
    canvas_t* vgcanvas_get_canvas (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | 成功返回 canvas 对象，失败返回 NULL。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_get_clip_rect 函数

* * *

  * 函数功能：



> 获取矩形裁剪。

  * 函数原型：


    
    
    const rectf_t* vgcanvas_get_clip_rect (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const rectf_t* | 返回裁剪区。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_get_height 函数

* * *

  * 函数功能：



> 获取高度。

  * 函数原型：


    
    
    wh_t vgcanvas_get_height (vgcanvas_t* vgcanvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回高度。  
vgcanvas | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_get_text_metrics 函数

* * *

  * 函数功能：



> 获取当前字体的度量信息。

  * 函数原型：


    
    
    ret_t vgcanvas_get_text_metrics (vgcanvas_t* vg, float_t* ascent, float_t* descent, float_t* line_hight);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
ascent | float_t* | 用于返回ascent。  
descent | float_t* | 用于返回descent。  
line_hight | float_t* | 用于返回line height。  
  
#### vgcanvas_get_width 函数

* * *

  * 函数功能：



> 获取宽度。

  * 函数原型：


    
    
    wh_t vgcanvas_get_width (vgcanvas_t* vgcanvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回宽度。  
vgcanvas | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_intersect_clip_rect 函数

* * *

  * 函数功能：



> 设置一个与前一个裁剪区做交集的矩形裁剪区。 如果下面这种情况，则不能直接调用 rect_intersect 函数来做矩形交集和 vgcanvas_clip_rect 函数设置裁剪区，而采用本函数做交集。 由于缩放和旋转以及平移会导致 vg 的坐标系和上一个裁剪区的坐标系不同， 导致直接使用做交集的话，裁剪区会出错。
    
    
    vgcanvas_clip_rect(vg, old_r.x, old_r.y, old_r.w, old_r.h);
    vgcanvas_save(vg);
    vgcanvas_scale(vg, scale_x, scale_y);
    vgcanvas_rotate(vg, TK_D2R(15));
    vgcanvas_intersect_clip_rect(vg, r.x, r.y, r.w, r.h);
    ..................
    vgcanvas_restore(vg);
    

  * 函数原型：


    
    
    ret_t vgcanvas_intersect_clip_rect (vgcanvas_t* vg, float_t x, float_t y, float_t w, float_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
w | float_t | 宽度。  
h | float_t | 高度。  
  
#### vgcanvas_is_point_in_path 函数

* * *

  * 函数功能：



> 检查点是否在当前路径中。

  * 函数原型：


    
    
    bool_t vgcanvas_is_point_in_path (vgcanvas_t* vg, float_t x, float_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示在，否则表示不在。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
  
#### vgcanvas_is_rectf_in_clip_rect 函数

* * *

  * 函数功能：



> 矩形区域是否在矩形裁剪中。

  * 函数原型：


    
    
    bool_t vgcanvas_is_rectf_in_clip_rect (vgcanvas_t* vg, float_t left, float_t top, float_t right, float_t bottom);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回 TURE 则在区域中，返回 FALSE 则不在区域中。  
vg | vgcanvas_t* | vgcanvas对象。  
left | float_t | 矩形区域左边。  
top | float_t | 矩形区域上边。  
right | float_t | 矩形区域右边。  
bottom | float_t | 矩形区域下边。  
  
#### vgcanvas_line_to 函数

* * *

  * 函数功能：



> 生成一条线段(从当前点到目标点)。

  * 函数原型：


    
    
    ret_t vgcanvas_line_to (vgcanvas_t* vg, float_t x, float_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
  
#### vgcanvas_measure_text 函数

* * *

  * 函数功能：



> 测量文本的宽度。

  * 函数原型：


    
    
    float_t vgcanvas_measure_text (vgcanvas_t* vg, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回text的宽度。  
vg | vgcanvas_t* | vgcanvas对象。  
text | const char* | text  
  
#### vgcanvas_move_to 函数

* * *

  * 函数功能：



> 移动当前点到指定点。

  * 函数原型：


    
    
    ret_t vgcanvas_move_to (vgcanvas_t* vg, float_t x, float_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
  
#### vgcanvas_paint 函数

* * *

  * 函数功能：



> 用图片填充/画多边形(可能存在可移植性问题，除非必要请勿使用)。 多边形的顶点必须在图片范围内，可以通过矩阵变化画到不同的位置。

  * 函数原型：


    
    
    ret_t vgcanvas_paint (vgcanvas_t* vg, bool_t stroke, bitmap_t* img);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
stroke | bool_t | TRUE表示画线FALSE表示填充。  
img | bitmap_t* | 图片。  
  
#### vgcanvas_path_winding 函数

* * *

  * 函数功能：



> 设置路径填充实心与否。
> 
> CCW(1)为实心，CW(2)为镂空，设置其他则默认根据非零环绕规则判断(nonzero)。

  * 函数原型：


    
    
    ret_t vgcanvas_path_winding (vgcanvas_t* vg, bool_t dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
dir | bool_t | 填充方法。  
  
#### vgcanvas_quad_to 函数

* * *

  * 函数功能：



> 生成一条二次贝塞尔曲线。

  * 函数原型：


    
    
    ret_t vgcanvas_quad_to (vgcanvas_t* vg, float_t cpx, float_t cpy, float_t x, float_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
cpx | float_t | 控制点x坐标。  
cpy | float_t | 控制点y坐标。  
x | float_t | x坐标。  
y | float_t | y坐标。  
  
#### vgcanvas_rect 函数

* * *

  * 函数功能：



> 生成一个矩形路径。

  * 函数原型：


    
    
    ret_t vgcanvas_rect (vgcanvas_t* vg, float_t x, float_t y, float_t w, float_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
w | float_t | 宽度。  
h | float_t | 高度。  
  
#### vgcanvas_reinit 函数

* * *

  * 函数功能：



> 重新初始化，系统内部调用。

  * 函数原型：


    
    
    ret_t vgcanvas_reinit (vgcanvas_t* vg, uint32_t w, uint32_t h, uint32_t stride, bitmap_format_t format, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
w | uint32_t | 宽度  
h | uint32_t | 高度  
stride | uint32_t | 一行占用的字节数。  
format | bitmap_format_t | 如果data是framebuffer，format指定data的格式。  
data | void* | framebuffer或其它ctx。  
  
#### vgcanvas_reset 函数

* * *

  * 函数功能：



> 重置所有状态。

  * 函数原型：


    
    
    ret_t vgcanvas_reset (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_reset_curr_state 函数

* * *

  * 函数功能：



> 重置当前状态。

  * 函数原型：


    
    
    ret_t vgcanvas_reset_curr_state (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_restore 函数

* * *

  * 函数功能：



> 恢复上次save的状态。
> 
> save/restore必须配套使用，否则可能导致状态混乱。

  * 函数原型：


    
    
    ret_t vgcanvas_restore (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_rotate 函数

* * *

  * 函数功能：



> 旋转。

  * 函数原型：


    
    
    ret_t vgcanvas_rotate (vgcanvas_t* vg, float_t rad);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
rad | float_t | 旋转角度(单位：弧度)  
  
#### vgcanvas_rounded_rect 函数

* * *

  * 函数功能：



> 生成一个圆角矩形路径。

  * 函数原型：


    
    
    ret_t vgcanvas_rounded_rect (vgcanvas_t* vg, float_t x, float_t y, float_t w, float_t h, float_t r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x坐标。  
y | float_t | y坐标。  
w | float_t | 宽度。  
h | float_t | 高度。  
r | float_t | 圆角半径。  
  
#### vgcanvas_save 函数

* * *

  * 函数功能：



> 保存当前的状态。如颜色和矩阵等信息。
> 
> save/restore必须配套使用，否则可能导致状态混乱。

  * 函数原型：


    
    
    ret_t vgcanvas_save (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_scale 函数

* * *

  * 函数功能：



> 缩放。

  * 函数原型：


    
    
    ret_t vgcanvas_scale (vgcanvas_t* vg, float_t x, float_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x方向缩放比例。  
y | float_t | y方向缩放比例。  
  
#### vgcanvas_set_antialias 函数

* * *

  * 函数功能：



> 设置是否启用反走样。

  * 函数原型：


    
    
    ret_t vgcanvas_set_antialias (vgcanvas_t* vg, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
value | bool_t | 是否启用反走样。  
  
#### vgcanvas_set_fill_color 函数

* * *

  * 函数功能：



> 设置填充颜色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_fill_color (vgcanvas_t* vg, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
color | color_t | 颜色。  
  
#### vgcanvas_set_fill_color_str 函数

* * *

  * 函数功能：



> 设置填充颜色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_fill_color_str (vgcanvas_t* vg, const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
color | const char* | 颜色。  
  
#### vgcanvas_set_fill_gradient 函数

* * *

  * 函数功能：



> 设置填充颜色为渐变色。
> 
> 目前只有部分backend支持(如cairo)。

  * 函数原型：


    
    
    ret_t vgcanvas_set_fill_gradient (vgcanvas_t* vg, const vg_gradient_t* gradient);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
gradient | const vg_gradient_t* | gradient对象。  
  
#### vgcanvas_set_fill_linear_gradient 函数

* * *

  * 函数功能：



> 设置填充颜色为线性渐变色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_fill_linear_gradient (vgcanvas_t* vg, float_t sx, float_t sy, float_t ex, float_t ey, color_t icolor, color_t ocolor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
sx | float_t | start x  
sy | float_t | start y  
ex | float_t | end x  
ey | float_t | end y  
icolor | color_t | 开始颜色。  
ocolor | color_t | 结束颜色。  
  
#### vgcanvas_set_fill_radial_gradient 函数

* * *

  * 函数功能：



> 设置填充颜色为径向渐变色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_fill_radial_gradient (vgcanvas_t* vg, float_t cx, float_t cy, float_t inr, float_t outr, color_t icolor, color_t ocolor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
cx | float_t | center x  
cy | float_t | center y  
inr | float_t | 内环半径  
outr | float_t | 外环半径。  
icolor | color_t | 开始颜色。  
ocolor | color_t | 结束颜色。  
  
#### vgcanvas_set_font 函数

* * *

  * 函数功能：



> 设置字体的名称。

  * 函数原型：


    
    
    ret_t vgcanvas_set_font (vgcanvas_t* vg, const char* font);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
font | const char* | 字体名称。  
  
#### vgcanvas_set_font_size 函数

* * *

  * 函数功能：



> 设置字体的大小。

  * 函数原型：


    
    
    ret_t vgcanvas_set_font_size (vgcanvas_t* vg, float_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
size | float_t | 字体大小。  
  
#### vgcanvas_set_global_alpha 函数

* * *

  * 函数功能：



> 设置全局透明度。

  * 函数原型：


    
    
    ret_t vgcanvas_set_global_alpha (vgcanvas_t* vg, float_t alpha);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
alpha | float_t | global alpha。  
  
#### vgcanvas_set_line_cap 函数

* * *

  * 函数功能：



> 设置line cap。

  * 函数原型：


    
    
    ret_t vgcanvas_set_line_cap (vgcanvas_t* vg, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
value | const char* | 取值：butt  
  
#### vgcanvas_set_line_join 函数

* * *

  * 函数功能：



> 设置line join。

  * 函数原型：


    
    
    ret_t vgcanvas_set_line_join (vgcanvas_t* vg, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
value | const char* | 取值：bevel  
  
#### vgcanvas_set_line_width 函数

* * *

  * 函数功能：



> 设置线条的宽度。

  * 函数原型：


    
    
    ret_t vgcanvas_set_line_width (vgcanvas_t* vg, float_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
value | float_t | 线宽。  
  
#### vgcanvas_set_miter_limit 函数

* * *

  * 函数功能：



> 设置miter limit。

  * 函数原型：


    
    
    ret_t vgcanvas_set_miter_limit (vgcanvas_t* vg, float_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
value | float_t | miter limit  
  
#### vgcanvas_set_stroke_color 函数

* * *

  * 函数功能：



> 设置线条颜色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_stroke_color (vgcanvas_t* vg, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
color | color_t | 颜色。  
  
#### vgcanvas_set_stroke_color_str 函数

* * *

  * 函数功能：



> 设置线条颜色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_stroke_color_str (vgcanvas_t* vg, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
str | const char* | 颜色。  
  
#### vgcanvas_set_stroke_gradient 函数

* * *

  * 函数功能：



> 设置线条颜色为渐变色。
> 
> 目前只有部分backend支持(如cairo)。

  * 函数原型：


    
    
    ret_t vgcanvas_set_stroke_gradient (vgcanvas_t* vg, const vg_gradient_t* gradient);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
gradient | const vg_gradient_t* | gradient对象。  
  
#### vgcanvas_set_stroke_linear_gradient 函数

* * *

  * 函数功能：



> 设置线条颜色为线性渐变色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_stroke_linear_gradient (vgcanvas_t* vg, float_t sx, float_t sy, float_t ex, float_t ey, color_t icolor, color_t ocolor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
sx | float_t | start x  
sy | float_t | start y  
ex | float_t | end x  
ey | float_t | end y  
icolor | color_t | 开始颜色。  
ocolor | color_t | 结束颜色。  
  
#### vgcanvas_set_stroke_radial_gradient 函数

* * *

  * 函数功能：



> 设置线条颜色为径向渐变色。

  * 函数原型：


    
    
    ret_t vgcanvas_set_stroke_radial_gradient (vgcanvas_t* vg, float_t cx, float_t cy, float_t inr, float_t outr, color_t icolor, color_t ocolor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
cx | float_t | center x  
cy | float_t | center y  
inr | float_t | 内环半径  
outr | float_t | 外环半径。  
icolor | color_t | 开始颜色。  
ocolor | color_t | 结束颜色。  
  
#### vgcanvas_set_text_align 函数

* * *

  * 函数功能：



> 设置文本水平对齐的方式。

  * 函数原型：


    
    
    ret_t vgcanvas_set_text_align (vgcanvas_t* vg, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
value | const char* | 取值：left  
  
#### vgcanvas_set_text_baseline 函数

* * *

  * 函数功能：



> 设置文本垂直对齐的方式。

  * 函数原型：


    
    
    ret_t vgcanvas_set_text_baseline (vgcanvas_t* vg, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
value | const char* | 取值：top  
  
#### vgcanvas_set_transform 函数

* * *

  * 函数功能：



> 设置变换矩阵。

  * 函数原型：


    
    
    ret_t vgcanvas_set_transform (vgcanvas_t* vg, float_t a, float_t b, float_t c, float_t d, float_t e, float_t f);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
a | float_t | a  
b | float_t | b  
c | float_t | c  
d | float_t | d  
e | float_t | e  
f | float_t | f  
  
#### vgcanvas_stroke 函数

* * *

  * 函数功能：



> 画线。

  * 函数原型：


    
    
    ret_t vgcanvas_stroke (vgcanvas_t* vg);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
  
#### vgcanvas_transform 函数

* * *

  * 函数功能：



> 变换矩阵。

  * 函数原型：


    
    
    ret_t vgcanvas_transform (vgcanvas_t* vg, float_t a, float_t b, float_t c, float_t d, float_t e, float_t f);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
a | float_t | a  
b | float_t | b  
c | float_t | c  
d | float_t | d  
e | float_t | e  
f | float_t | f  
  
#### vgcanvas_translate 函数

* * *

  * 函数功能：



> 平移。

  * 函数原型：


    
    
    ret_t vgcanvas_translate (vgcanvas_t* vg, float_t x, float_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
x | float_t | x方向偏移。  
y | float_t | y方向偏移。  
  
#### vgcanvas_unbind_fbo 函数

* * *

  * 函数功能：



> 解开绑定 fbo 对象。

  * 函数原型：


    
    
    ret_t vgcanvas_unbind_fbo (vgcanvas_t* vg, framebuffer_object_t* fbo);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vg | vgcanvas_t* | vgcanvas对象。  
fbo | framebuffer_object_t* | 需要创建 fbo 的对象。  
  
#### anti_alias 属性

* * *

> 是否启用反走样功能。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### fill_color 属性

* * *

> 填充颜色

  * 类型：color_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### font 属性

* * *

> 字体。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### font_size 属性

* * *

> 字体大小。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### global_alpha 属性

* * *

> 全局alpha。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### h 属性

* * *

> canvas的高度

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### line_cap 属性

* * *

> line_cap。 @see http://www.w3school.com.cn/tags/canvas_linecap.asp

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### line_join 属性

* * *

> line_join。 @see http://www.w3school.com.cn/tags/canvas_linejoin.asp

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### line_width 属性

* * *

> 线宽。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### miter_limit 属性

* * *

> miter_limit。 @see http://www.w3school.com.cn/tags/canvas_miterlimit.asp

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### ratio 属性

* * *

> 显示比例。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### stride 属性

* * *

> 一行占的字节

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### stroke_color 属性

* * *

> 线条颜色

  * 类型：color_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### text_align 属性

* * *

> 文本对齐方式。

@see http://www.w3school.com.cn/tags/canvas_textalign.asp

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### text_baseline 属性

* * *

> 文本基线。

@see http://www.w3school.com.cn/tags/canvas_textbaseline.asp

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### w 属性

* * *

> canvas的宽度

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
