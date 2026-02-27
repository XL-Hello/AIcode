## text_edit_t

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
text_edit_click | 处理点击事件。  
text_edit_copy | 拷贝文本。  
text_edit_create | 创建text_edit对象  
text_edit_cut | 剪切文本。  
text_edit_destroy | 销毁text_edit对象。  
text_edit_drag | 处理拖动事件。  
text_edit_get_cursor | 获取光标位置。  
text_edit_get_height | 获取偏移字符位置高度。  
text_edit_get_lines_of_each_row | 获取每一个逻辑行(row)占几个物理行(line)。  
text_edit_get_selected_text | 获取选中文本。  
text_edit_get_state | 获取编辑器的状态。  
text_edit_insert_text | 插入一段文本。  
text_edit_invert_caret_visible | 如果caret可见，将其设置为不可见。 如果caret不可见，将其设置为可见。  
text_edit_key_down | 处理按键事件。  
text_edit_key_up | 处理按键事件。  
text_edit_layout | 重新排版。  
text_edit_muti_line_insert_text_layout | 插入字符串后的重新排版。（内部使用函数）  
text_edit_paint | 绘制文本。  
text_edit_paste | 粘贴文本。  
text_edit_preedit | 进入预编辑状态。  
text_edit_preedit_abort | 取消预编辑的文本，并退出预编辑状态。  
text_edit_preedit_clear | 清除预编辑文本。  
text_edit_preedit_confirm | 提交预编辑的文本，并退出预编辑状态。  
text_edit_select_all | 全选。  
text_edit_set_canvas | 设置canvas对象。  
text_edit_set_caret_visible | 设置光标的看见性。  
text_edit_set_cursor | 设置光标位置。  
text_edit_set_mask | 设置是否马赛克字符(用于密码)。  
text_edit_set_mask_char | 设置马赛克字符。  
text_edit_set_max_chars | 设置最大字符数（0 为不限制字符）。  
text_edit_set_max_rows | 设置最大行数。  
text_edit_set_offset | 设置滚动偏移。  
text_edit_set_on_char_will_input | 设置字符输入回调函数。  
text_edit_set_on_state_changed | 设置状态改变回调函数。  
text_edit_set_on_text_will_delete | 设置文本删除回调函数。  
text_edit_set_select | 选择指定范围的文本。  
text_edit_set_tips | 设置提示信息。  
text_edit_set_wrap_word | 设置是否自动折行。  
text_edit_show_context_menu | 显示上下文菜单。  
text_edit_unselect | 取消选择。  
  
#### text_edit_click 函数

* * *

  * 函数功能：



