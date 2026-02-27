## dialog_highlighter_default_t

### 概述

缺省对话框高亮策略。

> 本策略在背景上画一层半透明的蒙版来高亮(突出)对话框本身。 对于性能不高的平台，建议将start_alpha和end_alpha设为相同。

* * *

### 函数

函数名称 | 说明  
---|---  
dialog_highlighter_default_create | 创建缺省的对话框高亮策略。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
end_alpha | uint8_t | 结束alpha，打开对话框的动画结束(直到对话框被关闭)时的alpha值。  
start_alpha | uint8_t | 起始alpha，打开对话框的动画开始时的alpha值。  
system_bar_alpha | uint8_t | 由于在没有过度动画的情况下，截图中已经包括黑色色块，为了让 system_bar 也同步高亮部分的色块透明。  
system_bar_bottom_clip_rects | darray_t | 截图的底部 system_bar 显示裁减区列表  
system_bar_top_clip_rects | darray_t | 截图的顶部 system_bar 显示裁减区列表  
update_background | bool_t | 是否刷新底层窗口的截图。  
win_mask_rect_list | slist_t | 窗口 mask 区域  
  
#### dialog_highlighter_default_create 函数

* * *

  * 函数功能：



> 创建缺省的对话框高亮策略。

  * 函数原型：


    
    
    dialog_highlighter_t* dialog_highlighter_default_create (tk_object_t* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | dialog_highlighter_t* | 返回对话框高亮策略对象。  
args | tk_object_t* | 参数。  
  
#### end_alpha 属性

* * *

> 结束alpha，打开对话框的动画结束(直到对话框被关闭)时的alpha值。

  * 类型：uint8_t



#### start_alpha 属性

* * *

> 起始alpha，打开对话框的动画开始时的alpha值。

  * 类型：uint8_t



#### system_bar_alpha 属性

* * *

> 由于在没有过度动画的情况下，截图中已经包括黑色色块，为了让 system_bar 也同步高亮部分的色块透明。

  * 类型：uint8_t



#### system_bar_bottom_clip_rects 属性

* * *

> 截图的底部 system_bar 显示裁减区列表

  * 类型：darray_t



#### system_bar_top_clip_rects 属性

* * *

> 截图的顶部 system_bar 显示裁减区列表

  * 类型：darray_t



#### update_background 属性

* * *

> 是否刷新底层窗口的截图。

  * 类型：bool_t



#### win_mask_rect_list 属性

* * *

> 窗口 mask 区域

  * 类型：slist_t


