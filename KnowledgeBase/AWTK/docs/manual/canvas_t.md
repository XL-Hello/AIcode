## canvas_t

### 概述

## 提供基本的绘图功能和状态管理。

### 函数

函数名称 | 说明  
---|---  
canvas_begin_frame | 绘制开始。  
canvas_cast | 转换为canvas对象(供脚本语言使用)。  
canvas_clear_rect | 用填充颜色填充指定矩形。  
canvas_draw_hline | 画水平线。  
canvas_draw_icon | 绘制图标。  
canvas_draw_icon_in_rect | 在指定rect内绘制icon。  
canvas_draw_image | 绘制图片。  
canvas_draw_image_at | 在指定位置画图。  
canvas_draw_image_ex | 绘制图片。  
canvas_draw_image_ex2 | 绘制图片。  
canvas_draw_line | 画直线。  
canvas_draw_points | 画多个点。  
canvas_draw_text | 绘制文本。  
canvas_draw_text_bidi_in_rect | 绘制文本(支持Unicode Bidirectional Algorithm)。  
canvas_draw_text_in_rect | 绘制文本。  
canvas_draw_utf8 | 绘制文本。  
canvas_draw_utf8_in_rect | 绘制文本。  
canvas_draw_vline | 画垂直线。  
canvas_end_frame | 绘制结束。  
canvas_fill_rect | 绘制矩形。  
canvas_fill_rect_gradient | 绘制矩形。  
canvas_fill_rounded_rect | 填充区域。  
canvas_fill_rounded_rect_ex | 填充圆角矩形区域。  
canvas_fill_rounded_rect_gradient | 填充圆角矩形区域。  
canvas_fill_rounded_rect_gradient_ex | 填充圆角矩形区域。  
canvas_get_clip_rect | 获取裁剪区。  
canvas_get_font_height | 获取字体的高度。  
canvas_get_height | 获取画布的高度。  
canvas_get_text_metrics | 获取当前字体的度量信息。  
canvas_get_vgcanvas | 获取vgcanvas对象。  
canvas_get_width | 获取画布的宽度。  
canvas_init | 初始化，系统内部调用。  
canvas_is_rect_in_clip_rect | 判断改矩形区域是否在裁剪区中  
canvas_measure_text | 计算文本所占的宽度。  
canvas_measure_utf8 | 计算文本所占的宽度。  
canvas_reset | 释放相关资源。  
canvas_reset_cache | 清除canvas中缓存。  
canvas_reset_font | 释放canvas中字体相关的资源。  
canvas_set_assets_manager | 设置canvas的assets_manager对象。  
canvas_set_clip_rect | 设置裁剪区。  
canvas_set_clip_rect_ex | 设置裁剪区。  
canvas_set_fill_color | 设置填充颜色。  
canvas_set_fill_color_str | 设置填充颜色。  
canvas_set_font | 设置字体。  
canvas_set_font_manager | 设置canvas的font_manager对象。  
canvas_set_fps | 设置FPS。  
canvas_set_global_alpha | 设置全局alpha值。  
canvas_set_stroke_color | 设置线条颜色。  
canvas_set_stroke_color_str | 设置线条颜色。  
canvas_set_text_align | 设置文本对齐方式。  
canvas_set_text_color | 设置文本颜色。  
canvas_set_text_color_str | 设置文本颜色。  
canvas_stroke_rect | 绘制矩形。  
canvas_stroke_rounded_rect | 绘制边框。  
canvas_stroke_rounded_rect_ex | 绘制边框。  
canvas_translate | 平移原点坐标。  
canvas_untranslate | 反向平移原点坐标。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
assets_manager | assets_manager_t* | 资源管理器对象。  
clip_bottom | xy_t | 当前裁剪矩形的底部位置。  
clip_left | xy_t | 当前裁剪矩形的左边位置。  
clip_right | xy_t | 当前裁剪矩形的右边位置。  
clip_top | xy_t | 当前裁剪矩形的顶部位置。  
font | font_t* | 字体对象。  
font_manager | font_manager_t* | 字体管理器对象。  
font_name | char* | 当前字体名称。  
font_size | font_size_t | 当前字体大小。  
fps | uint32_t | 当前的帧率。  
fps_position | point_t | 当前的帧率绘制坐标。  
global_alpha | uint8_t | 当前全局alpha。  
lcd | lcd_t* | lcd对象。  
ox | xy_t | x坐标偏移。  
oy | xy_t | y坐标偏移。  
show_fps | bool_t | 是否显示帧率。  
text_align_h | align_h_t | 文本水平对齐方式。  
text_align_v | align_v_t | 文本垂直对齐方式。  
  
