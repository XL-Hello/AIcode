## mledit_t

### 概述

![image](images/mledit_t_0.png)

多行编辑器控件。

mledit_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于mledit_t控件。

在xml中使用”mledit”标签创建多行编辑器控件。如：
    
    
    <mledit x="c" y="m" w="300" h="300" />
    

> 更多用法请参考：[mledit.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/mledit.xml)

在c代码中使用函数mledit_create创建多行编辑器控件。如：
    
    
    widget_t* tc = mledit_create(win, 10, 10, 240, 240);
    

> 完整示例请参考：[mledit demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/mledit.c)

## time_clock一般不需要设置style。

### 函数

函数名称 | 说明  
---|---  
mledit_cast | 转换为mledit对象(供脚本语言使用)。  
mledit_create | 创建mledit对象  
mledit_get_current_line_index | 获取光标所在视觉行号(一行文本可能分多行显示)。  
mledit_get_current_row_index | 获取光标所在物理行号。  
mledit_get_cursor | 获取编辑器光标位置。  
mledit_get_selected_text | 获取选中的文本。  
mledit_get_widget_vtable | 获取 mledit 虚表。  
mledit_insert_text | 插入一段文本。  
mledit_scroll_to_offset | 设置编辑器滚动到指定偏移位置。  
mledit_set_cancelable | 设置编辑器是否为可撤销修改。  
mledit_set_close_im_when_blured | 设置编辑器是否在失去焦点时关闭输入法。  
mledit_set_cursor | 设置编辑器光标位置。  
mledit_set_focus | 设置为焦点。  
mledit_set_keyboard | 设置自定义软键盘名称。  
mledit_set_max_chars | 设置编辑器的最大字符数（0 为不限制字符数）。  
mledit_set_max_lines | 设置编辑器的最大行数。  
mledit_set_open_im_when_focused | 设置编辑器是否在获得焦点时打开输入法。  
mledit_set_overwrite | 设置编辑器是否启用覆盖行（在行数达到最大行数时，可继续新增行，但最早的行将会消失）。  
mledit_set_readonly | 设置编辑器是否为只读。  
mledit_set_scroll_line | 设置编辑器滚动速度。  
mledit_set_select | 选择编辑器中指定范围的文本。  
mledit_set_tips | 设置编辑器的输入提示。  
mledit_set_tr_tips | 获取翻译之后的文本，然后调用mledit_set_tips。  
mledit_set_wrap_word | 设置编辑器是否自动折行。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
cancelable | bool_t | 是否支持撤销编辑。如果为TRUE，在失去焦点之前可以撤销所有修改(恢复获得焦点之前的内容)。  
close_im_when_blured | bool_t | 是否在失去焦点时关闭输入法(默认是)。  
keyboard | char* | 自定义软键盘名称。  
max_chars | uint32_t | 最大字符数。  
max_lines | uint32_t | 最大行数。  
open_im_when_focused | bool_t | 获得焦点时打开输入法。  
overwrite | bool_t | 是否启用覆盖行。  
readonly | bool_t | 编辑器是否为只读。  
scroll_line | uint32_t | 鼠标一次滚动行数。  
tips | char* | 输入提示。  
tr_tips | char* | 保存用于翻译的提示信息。  
wrap_word | bool_t | 是否自动折行。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_CHANGING | value_change_event_t | 文本正在改变事件(编辑中)。  
EVT_VALUE_CHANGED | value_change_event_t | 文本改变事件(编辑完成或设置文本时触发)。  
  
#### mledit_cast 函数

* * *

  * 函数功能：



> 转换为mledit对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* mledit_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | mledit对象。  
widget | widget_t* | mledit对象。  
  
#### mledit_create 函数

* * *

  * 函数功能：



> 创建mledit对象

  * 函数原型：


    
    
    widget_t* mledit_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### mledit_get_current_line_index 函数

* * *

  * 函数功能：



