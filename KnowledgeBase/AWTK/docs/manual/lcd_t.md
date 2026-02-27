## lcd_t

### 概述

## 显示设备抽象基类。

### 函数

函数名称 | 说明  
---|---  
lcd_begin_frame | 准备绘制。  
lcd_clear_rect | 填充实心矩形。  
lcd_destroy | 销毁lcd对象。  
lcd_draw_glyph | 绘制字符。如果实现了measure_text/draw_text则不需要实现本函数。  
lcd_draw_hline | 绘制一条水平线。  
lcd_draw_image | 绘制图片。  
lcd_draw_image_matrix | 绘制图片。  
lcd_draw_points | 绘制一组点。  
lcd_draw_text | 绘制字符。  
lcd_draw_vline | 绘制一条垂直线。  
lcd_end_frame | 完成绘制，同步到显示设备。  
lcd_fill_rect | 绘制实心矩形。  
lcd_get_clip_rect | 获取裁剪区域。  
lcd_get_desired_bitmap_format | 获取期望的位图格式。绘制期望的位图格式可以提高绘制性能。  
lcd_get_dirty_rect | 获取 lcd 对象的脏矩形。  
lcd_get_dirty_rects | 获取 lcd 对象的脏矩形列表。  
lcd_get_height | 获取高度。  
lcd_get_physical_height | 获取真实物理高度。  
lcd_get_physical_width | 获取真实物理宽度。  
lcd_get_point_color | 获取指定点的颜色，对于基于非FrameBuffer的LCD，返回当前的fill_color。  
lcd_get_text_metrics | 获取当前字体的度量信息。  
lcd_get_type | 获取 lcd 类型。  
lcd_get_vgcanvas | 获取矢量图canvas。  
lcd_get_width | 获取宽度。  
lcd_is_support_dirty_rect | 获取 lcd 对象是否支持脏矩形。  
lcd_is_swappable | 判读lcd是否支持swap。  
lcd_measure_text | 测量字符串占用的宽度。  
lcd_resize | 基于SDL的PC软件，在SDL窗口resize时，需要调用本函数resize lcd。  
lcd_set_clip_rect | 设置裁剪区域。  
lcd_set_fill_color | 设置填充颜色。  
lcd_set_font_name | 设置字体名称。  
lcd_set_font_size | 设置字体大小。  
lcd_set_global_alpha | 设置全局alpha。  
lcd_set_line_length | 设置 line_length 。  
lcd_set_stroke_color | 设置线条颜色。  
lcd_set_text_color | 设置文本颜色。  
lcd_set_vgcanvas | 设置 vgcanvas。  
lcd_stroke_rect | 绘制矩形边框。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
draw_mode | lcd_draw_mode_t | 绘制模式。  
fill_color | color_t | 填充颜色  
font_name | char* | 字体名称。  
font_size | uint32_t | 字体大小。  
global_alpha | uint8_t | 全局alpha  
h | wh_t | 屏幕的高度  
last_update_time | uint64_t | last update time  
ratio | float_t | 屏幕密度。  
stroke_color | color_t | 线条颜色  
support_dirty_rect | bool_t | 是否支持脏矩形。  
text_color | color_t | 文本颜色  
type | lcd_type_t | LCD的类型。  
w | wh_t | 屏幕的宽度  
  
#### lcd_begin_frame 函数

* * *

  * 函数功能：



> 准备绘制。

  * 函数原型：


    
    
    ret_t lcd_begin_frame (lcd_t* lcd, const dirty_rects_t* dirty_rects, lcd_draw_mode_t draw_mode);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
dirty_rects | const dirty_rects_t* | 需要绘制的区域。  
draw_mode | lcd_draw_mode_t | 绘制模式，如果可能，直接画到显存而不是离线的framebuffer。  
  
#### lcd_clear_rect 函数

* * *

  * 函数功能：