#### canvas_begin_frame 函数

* * *

  * 函数功能：



> 绘制开始。

  * 函数原型：


    
    
    ret_t canvas_begin_frame (canvas_t* c, const dirty_rects_t* dirty_rects, lcd_draw_mode_t draw_mode);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
dirty_rects | const dirty_rects_t* | 脏矩形。  
draw_mode | lcd_draw_mode_t | 绘制模式。  
  
#### canvas_cast 函数

* * *

  * 函数功能：



> 转换为canvas对象(供脚本语言使用)。

  * 函数原型：


    
    
    canvas_t* canvas_cast (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | canvas对象。  
c | canvas_t* | canvas对象。  
  
#### canvas_clear_rect 函数

* * *

  * 函数功能：



> 用填充颜色填充指定矩形。
> 
> 如果lcd的颜色格式带alpha通道，连同alpha的值一起修改。

  * 函数原型：


    
    
    ret_t canvas_clear_rect (canvas_t* c, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### canvas_draw_hline 函数

* * *

  * 函数功能：



> 画水平线。

  * 函数原型：


    
    
    ret_t canvas_draw_hline (canvas_t* c, xy_t x, xy_t y, wh_t w);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
  
#### canvas_draw_icon 函数

* * *

  * 函数功能：



> 绘制图标。

  * 函数原型：


    
    
    ret_t canvas_draw_icon (canvas_t* c, bitmap_t* img, xy_t cx, xy_t cy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
img | bitmap_t* | 图片对象。  
cx | xy_t | 中心点x坐标。  
cy | xy_t | 中心点y坐标。  
  
#### canvas_draw_icon_in_rect 函数

* * *

  * 函数功能：



> 在指定rect内绘制icon。

  * 函数原型：


    
    
    ret_t canvas_draw_icon_in_rect (canvas_t* c, bitmap_t* img, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
img | bitmap_t* | 图片对象。  
r | const rect_t* | 矩形区域。  
  
#### canvas_draw_image 函数

* * *

  * 函数功能：



> 绘制图片。

  * 函数原型：


    
    
    ret_t canvas_draw_image (canvas_t* c, bitmap_t* img, const rect_t* src, const rect_t* dst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
img | bitmap_t* | 图片对象。  
src | const rect_t* | 源区域。  
dst | const rect_t* | 目的区域。  
  
#### canvas_draw_image_at 函数

* * *

  * 函数功能：



> 在指定位置画图。

  * 函数原型：


    
    
    ret_t canvas_draw_image_at (canvas_t* c, bitmap_t* img, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
img | bitmap_t* | 图片对象。  
x | xy_t | x坐标。  
y | xy_t | w坐标。  
  
#### canvas_draw_image_ex 函数

* * *

  * 函数功能：



> 绘制图片。

  * 函数原型：


    
    
    ret_t canvas_draw_image_ex (canvas_t* c, bitmap_t* img, image_draw_type_t draw_type, const rect_t* dst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
img | bitmap_t* | 图片对象。  
draw_type | image_draw_type_t | 绘制类型。  
dst | const rect_t* | 目的区域。  
  
#### canvas_draw_image_ex2 函数

* * *

  * 函数功能：



> 绘制图片。

  * 函数原型：


    
    
    ret_t canvas_draw_image_ex2 (canvas_t* c, bitmap_t* img, image_draw_type_t draw_type, const rect_t* src, const rect_t* dst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
img | bitmap_t* | 图片对象。  
draw_type | image_draw_type_t | 绘制类型。  
src | const rect_t* | 源区域。  
dst | const rect_t* | 目的区域。  
  
#### canvas_draw_line 函数

* * *

  * 函数功能：



> 画直线。

  * 函数原型：


    
    
    ret_t canvas_draw_line (canvas_t* c, xy_t x1, xy_t y1, xy_t x2, xy_t y2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
x1 | xy_t | 起始点的x坐标。  
y1 | xy_t | 起始点的y坐标。  
x2 | xy_t | 结束点的x坐标。  
y2 | xy_t | 结束点的y坐标。  
  
#### canvas_draw_points 函数

* * *

  * 函数功能：



> 画多个点。

  * 函数原型：


    
    
    ret_t canvas_draw_points (canvas_t* c, const point_t* points, uint32_t nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
points | const point_t* | 点数组。  
nr | uint32_t | 点的个数。  
  
#### canvas_draw_text 函数

* * *

  * 函数功能：



> 绘制文本。

  * 函数原型：


    
    
    ret_t canvas_draw_text (canvas_t* c, const wchar_t* str, uint32_t nr, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
str | const wchar_t* | 字符串。  
nr | uint32_t | 字符数。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### canvas_draw_text_bidi_in_rect 函数

* * *

  * 函数功能：



> 绘制文本(支持Unicode Bidirectional Algorithm)。

  * 函数原型：


    
    
    ret_t canvas_draw_text_bidi_in_rect (canvas_t* c, const wchar_t* str, uint32_t nr, const rect_t* r, const char* bidi_type, bool_t ellipses);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
str | const wchar_t* | 字符串。  
nr | uint32_t | 字符数。  
r | const rect_t* | 矩形区域。  
bidi_type | const char* | 类型。  
ellipses | bool_t | 如果目标宽度不够，是否显示省略号。  
  
#### canvas_draw_text_in_rect 函数

* * *

  * 函数功能：



> 绘制文本。

  * 函数原型：


    
    
    ret_t canvas_draw_text_in_rect (canvas_t* c, const wchar_t* str, uint32_t nr, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
str | const wchar_t* | 字符串。  
nr | uint32_t | 字符数。  
r | const rect_t* | 矩形区域。  
  
#### canvas_draw_utf8 函数

* * *

  * 函数功能：



> 绘制文本。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    ret_t canvas_draw_utf8 (canvas_t* c, const char* str, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
str | const char* | 字符串。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### canvas_draw_utf8_in_rect 函数

* * *

  * 函数功能：



> 绘制文本。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    ret_t canvas_draw_utf8_in_rect (canvas_t* c, const char* str, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
str | const char* | 字符串。  
r | const rect_t* | 矩形区域。  
  
#### canvas_draw_vline 函数

* * *

  * 函数功能：



> 画垂直线。

  * 函数原型：


    
    
    ret_t canvas_draw_vline (canvas_t* c, xy_t x, xy_t y, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
h | wh_t | 高度。  
  
#### canvas_end_frame 函数

* * *

  * 函数功能：



> 绘制结束。

  * 函数原型：


    
    
    ret_t canvas_end_frame (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
  
#### canvas_fill_rect 函数

* * *

  * 函数功能：



> 绘制矩形。

  * 函数原型：


    
    
    ret_t canvas_fill_rect (canvas_t* c, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### canvas_fill_rect_gradient 函数

* * *

  * 函数功能：



> 绘制矩形。

  * 函数原型：


    
    
    ret_t canvas_fill_rect_gradient (canvas_t* c, xy_t x, xy_t y, wh_t w, wh_t h, gradient_t* gradient);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
gradient | gradient_t* | 渐变颜色。  
  
#### canvas_fill_rounded_rect 函数

* * *

  * 函数功能：



> 填充区域。

  * 函数原型：


    
    
    ret_t canvas_fill_rounded_rect (canvas_t* c, const rect_t* r, const rect_t* bg_r, const color_t* color, uint32_t radius);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | 矩形。  
bg_r | const rect_t* | 矩形（默认为 NULL，当圆角直径大于 r 矩形的宽高后，会根据 bg_r 矩形来决定是否需要缩小圆角半径）。  
color | const color_t* | 颜色。  
radius | uint32_t | 圆角半径。  
  
#### canvas_fill_rounded_rect_ex 函数

* * *

  * 函数功能：



> 填充圆角矩形区域。 半径半径小于等于2，则表示该角为直角，如果全部角都为直角则返回RET_FAIL。（如果全是直角，该函数效率没有canvas_fill_rect函数快） 如果各个半径都不一样的话，就是会使用vg，如果不支持vg就会返回RET_FAIL（直角的情况除外）。

  * 函数原型：


    
    
    ret_t canvas_fill_rounded_rect_ex (canvas_t* c, const rect_t* r, const rect_t* bg_r, const color_t* color, uint32_t radius_tl, uint32_t radius_tr, uint32_t radius_bl, uint32_t radius_br);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | 矩形。  
bg_r | const rect_t* | 矩形。（默认为 NULL，当圆角直径大于 r 矩形的宽高后，会根据 bg_r 矩形来决定是否需要缩小圆角半径）  
color | const color_t* | 颜色。  
radius_tl | uint32_t | 左上角圆角半径。  
radius_tr | uint32_t | 右上角圆角半径。  
radius_bl | uint32_t | 左下角圆角半径。  
radius_br | uint32_t | 右下角圆角半径。  
  
#### canvas_fill_rounded_rect_gradient 函数

* * *

  * 函数功能：



> 填充圆角矩形区域。

  * 函数原型：


    
    
    ret_t canvas_fill_rounded_rect_gradient (canvas_t* c, const rect_t* r, const rect_t* bg_r, const gradient_t* gradient, uint32_t radius);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | 矩形。  
bg_r | const rect_t* | 矩形（默认为 NULL，当圆角直径大于 r 矩形的宽高后，会根据 bg_r 矩形来决定是否需要缩小圆角半径）。  
gradient | const gradient_t* | 渐变颜色。  
radius | uint32_t | 圆角半径。  
  
#### canvas_fill_rounded_rect_gradient_ex 函数

* * *

  * 函数功能：



> 填充圆角矩形区域。 半径半径小于等于2，则表示该角为直角，如果全部角都为直角则返回RET_FAIL。（如果全是直角，该函数效率没有canvas_fill_rect函数快） 如果各个半径都不一样的话，就是会使用vg，如果不支持vg就会返回RET_FAIL（直角的情况除外）。

  * 函数原型：


    
    
    ret_t canvas_fill_rounded_rect_gradient_ex (canvas_t* c, const rect_t* r, const rect_t* bg_r, const gradient_t* gradient, uint32_t radius_tl, uint32_t radius_tr, uint32_t radius_bl, uint32_t radius_br);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | 矩形。  
bg_r | const rect_t* | 矩形。（默认为 NULL，当圆角直径大于 r 矩形的宽高后，会根据 bg_r 矩形来决定是否需要缩小圆角半径）  
gradient | const gradient_t* | 渐变颜色。  
radius_tl | uint32_t | 左上角圆角半径。  
radius_tr | uint32_t | 右上角圆角半径。  
radius_bl | uint32_t | 左下角圆角半径。  
radius_br | uint32_t | 右下角圆角半径。  
  
#### canvas_get_clip_rect 函数

* * *

  * 函数功能：



> 获取裁剪区。

  * 函数原型：


    
    
    ret_t canvas_get_clip_rect (canvas_t* c, rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | rect_t* | rect对象。  
  
#### canvas_get_font_height 函数

* * *

  * 函数功能：



> 获取字体的高度。

  * 函数原型：


    
    
    float_t canvas_get_font_height (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回字体的高度。  
c | canvas_t* | canvas对象。  
  
#### canvas_get_height 函数

* * *

  * 函数功能：



> 获取画布的高度。

  * 函数原型：


    
    
    wh_t canvas_get_height (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回画布的高度。  
c | canvas_t* | canvas对象。  
  
#### canvas_get_text_metrics 函数

* * *

  * 函数功能：



> 获取当前字体的度量信息。

  * 函数原型：


    
    
    ret_t canvas_get_text_metrics (canvas_t* canvas, float_t* ascent, float_t* descent, float_t* line_hight);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
canvas | canvas_t* | canvas对象。  
ascent | float_t* | 用于返回ascent。  
descent | float_t* | 用于返回descent。  
line_hight | float_t* | 用于返回line height。  
  
#### canvas_get_vgcanvas 函数

* * *

  * 函数功能：



> 获取vgcanvas对象。

  * 函数原型：


    
    
    vgcanvas_t* canvas_get_vgcanvas (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | vgcanvas_t* | 返回vgcanvas对象。  
c | canvas_t* | canvas对象。  
  
#### canvas_get_width 函数

* * *

  * 函数功能：



> 获取画布的宽度。

  * 函数原型：


    
    
    wh_t canvas_get_width (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wh_t | 返回画布的宽度。  
c | canvas_t* | canvas对象。  
  
#### canvas_init 函数

* * *

  * 函数功能：



> 初始化，系统内部调用。

  * 函数原型：


    
    
    canvas_t* canvas_init (canvas_t* c, lcd_t* lcd, font_manager_t* font_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | 返回canvas对象本身。  
c | canvas_t* | canvas对象。  
lcd | lcd_t* | lcd对象。  
font_manager | font_manager_t* | 字体管理器对象。  
  
#### canvas_is_rect_in_clip_rect 函数

* * *

  * 函数功能：



> 判断改矩形区域是否在裁剪区中

  * 函数原型：


    
    
    bool_t canvas_is_rect_in_clip_rect (canvas_t* c, xy_t left, xy_t top, xy_t right, xy_t bottom);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示不是。  
c | canvas_t* | canvas对象。  
left | xy_t | 矩形区域左边。  
top | xy_t | 矩形区域上边。  
right | xy_t | 矩形区域右边。  
bottom | xy_t | 矩形区域下边。  
  
#### canvas_measure_text 函数

* * *

  * 函数功能：



> 计算文本所占的宽度。

  * 函数原型：


    
    
    float_t canvas_measure_text (canvas_t* c, const wchar_t* str, uint32_t nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回文本所占的宽度。  
c | canvas_t* | canvas对象。  
str | const wchar_t* | 字符串。  
nr | uint32_t | 字符数。  
  
#### canvas_measure_utf8 函数

* * *

  * 函数功能：



> 计算文本所占的宽度。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    float_t canvas_measure_utf8 (canvas_t* c, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回文本所占的宽度。  
c | canvas_t* | canvas对象。  
str | const char* | 字符串。  
  
#### canvas_reset 函数

* * *

  * 函数功能：



> 释放相关资源。

  * 函数原型：


    
    
    ret_t canvas_reset (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
  
#### canvas_reset_cache 函数

* * *

  * 函数功能：



> 清除canvas中缓存。 备注：主要用于窗口动画的离线画布绘制完成后重置在线画布，使下一帧中lcd对象的数据保持一致。

  * 函数原型：


    
    
    ret_t canvas_reset_cache (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
  
#### canvas_reset_font 函数

* * *

  * 函数功能：



> 释放canvas中字体相关的资源。

  * 函数原型：


    
    
    ret_t canvas_reset_font (canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
  
#### canvas_set_assets_manager 函数

* * *

  * 函数功能：



> 设置canvas的assets_manager对象。

  * 函数原型：


    
    
    ret_t canvas_set_assets_manager (canvas_t* c, assets_manager_t* assets_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
assets_manager | assets_manager_t* | assets_manager对象。  
  
#### canvas_set_clip_rect 函数

* * *

  * 函数功能：



> 设置裁剪区。

  * 函数原型：


    
    
    ret_t canvas_set_clip_rect (canvas_t* c, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | rect对象。  
  
#### canvas_set_clip_rect_ex 函数

* * *

  * 函数功能：



> 设置裁剪区。

  * 函数原型：


    
    
    ret_t canvas_set_clip_rect_ex (canvas_t* c, const rect_t* r, bool_t translate);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | rect对象。  
translate | bool_t | 是否将裁剪区的位置加上canvas当前的偏移。  
  
#### canvas_set_fill_color 函数

* * *

  * 函数功能：



> 设置填充颜色。

  * 函数原型：


    
    
    ret_t canvas_set_fill_color (canvas_t* c, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
color | color_t | 颜色。  
  
#### canvas_set_fill_color_str 函数

* * *

  * 函数功能：



> 设置填充颜色。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    ret_t canvas_set_fill_color_str (canvas_t* c, const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
color | const char* | 颜色。  
  
#### canvas_set_font 函数

* * *

  * 函数功能：



> 设置字体。

  * 函数原型：


    
    
    ret_t canvas_set_font (canvas_t* c, const char* name, font_size_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
name | const char* | 字体名称。  
size | font_size_t | 字体大小。  
  
#### canvas_set_font_manager 函数

* * *

  * 函数功能：



> 设置canvas的font_manager对象。

  * 函数原型：


    
    
    ret_t canvas_set_font_manager (canvas_t* c, font_manager_t* font_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
font_manager | font_manager_t* | font_manager对象。  
  
#### canvas_set_fps 函数

* * *

  * 函数功能：



> 设置FPS。

  * 函数原型：


    
    
    ret_t canvas_set_fps (canvas_t* c, bool_t show_fps, uint32_t fps);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
show_fps | bool_t | 是否显示fps。  
fps | uint32_t | FPS。  
  
#### canvas_set_global_alpha 函数

* * *

  * 函数功能：



> 设置全局alpha值。

  * 函数原型：


    
    
    ret_t canvas_set_global_alpha (canvas_t* c, uint8_t alpha);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
alpha | uint8_t | alpha值。  
  
#### canvas_set_stroke_color 函数

* * *

  * 函数功能：



> 设置线条颜色。

  * 函数原型：


    
    
    ret_t canvas_set_stroke_color (canvas_t* c, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
color | color_t | 颜色。  
  
#### canvas_set_stroke_color_str 函数

* * *

  * 函数功能：



> 设置线条颜色。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    ret_t canvas_set_stroke_color_str (canvas_t* c, const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
color | const char* | 颜色。  
  
#### canvas_set_text_align 函数

* * *

  * 函数功能：



> 设置文本对齐方式。

  * 函数原型：


    
    
    ret_t canvas_set_text_align (canvas_t* c, align_h_t align_h, align_v_t align_v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
align_h | align_h_t | 水平对齐方式。  
align_v | align_v_t | 垂直对齐方式。  
  
#### canvas_set_text_color 函数

* * *

  * 函数功能：



> 设置文本颜色。

  * 函数原型：


    
    
    ret_t canvas_set_text_color (canvas_t* c, color_t color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
color | color_t | 颜色。  
  
#### canvas_set_text_color_str 函数

* * *

  * 函数功能：



> 设置文本颜色。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    ret_t canvas_set_text_color_str (canvas_t* c, const char* color);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
color | const char* | 颜色。  
  
#### canvas_stroke_rect 函数

* * *

  * 函数功能：



> 绘制矩形。

  * 函数原型：


    
    
    ret_t canvas_stroke_rect (canvas_t* c, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### canvas_stroke_rounded_rect 函数

* * *

  * 函数功能：



> 绘制边框。

  * 函数原型：


    
    
    ret_t canvas_stroke_rounded_rect (canvas_t* c, const rect_t* r, const rect_t* bg_r, const color_t* color, uint32_t radius, uint32_t border_width);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | 矩形。  
bg_r | const rect_t* | 矩形（默认为 NULL，当圆角直径大于 r 矩形的宽高后，会根据 bg_r 矩形来决定是否需要缩小圆角半径）。  
color | const color_t* | 颜色。  
radius | uint32_t | 圆角半径。  
border_width | uint32_t | 边宽。  
  
#### canvas_stroke_rounded_rect_ex 函数

* * *

  * 函数功能：



> 绘制边框。 半径半径小于等于2，则表示该角为直角，如果全部角都为直角则返回RET_FAIL。（如果全是直角，该函数效率没有canvas_stroke_rect函数快） 如果各个半径都不一样的话，就是会使用vg，如果不支持vg就会返回RET_FAIL（直角的情况除外）。

  * 函数原型：


    
    
    ret_t canvas_stroke_rounded_rect_ex (canvas_t* c, const rect_t* r, const rect_t* bg_r, const color_t* color, uint32_t radius_tl, uint32_t radius_tr, uint32_t radius_bl, uint32_t radius_br, uint32_t border_width, int32_t border_model);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
r | const rect_t* | 矩形。  
bg_r | const rect_t* | 矩形（默认为 NULL，当圆角直径大于 r 矩形的宽高后，会根据 bg_r 矩形来决定是否需要缩小圆角半径）。  
color | const color_t* | 颜色。  
radius_tl | uint32_t | 左上角圆角半径。  
radius_tr | uint32_t | 右上角圆角半径。  
radius_bl | uint32_t | 左下角圆角半径。  
radius_br | uint32_t | 右下角圆角半径。  
border_width | uint32_t | 边宽。  
border_model | int32_t | 边框类型。  
  
#### canvas_translate 函数

* * *

  * 函数功能：



> 平移原点坐标。

  * 函数原型：


    
    
    ret_t canvas_translate (canvas_t* c, xy_t dx, xy_t dy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
dx | xy_t | x偏移。  
dy | xy_t | y偏移。  
  
#### canvas_untranslate 函数

* * *

  * 函数功能：



> 反向平移原点坐标。

  * 函数原型：


    
    
    ret_t canvas_untranslate (canvas_t* c, xy_t dx, xy_t dy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
c | canvas_t* | canvas对象。  
dx | xy_t | x偏移。  
dy | xy_t | y偏移。  
  
#### assets_manager 属性

* * *

> 资源管理器对象。

  * 类型：assets_manager_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### clip_bottom 属性

* * *

> 当前裁剪矩形的底部位置。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### clip_left 属性

* * *

> 当前裁剪矩形的左边位置。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### clip_right 属性

* * *

> 当前裁剪矩形的右边位置。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### clip_top 属性

* * *

> 当前裁剪矩形的顶部位置。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### font 属性

* * *

> 字体对象。

  * 类型：font_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### font_manager 属性

* * *

> 字体管理器对象。

  * 类型：font_manager_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### font_name 属性

* * *

> 当前字体名称。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### font_size 属性

* * *

> 当前字体大小。

  * 类型：font_size_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### fps 属性

* * *

> 当前的帧率。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### fps_position 属性

* * *

> 当前的帧率绘制坐标。

  * 类型：point_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### global_alpha 属性

* * *

> 当前全局alpha。

  * 类型：uint8_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### lcd 属性

* * *

> lcd对象。

  * 类型：lcd_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### ox 属性

* * *

> x坐标偏移。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### oy 属性

* * *

> y坐标偏移。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### show_fps 属性

* * *

> 是否显示帧率。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### text_align_h 属性

* * *

> 文本水平对齐方式。

  * 类型：align_h_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### text_align_v 属性

* * *

> 文本垂直对齐方式。

  * 类型：align_v_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
