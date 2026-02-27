## dialog_highlighter_t

### 概述

对话框高亮策略。

## > 高亮策略的基本思路是对背景进行处理，比如将背景变暗或变模糊。

### 函数

函数名称 | 说明  
---|---  
dialog_highlighter_create | 创建对话框高亮策略对象。  
dialog_highlighter_destroy | 销毁对话框高亮策略对象。  
dialog_highlighter_draw | 绘制背景。  
dialog_highlighter_draw_mask | 绘制背景高亮部分。  
dialog_highlighter_get_alpha | 获取高亮的透明度。  
dialog_highlighter_is_dynamic | 是否是动态绘制(方便外层优化)。  
dialog_highlighter_prepare | 初始化。在绘制完背景，在截图前调用。  
dialog_highlighter_prepare_ex | 初始化。在绘制完背景，在截图前调用。  
dialog_highlighter_set_bg | 设置背景图片。  
dialog_highlighter_set_bg_clip_rect | 设置背景图片的显示裁剪区。  
dialog_highlighter_set_system_bar_alpha | 设置 sytem_bar 的高亮透明值。  
dialog_highlighter_set_win | 设置底层窗口。  
dialog_highlighter_system_bar_bottom_append_clip_rect | 增加底部 system_bar 的显示裁剪区  
dialog_highlighter_system_bar_top_append_clip_rect | 增加顶部 system_bar 的显示裁剪区  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
canvas | canvas_t* | 画布。  
clip_rect | rect_t | 截图的显示裁减区  
dialog | widget_t* | 对应的对话框。  
img | bitmap_t | 底层窗口的截图。  
used_by_others | bool_t | 是否给了别的窗口使用。  
win | widget_t* | 底层窗口。  
  
#### dialog_highlighter_create 函数

* * *

  * 函数功能：



> 创建对话框高亮策略对象。
> 
> 供子类构造函数用。

  * 函数原型：


    
    
    dialog_highlighter_t* dialog_highlighter_create (const dialog_highlighter_vtable_t* vt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | dialog_highlighter_t* | 返回对话框高亮策略对象  
vt | const dialog_highlighter_vtable_t* | 虚表对象。  
  
#### dialog_highlighter_destroy 函数

* * *

  * 函数功能：



> 销毁对话框高亮策略对象。

  * 函数原型：


    
    
    ret_t dialog_highlighter_destroy (dialog_highlighter_t* h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
  
#### dialog_highlighter_draw 函数

* * *

  * 函数功能：



> 绘制背景。

  * 函数原型：


    
    
    ret_t dialog_highlighter_draw (dialog_highlighter_t* h, float_t percent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
percent | float_t | 动画进度(0-1)，1表示打开已经完成。  
  
#### dialog_highlighter_draw_mask 函数

* * *

  * 函数功能：



> 绘制背景高亮部分。

  * 函数原型：


    
    
    ret_t dialog_highlighter_draw_mask (dialog_highlighter_t* h, canvas_t* c, float_t percent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
c | canvas_t* | 画布。  
percent | float_t | 高亮的百分比。  
  
#### dialog_highlighter_get_alpha 函数

* * *

  * 函数功能：



> 获取高亮的透明度。

  * 函数原型：


    
    
    uint8_t dialog_highlighter_get_alpha (dialog_highlighter_t* h, float_t percent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t | 返回透明度。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
percent | float_t | 高亮的百分比。  
  
#### dialog_highlighter_is_dynamic 函数

* * *

  * 函数功能：



> 是否是动态绘制(方便外层优化)。

  * 函数原型：


    
    
    bool_t dialog_highlighter_is_dynamic (dialog_highlighter_t* h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示动态绘制，否则表示不是动态绘制。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
  
#### dialog_highlighter_prepare 函数

* * *

  * 函数功能：



> 初始化。在绘制完背景，在截图前调用。

  * 函数原型：


    
    
    ret_t dialog_highlighter_prepare (dialog_highlighter_t* h, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
c | canvas_t* | 画布。  
  
#### dialog_highlighter_prepare_ex 函数

* * *

  * 函数功能：



> 初始化。在绘制完背景，在截图前调用。

  * 函数原型：


    
    
    ret_t dialog_highlighter_prepare_ex (dialog_highlighter_t* h, canvas_t* c, canvas_t* canvas_offline);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
c | canvas_t* | 画布。  
canvas_offline | canvas_t* | 离线画布。  
  
#### dialog_highlighter_set_bg 函数

* * *

  * 函数功能：



> 设置背景图片。

  * 函数原型：


    
    
    ret_t dialog_highlighter_set_bg (dialog_highlighter_t* h, bitmap_t* img);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
img | bitmap_t* | 背景截图。  
  
#### dialog_highlighter_set_bg_clip_rect 函数

* * *

  * 函数功能：



> 设置背景图片的显示裁剪区。

  * 函数原型：


    
    
    ret_t dialog_highlighter_set_bg_clip_rect (dialog_highlighter_t* h, rect_t* clip_rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
clip_rect | rect_t* | 背景显示裁剪区。  
  
#### dialog_highlighter_set_system_bar_alpha 函数

* * *

  * 函数功能：



> 设置 sytem_bar 的高亮透明值。

  * 函数原型：


    
    
    ret_t dialog_highlighter_set_system_bar_alpha (dialog_highlighter_t* h, uint8_t alpha);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
alpha | uint8_t | 设置 sytem_bar 的高亮透明值。  
  
#### dialog_highlighter_set_win 函数

* * *

  * 函数功能：



> 设置底层窗口。

  * 函数原型：


    
    
    ret_t dialog_highlighter_set_win (dialog_highlighter_t* h, widget_t* win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
win | widget_t* | 底层窗口。  
  
#### dialog_highlighter_system_bar_bottom_append_clip_rect 函数

* * *

  * 函数功能：



> 增加底部 system_bar 的显示裁剪区

  * 函数原型：


    
    
    ret_t dialog_highlighter_system_bar_bottom_append_clip_rect (dialog_highlighter_t* h, rect_t* rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
rect | rect_t* | 裁剪区域  
  
#### dialog_highlighter_system_bar_top_append_clip_rect 函数

* * *

  * 函数功能：



> 增加顶部 system_bar 的显示裁剪区

  * 函数原型：


    
    
    ret_t dialog_highlighter_system_bar_top_append_clip_rect (dialog_highlighter_t* h, rect_t* rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
h | dialog_highlighter_t* | 对话框高亮策略对象。  
rect | rect_t* | 裁剪区域  
  
#### canvas 属性

* * *

> 画布。

  * 类型：canvas_t*



#### clip_rect 属性

* * *

> 截图的显示裁减区

  * 类型：rect_t



#### dialog 属性

* * *

> 对应的对话框。

  * 类型：widget_t*



#### img 属性

* * *

> 底层窗口的截图。

  * 类型：bitmap_t



#### used_by_others 属性

* * *

> 是否给了别的窗口使用。

  * 类型：bool_t



#### win 属性

* * *

> 底层窗口。

  * 类型：widget_t*


