## edit_t

### 概述

![image](images/edit_t_0.png)

单行编辑器控件。

在基于SDL的平台，单行编辑器控件使用平台原生的输入法，对于嵌入式平台使用内置的输入法。

在使用内置的输入法时，软键盘由输入类型决定，开发者可以自定义软键盘的界面。

edit_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于edit_t控件。

edit_t本身可以做为容器，放入按钮等控件。有几个特殊的子控件：

  * 名为”clear”的按钮。点击时清除编辑器中的内容。
  * 名为”inc”的按钮。点击时增加编辑器的值，用于实现类似于spinbox的功能。
  * 名为”dec”的按钮。点击时减少编辑器的值，用于实现类似于spinbox的功能。
  * 名为”visible”的复选框。勾选时显示密码，反之不显示密码。



在xml中使用”edit”标签创建编辑器控件。如：
    
    
    <edit x="c" y="m" w="80" h="30"
    tips="age" input_type="uint" min="0" max="150" step="1" auto_fix="true" style="number" />
    

> XXX：需要在min/max/step之前设置input_type。
> 
> 更多用法请参考： [edit.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/edit.xml)

在c代码中使用函数edit_create创建编辑器控件。如：
    
    
    widget_t* edit = edit_create(win, 10, 10, 128, 30);
    widget_set_text(edit, L"OK");
    

> 创建之后，可以用widget_set_text或widget_set_text_utf8设置文本内容。
> 
> 完整示例请参考： [edit demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/edit.c)

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <style name="default" border_color="#a0a0a0"  text_color="black" text_align_h="left">
    <normal     bg_color="#f0f0f0" />
    <focused    bg_color="#f0f0f0" border_color="black"/>
    <disable    bg_color="gray" text_color="#d0d0d0" />
    <error      bg_color="#f0f0f0" text_color="red" />
    <empty      bg_color="#f0f0f0" text_color="#a0a0a0" />
    </style>
    

> 更多用法请参考： [theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L104)

* * *

### 函数

函数名称 | 说明  
---|---  
edit_cast | 转换为edit对象(供脚本语言使用)。  
edit_create | 创建edit对象  
edit_get_cursor | 获取输入框的光标位置。  
edit_get_double | 获取double类型的值。  
edit_get_int | 获取int类型的值。  
edit_get_selected_text | 获取选中的文本。  
edit_get_widget_vtable | 获取 edit 虚表。  
edit_set_action_text | 设置软键盘上action按钮的文本。  
edit_set_auto_fix | 设置编辑器是否为自动改正。  
edit_set_cancelable | 设置编辑器是否为可撤销修改。  
edit_set_close_im_when_blured | 设置编辑器是否在失去焦点时关闭输入法。  
edit_set_cursor | 设置输入框的光标位置。  
edit_set_dec_value | 设置减少值的回调函数。  
edit_set_double | 设置double类型的值。  
edit_set_double_ex | 设置double类型的值。  
edit_set_fix_value | 设置修正输入内容的回调函数。  
edit_set_float_limit | 设置为浮点数输入及取值范围。  
edit_set_focus | 设置为焦点。  
edit_set_focus_next_when_enter | 设置输入回车后是否跳到下一个控件中。  
edit_set_inc_value | 设置增加值的回调函数。  
edit_set_input_type | 设置编辑器的输入类型。  
edit_set_int | 设置int类型的值。  
edit_set_int_limit | 设置为整数输入及取值范围。  
edit_set_is_valid_char | 设置输入字符检查函数。  
edit_set_is_valid_value | 设置输入内容检查函数。  
edit_set_keyboard | 设置自定义软键盘名称。  
edit_set_open_im_when_focused | 设置编辑器是否在获得焦点时打开输入法。  
edit_set_password_visible | 当编辑器输入类型为密码时，设置密码是否可见。  
edit_set_pre_delete | 设置预删除处理的回调函数。  
edit_set_pre_input | 设置预输入处理的回调函数。  
edit_set_readonly | 设置编辑器是否为只读。  
edit_set_select | 选择指定范围的文本。  
edit_set_select_none_when_focused | 设置编辑器是否在获得焦点时不选中文本。  
edit_set_text_limit | 设置为文本输入及其长度限制，不允许输入超过max个字符，少于min个字符时进入error状态。  
edit_set_tips | 设置编辑器的输入提示。  
edit_set_tr_tips | 获取翻译之后的文本，然后调用edit_set_tips。  
edit_set_validator | 设置输入内容校验脚本。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
action_text | char* | 软键盘上action按钮的文本。内置取值有：  
auto_fix | bool_t | 输入无效时，是否自动改正。  
cancelable | bool_t | 是否支持撤销编辑。如果为TRUE，在失去焦点之前可以撤销所有修改(恢复获得焦点之前的内容)。  
close_im_when_blured | bool_t | 是否在失去焦点时关闭输入法(默认是)。  
focus_next_when_enter | bool_t | 输入回车后是否跳到下一个控件中。  
input_type | input_type_t | 输入类型。  
keyboard | char* | 自定义软键盘名称。AWTK优先查找keyboard属性设置的键盘文件名（该键盘的XML文件需要在default\raw\ui目录下存在），如果没有指定keyboard，就找input_type设置的键盘类型。如果指定为空字符串，则表示不需要软键盘。  
max | double | 最大值或最大长度。  
min | double | 最小值或最小长度。  
open_im_when_focused | bool_t | 获得焦点时打开输入法。  
password_visible | bool_t | 密码是否可见。  
readonly | bool_t | 编辑器是否为只读。  
select_none_when_focused | bool_t | 获得焦点时不选中文本。  
step | double | 步长。  
tips | char* | 输入提示。  
tr_tips | char* | 保存用于翻译的提示信息。  
validator | char* | fscript脚本，用输入校验，如：(len(text) > 3) && (len(text) < 10)。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_VALUE_CHANGING | value_change_event_t | 文本正在改变事件(编辑中)。  
EVT_VALUE_CHANGED | value_change_event_t | 文本改变事件(编辑完成或设置文本时触发)。  
EVT_IM_ACTION | event_t | 软键盘Action点击事件。  
  