> 获取光标所在视觉行号(一行文本可能分多行显示)。

  * 函数原型：


    
    
    uint32_t mledit_get_current_line_index (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回光标所在行号。  
widget | widget_t* | widget对象。  
  
#### mledit_get_current_row_index 函数

* * *

  * 函数功能：



> 获取光标所在物理行号。

  * 函数原型：


    
    
    uint32_t mledit_get_current_row_index (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回光标所在行号。  
widget | widget_t* | widget对象。  
  
#### mledit_get_cursor 函数

* * *

  * 函数功能：



> 获取编辑器光标位置。

  * 函数原型：


    
    
    uint32_t mledit_get_cursor (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回光标位置。  
widget | widget_t* | widget对象。  
  
#### mledit_get_selected_text 函数

* * *

  * 函数功能：



> 获取选中的文本。 使用完后需调用 TKMEM_FREE() 进行释放文本占有内存。

  * 函数原型：


    
    
    char* mledit_get_selected_text (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回选中文本。  
widget | widget_t* | widget对象。  
  
#### mledit_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 mledit 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* mledit_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 mledit 虚表。  
  
#### mledit_insert_text 函数

* * *

  * 函数功能：



> 插入一段文本。

  * 函数原型：


    
    
    ret_t mledit_insert_text (widget_t* widget, uint32_t offset, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
offset | uint32_t | 插入的偏移位置。  
text | const char* | 待插入的文本。  
  
#### mledit_scroll_to_offset 函数

* * *

  * 函数功能：



> 设置编辑器滚动到指定偏移位置。

  * 函数原型：


    
    
    ret_t mledit_scroll_to_offset (widget_t* widget, uint32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
offset | uint32_t | 偏移位置。  
  
#### mledit_set_cancelable 函数

* * *

  * 函数功能：



> 设置编辑器是否为可撤销修改。

  * 函数原型：


    
    
    ret_t mledit_set_cancelable (widget_t* widget, bool_t cancelable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
cancelable | bool_t | 是否为可撤销修。  
  
#### mledit_set_close_im_when_blured 函数

* * *

  * 函数功能：



> 设置编辑器是否在失去焦点时关闭输入法。

  * 函数原型：


    
    
    ret_t mledit_set_close_im_when_blured (widget_t* widget, bool_t close_im_when_blured);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
close_im_when_blured | bool_t | 是否是否在失去焦点时关闭输入法。在失去焦点时关闭输入法。  
  
#### mledit_set_cursor 函数

* * *

  * 函数功能：



> 设置编辑器光标位置。

  * 函数原型：


    
    
    ret_t mledit_set_cursor (widget_t* widget, uint32_t cursor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
cursor | uint32_t | 光标位置。  
  
#### mledit_set_focus 函数

* * *

  * 函数功能：



> 设置为焦点。

  * 函数原型：


    
    
    ret_t mledit_set_focus (widget_t* widget, bool_t focus);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
focus | bool_t | 是否为焦点。  
  
#### mledit_set_keyboard 函数

* * *

  * 函数功能：



> 设置自定义软键盘名称。

  * 函数原型：


    
    
    ret_t mledit_set_keyboard (widget_t* widget, const char* keyboard);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
keyboard | const char* | 键盘名称(相应UI资源必须存在)。  
  
#### mledit_set_max_chars 函数

* * *

  * 函数功能：



> 设置编辑器的最大字符数（0 为不限制字符数）。

  * 函数原型：


    
    
    ret_t mledit_set_max_chars (widget_t* widget, uint32_t max_chars);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
max_chars | uint32_t | 最大字符数。  
  
#### mledit_set_max_lines 函数

* * *

  * 函数功能：



> 设置编辑器的最大行数。

  * 函数原型：


    
    
    ret_t mledit_set_max_lines (widget_t* widget, uint32_t max_lines);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
max_lines | uint32_t | 最大行数。  
  
#### mledit_set_open_im_when_focused 函数

* * *

  * 函数功能：



> 设置编辑器是否在获得焦点时打开输入法。
> 
>   * 设置默认焦点时，打开窗口时不弹出软键盘。
>   * 用键盘切换焦点时，编辑器获得焦点时不弹出软键盘。
> 


  * 函数原型：


    
    
    ret_t mledit_set_open_im_when_focused (widget_t* widget, bool_t open_im_when_focused);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
open_im_when_focused | bool_t | 是否在获得焦点时打开输入法。  
  
#### mledit_set_overwrite 函数

* * *

  * 函数功能：



> 设置编辑器是否启用覆盖行（在行数达到最大行数时，可继续新增行，但最早的行将会消失）。

  * 函数原型：


    
    
    ret_t mledit_set_overwrite (widget_t* widget, bool_t overwrite);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
overwrite | bool_t | 是否启用覆盖行。  
  
#### mledit_set_readonly 函数

* * *

  * 函数功能：



> 设置编辑器是否为只读。

  * 函数原型：


    
    
    ret_t mledit_set_readonly (widget_t* widget, bool_t readonly);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
readonly | bool_t | 只读。  
  
#### mledit_set_scroll_line 函数

* * *

  * 函数功能：



> 设置编辑器滚动速度。

  * 函数原型：


    
    
    ret_t mledit_set_scroll_line (widget_t* widget, uint32_t scroll_line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
scroll_line | uint32_t | 滚动行数。  
  
#### mledit_set_select 函数

* * *

  * 函数功能：



> 选择编辑器中指定范围的文本。

  * 函数原型：


    
    
    ret_t mledit_set_select (widget_t* widget, uint32_t start, uint32_t end);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
start | uint32_t | 起始偏移。  
end | uint32_t | 结束偏移。  
  
#### mledit_set_tips 函数

* * *

  * 函数功能：



> 设置编辑器的输入提示。

  * 函数原型：


    
    
    ret_t mledit_set_tips (widget_t* widget, const char* tips);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
tips | const char* | 输入提示。  
  
#### mledit_set_tr_tips 函数

* * *

  * 函数功能：



> 获取翻译之后的文本，然后调用mledit_set_tips。

  * 函数原型：


    
    
    ret_t mledit_set_tr_tips (widget_t* widget, const char* tr_tips);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
tr_tips | const char* | 提示信息。  
  
#### mledit_set_wrap_word 函数

* * *

  * 函数功能：



> 设置编辑器是否自动折行。

  * 函数原型：


    
    
    ret_t mledit_set_wrap_word (widget_t* widget, bool_t wrap_word);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
wrap_word | bool_t | 是否自动折行。  
  
#### cancelable 属性

* * *

> 是否支持撤销编辑。如果为TRUE，在失去焦点之前可以撤销所有修改(恢复获得焦点之前的内容)。
> 
>   * 1.一般配合keyboard的”cancel”按钮使用。
>   * 2.为TRUE时，如果内容有变化，会设置编辑器的状态为changed，所以此时编辑器需要支持changed状态的style。
> 


  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### close_im_when_blured 属性

* * *

> 是否在失去焦点时关闭输入法(默认是)。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### keyboard 属性

* * *

> 自定义软键盘名称。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### max_chars 属性

* * *

> 最大字符数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### max_lines 属性

* * *

> 最大行数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### open_im_when_focused 属性

* * *

> 获得焦点时打开输入法。
> 
> 主要用于没有指针设备的情况，否则每次切换焦点时都打开输入法。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### overwrite 属性

* * *

> 是否启用覆盖行。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### readonly 属性

* * *

> 编辑器是否为只读。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### scroll_line 属性

* * *

> 鼠标一次滚动行数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### tips 属性

* * *

> 输入提示。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### tr_tips 属性

* * *

> 保存用于翻译的提示信息。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### wrap_word 属性

* * *

> 是否自动折行。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是