> 处理点击事件。

  * 函数原型：


    
    
    ret_t text_edit_click (text_edit_t* text_edit, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### text_edit_copy 函数

* * *

  * 函数功能：



> 拷贝文本。

  * 函数原型：


    
    
    ret_t text_edit_copy (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_create 函数

* * *

  * 函数功能：



> 创建text_edit对象

  * 函数原型：


    
    
    text_edit_t* text_edit_create (widget_t* widget, bool_t single_line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | text_edit_t* | 对象。  
widget | widget_t* | 控件  
single_line | bool_t | 是否是单行编辑器。  
  
#### text_edit_cut 函数

* * *

  * 函数功能：



> 剪切文本。

  * 函数原型：


    
    
    ret_t text_edit_cut (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_destroy 函数

* * *

  * 函数功能：



> 销毁text_edit对象。

  * 函数原型：


    
    
    ret_t text_edit_destroy (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_drag 函数

* * *

  * 函数功能：



> 处理拖动事件。

  * 函数原型：


    
    
    ret_t text_edit_drag (text_edit_t* text_edit, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### text_edit_get_cursor 函数

* * *

  * 函数功能：



> 获取光标位置。

  * 函数原型：


    
    
    uint32_t text_edit_get_cursor (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回光标的位置。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_get_height 函数

* * *

  * 函数功能：



> 获取偏移字符位置高度。

  * 函数原型：


    
    
    uint32_t text_edit_get_height (text_edit_t* text_edit, uint32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回偏移位置字符位置高度。  
text_edit | text_edit_t* | text_edit对象。  
offset | uint32_t | 偏移位置。  
  
#### text_edit_get_lines_of_each_row 函数

* * *

  * 函数功能：



> 获取每一个逻辑行(row)占几个物理行(line)。

  * 函数原型：


    
    
    const uint32_t* text_edit_get_lines_of_each_row (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const uint32_t* | 返回每一个 row 占用多少个 line 数组。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_get_selected_text 函数

* * *

  * 函数功能：



> 获取选中文本。 使用完后需调用 TKMEM_FREE() 进行释放文本占有内存。

  * 函数原型：


    
    
    char* text_edit_get_selected_text (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回选中文本。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_get_state 函数

* * *

  * 函数功能：



> 获取编辑器的状态。

  * 函数原型：


    
    
    ret_t text_edit_get_state (text_edit_t* text_edit, text_edit_state_t* state);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
state | text_edit_state_t* | 状态。  
  
#### text_edit_insert_text 函数

* * *

  * 函数功能：



> 插入一段文本。

  * 函数原型：


    
    
    ret_t text_edit_insert_text (text_edit_t* text_edit, uint32_t offset, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
offset | uint32_t | 插入的偏移位置。  
text | const char* | 待插入的文本。  
  
#### text_edit_invert_caret_visible 函数

* * *

  * 函数功能：



> 如果caret可见，将其设置为不可见。 如果caret不可见，将其设置为可见。

  * 函数原型：


    
    
    ret_t text_edit_invert_caret_visible (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_key_down 函数

* * *

  * 函数功能：



> 处理按键事件。

  * 函数原型：


    
    
    ret_t text_edit_key_down (text_edit_t* text_edit, key_event_t* evt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
evt | key_event_t* | event  
  
#### text_edit_key_up 函数

* * *

  * 函数功能：



> 处理按键事件。

  * 函数原型：


    
    
    ret_t text_edit_key_up (text_edit_t* text_edit, key_event_t* evt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
evt | key_event_t* | event  
  
#### text_edit_layout 函数

* * *

  * 函数功能：



> 重新排版。

  * 函数原型：


    
    
    ret_t text_edit_layout (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_muti_line_insert_text_layout 函数

* * *

  * 函数功能：



> 插入字符串后的重新排版。（内部使用函数）

  * 函数原型：


    
    
    ret_t text_edit_muti_line_insert_text_layout (text_edit_t* text_edit, uint32_t offset, uint32_t insert_length, const wchar_t* wtext, bool_t overwrite, uint32_t rm_num);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
offset | uint32_t | 插入的字符串偏移。  
insert_length | uint32_t | 插入的字符串长度。  
wtext | const wchar_t* | 插入的字符串。  
overwrite | bool_t | 是否为覆写模式。  
rm_num | uint32_t | 移除的字符串长度。  
  
#### text_edit_paint 函数

* * *

  * 函数功能：



> 绘制文本。

  * 函数原型：


    
    
    ret_t text_edit_paint (text_edit_t* text_edit, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
c | canvas_t* | canvas对象。  
  
#### text_edit_paste 函数

* * *

  * 函数功能：



> 粘贴文本。

  * 函数原型：


    
    
    ret_t text_edit_paste (text_edit_t* text_edit, const wchar_t* str, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
str | const wchar_t* | 文本。  
size | uint32_t | 文本长度。  
  
#### text_edit_preedit 函数

* * *

  * 函数功能：



> 进入预编辑状态。

  * 函数原型：


    
    
    ret_t text_edit_preedit (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_preedit_abort 函数

* * *

  * 函数功能：



> 取消预编辑的文本，并退出预编辑状态。

  * 函数原型：


    
    
    ret_t text_edit_preedit_abort (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_preedit_clear 函数

* * *

  * 函数功能：



> 清除预编辑文本。

  * 函数原型：


    
    
    ret_t text_edit_preedit_clear (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_preedit_confirm 函数

* * *

  * 函数功能：



> 提交预编辑的文本，并退出预编辑状态。

  * 函数原型：


    
    
    ret_t text_edit_preedit_confirm (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_select_all 函数

* * *

  * 函数功能：



> 全选。

  * 函数原型：


    
    
    ret_t text_edit_select_all (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
  
#### text_edit_set_canvas 函数

* * *

  * 函数功能：



> 设置canvas对象。

  * 函数原型：


    
    
    ret_t text_edit_set_canvas (text_edit_t* text_edit, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
c | canvas_t* | canvas对象。  
  
#### text_edit_set_caret_visible 函数

* * *

  * 函数功能：



> 设置光标的看见性。

  * 函数原型：


    
    
    ret_t text_edit_set_caret_visible (text_edit_t* text_edit, bool_t caret_visible);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
caret_visible | bool_t | 是否可见。  
  
#### text_edit_set_cursor 函数

* * *

  * 函数功能：



> 设置光标位置。

  * 函数原型：


    
    
    ret_t text_edit_set_cursor (text_edit_t* text_edit, uint32_t cursor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
cursor | uint32_t | 光标偏移。  
  
#### text_edit_set_mask 函数

* * *

  * 函数功能：



> 设置是否马赛克字符(用于密码)。

  * 函数原型：


    
    
    ret_t text_edit_set_mask (text_edit_t* text_edit, bool_t mask);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
mask | bool_t | 是否马赛克字符。  
  
#### text_edit_set_mask_char 函数

* * *

  * 函数功能：



> 设置马赛克字符。

  * 函数原型：


    
    
    ret_t text_edit_set_mask_char (text_edit_t* text_edit, wchar_t mask_char);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
mask_char | wchar_t | 马赛克字符。  
  
#### text_edit_set_max_chars 函数

* * *

  * 函数功能：



> 设置最大字符数（0 为不限制字符）。

  * 函数原型：


    
    
    ret_t text_edit_set_max_chars (text_edit_t* text_edit, uint32_t max_chars);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
max_chars | uint32_t | 最大行数。  
  
#### text_edit_set_max_rows 函数

* * *

  * 函数功能：



> 设置最大行数。

  * 函数原型：


    
    
    ret_t text_edit_set_max_rows (text_edit_t* text_edit, uint32_t max_rows);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
max_rows | uint32_t | 最大行数。  
  
#### text_edit_set_offset 函数

* * *

  * 函数功能：



> 设置滚动偏移。

  * 函数原型：


    
    
    ret_t text_edit_set_offset (text_edit_t* text_edit, int32_t ox, int32_t oy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
ox | int32_t | x偏移量。  
oy | int32_t | y偏移量。  
  
#### text_edit_set_on_char_will_input 函数

* * *

  * 函数功能：



> 设置字符输入回调函数。

  * 函数原型：


    
    
    ret_t text_edit_set_on_char_will_input (text_edit_t* text_edit, text_edit_on_char_will_input_t on_char_will_input, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
on_char_will_input | text_edit_on_char_will_input_t | 回调函数。  
ctx | void* | 回调函数上下文。  
  
#### text_edit_set_on_state_changed 函数

* * *

  * 函数功能：



> 设置状态改变回调函数。

  * 函数原型：


    
    
    ret_t text_edit_set_on_state_changed (text_edit_t* text_edit, text_edit_on_state_changed_t on_state_changed, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
on_state_changed | text_edit_on_state_changed_t | 回调函数。  
ctx | void* | 回调函数上下文。  
  
#### text_edit_set_on_text_will_delete 函数

* * *

  * 函数功能：



> 设置文本删除回调函数。

  * 函数原型：


    
    
    ret_t text_edit_set_on_text_will_delete (text_edit_t* text_edit, text_edit_on_text_will_delete_t on_text_will_delete, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
on_text_will_delete | text_edit_on_text_will_delete_t | 回调函数。  
ctx | void* | 回调函数上下文。  
  
#### text_edit_set_select 函数

* * *

  * 函数功能：



> 选择指定范围的文本。

  * 函数原型：


    
    
    ret_t text_edit_set_select (text_edit_t* text_edit, uint32_t start, uint32_t end);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
start | uint32_t | 起始偏移。  
end | uint32_t | 结束偏移。  
  
#### text_edit_set_tips 函数

* * *

  * 函数功能：



> 设置提示信息。

  * 函数原型：


    
    
    ret_t text_edit_set_tips (text_edit_t* text_edit, const char* tips, bool_t mlines);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
tips | const char* | 提示信息。  
mlines | bool_t | 提示信息是否多行显示。  
  
#### text_edit_set_wrap_word 函数

* * *

  * 函数功能：



> 设置是否自动折行。

  * 函数原型：


    
    
    ret_t text_edit_set_wrap_word (text_edit_t* text_edit, bool_t wrap_word);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
wrap_word | bool_t | 是否自动折行。  
  
#### text_edit_show_context_menu 函数

* * *

  * 函数功能：



> 显示上下文菜单。

  * 函数原型：


    
    
    ret_t text_edit_show_context_menu (text_edit_t* text_edit, int32_t x, int32_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。  
x | int32_t | x位置。  
y | int32_t | y位置。  
  
#### text_edit_unselect 函数

* * *

  * 函数功能：



> 取消选择。

  * 函数原型：


    
    
    ret_t text_edit_unselect (text_edit_t* text_edit);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
text_edit | text_edit_t* | text_edit对象。