#### edit_cast 函数

* * *

  * 函数功能：



> 转换为edit对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* edit_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | edit对象。  
widget | widget_t* | edit对象。  
  
#### edit_create 函数

* * *

  * 函数功能：



> 创建edit对象

  * 函数原型：


    
    
    widget_t* edit_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### edit_get_cursor 函数

* * *

  * 函数功能：



> 获取输入框的光标位置。

  * 函数原型：


    
    
    uint32_t edit_get_cursor (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回光标位置。  
widget | widget_t* | widget对象。  
  
#### edit_get_double 函数

* * *

  * 函数功能：



> 获取double类型的值。

  * 函数原型：


    
    
    double edit_get_double (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回double的值。  
widget | widget_t* | widget对象。  
  
#### edit_get_int 函数

* * *

  * 函数功能：



> 获取int类型的值。

  * 函数原型：


    
    
    int32_t edit_get_int (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回int的值。  
widget | widget_t* | widget对象。  
  
#### edit_get_selected_text 函数

* * *

  * 函数功能：



> 获取选中的文本。 使用完后需调用 TKMEM_FREE() 进行释放文本占有内存。

  * 函数原型：


    
    
    char* edit_get_selected_text (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回选中文本。  
widget | widget_t* | widget对象。  
  
#### edit_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 edit 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* edit_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 edit 虚表。  
  
#### edit_set_action_text 函数

* * *

  * 函数功能：



> 设置软键盘上action按钮的文本。

  * 函数原型：


    
    
    ret_t edit_set_action_text (widget_t* widget, const char* action_text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
action_text | const char* | 软键盘上action按钮的文本。  
  
#### edit_set_auto_fix 函数

* * *

  * 函数功能：



> 设置编辑器是否为自动改正。

  * 函数原型：


    
    
    ret_t edit_set_auto_fix (widget_t* widget, bool_t auto_fix);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
auto_fix | bool_t | 自动改正。  
  
#### edit_set_cancelable 函数

* * *

  * 函数功能：



> 设置编辑器是否为可撤销修改。

  * 函数原型：


    
    
    ret_t edit_set_cancelable (widget_t* widget, bool_t cancelable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
cancelable | bool_t | 是否为可撤销修。  
  
#### edit_set_close_im_when_blured 函数

* * *

  * 函数功能：



> 设置编辑器是否在失去焦点时关闭输入法。

  * 函数原型：


    
    
    ret_t edit_set_close_im_when_blured (widget_t* widget, bool_t close_im_when_blured);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
close_im_when_blured | bool_t | 是否是否在失去焦点时关闭输入法。在失去焦点时关闭输入法。  
  
#### edit_set_cursor 函数

* * *

  * 函数功能：



> 设置输入框的光标位置。

  * 函数原型：


    
    
    ret_t edit_set_cursor (widget_t* widget, uint32_t cursor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
cursor | uint32_t | 光标位置。  
  
#### edit_set_dec_value 函数

* * *

  * 函数功能：



> 设置减少值的回调函数。 如果内置函数不能满足需求时，可以设置自定义的检查函数。

  * 函数原型：


    
    
    ret_t edit_set_dec_value (widget_t* widget, edit_dec_value_t dec_value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
dec_value | edit_dec_value_t | 减少值的回调函数。  
  
#### edit_set_double 函数

* * *

  * 函数功能：



> 设置double类型的值。

  * 函数原型：


    
    
    ret_t edit_set_double (widget_t* widget, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
value | double | 值。  
  
#### edit_set_double_ex 函数

* * *

  * 函数功能：



> 设置double类型的值。

  * 函数原型：


    
    
    ret_t edit_set_double_ex (widget_t* widget, const char* format, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
format | const char* | 格式(缺省为”%2.2lf”)。  
value | double | 值。  
  
#### edit_set_fix_value 函数

* * *

  * 函数功能：



> 设置修正输入内容的回调函数。 如果内置函数不能满足需求时，可以设置自定义的检查函数。

  * 函数原型：


    
    
    ret_t edit_set_fix_value (widget_t* widget, edit_fix_value_t fix_value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
fix_value | edit_fix_value_t | 修正输入内容的回调函数。  
  
#### edit_set_float_limit 函数

* * *

  * 函数功能：



> 设置为浮点数输入及取值范围。

  * 函数原型：


    
    
    ret_t edit_set_float_limit (widget_t* widget, double min, double max, double step);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
min | double | 最小值。  
max | double | 最大值。  
step | double | 步长。  
  
#### edit_set_focus 函数

* * *

  * 函数功能：



> 设置为焦点。

  * 函数原型：


    
    
    ret_t edit_set_focus (widget_t* widget, bool_t focus);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
focus | bool_t | 是否为焦点。  
  
#### edit_set_focus_next_when_enter 函数

* * *

  * 函数功能：



> 设置输入回车后是否跳到下一个控件中。

  * 函数原型：


    
    
    ret_t edit_set_focus_next_when_enter (widget_t* widget, bool_t focus_next_when_enter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
focus_next_when_enter | bool_t | 是否跳入下一个控件中。  
  
#### edit_set_inc_value 函数

* * *

  * 函数功能：



> 设置增加值的回调函数。 如果内置函数不能满足需求时，可以设置自定义的检查函数。

  * 函数原型：


    
    
    ret_t edit_set_inc_value (widget_t* widget, edit_inc_value_t inc_value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
inc_value | edit_inc_value_t | 增加值的回调函数。  
  
#### edit_set_input_type 函数

* * *

  * 函数功能：



> 设置编辑器的输入类型。

  * 函数原型：


    
    
    ret_t edit_set_input_type (widget_t* widget, input_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
type | input_type_t | 输入类型。  
  
#### edit_set_int 函数

* * *

  * 函数功能：



> 设置int类型的值。

  * 函数原型：


    
    
    ret_t edit_set_int (widget_t* widget, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
value | int32_t | 值。  
  
#### edit_set_int_limit 函数

* * *

  * 函数功能：



> 设置为整数输入及取值范围。

  * 函数原型：


    
    
    ret_t edit_set_int_limit (widget_t* widget, int32_t min, int32_t max, uint32_t step);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
min | int32_t | 最小值。  
max | int32_t | 最大值。  
step | uint32_t | 步长。  
  
#### edit_set_is_valid_char 函数

* * *

  * 函数功能：



> 设置输入字符检查函数。 如果内置函数不能满足需求时，可以设置自定义的检查函数。

  * 函数原型：


    
    
    ret_t edit_set_is_valid_char (widget_t* widget, edit_is_valid_char_t is_valid_char);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
is_valid_char | edit_is_valid_char_t | 检查输入字符是否有效的回调函数。  
  
#### edit_set_is_valid_value 函数

* * *

  * 函数功能：



> 设置输入内容检查函数。 如果内置函数不能满足需求时，可以设置自定义的检查函数。

  * 函数原型：


    
    
    ret_t edit_set_is_valid_value (widget_t* widget, edit_is_valid_value_t is_valid_value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
is_valid_value | edit_is_valid_value_t | 检查输入内容是否有效的回调函数。  
  
#### edit_set_keyboard 函数

* * *

  * 函数功能：



> 设置自定义软键盘名称。

  * 函数原型：


    
    
    ret_t edit_set_keyboard (widget_t* widget, const char* keyboard);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
keyboard | const char* | 键盘名称(相应UI资源必须存在)。  
  
#### edit_set_open_im_when_focused 函数

* * *

  * 函数功能：



> 设置编辑器是否在获得焦点时打开输入法。
> 
>   * 设置默认焦点时，打开窗口时不弹出软键盘。
>   * 用键盘切换焦点时，编辑器获得焦点时不弹出软键盘。
> 


  * 函数原型：


    
    
    ret_t edit_set_open_im_when_focused (widget_t* widget, bool_t open_im_when_focused);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
open_im_when_focused | bool_t | 是否在获得焦点时打开输入法。  
  
#### edit_set_password_visible 函数

* * *

  * 函数功能：



> 当编辑器输入类型为密码时，设置密码是否可见。

  * 函数原型：


    
    
    ret_t edit_set_password_visible (widget_t* widget, bool_t password_visible);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
password_visible | bool_t | 密码是否可见。  
  
#### edit_set_pre_delete 函数

* * *

  * 函数功能：



> 设置预删除处理的回调函数。 如果内置函数不能满足需求时，可以设置自定义的检查函数。

  * 函数原型：


    
    
    ret_t edit_set_pre_delete (widget_t* widget, edit_pre_delete_t pre_delete);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
pre_delete | edit_pre_delete_t | 预删除处理的回调函数(删除时保留分隔符)。  
  
#### edit_set_pre_input 函数

* * *

  * 函数功能：



> 设置预输入处理的回调函数。 如果内置函数不能满足需求时，可以设置自定义的检查函数。

  * 函数原型：


    
    
    ret_t edit_set_pre_input (widget_t* widget, edit_pre_input_t pre_input);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
pre_input | edit_pre_input_t | 预输入处理的回调函数(处理一些特殊的键)。  
  
#### edit_set_readonly 函数

* * *

  * 函数功能：



> 设置编辑器是否为只读。

  * 函数原型：


    
    
    ret_t edit_set_readonly (widget_t* widget, bool_t readonly);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
readonly | bool_t | 只读。  
  
#### edit_set_select 函数

* * *

  * 函数功能：



> 选择指定范围的文本。

  * 函数原型：


    
    
    ret_t edit_set_select (widget_t* widget, uint32_t start, uint32_t end);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
start | uint32_t | 起始偏移。  
end | uint32_t | 结束偏移。  
  
#### edit_set_select_none_when_focused 函数

* * *

  * 函数功能：



> 设置编辑器是否在获得焦点时不选中文本。

  * 函数原型：


    
    
    ret_t edit_set_select_none_when_focused (widget_t* widget, bool_t select_none_when_focused);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
select_none_when_focused | bool_t | 是否在获得焦点时不选中文本。  
  
#### edit_set_text_limit 函数

* * *

  * 函数功能：



> 设置为文本输入及其长度限制，不允许输入超过max个字符，少于min个字符时进入error状态。

  * 函数原型：


    
    
    ret_t edit_set_text_limit (widget_t* widget, uint32_t min, uint32_t max);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
min | uint32_t | 最小长度。  
max | uint32_t | 最大长度。  
  
#### edit_set_tips 函数

* * *

  * 函数功能：



> 设置编辑器的输入提示。

  * 函数原型：


    
    
    ret_t edit_set_tips (widget_t* widget, const char* tips);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
tips | const char* | 输入提示。  
  
#### edit_set_tr_tips 函数

* * *

  * 函数功能：



> 获取翻译之后的文本，然后调用edit_set_tips。

  * 函数原型：


    
    
    ret_t edit_set_tr_tips (widget_t* widget, const char* tr_tips);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
tr_tips | const char* | 提示信息。  
  
#### edit_set_validator 函数

* * *

  * 函数功能：



> 设置输入内容校验脚本。 如果内置函数不能满足需求时，可以设置自定义的检查脚本。

  * 函数原型：


    
    
    ret_t edit_set_validator (widget_t* widget, const char* validator);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
validator | const char* | 校验输入内容的脚本。  
  
#### action_text 属性

* * *

> 软键盘上action按钮的文本。内置取值有：

  * next 将焦点切换到下一个控件。
  * done 完成，关闭软键盘。



也可以使用其它文本，比如send表示发送。这个需要自己实现相应的功能，处理EVT_IM_ACTION事件即可。

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
  
#### auto_fix 属性

* * *

> 输入无效时，是否自动改正。

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
  
#### focus_next_when_enter 属性

* * *

> 输入回车后是否跳到下一个控件中。

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
  
#### input_type 属性

* * *

> 输入类型。

  * 类型：input_type_t

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

> 自定义软键盘名称。AWTK优先查找keyboard属性设置的键盘文件名（该键盘的XML文件需要在default\raw\ui目录下存在），如果没有指定keyboard，就找input_type设置的键盘类型。如果指定为空字符串，则表示不需要软键盘。

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
  
#### max 属性

* * *

> 最大值或最大长度。

  * 类型：double

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
  
#### min 属性

* * *

> 最小值或最小长度。

  * 类型：double

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
  
#### password_visible 属性

* * *

> 密码是否可见。

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
  
#### select_none_when_focused 属性

* * *

> 获得焦点时不选中文本。
> 
> 主要用于没有指针设备的情况，否则软键盘无法取消选中文本。

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
  
#### step 属性

* * *

> 步长。 作为数值型编辑器时，一次增加和减少时的数值。

  * 类型：double

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
  
#### validator 属性

* * *

> fscript脚本，用输入校验，如：(len(text) > 3) && (len(text) < 10)。
> 
> 用于校验输入的文本是否合法。

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