> 填充实心矩形。

  * 函数原型：


    
    
    ret_t lcd_clear_rect (lcd_t* lcd, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### lcd_destroy 函数

* * *

  * 函数功能：



> 销毁lcd对象。

  * 函数原型：


    
    
    ret_t lcd_destroy (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_draw_glyph 函数

* * *

  * 函数功能：



> 绘制字符。如果实现了measure_text/draw_text则不需要实现本函数。

  * 函数原型：


    
    
    ret_t lcd_draw_glyph (lcd_t* lcd, glyph_t* glyph, const rect_t* src, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
glyph | glyph_t* | 字模  
src | const rect_t* | 只绘制指定区域的部分。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### lcd_draw_hline 函数

* * *

  * 函数功能：



> 绘制一条水平线。

  * 函数原型：


    
    
    ret_t lcd_draw_hline (lcd_t* lcd, xy_t x, xy_t y, wh_t w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 直线宽度。  
  
#### lcd_draw_image 函数

* * *

  * 函数功能：



> 绘制图片。

  * 函数原型：


    
    
    ret_t lcd_draw_image (lcd_t* lcd, bitmap_t* img, const rectf_t* src, const rectf_t* dst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
img | bitmap_t* | 图片。  
src | const rectf_t* | 只绘制指定区域的部分。  
dst | const rectf_t* | 绘制到目标区域。  
  
#### lcd_draw_image_matrix 函数

* * *

  * 函数功能：



> 绘制图片。

  * 函数原型：


    
    
    ret_t lcd_draw_image_matrix (lcd_t* lcd, draw_image_info_t* info);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
info | draw_image_info_t* | 绘制参数。  
  
#### lcd_draw_points 函数

* * *

  * 函数功能：



> 绘制一组点。

  * 函数原型：


    
    
    ret_t lcd_draw_points (lcd_t* lcd, point_t* points, uint32_t nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
points | point_t* | 要绘制的点集合。  
nr | uint32_t | 点的个数。  
  
#### lcd_draw_text 函数

* * *

  * 函数功能：



> 绘制字符。

  * 函数原型：


    
    
    ret_t lcd_draw_text (lcd_t* lcd, const wchar_t* str, uint32_t nr, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
str | const wchar_t* | 字符串。  
nr | uint32_t | 字符数。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### lcd_draw_vline 函数

* * *

  * 函数功能：



> 绘制一条垂直线。

  * 函数原型：


    
    
    ret_t lcd_draw_vline (lcd_t* lcd, xy_t x, xy_t y, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
h | wh_t | 直线高度。  
  
#### lcd_end_frame 函数

* * *

  * 函数功能：



> 完成绘制，同步到显示设备。

  * 函数原型：


    
    
    ret_t lcd_end_frame (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_fill_rect 函数

* * *

  * 函数功能：



> 绘制实心矩形。

  * 函数原型：


    
    
    ret_t lcd_fill_rect (lcd_t* lcd, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### lcd_get_clip_rect 函数

* * *

  * 函数功能：



> 获取裁剪区域。

  * 函数原型：


    
    
    ret_t lcd_get_clip_rect (lcd_t* lcd, rect_t* rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
rect | rect_t* | 裁剪区域。  
  
#### lcd_get_desired_bitmap_format 函数

* * *

  * 函数功能：



> 获取期望的位图格式。绘制期望的位图格式可以提高绘制性能。

  * 函数原型：


    
    
    bitmap_format_t lcd_get_desired_bitmap_format (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_format_t | 返回期望的位图格式。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_get_dirty_rect 函数

* * *

  * 函数功能：



> 获取 lcd 对象的脏矩形。

  * 函数原型：


    
    
    ret_t lcd_get_dirty_rect (lcd_t* lcd, rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
r | rect_t* | 返回脏矩形。  
  
#### lcd_get_dirty_rects 函数

* * *

  * 函数功能：



> 获取 lcd 对象的脏矩形列表。

  * 函数原型：


    
    
    const dirty_rects_t* lcd_get_dirty_rects (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const dirty_rects_t* | 成功返回脏矩形列表，失败返回 NULL。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_get_height 函数

* * *

  * 函数功能：



> 获取高度。

  * 函数原型：


    
    
    wh_t lcd_get_height (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回高度。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_get_physical_height 函数

* * *

  * 函数功能：



> 获取真实物理高度。

  * 函数原型：


    
    
    wh_t lcd_get_physical_height (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回真实物理高度。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_get_physical_width 函数

* * *

  * 函数功能：



> 获取真实物理宽度。

  * 函数原型：


    
    
    wh_t lcd_get_physical_width (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回真实物理宽度。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_get_point_color 函数

* * *

  * 函数功能：



> 获取指定点的颜色，对于基于非FrameBuffer的LCD，返回当前的fill_color。

  * 函数原型：


    
    
    color_t lcd_get_point_color (lcd_t* lcd, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | color_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### lcd_get_text_metrics 函数

* * *

  * 函数功能：



> 获取当前字体的度量信息。

  * 函数原型：


    
    
    ret_t lcd_get_text_metrics (lcd_t* lcd, float_t* ascent, float_t* descent, float_t* line_hight);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
ascent | float_t* | 用于返回ascent。  
descent | float_t* | 用于返回descent。  
line_hight | float_t* | 用于返回line height。  
  
#### lcd_get_type 函数

* * *

  * 函数功能：



> 获取 lcd 类型。

  * 函数原型：


    
    
    lcd_type_t lcd_get_type (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | lcd_type_t | 返回 lcd_type。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_get_vgcanvas 函数

* * *

  * 函数功能：



> 获取矢量图canvas。

  * 函数原型：


    
    
    vgcanvas_t* lcd_get_vgcanvas (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | vgcanvas_t* | 返回矢量图canvas。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_get_width 函数

* * *

  * 函数功能：



> 获取宽度。

  * 函数原型：


    
    
    wh_t lcd_get_width (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回宽度。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_is_support_dirty_rect 函数

* * *

  * 函数功能：



> 获取 lcd 对象是否支持脏矩形。

  * 函数原型：


    
    
    bool_t lcd_is_support_dirty_rect (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示支持，否则表示不支持。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_is_swappable 函数

* * *

  * 函数功能：



> 判读lcd是否支持swap。

  * 函数原型：


    
    
    bool_t lcd_is_swappable (lcd_t* lcd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回是否支持swap。  
lcd | lcd_t* | lcd对象。  
  
#### lcd_measure_text 函数

* * *

  * 函数功能：



> 测量字符串占用的宽度。

  * 函数原型：


    
    
    float_t lcd_measure_text (lcd_t* lcd, const wchar_t* str, uint32_t nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回字符串占用的宽度。  
lcd | lcd_t* | lcd对象。  
str | const wchar_t* | 字符串。  
nr | uint32_t | 字符数。  
  
#### lcd_resize 函数

* * *

  * 函数功能：



> 基于SDL的PC软件，在SDL窗口resize时，需要调用本函数resize lcd。 屏幕旋转时会调用本函数，调整LCD的大小。

  * 函数原型：


    
    
    ret_t lcd_resize (lcd_t* lcd, wh_t w, wh_t h, uint32_t line_length);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
w | wh_t | 新的宽度。  
h | wh_t | 新的高度。  
line_length | uint32_t | line_length。  
  
#### lcd_set_clip_rect 函数

* * *

  * 函数功能：



> 设置裁剪区域。

  * 函数原型：


    
    
    ret_t lcd_set_clip_rect (lcd_t* lcd, const rect_t* rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
rect | const rect_t* | 裁剪区域。  
  
#### lcd_set_fill_color 函数

* * *

  * 函数功能：



> 设置填充颜色。

  * 函数原型：


    
    
    ret_t lcd_set_fill_color (lcd_t* lcd, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
color | color_t | 颜色。  
  
#### lcd_set_font_name 函数

* * *

  * 函数功能：



> 设置字体名称。

  * 函数原型：


    
    
    ret_t lcd_set_font_name (lcd_t* lcd, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
name | const char* | 字体名称。  
  
#### lcd_set_font_size 函数

* * *

  * 函数功能：



> 设置字体大小。

  * 函数原型：


    
    
    ret_t lcd_set_font_size (lcd_t* lcd, uint32_t font_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
font_size | uint32_t | 字体大小。  
  
#### lcd_set_global_alpha 函数

* * *

  * 函数功能：



> 设置全局alpha。

  * 函数原型：


    
    
    ret_t lcd_set_global_alpha (lcd_t* lcd, uint8_t alpha);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
alpha | uint8_t | 全局alpha。  
  
#### lcd_set_line_length 函数

* * *

  * 函数功能：



> 设置 line_length 。

  * 函数原型：


    
    
    ret_t lcd_set_line_length (lcd_t* lcd, uint32_t line_length);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
line_length | uint32_t | 一行的字节长度。  
  
#### lcd_set_stroke_color 函数

* * *

  * 函数功能：



> 设置线条颜色。

  * 函数原型：


    
    
    ret_t lcd_set_stroke_color (lcd_t* lcd, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
color | color_t | 颜色。  
  
#### lcd_set_text_color 函数

* * *

  * 函数功能：



> 设置文本颜色。

  * 函数原型：


    
    
    ret_t lcd_set_text_color (lcd_t* lcd, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
color | color_t | 颜色。  
  
#### lcd_set_vgcanvas 函数

* * *

  * 函数功能：



> 设置 vgcanvas。

  * 函数原型：


    
    
    ret_t lcd_set_vgcanvas (lcd_t* lcd, vgcanvas_t* vgcanvas);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
vgcanvas | vgcanvas_t* | vgcanvas对象。  
  
#### lcd_stroke_rect 函数

* * *

  * 函数功能：



> 绘制矩形边框。

  * 函数原型：


    
    
    ret_t lcd_stroke_rect (lcd_t* lcd, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
lcd | lcd_t* | lcd对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### draw_mode 属性

* * *

> 绘制模式。

  * 类型：lcd_draw_mode_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### fill_color 属性

* * *

> 填充颜色

  * 类型：color_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### font_name 属性

* * *

> 字体名称。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### font_size 属性

* * *

> 字体大小。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### global_alpha 属性

* * *

> 全局alpha

  * 类型：uint8_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### h 属性

* * *

> 屏幕的高度

  * 类型：wh_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### last_update_time 属性

* * *

> last update time

  * 类型：uint64_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### ratio 属性

* * *

> 屏幕密度。

  * 类型：float_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### stroke_color 属性

* * *

> 线条颜色

  * 类型：color_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### support_dirty_rect 属性

* * *

> 是否支持脏矩形。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### text_color 属性

* * *

> 文本颜色

  * 类型：color_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### type 属性

* * *

> LCD的类型。

  * 类型：lcd_type_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### w 属性

* * *

> 屏幕的宽度

  * 类型：wh_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
