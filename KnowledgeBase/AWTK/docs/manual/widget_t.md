## widget_t

### 概述

**widget_t** 是所有控件、窗口和窗口管理器的基类。 **widget_t** 也是一个容器，可放其它**widget_t** 到它的内部，形成一个树形结构。

![image](images/widget_t_0.png)

通常**widget_t** 通过一个矩形区域向用户呈现一些信息，接受用户的输入，并据此做出适当的反应。 它负责控件的生命周期、通用状态、事件分发和Style的管理。 本类提供的接口(函数和属性)除非特别说明，一般都适用于子类控件。

为了便于解释，这里特别说明一下几个术语：

  * **父控件与子控件** ：父控件与子控件指的两个控件的组合关系(这是在运行时决定的)。 比如：在窗口中放一个按钮，此时，我们称按钮是窗口的子控件，窗口是按钮的父控件。



![image](images/widget_t_1.png)

  * **子类控件与父类控件** ：子类控件与父类控件指的两类控件的继承关系(这是在设计时决定的)。 比如：我们称**button_t** 是**widget_t** 的子类控件，**widget_t** 是**button_t** 的父类控件。



![image](images/widget_t_2.png)

widget相关的函数都只能在GUI线程中执行，如果需在非GUI线程中想调用widget相关函数， 请用idle_queue或timer_queue进行串行化。 请参考[demo thread](https://github.com/zlgopen/awtk/blob/master/demos/demo_thread_app.c)

**widget_t** 是抽象类，不要直接创建**widget_t** 的实例。控件支持两种创建方式：

  * 通过XML创建。如：


    
    
    <button x="c" y="m" w="80" h="30" text="OK"/>
    

  * 通过代码创建。如：


    
    
    widget_t* button = button_create(win, 10, 10, 128, 30);
    widget_set_text(button, L"OK");
    widget_on(button, EVT_CLICK, on_click, NULL);
    

* * *

### 函数

函数名称 | 说明  
---|---  
widget_add_child | 加入一个子控件。  
widget_add_child_default | 加入一个子控件默认实现(供子类调用)。  
widget_add_idle | 创建idle。  
widget_add_timer | 创建定时器。  
widget_add_value | 增加控件的值。  
widget_add_value_int | 增加控件的值。  
widget_animate_value_to | 设置控件的值(以动画形式变化到指定的值)。  
widget_auto_scale_children | 根据缩放子控件的位置和大小。  
widget_back | 请求返回到前一个窗口。  
widget_back_to_home | 请求返回到home窗口。  
widget_begin_wait_pointer_cursor | 开始等待鼠标指针。  
widget_calc_icon_text_rect | 计算icon text的位置。  
widget_cast | 转换为widget对象(供脚本语言使用)。  
widget_child | 查找指定名称的子控件(同widget_lookup(widget, name, FALSE))。  
widget_child_on | 为指定名称的子控件注册指定事件的处理函数。  
widget_clone | clone。  
widget_close_window | 关闭控件所在的窗口。  
widget_close_window_force | 关闭控件所在的窗口。  
widget_count_children | 获取子控件的个数。  
widget_create | 创建控件。仅在子类控件构造函数中使用。  
widget_create_animator | 创建动画。  
widget_destroy | 从父控件中移除控件，并调用unref函数销毁控件。  
widget_destroy_animator | 销毁动画。  
widget_destroy_async | 从父控件中移除控件，并调用unref函数销毁控件。  
widget_destroy_children | 销毁全部子控件。  
widget_dispatch | 分发一个事件。  
widget_dispatch_async | 异步分发一个事件。  
widget_dispatch_event_to_target_recursive | 递归分发事件到targe控件。  
widget_dispatch_model_event | 分发model事件(分发到各个窗口)。  
widget_dispatch_recursive | 分发一个事件控件本身及所有子控件。  
widget_dispatch_simple_event | 分发一个简单事件。  
widget_dispatch_to_key_target | 递归的分发一个事件到所有key_target子控件。  
widget_dispatch_to_target | 递归的分发一个事件到所有target子控件。  
widget_draw_arc_at_center | 以控件中心为中心绘制圆弧。  
widget_draw_background | 根据控件的style绘制背景矩形。  
widget_draw_text_in_rect | 在canvas绘制一行文本。  
widget_end_wait_pointer_cursor | 结束等待鼠标指针。  
widget_ensure_visible_in_viewport | 使控件滚动到可见区域。  
widget_equal | 判断两个widget是否相同。  
widget_fill_bg_rect | 根据控件的style绘制背景矩形。  
widget_fill_fg_rect | 根据控件的style绘制前景矩形。  
widget_find_animator | 查找指定名称的动画。  
widget_find_parent_by_name | 通过名称查找父控件。  
widget_find_parent_by_type | 通过类型查找父控件。  
widget_find_target | 查找x/y坐标对应的子控件。  
widget_focus_first | 置焦点于第一个控件。  
widget_focus_next | 把焦点移动下一个控件。  
widget_focus_prev | 把焦点移动前一个控件。  
widget_foreach | 遍历当前控件及子控件。  
widget_get_assets_manager | 获取assets_manager对象。  
widget_get_auto_adjust_size | 获取控件auto_adjust_size属性值。  
widget_get_canvas | 获取canvas对象。  
widget_get_child | 获取指定索引的子控件。  
widget_get_child_text_utf8 | 获取子控件的文本。  
widget_get_content_area | 获取widget去掉margin之外的区域。  
widget_get_enable | 获取控件enable属性值。  
widget_get_feedback | 获取控件feedback属性值。  
widget_get_floating | 获取控件floating属性值。  
widget_get_focusable | 获取控件focusable属性值。  
widget_get_focused_widget | 获取当前窗口中的焦点控件。  
widget_get_font_manager | 获取font_manager对象。  
widget_get_image_manager | 获取image_manager对象。  
widget_get_locale_info | 获取locale_info对象。  
widget_get_native_window | 获取原生窗口对象。  
widget_get_prop | 获取控件指定属性的值。  
widget_get_prop_bool | 获取布尔格式的属性。  
widget_get_prop_default_value | 获取控件指定属性的缺省值(在持久化控件时，无需保存缺省值)。  
widget_get_prop_float | 获取浮点数格式的属性。  
widget_get_prop_int | 获取整数格式的属性。  
widget_get_prop_pointer | 获取指针格式的属性。  
widget_get_prop_str | 获取字符串格式的属性。  
widget_get_sensitive | 获取控件sensitive属性值。  
widget_get_state_for_style | 把控件的状态转成获取style选要的状态，一般只在子类中使用。  
widget_get_style | 获取widget样式。  
widget_get_style_type | 获取 widget 对应风格类型  
widget_get_text | 获取控件的文本。  
widget_get_text_utf8 | 获取控件的文本。  
widget_get_theme_name | 获取 theme 的名称  
widget_get_type | 获取当前控件的类型名称。  
widget_get_value | 获取控件的值。只是对widget_get_prop的包装，值的意义由子类控件决定。  
widget_get_value_int | 获取控件的值。只是对widget_get_prop的包装，值的意义由子类控件决定。  
widget_get_visible | 获取控件visible属性值。  
widget_get_widget_vtable | 获取 widget 虚表。  
widget_get_window | 获取当前控件所在的窗口。  
widget_get_window_manager | 获取当前的窗口管理器。  
widget_get_window_theme | 获取控件的窗体样式。  
widget_get_with_focus_state | 获取控件with_focus_state属性值。  
widget_grab | 让指定子控件抓住事件。  
widget_has_highlighter | 判断widget拥有高亮属性。  
widget_index_of | 获取控件在父控件中的索引编号。  
widget_init | 初始化控件。仅在子类控件构造函数中使用。  
widget_insert_child | 插入子控件到指定的位置。  
widget_invalidate | 请求重绘指定的区域  
widget_invalidate_force | 请求强制重绘控件。  
widget_is_always_on_top | 检查控件是否总在最上层。  
widget_is_change_focus_key | 是否是切换焦点的键。  
widget_is_designing_window | 判断当前控件是否是设计窗口。  
widget_is_dialog | 检查控件是否是对话框类型。  
widget_is_direct_parent_of | 判断当前控件是否是指定控件的直系父控件。  
widget_is_fullscreen_window | 检查控件是否是全屏窗口。  
widget_is_instance_of | 检查控件是否是指定的类型。  
widget_is_keyboard | 判断当前控件是否是keyboard。  
widget_is_normal_window | 检查控件是否是普通窗口类型。  
widget_is_opened_dialog | 检查控件弹出对话框控件是否已经打开了（而非挂起状态）。  
widget_is_opened_popup | 检查控件弹出窗口控件是否已经打开了（而非挂起状态）。  
widget_is_overlay | 检查控件是否是overlay窗口类型。  
widget_is_parent_of | 判断当前控件是否是指定控件的父控件(包括非直系)。  
widget_is_point_in | 判断一个点是否在控件内。  
widget_is_popup | 检查控件是否是弹出窗口类型。  
widget_is_style_exist | 查询指定的style是否存在。  
widget_is_support_highlighter | 判断widget是否支持高亮。  
widget_is_system_bar | 检查控件是否是system bar类型。  
widget_is_window | 判断当前控件是否是窗口。  
widget_is_window_created | 判断窗口及子控件创建或加载是否完成。  
widget_is_window_manager | 判断当前控件是否是窗口管理器。  
widget_is_window_opened | 判断当前控件所在的窗口是否已经打开。  
widget_layout | 布局当前控件及子控件。  
widget_layout_children | layout子控件。  
widget_load_asset | 加载资源。  
widget_load_asset_ex | 加载资源。  
widget_load_image | 加载图片。  
widget_lookup | 查找指定名称的子控件(返回第一个)。  
widget_lookup_by_type | 查找指定类型的子控件(返回第一个)。  
widget_measure_text | 计算文本的宽度。  
widget_move | 移动控件。  
widget_move_resize | 移动控件并调整控件的大小。  
widget_move_resize_ex | 移动控件并调整控件的大小。  
widget_move_to_center | 移动控件到父控件中间。  
widget_off | 注销指定事件的处理函数。  
widget_off_by_ctx | 注销指定ctx的事件处理函数。  
widget_off_by_func | 注销指定函数的事件处理函数。  
widget_off_by_tag | 注销指定tag的事件处理函数。  
widget_on | 注册指定事件的处理函数。  
widget_on_keydown | 处理key down事件。  
widget_on_keyup | 处理key up事件。  
widget_on_paint_background | 绘制背景。  
widget_on_paint_border | 绘制边框。  
widget_on_paint_children | 绘制子控件。  
widget_on_paint_self | 绘制自身。  
widget_on_pointer_down_children | 处理子控件的pointer down事件。  
widget_on_pointer_move_children | 处理子控件的pointer move事件。  
widget_on_pointer_up_children | 处理子控件的pointer up事件。  
widget_on_with_tag | 注册指定tag的事件处理函数。  
widget_paint | 绘制控件到一个canvas上。  
widget_paint_helper | 帮助子控件实现自己的绘制函数。  
widget_pause_animator | 暂停动画。  
widget_prepare_text_style | 从widget的style中取出字体名称、大小和颜色数据，设置到canvas中。  
widget_prepare_text_style_ex | 从widget的style中取出字体名称、大小和颜色数据，设置到canvas中。  
widget_re_translate_text | 语言改变后，重新翻译控件上的文本(包括子控件)。  
widget_ref | 增加控件的引用计数。  
widget_remove_child | 移出指定的子控件(并不销毁)。  
widget_remove_idle | 删除指定的idle。  
widget_remove_timer | 删除指定的timer。  
widget_reset_canvas | 重置canvas对象。for designer only,调用者需要unload全部图片  
widget_resize | 调整控件的大小。  
widget_restack | 调整控件在父控件中的位置序数。  
widget_set_animation | 设置控件的动画参数(仅用于在UI文件使用)。  
widget_set_animator_time_scale | 设置动画的时间倍率，<0: 时间倒退，<1: 时间变慢，>1 时间变快。  
widget_set_as_key_target | 递归的把父控件的key_target设置为自己。  
widget_set_auto_adjust_size | 设置控件是否根据子控件和文本自动调整控件自身大小。  
widget_set_child_text_utf8 | 设置子控件的文本。  
widget_set_child_text_with_double | 用一个浮点数去设置子控件的文本。  
widget_set_child_text_with_int | 用一个整数去设置子控件的文本。  
widget_set_children_layout | 设置子控件的布局参数。  
widget_set_dirty_rect_tolerance | 设置控件脏矩形超出控件本身大小的最大范围(一般不用指定)。  
widget_set_enable | 设置控件的可用性。  
widget_set_feedback | 设置控件是否启用反馈。  
widget_set_floating | 设置控件的floating标志。  
widget_set_focusable | 设置控件是否可获得焦点。  
widget_set_focused | 设置控件是否获得焦点。  
widget_set_name | 设置控件的名称。  
widget_set_need_relayout | 设置控件需要relayout标识。  
widget_set_need_relayout_children | 设置控件需要relayout标识。  
widget_set_need_update_style | 设置需要更新Style。  
widget_set_need_update_style_recursive | 让控件及子控件设置需要更新Style。  
widget_set_opacity | 设置控件的不透明度。  
widget_set_pointer_cursor | 设置鼠标指针的图片名。  
widget_set_prop | 设置控件指定属性的值。  
widget_set_prop_bool | 设置布尔格式的属性。  
widget_set_prop_float | 设置浮点数格式的属性。  
widget_set_prop_int | 设置整数格式的属性。  
widget_set_prop_pointer | 设置指针格式的属性。  
widget_set_prop_pointer_ex | 设置指针格式的属性。  
widget_set_prop_str | 设置字符串格式的属性。  
widget_set_props | 设置多个参数。  
widget_set_self_layout | 设置控件自己的布局参数。  
widget_set_self_layout_params | 设置控件自己的布局(缺省布局器)参数(建议用widget_set_self_layout)。  
widget_set_sensitive | 设置控件是否接受用户事件。  
widget_set_state | 设置控件的状态。  
widget_set_style | 设置widget私有样式。  
widget_set_style_color | 设置颜色类型的style。  
widget_set_style_int | 设置整数类型的style。  
widget_set_style_str | 设置字符串类型的style。  
widget_set_text | 设置控件的文本。（如果字符串相同，则不会重复设置以及触发事件）  
widget_set_text_ex | 设置控件的文本。  
widget_set_text_utf8 | 设置控件的文本。（如果字符串相同，则不会重复设置以及触发事件）  
widget_set_text_utf8_ex | 设置控件的文本。  
widget_set_text_with_double | 设置控件的文本。  
widget_set_theme | 设置theme的名称，用于动态切换主题。名称与当前主题名称相同，则重新加载全部资源。  
widget_set_tr_text | 获取翻译之后的文本，然后调用widget_set_text。  
widget_set_value | 设置控件的值。  
widget_set_value_int | 设置控件的值。  
widget_set_visible | 设置控件的可见性。  
widget_set_visible_only | 设置控件的可见性(不触发repaint和relayout)。  
widget_start_animator | 播放动画。  
widget_stop_animator | 停止动画(控件的相应属性回归原位)。  
widget_stroke_border_rect | 根据控件的style绘制边框矩形。  
widget_take_snapshot | 创建一个bitmap对象，将控件绘制到bitmap上，并返回bitmap对象。  
widget_take_snapshot_rect | 创建一个bitmap对象，将控件绘制到bitmap上并且可以设置该控件的截屏区域，返回bitmap对象。  
widget_to_global | 将控件内的本地坐标转换成全局坐标。  
widget_to_local | 将屏幕坐标转换成控件内的本地坐标，即相对于控件左上角的坐标。  
widget_to_screen | 将控件内的本地坐标转换成屏幕上的坐标。  
widget_to_screen_ex | 将控件内的本地坐标根据祖父级控件转换成相对于祖父级控件的屏幕相对坐标。  
widget_to_xml | 将widget转换成xml。  
widget_ungrab | 让指定子控件放弃抓住事件。  
widget_unload_asset | 卸载资源。  
widget_unload_image | 卸载图片。  
widget_unref | 减少控件的引用计数。引用计数为0时销毁控件。  
widget_update_pointer_cursor | 更新鼠标指针。  
widget_update_style | 让控件根据自己当前状态更新style。  
widget_update_style_recursive | 让控件及子控件根据自己当前状态更新style。  
widget_use_style | 启用指定的style。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
animation | char* | 动画参数。请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)  
astyle | style_t* | Style对象。  
auto_adjust_size | bool_t | 是否根据子控件和文本自动调整控件自身大小。  
auto_created | bool_t | 是否由父控件自动创建。  
children | darray_t* | 全部子控件。  
children_layout | children_layouter_t* | 子控件布局器。请参考[控件布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)  
custom_props | tk_object_t* | 自定义属性。  
destroying | bool_t | 标识控件正在被销毁。  
dirty | bool_t | 标识控件是否需要重绘。  
dirty_rect_tolerance | uint16_t | 脏矩形超出控件本身大小的最大范围(一般不用指定)。  
emitter | emitter_t* | 事件发射器。  
enable | bool_t | 启用/禁用状态。  
feedback | bool_t | 是否启用按键音、触屏音和震动等反馈。  
floating | bool_t | 标识控件是否启用浮动布局，不受父控件的children_layout的控制。  
focusable | bool_t | 是否支持焦点停留。  
focused | bool_t | 是否得到焦点。  
h | wh_t | 高度。  
initializing | bool_t | 标识控件正在初始化。  
loading | bool_t | 标识控件正在加载。  
name | char* | 控件名字。  
need_update_style | bool_t | 标识控件是否需要update style。  
opacity | uint8_t | 不透明度(0-255)，0完全透明，255完全不透明。  
parent | widget_t* | 父控件  
pointer_cursor | char* | 鼠标光标图片名称。  
ref_count | int32_t | 引用计数，计数为0时销毁。  
self_layout | self_layouter_t* | 控件布局器。请参考[控件布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)  
sensitive | bool_t | 是否接受用户事件。  
state | char* | 控件的状态(取值参考widget_state_t)。  
style | char* | style的名称。  
text | wstr_t | 文本。用途视具体情况而定。  
tr_text | char* | 保存用于翻译的字符串。  
visible | bool_t | 是否可见。  
vt | const widget_vtable_t* | 虚函数表。  
w | wh_t | 宽度。  
with_focus_state | bool_t | 是否支持焦点状态。  
x | xy_t | x坐标(相对于父控件的x坐标)。  
y | xy_t | y坐标(相对于父控件的y坐标)。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_WILL_MOVE | event_t | 控件移动前触发。  
EVT_MOVE | event_t | 控件移动后触发。  
EVT_WILL_RESIZE | event_t | 控件调整大小前触发。  
EVT_RESIZE | event_t | 控件调整大小后触发。  
EVT_WILL_MOVE_RESIZE | event_t | 控件移动并调整大小前触发。  
EVT_MOVE_RESIZE | event_t | 控件移动并调整大小后触发。  
EVT_THEME_CHANGED | event_t | 主题变化事件。  
EVT_FOCUS | event_t | 控件得到焦点时触发。  
EVT_BLUR | event_t | 控件失去焦点时触发。  
EVT_WIDGET_ADD_CHILD | event_t | 控件加载新的子控件。  
EVT_WIDGET_REMOVE_CHILD | event_t | 控件移除子控件。  
EVT_WIDGET_WILL_RESTACK_CHILD | event_t | 控件即将调整子控件位置序数。  
在该的回调函数中返回RET_STOP停止调整动作。 |  |   
EVT_WIDGET_RESTACK_CHILD | event_t | 控件调整子控件位置序数。  
EVT_PROP_WILL_CHANGE | prop_change_event_t | 控件属性改变前触发(通过set_prop设置属性，才会触发)。  
EVT_PROP_CHANGED | prop_change_event_t | 控件属性改变后触发(通过set_prop设置属性，才会触发)。  
EVT_PAINT | paint_event_t | 控件绘制时触发。  
EVT_BEFORE_PAINT | paint_event_t | 控件绘制前触发。  
EVT_AFTER_PAINT | paint_event_t | 控件绘制完成时触发。  
EVT_PAINT_DONE | paint_event_t | 控件绘制完成时(canvas状态已经恢复)触发。  
EVT_WHEEL_BEFORE_CHILDREN | wheel_event_t | 鼠标滚轮事件，在子控件处理之前触发。  
EVT_WHEEL | wheel_event_t | 鼠标滚轮事件。  
EVT_POINTER_LEAVE | pointer_event_t | 鼠标指针离开控件时触发。  
EVT_POINTER_ENTER | pointer_event_t | 鼠标指针进入控件时触发。  
EVT_KEY_DOWN_BEFORE_CHILDREN | key_event_t | 键按下事件，在子控件处理之前触发。  
EVT_KEY_DOWN | key_event_t | 键按下事件。  
EVT_KEY_LONG_PRESS | key_event_t | 键长按事件。  
EVT_KEY_UP_BEFORE_CHILDREN | key_event_t | 键释放事件，在子控件处理之前触发。  
EVT_KEY_UP | key_event_t | 键释放事件。  
EVT_POINTER_DOWN_BEFORE_CHILDREN | pointer_event_t | 指针设备按下事件，在子控件处理之前触发。  
EVT_POINTER_DOWN | pointer_event_t | 指针设备按下事件。  
EVT_POINTER_DOWN_ABORT | pointer_event_t | 取消指针设备按下事件。  
EVT_POINTER_MOVE | pointer_event_t | 指针设备移动事件。  
EVT_POINTER_MOVE_BEFORE_CHILDREN | pointer_event_t | 指针设备移动事件，在子控件处理之前触发。  
EVT_POINTER_UP | pointer_event_t | 指针设备释放事件。  
EVT_POINTER_UP_BEFORE_CHILDREN | pointer_event_t | 指针设备释放事件，在子控件处理之前触发。  
EVT_DESTROY | event_t | 控件销毁时触发。  
  
#### widget_add_child 函数

* * *

  * 函数功能：



> 加入一个子控件。

  * 函数原型：


    
    
    ret_t widget_add_child (widget_t* widget, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
child | widget_t* | 子控件对象。  
  
#### widget_add_child_default 函数

* * *

  * 函数功能：



> 加入一个子控件默认实现(供子类调用)。

  * 函数原型：


    
    
    ret_t widget_add_child_default (widget_t* widget, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
child | widget_t* | 子控件对象。  
  
#### widget_add_idle 函数

* * *

  * 函数功能：



> 创建idle。 该idle在控件销毁时自动销毁，**idle_info_t** 的ctx为widget。 如果idle的生命周期与控件无关，请直接调用**idle_add** ，以避免不必要的内存开销。

  * 函数原型：


    
    
    uint32_t widget_add_idle (widget_t* widget, idle_func_t on_idle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle的ID，TK_INVALID_ID表示失败。  
widget | widget_t* | 控件对象。  
on_idle | idle_func_t | idle回调函数。  
  
#### widget_add_timer 函数

* * *

  * 函数功能：



> 创建定时器。 该定时器在控件销毁时自动销毁，**timer_info_t** 的ctx为widget。 如果定时器的生命周期与控件无关，请直接调用**timer_add** ，以避免不必要的内存开销。

使用示例：
    
    
    static ret_t digit_clock_on_timer(const timer_info_t* info) {
    widget_t* widget = WIDGET(info->ctx);
    
    return RET_REPEAT;
    }
    ...
    widget_add_timer(widget, digit_clock_on_timer, 1000);
    

  * 函数原型：


    
    
    uint32_t widget_add_timer (widget_t* widget, timer_func_t on_timer, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回timer的ID，TK_INVALID_ID表示失败。  
widget | widget_t* | 控件对象。  
on_timer | timer_func_t | timer回调函数。  
duration | uint32_t | 时间(毫秒)。  
  
#### widget_add_value 函数

* * *

  * 函数功能：



> 增加控件的值。 只是对widget_set_prop的包装，值的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_add_value (widget_t* widget, float_t delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
delta | float_t | 增量。  
  
#### widget_add_value_int 函数

* * *

  * 函数功能：



> 增加控件的值。 只是对widget_set_prop的包装，值的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_add_value_int (widget_t* widget, int32_t delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
delta | int32_t | 增量。  
  
#### widget_animate_value_to 函数

* * *

  * 函数功能：



> 设置控件的值(以动画形式变化到指定的值)。 只是对widget_set_prop的包装，值的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_animate_value_to (widget_t* widget, float_t value, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
value | float_t | 值。  
duration | uint32_t | 动画持续时间(毫秒)。  
  
#### widget_auto_scale_children 函数

* * *

  * 函数功能：



> 根据缩放子控件的位置和大小。

  * 函数原型：


    
    
    ret_t widget_auto_scale_children (widget_t* widget, int32_t design_w, int32_t design_h, bool_t auto_scale_children_x, bool_t auto_scale_children_y, bool_t auto_scale_children_w, bool_t auto_scale_children_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
design_w | int32_t | 设置时的宽度。  
design_h | int32_t | 设置时的高度。  
auto_scale_children_x | bool_t | 缩放子控件的x坐标。  
auto_scale_children_y | bool_t | 缩放子控件的y坐标。  
auto_scale_children_w | bool_t | 缩放子控件的宽度。  
auto_scale_children_h | bool_t | 缩放子控件的高度。  
  
#### widget_back 函数

* * *

  * 函数功能：



> 请求返回到前一个窗口。

  * 函数原型：


    
    
    ret_t widget_back (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_back_to_home 函数

* * *

  * 函数功能：



> 请求返回到home窗口。

  * 函数原型：


    
    
    ret_t widget_back_to_home (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_begin_wait_pointer_cursor 函数

* * *

  * 函数功能：



> 开始等待鼠标指针。

  * 函数原型：


    
    
    ret_t widget_begin_wait_pointer_cursor (widget_t* widget, bool_t ignore_user_input);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
ignore_user_input | bool_t | 是否忽略用户输入。  
  
#### widget_calc_icon_text_rect 函数

* * *

  * 函数功能：



> 计算icon text的位置。

  * 函数原型：


    
    
    ret_t widget_calc_icon_text_rect (const rect_t* ir, int32_t font_size, float_t text_size, int32_t icon_at, uint32_t img_w, uint32_t img_h, int32_t spacer, rect_t* r_text, rect_t* r_icon);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ir | const rect_t* | ir。  
font_size | int32_t | 字体大小。  
text_size | float_t | 文本大小。  
icon_at | int32_t | icon的位置。  
img_w | uint32_t | 图像宽度。  
img_h | uint32_t | 图像高度。  
spacer | int32_t | 间距。  
r_text | rect_t* | 返回文本的矩形区域。  
r_icon | rect_t* | 返回icon的矩形区域。  
  
#### widget_cast 函数

* * *

  * 函数功能：



> 转换为widget对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* widget_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | widget对象。  
widget | widget_t* | widget对象。  
  
#### widget_child 函数

* * *

  * 函数功能：



> 查找指定名称的子控件(同widget_lookup(widget, name, FALSE))。

  * 函数原型：


    
    
    widget_t* widget_child (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 子控件或NULL。  
widget | widget_t* | 控件对象。  
name | const char* | 子控件的名称。  
  
#### widget_child_on 函数

* * *

  * 函数功能：



> 为指定名称的子控件注册指定事件的处理函数。 递归查找指定名称的子控件，然后为其注册指定事件的处理函数。

  * 函数原型：


    
    
    uint32_t widget_child_on (widget_t* widget, const char* name, uint32_t type, event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于widget_off。  
widget | widget_t* | 控件对象。  
name | const char* | 子控件的名称。  
type | uint32_t | 事件类型。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### widget_clone 函数

* * *

  * 函数功能：



> clone。

  * 函数原型：


    
    
    widget_t* widget_clone (widget_t* widget, widget_t* parent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回clone的对象。  
widget | widget_t* | 控件对象。  
parent | widget_t* | clone新控件的parent对象。  
  
#### widget_close_window 函数

* * *

  * 函数功能：



> 关闭控件所在的窗口。

  * 函数原型：


    
    
    ret_t widget_close_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_close_window_force 函数

* * *

  * 函数功能：



> 关闭控件所在的窗口。

  * 函数原型：


    
    
    ret_t widget_close_window_force (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_count_children 函数

* * *

  * 函数功能：



> 获取子控件的个数。

  * 函数原型：


    
    
    int32_t widget_count_children (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 子控件的个数。  
widget | widget_t* | 控件对象。  
  
#### widget_create 函数

* * *

  * 函数功能：



> 创建控件。仅在子类控件构造函数中使用。

  * 函数原型：


    
    
    widget_t* widget_create (widget_t* parent, const widget_vtable_t* vt, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | widget对象本身。  
parent | widget_t* | widget的父控件。  
vt | const widget_vtable_t* | 虚表。  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### widget_create_animator 函数

* * *

  * 函数功能：



> 创建动画。 请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

  * 除非指定auto_start=false，动画创建后自动启动。
  * 除非指定auto_destroy=false，动画播放完成后自动销毁。

  * 函数原型：



    
    
    ret_t widget_create_animator (widget_t* widget, const char* animation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
animation | const char* | 动画参数。  
  
#### widget_destroy 函数

* * *

  * 函数功能：



> 从父控件中移除控件，并调用unref函数销毁控件。
> 
> 一般无需直接调用，关闭窗口时，自动销毁相关控件。

  * 函数原型：


    
    
    ret_t widget_destroy (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_destroy_animator 函数

* * *

  * 函数功能：



> 销毁动画。 请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

  * 1.widget为NULL时，销毁所有名称为name的动画。
  * 2.name为NULL时，销毁所有widget相关的动画。
  * 3.widget和name均为NULL，销毁所有动画。

  * 函数原型：



    
    
    ret_t widget_destroy_animator (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_destroy_async 函数

* * *

  * 函数功能：



> 从父控件中移除控件，并调用unref函数销毁控件。
> 
> 一般无需直接调用，关闭窗口时，自动销毁相关控件。

  * 函数原型：


    
    
    ret_t widget_destroy_async (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_destroy_children 函数

* * *

  * 函数功能：



> 销毁全部子控件。

  * 函数原型：


    
    
    ret_t widget_destroy_children (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_dispatch 函数

* * *

  * 函数功能：



> 分发一个事件。

  * 函数原型：


    
    
    ret_t widget_dispatch (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | event_t* | 事件。  
  
#### widget_dispatch_async 函数

* * *

  * 函数功能：



> 异步分发一个事件。

  * 函数原型：


    
    
    ret_t widget_dispatch_async (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | event_t* | 事件。  
  
#### widget_dispatch_event_to_target_recursive 函数

* * *

  * 函数功能：



> 递归分发事件到targe控件。

  * 函数原型：


    
    
    ret_t widget_dispatch_event_to_target_recursive (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | event_t* | 事件对象。  
  
#### widget_dispatch_model_event 函数

* * *

  * 函数功能：



> 分发model事件(分发到各个窗口)。

  * 函数原型：


    
    
    ret_t widget_dispatch_model_event (widget_t* widget, const char* name, const char* change_type, tk_object_t* model);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 名称。  
change_type | const char* | 变化类型。  
model | tk_object_t* | 模型。  
  
#### widget_dispatch_recursive 函数

* * *

  * 函数功能：



> 分发一个事件控件本身及所有子控件。

  * 函数原型：


    
    
    ret_t widget_dispatch_recursive (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | event_t* | 事件。  
  
#### widget_dispatch_simple_event 函数

* * *

  * 函数功能：



> 分发一个简单事件。

  * 函数原型：


    
    
    ret_t widget_dispatch_simple_event (widget_t* widget, uint32_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
type | uint32_t | 事件类型。  
  
#### widget_dispatch_to_key_target 函数

* * *

  * 函数功能：



> 递归的分发一个事件到所有key_target子控件。

  * 函数原型：


    
    
    ret_t widget_dispatch_to_key_target (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | event_t* | 事件。  
  
#### widget_dispatch_to_target 函数

* * *

  * 函数功能：



> 递归的分发一个事件到所有target子控件。

  * 函数原型：


    
    
    ret_t widget_dispatch_to_target (widget_t* widget, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | event_t* | 事件。  
  
#### widget_draw_arc_at_center 函数

* * *

  * 函数功能：



> 以控件中心为中心绘制圆弧。

  * 函数原型：


    
    
    ret_t widget_draw_arc_at_center (widget_t* widget, canvas_t* c, bool_t bg, double line_width, double start_angle, double end_angle, bool_t counter_clock_wise, const char* line_cap, double r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
bg | bool_t | 是否是背景。  
line_width | double | 线宽。  
start_angle | double | 开始角度。  
end_angle | double | 结束角度。  
counter_clock_wise | bool_t | 是否是逆时针。  
line_cap | const char* | 线帽。  
r | double | 半径。  
  
#### widget_draw_background 函数

* * *

  * 函数功能：



> 根据控件的style绘制背景矩形。

  * 函数原型：


    
    
    ret_t widget_draw_background (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
  
#### widget_draw_text_in_rect 函数

* * *

  * 函数功能：



> 在canvas绘制一行文本。

  * 函数原型：


    
    
    ret_t widget_draw_text_in_rect (widget_t* widget, canvas_t* c, const wchar_t* str, uint32_t size, const rect_t* r, bool_t ellipses);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
str | const wchar_t* | 文本。  
size | uint32_t | 文本长度。  
r | const rect_t* | 矩形区域。  
ellipses | bool_t | 宽度不够时是否显示省略号。  
  
#### widget_end_wait_pointer_cursor 函数

* * *

  * 函数功能：



> 结束等待鼠标指针。

  * 函数原型：


    
    
    ret_t widget_end_wait_pointer_cursor (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_ensure_visible_in_viewport 函数

* * *

  * 函数功能：



> 使控件滚动到可见区域。

  * 函数原型：


    
    
    ret_t widget_ensure_visible_in_viewport (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回。  
widget | widget_t* | 控件对象。  
  
#### widget_equal 函数

* * *

  * 函数功能：



> 判断两个widget是否相同。

  * 函数原型：


    
    
    bool_t widget_equal (widget_t* widget, widget_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示相同，否则表示不同。  
widget | widget_t* | 控件对象。  
other | widget_t* | 要比较的控件对象。  
  
#### widget_fill_bg_rect 函数

* * *

  * 函数功能：



> 根据控件的style绘制背景矩形。

  * 函数原型：


    
    
    ret_t widget_fill_bg_rect (widget_t* widget, canvas_t* c, const rect_t* r, image_draw_type_t draw_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
r | const rect_t* | 矩形区域。  
draw_type | image_draw_type_t | 图片缺省绘制方式。  
  
#### widget_fill_fg_rect 函数

* * *

  * 函数功能：



> 根据控件的style绘制前景矩形。

  * 函数原型：


    
    
    ret_t widget_fill_fg_rect (widget_t* widget, canvas_t* c, const rect_t* r, image_draw_type_t draw_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
r | const rect_t* | 矩形区域。  
draw_type | image_draw_type_t | 图片缺省绘制方式。  
  
#### widget_find_animator 函数

* * *

  * 函数功能：



> 查找指定名称的动画。

  * 函数原型：


    
    
    widget_animator_t* widget_find_animator (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_t* | 成功返回动画对象，失败返回NULL。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_find_parent_by_name 函数

* * *

  * 函数功能：



> 通过名称查找父控件。

  * 函数原型：


    
    
    widget_t* widget_find_parent_by_name (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 父控件。  
widget | widget_t* | 控件对象。  
name | const char* | 名称。  
  
#### widget_find_parent_by_type 函数

* * *

  * 函数功能：



> 通过类型查找父控件。

  * 函数原型：


    
    
    widget_t* widget_find_parent_by_type (widget_t* widget, const char* type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 父控件。  
widget | widget_t* | 控件对象。  
type | const char* | 类型。  
  
#### widget_find_target 函数

* * *

  * 函数功能：



> 查找x/y坐标对应的子控件。

  * 函数原型：


    
    
    widget_t* widget_find_target (widget_t* widget, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 子控件或NULL。  
widget | widget_t* | 控件对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### widget_focus_first 函数

* * *

  * 函数功能：



> 置焦点于第一个控件。

  * 函数原型：


    
    
    ret_t widget_focus_first (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_focus_next 函数

* * *

  * 函数功能：



> 把焦点移动下一个控件。
> 
> widget必须是当前焦点控件。

  * 函数原型：


    
    
    ret_t widget_focus_next (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_focus_prev 函数

* * *

  * 函数功能：



> 把焦点移动前一个控件。
> 
> widget必须是当前焦点控件。

  * 函数原型：


    
    
    ret_t widget_focus_prev (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_foreach 函数

* * *

  * 函数功能：



> 遍历当前控件及子控件。

  * 函数原型：


    
    
    ret_t widget_foreach (widget_t* widget, tk_visit_t visit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
visit | tk_visit_t | 遍历的回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### widget_get_assets_manager 函数

* * *

  * 函数功能：



> 获取assets_manager对象。

  * 函数原型：


    
    
    assets_manager_t* widget_get_assets_manager (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | assets_manager_t* | 返回assets_manager对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_auto_adjust_size 函数

* * *

  * 函数功能：



> 获取控件auto_adjust_size属性值。

  * 函数原型：


    
    
    bool_t widget_get_auto_adjust_size (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回auto_adjust_size。  
widget | widget_t* | 控件对象。  
  
#### widget_get_canvas 函数

* * *

  * 函数功能：



> 获取canvas对象。

  * 函数原型：


    
    
    canvas_t* widget_get_canvas (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | canvas_t* | 返回canvas对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_child 函数

* * *

  * 函数功能：



> 获取指定索引的子控件。

  * 函数原型：


    
    
    widget_t* widget_get_child (widget_t* widget, int32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 子控件。  
widget | widget_t* | 控件对象。  
index | int32_t | 索引。  
  
#### widget_get_child_text_utf8 函数

* * *

  * 函数功能：



> 获取子控件的文本。 只是对widget_get_prop的包装，文本的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_get_child_text_utf8 (widget_t* widget, const char* name, char* text, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 子控件的名称。  
text | char* | 用于返回文本。  
size | uint32_t | text内存长度。  
  
#### widget_get_content_area 函数

* * *

  * 函数功能：



> 获取widget去掉margin之外的区域。

  * 函数原型：


    
    
    rect_t widget_get_content_area (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t | 返回去掉margin之外的区域。  
widget | widget_t* | 控件对象。  
  
#### widget_get_enable 函数

* * *

  * 函数功能：



> 获取控件enable属性值。

  * 函数原型：


    
    
    bool_t widget_get_enable (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回enable。  
widget | widget_t* | 控件对象。  
  
#### widget_get_feedback 函数

* * *

  * 函数功能：



> 获取控件feedback属性值。

  * 函数原型：


    
    
    bool_t widget_get_feedback (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回feedback。  
widget | widget_t* | 控件对象。  
  
#### widget_get_floating 函数

* * *

  * 函数功能：



> 获取控件floating属性值。

  * 函数原型：


    
    
    bool_t widget_get_floating (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回floating。  
widget | widget_t* | 控件对象。  
  
#### widget_get_focusable 函数

* * *

  * 函数功能：



> 获取控件focusable属性值。

  * 函数原型：


    
    
    bool_t widget_get_focusable (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回focusable。  
widget | widget_t* | 控件对象。  
  
#### widget_get_focused_widget 函数

* * *

  * 函数功能：



> 获取当前窗口中的焦点控件。

  * 函数原型：


    
    
    widget_t* widget_get_focused_widget (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 焦点控件。  
widget | widget_t* | 控件对象。  
  
#### widget_get_font_manager 函数

* * *

  * 函数功能：



> 获取font_manager对象。

  * 函数原型：


    
    
    font_manager_t* widget_get_font_manager (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | font_manager_t* | 返回font_manager对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_image_manager 函数

* * *

  * 函数功能：



> 获取image_manager对象。

  * 函数原型：


    
    
    image_manager_t* widget_get_image_manager (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | image_manager_t* | 返回image_manager对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_locale_info 函数

* * *

  * 函数功能：



> 获取locale_info对象。

  * 函数原型：


    
    
    locale_info_t* widget_get_locale_info (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | locale_info_t* | 返回locale_info对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_native_window 函数

* * *

  * 函数功能：



> 获取原生窗口对象。

  * 函数原型：


    
    
    native_window_t* widget_get_native_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | native_window_t* | 原生窗口对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_prop 函数

* * *

  * 函数功能：



> 获取控件指定属性的值。

  * 函数原型：


    
    
    ret_t widget_get_prop (widget_t* widget, const char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | value_t* | 返回属性的值。  
  
#### widget_get_prop_bool 函数

* * *

  * 函数功能：



> 获取布尔格式的属性。

  * 函数原型：


    
    
    bool_t widget_get_prop_bool (widget_t* widget, const char* name, bool_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回属性的值。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
defval | bool_t | 缺省值。  
  
#### widget_get_prop_default_value 函数

* * *

  * 函数功能：



> 获取控件指定属性的缺省值(在持久化控件时，无需保存缺省值)。

  * 函数原型：


    
    
    ret_t widget_get_prop_default_value (widget_t* widget, const char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | value_t* | 返回属性的缺省值。  
  
#### widget_get_prop_float 函数

* * *

  * 函数功能：



> 获取浮点数格式的属性。

  * 函数原型：


    
    
    float_t widget_get_prop_float (widget_t* widget, const char* name, float_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回属性的值。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
defval | float_t | 缺省值。  
  
#### widget_get_prop_int 函数

* * *

  * 函数功能：



> 获取整数格式的属性。

  * 函数原型：


    
    
    int32_t widget_get_prop_int (widget_t* widget, const char* name, int32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回属性的值。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
defval | int32_t | 缺省值。  
  
#### widget_get_prop_pointer 函数

* * *

  * 函数功能：



> 获取指针格式的属性。

  * 函数原型：


    
    
    void* widget_get_prop_pointer (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回属性的值。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
  
#### widget_get_prop_str 函数

* * *

  * 函数功能：



> 获取字符串格式的属性。

  * 函数原型：


    
    
    const char* widget_get_prop_str (widget_t* widget, const char* name, const char* defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回属性的值。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
defval | const char* | 缺省值。  
  
#### widget_get_sensitive 函数

* * *

  * 函数功能：



> 获取控件sensitive属性值。

  * 函数原型：


    
    
    bool_t widget_get_sensitive (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回sensitive。  
widget | widget_t* | 控件对象。  
  
#### widget_get_state_for_style 函数

* * *

  * 函数功能：



> 把控件的状态转成获取style选要的状态，一般只在子类中使用。

  * 函数原型：


    
    
    const char* widget_get_state_for_style (widget_t* widget, bool_t active, bool_t checked);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回状态值。  
widget | widget_t* | widget对象。  
active | bool_t | 控件是否为当前项。  
checked | bool_t | 控件是否为选中项。  
  
#### widget_get_style 函数

* * *

  * 函数功能：



> 获取widget样式。

  * 函数原型：


    
    
    ret_t widget_get_style (widget_t* widget, const char* state_and_name, value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
state_and_name | const char* | 样式对应类型与名字。  
value | value_t* | 返回样式数据值。  
  
#### widget_get_style_type 函数

* * *

  * 函数功能：



> 获取 widget 对应风格类型

  * 函数原型：


    
    
    const char* widget_get_style_type (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回 widget 的对应风格类型。  
widget | widget_t* | widget对象。  
  
#### widget_get_text 函数

* * *

  * 函数功能：



> 获取控件的文本。 只是对widget_get_prop的包装，文本的意义由子类控件决定。

如果希望获取UTF8格式的文本，可以参考下面的代码：
    
    
    str_t str;
    str_init(&str, 0);
    str_from_wstr(&str, widget_get_text(target));
    log_debug("%s: %s\n", target->name, str.str);
    str_reset(&str);
    

  * 函数原型：


    
    
    const wchar_t* widget_get_text (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const wchar_t* | 返回文本。  
widget | widget_t* | 控件对象。  
  
#### widget_get_text_utf8 函数

* * *

  * 函数功能：



> 获取控件的文本。 只是对widget_get_prop的包装，文本的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_get_text_utf8 (widget_t* widget, char* text, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
text | char* | 用于返回文本。  
size | uint32_t | text内存长度。  
  
#### widget_get_theme_name 函数

* * *

  * 函数功能：



> 获取 theme 的名称

  * 函数原型：


    
    
    const char* widget_get_theme_name (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 成功返回主题名称，失败否则 NULL。  
widget | widget_t* | 控件对象。  
  
#### widget_get_type 函数

* * *

  * 函数功能：



> 获取当前控件的类型名称。

  * 函数原型：


    
    
    const char* widget_get_type (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回类型名。  
widget | widget_t* | 控件对象。  
  
#### widget_get_value 函数

* * *

  * 函数功能：



> 获取控件的值。只是对widget_get_prop的包装，值的意义由子类控件决定。

  * 函数原型：


    
    
    float_t widget_get_value (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回值。  
widget | widget_t* | 控件对象。  
  
#### widget_get_value_int 函数

* * *

  * 函数功能：



> 获取控件的值。只是对widget_get_prop的包装，值的意义由子类控件决定。

  * 函数原型：


    
    
    int32_t widget_get_value_int (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回值。  
widget | widget_t* | 控件对象。  
  
#### widget_get_visible 函数

* * *

  * 函数功能：



> 获取控件visible属性值。

  * 函数原型：


    
    
    bool_t widget_get_visible (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回visible。  
widget | widget_t* | 控件对象。  
  
#### widget_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 widget 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* widget_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 widget 虚表。  
  
#### widget_get_window 函数

* * *

  * 函数功能：



> 获取当前控件所在的窗口。

  * 函数原型：


    
    
    widget_t* widget_get_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 窗口对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_window_manager 函数

* * *

  * 函数功能：



> 获取当前的窗口管理器。

  * 函数原型：


    
    
    widget_t* widget_get_window_manager (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 窗口管理器对象。  
widget | widget_t* | 控件对象。  
  
#### widget_get_window_theme 函数

* * *

  * 函数功能：



> 获取控件的窗体样式。

  * 函数原型：


    
    
    ret_t widget_get_window_theme (widget_t* widget, theme_t** win_theme, theme_t** default_theme);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
win_theme | theme_t** | 返回窗体样式。  
default_theme | theme_t** | 返回全局默认窗体样式。  
  
#### widget_get_with_focus_state 函数

* * *

  * 函数功能：



> 获取控件with_focus_state属性值。

  * 函数原型：


    
    
    bool_t widget_get_with_focus_state (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回with_focus_state。  
widget | widget_t* | 控件对象。  
  
#### widget_grab 函数

* * *

  * 函数功能：



> 让指定子控件抓住事件。 控件抓住之后，事件直接分发给该控件。

  * 函数原型：


    
    
    ret_t widget_grab (widget_t* widget, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
child | widget_t* | 子控件对象。  
  
#### widget_has_highlighter 函数

* * *

  * 函数功能：



> 判断widget拥有高亮属性。

  * 函数原型：


    
    
    bool_t widget_has_highlighter (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 拥有返回 TRUE，没有返回 FALSE。  
widget | widget_t* | 控件对象。  
  
#### widget_index_of 函数

* * *

  * 函数功能：



> 获取控件在父控件中的索引编号。

  * 函数原型：


    
    
    int32_t widget_index_of (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 在父控件中的索引编号。  
widget | widget_t* | 控件对象。  
  
#### widget_init 函数

* * *

  * 函数功能：



> 初始化控件。仅在子类控件构造函数中使用。
> 
> 请用widget_create代替本函数。

@depreated

  * 函数原型：


    
    
    widget_t* widget_init (widget_t* widget, widget_t* parent, const widget_vtable_t* vt, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | widget对象本身。  
widget | widget_t* | widget对象。  
parent | widget_t* | widget的父控件。  
vt | const widget_vtable_t* | 虚表。  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### widget_insert_child 函数

* * *

  * 函数功能：



> 插入子控件到指定的位置。

  * 函数原型：


    
    
    ret_t widget_insert_child (widget_t* widget, uint32_t index, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
index | uint32_t | 位置序数(大于等于总个数，则放到最后)。  
child | widget_t* | 子控件对象。  
  
#### widget_invalidate 函数

* * *

  * 函数功能：



> 请求重绘指定的区域

备注： 1，函数执行成功后，会把 widget->dirty 修改为 TRUE，如果 widget->dirty 已经为 TRUE，则直接返回 RET_OK，不再增加重绘区。 2，当控件执行 widget_paint 后会把 widget->dirty 修改为 FALSE。 3，如果同一个控件在同一帧内多次请求重绘不同区域的话，请使用 widget_invalidate_force。

  * 函数原型：


    
    
    ret_t widget_invalidate (widget_t* widget, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
r | const rect_t* | 矩形对象(widget本地坐标)。  
  
#### widget_invalidate_force 函数

* * *

  * 函数功能：



> 请求强制重绘控件。

  * 函数原型：


    
    
    ret_t widget_invalidate_force (widget_t* widget, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
r | const rect_t* | 矩形对象(widget本地坐标)。  
  
#### widget_is_always_on_top 函数

* * *

  * 函数功能：



> 检查控件是否总在最上层。

  * 函数原型：


    
    
    bool_t widget_is_always_on_top (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_change_focus_key 函数

* * *

  * 函数功能：



> 是否是切换焦点的键。

  * 函数原型：


    
    
    bool_t widget_is_change_focus_key (widget_t* widget, key_event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示否。  
widget | widget_t* | 控件对象。  
e | key_event_t* | 事件对象。  
  
#### widget_is_designing_window 函数

* * *

  * 函数功能：



> 判断当前控件是否是设计窗口。

  * 函数原型：


    
    
    bool_t widget_is_designing_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回当前控件是否是设计窗口。  
widget | widget_t* | 控件对象。  
  
#### widget_is_dialog 函数

* * *

  * 函数功能：



> 检查控件是否是对话框类型。

  * 函数原型：


    
    
    bool_t widget_is_dialog (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_direct_parent_of 函数

* * *

  * 函数功能：



> 判断当前控件是否是指定控件的直系父控件。

  * 函数原型：


    
    
    bool_t widget_is_direct_parent_of (widget_t* widget, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示不是。  
widget | widget_t* | 控件对象。  
child | widget_t* | 控件对象。  
  
#### widget_is_fullscreen_window 函数

* * *

  * 函数功能：



> 检查控件是否是全屏窗口。

  * 函数原型：


    
    
    bool_t widget_is_fullscreen_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_instance_of 函数

* * *

  * 函数功能：



> 检查控件是否是指定的类型。

  * 函数原型：


    
    
    bool_t widget_is_instance_of (widget_t* widget, const widget_vtable_t* vt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，FALSE表示否。  
widget | widget_t* | 控件对象。  
vt | const widget_vtable_t* | 虚表。  
  
#### widget_is_keyboard 函数

* * *

  * 函数功能：



> 判断当前控件是否是keyboard。
> 
> keyboard收到pointer事件时，不会让当前控件失去焦点。

在自定义软键盘时，将所有按钮放到一个容器当中，并设置为is_keyboard。
    
    
    widget_set_prop_bool(group, WIDGET_PROP_IS_KEYBOARD, TRUE);
    

  * 函数原型：


    
    
    bool_t widget_is_keyboard (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | 控件对象。  
  
#### widget_is_normal_window 函数

* * *

  * 函数功能：



> 检查控件是否是普通窗口类型。

  * 函数原型：


    
    
    bool_t widget_is_normal_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_opened_dialog 函数

* * *

  * 函数功能：



> 检查控件弹出对话框控件是否已经打开了（而非挂起状态）。

  * 函数原型：


    
    
    bool_t widget_is_opened_dialog (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_opened_popup 函数

* * *

  * 函数功能：



> 检查控件弹出窗口控件是否已经打开了（而非挂起状态）。

  * 函数原型：


    
    
    bool_t widget_is_opened_popup (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_overlay 函数

* * *

  * 函数功能：



> 检查控件是否是overlay窗口类型。

  * 函数原型：


    
    
    bool_t widget_is_overlay (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_parent_of 函数

* * *

  * 函数功能：



> 判断当前控件是否是指定控件的父控件(包括非直系)。

  * 函数原型：


    
    
    bool_t widget_is_parent_of (widget_t* widget, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示不是。  
widget | widget_t* | 控件对象。  
child | widget_t* | 控件对象。  
  
#### widget_is_point_in 函数

* * *

  * 函数功能：



> 判断一个点是否在控件内。

  * 函数原型：


    
    
    bool_t widget_is_point_in (widget_t* widget, xy_t x, xy_t y, bool_t is_local);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
x | xy_t | x坐标  
y | xy_t | y坐标  
is_local | bool_t | TRUE表示是相对与控件左上角的坐标，否则表示全局坐标。  
  
#### widget_is_popup 函数

* * *

  * 函数功能：



> 检查控件是否是弹出窗口类型。

  * 函数原型：


    
    
    bool_t widget_is_popup (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_style_exist 函数

* * *

  * 函数功能：



> 查询指定的style是否存在。

  * 函数原型：


    
    
    bool_t widget_is_style_exist (widget_t* widget, const char* style_name, const char* state_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 存在返回 TRUE，不存在返回 FALSE。  
widget | widget_t* | 控件对象。  
style_name | const char* | style的名称（如果为 NULL，则默认为 default）。  
state_name | const char* | state的名称（如果为 NULL，则默认为 normal）。  
  
#### widget_is_support_highlighter 函数

* * *

  * 函数功能：



> 判断widget是否支持高亮。

  * 函数原型：


    
    
    bool_t widget_is_support_highlighter (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 支持返回 TRUE，不支持返回 FALSE。  
widget | widget_t* | 控件对象。  
  
#### widget_is_system_bar 函数

* * *

  * 函数功能：



> 检查控件是否是system bar类型。

  * 函数原型：


    
    
    bool_t widget_is_system_bar (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回FALSE表示不是，否则表示是。  
widget | widget_t* | widget对象。  
  
#### widget_is_window 函数

* * *

  * 函数功能：



> 判断当前控件是否是窗口。

  * 函数原型：


    
    
    bool_t widget_is_window (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回当前控件是否是窗口。  
widget | widget_t* | 控件对象。  
  
#### widget_is_window_created 函数

* * *

  * 函数功能：



> 判断窗口及子控件创建或加载是否完成。

  * 函数原型：


    
    
    bool_t widget_is_window_created (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回创建或加载是否完成。  
widget | widget_t* | 控件对象。  
  
#### widget_is_window_manager 函数

* * *

  * 函数功能：



> 判断当前控件是否是窗口管理器。

  * 函数原型：


    
    
    bool_t widget_is_window_manager (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回当前控件是否是窗口管理器。  
widget | widget_t* | 控件对象。  
  
#### widget_is_window_opened 函数

* * *

  * 函数功能：



> 判断当前控件所在的窗口是否已经打开。

  * 函数原型：


    
    
    bool_t widget_is_window_opened (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回当前控件所在的窗口是否已经打开。  
widget | widget_t* | 控件对象。  
  
#### widget_layout 函数

* * *

  * 函数功能：



> 布局当前控件及子控件。

  * 函数原型：


    
    
    ret_t widget_layout (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_layout_children 函数

* * *

  * 函数功能：



> layout子控件。

  * 函数原型：


    
    
    ret_t widget_layout_children (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_load_asset 函数

* * *

  * 函数功能：



> 加载资源。

使用示例：
    
    
    const asset_info_t* asset = widget_load_asset(widget, ASSET_TYPE_IMAGE, "mysvg");
    ...
    widget_unload_asset(widget, asset);
    

  * 函数原型：


    
    
    const asset_info_t* widget_load_asset (widget_t* widget, asset_type_t type, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const asset_info_t* | 返回资源句柄。  
widget | widget_t* | 控件对象。  
type | asset_type_t | 资源类型。  
name | const char* | 资源名。  
  
#### widget_load_asset_ex 函数

* * *

  * 函数功能：



> 加载资源。

使用示例：
    
    
    const asset_info_t* asset = widget_load_asset_ex(widget, ASSET_TYPE_IMAGE, ASSET_TYPE_IMAGE_BSVG, "mysvg");
    ...
    widget_unload_asset(widget, asset);
    

  * 函数原型：


    
    
    const asset_info_t* widget_load_asset_ex (widget_t* widget, asset_type_t type, uint16_t subtype, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const asset_info_t* | 返回资源句柄。  
widget | widget_t* | 控件对象。  
type | asset_type_t | 资源类型。  
subtype | uint16_t | 资源子类型。  
name | const char* | 资源名。  
  
#### widget_load_image 函数

* * *

  * 函数功能：



> 加载图片。 返回的bitmap对象只在当前调用有效，请不保存对bitmap对象的引用。

使用示例：
    
    
    bitmap_t bitmap;
    widget_load_image(widget, "myimage", &bitmap);
    

  * 函数原型：


    
    
    ret_t widget_load_image (widget_t* widget, const char* name, bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 图片名(不带扩展名)。  
bitmap | bitmap_t* | 返回图片对象。  
  
#### widget_lookup 函数

* * *

  * 函数功能：



> 查找指定名称的子控件(返回第一个)。

  * 函数原型：


    
    
    widget_t* widget_lookup (widget_t* widget, const char* name, bool_t recursive);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 子控件或NULL。  
widget | widget_t* | 控件对象。  
name | const char* | 子控件的名称。  
recursive | bool_t | 是否递归查找全部子控件。  
  
#### widget_lookup_by_type 函数

* * *

  * 函数功能：



> 查找指定类型的子控件(返回第一个)。

  * 函数原型：


    
    
    widget_t* widget_lookup_by_type (widget_t* widget, const char* type, bool_t recursive);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 子控件或NULL。  
widget | widget_t* | 控件对象。  
type | const char* | 子控件的名称。  
recursive | bool_t | 是否递归查找全部子控件。  
  
#### widget_measure_text 函数

* * *

  * 函数功能：



> 计算文本的宽度。 字体由控件当前的状态和style决定。

  * 函数原型：


    
    
    float_t widget_measure_text (widget_t* widget, const wchar_t* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回文本的宽度。  
widget | widget_t* | 控件对象。  
text | const wchar_t* | 文本。  
  
#### widget_move 函数

* * *

  * 函数功能：



> 移动控件。

  * 函数原型：


    
    
    ret_t widget_move (widget_t* widget, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
x | xy_t | x坐标  
y | xy_t | y坐标  
  
#### widget_move_resize 函数

* * *

  * 函数功能：



> 移动控件并调整控件的大小。

  * 函数原型：


    
    
    ret_t widget_move_resize (widget_t* widget, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### widget_move_resize_ex 函数

* * *

  * 函数功能：



> 移动控件并调整控件的大小。

  * 函数原型：


    
    
    ret_t widget_move_resize_ex (widget_t* widget, xy_t x, xy_t y, wh_t w, wh_t h, bool_t update_layout);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
update_layout | bool_t | 是否更新布局  
  
#### widget_move_to_center 函数

* * *

  * 函数功能：



> 移动控件到父控件中间。

  * 函数原型：


    
    
    ret_t widget_move_to_center (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_off 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t widget_off (widget_t* widget, uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
id | uint32_t | widget_on返回的ID。  
  
#### widget_off_by_ctx 函数

* * *

  * 函数功能：



> 注销指定ctx的事件处理函数。

  * 函数原型：


    
    
    ret_t widget_off_by_ctx (widget_t* widget, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
ctx | void* | 事件处理函数上下文。  
  
#### widget_off_by_func 函数

* * *

  * 函数功能：



> 注销指定函数的事件处理函数。

  * 函数原型：


    
    
    ret_t widget_off_by_func (widget_t* widget, uint32_t type, event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
type | uint32_t | 事件类型。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### widget_off_by_tag 函数

* * *

  * 函数功能：



> 注销指定tag的事件处理函数。

  * 函数原型：


    
    
    ret_t widget_off_by_tag (widget_t* widget, uint32_t tag);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
tag | uint32_t | tag。  
  
#### widget_on 函数

* * *

  * 函数功能：



> 注册指定事件的处理函数。 使用示例：
    
    
    widget_t* ok = button_create(win, 10, 10, 80, 30);
    widget_on(ok, EVT_CLICK, on_click, NULL);
    

  * 函数原型：


    
    
    uint32_t widget_on (widget_t* widget, uint32_t type, event_func_t on_event, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于widget_off。  
widget | widget_t* | 控件对象。  
type | uint32_t | 事件类型。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### widget_on_keydown 函数

* * *

  * 函数功能：



> 处理key down事件。

  * 函数原型：


    
    
    ret_t widget_on_keydown (widget_t* widget, key_event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | key_event_t* | 事件对象。  
  
#### widget_on_keyup 函数

* * *

  * 函数功能：



> 处理key up事件。

  * 函数原型：


    
    
    ret_t widget_on_keyup (widget_t* widget, key_event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | key_event_t* | 事件对象。  
  
#### widget_on_paint_background 函数

* * *

  * 函数功能：



> 绘制背景。

  * 函数原型：


    
    
    ret_t widget_on_paint_background (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回。  
widget | widget_t* | 控件对象。  
c | canvas_t* | canvas对象。  
  
#### widget_on_paint_border 函数

* * *

  * 函数功能：



> 绘制边框。

  * 函数原型：


    
    
    ret_t widget_on_paint_border (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回。  
widget | widget_t* | 控件对象。  
c | canvas_t* | canvas对象。  
  
#### widget_on_paint_children 函数

* * *

  * 函数功能：



> 绘制子控件。

  * 函数原型：


    
    
    ret_t widget_on_paint_children (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回。  
widget | widget_t* | 控件对象。  
c | canvas_t* | canvas对象。  
  
#### widget_on_paint_self 函数

* * *

  * 函数功能：



> 绘制自身。

  * 函数原型：


    
    
    ret_t widget_on_paint_self (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回。  
widget | widget_t* | 控件对象。  
c | canvas_t* | canvas对象。  
  
#### widget_on_pointer_down_children 函数

* * *

  * 函数功能：



> 处理子控件的pointer down事件。

  * 函数原型：


    
    
    ret_t widget_on_pointer_down_children (widget_t* widget, pointer_event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | pointer_event_t* | 事件对象。  
  
#### widget_on_pointer_move_children 函数

* * *

  * 函数功能：



> 处理子控件的pointer move事件。

  * 函数原型：


    
    
    ret_t widget_on_pointer_move_children (widget_t* widget, pointer_event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | pointer_event_t* | 事件对象。  
  
#### widget_on_pointer_up_children 函数

* * *

  * 函数功能：



> 处理子控件的pointer up事件。

  * 函数原型：


    
    
    ret_t widget_on_pointer_up_children (widget_t* widget, pointer_event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
e | pointer_event_t* | 事件对象。  
  
#### widget_on_with_tag 函数

* * *

  * 函数功能：



> 注册指定tag的事件处理函数。
> 
> 注册时指定一个tag，可用widget_off_by_tag注销相同tag的事件处理函数。

  * 函数原型：


    
    
    uint32_t widget_on_with_tag (widget_t* widget, uint32_t type, event_func_t on_event, void* ctx, uint32_t tag);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于widget_off。  
widget | widget_t* | 控件对象。  
type | uint32_t | 事件类型。  
on_event | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
tag | uint32_t | tag。  
  
#### widget_paint 函数

* * *

  * 函数功能：



> 绘制控件到一个canvas上。

  * 函数原型：


    
    
    ret_t widget_paint (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
  
#### widget_paint_helper 函数

* * *

  * 函数功能：



> 帮助子控件实现自己的绘制函数。

  * 函数原型：


    
    
    ret_t widget_paint_helper (widget_t* widget, canvas_t* c, const char* icon, wstr_t* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
icon | const char* | 图标的名称。  
text | wstr_t* | 文字。  
  
#### widget_pause_animator 函数

* * *

  * 函数功能：



> 暂停动画。 请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

  * 1.widget为NULL时，暂停所有名称为name的动画。
  * 2.name为NULL时，暂停所有widget相关的动画。
  * 3.widget和name均为NULL，暂停所有动画。

  * 函数原型：



    
    
    ret_t widget_pause_animator (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_prepare_text_style 函数

* * *

  * 函数功能：



> 从widget的style中取出字体名称、大小和颜色数据，设置到canvas中。

  * 函数原型：


    
    
    ret_t widget_prepare_text_style (widget_t* widget, canvas_t* c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
  
#### widget_prepare_text_style_ex 函数

* * *

  * 函数功能：



> 从widget的style中取出字体名称、大小和颜色数据，设置到canvas中。 备注：如果在风格中找不到才会使用默认的设置。

  * 函数原型：


    
    
    ret_t widget_prepare_text_style_ex (widget_t* widget, canvas_t* c, color_t default_trans, const char* default_font, uint16_t default_font_size, align_h_t default_align_h, align_v_t default_align_v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
default_trans | color_t | 默认文字颜色。  
default_font | const char* | 默认字库名字。  
default_font_size | uint16_t | 默认字体大小。  
default_align_h | align_h_t | 默认文字水平方向对齐。  
default_align_v | align_v_t | 默认文字垂直方向对齐。  
  
#### widget_re_translate_text 函数

* * *

  * 函数功能：



> 语言改变后，重新翻译控件上的文本(包括子控件)。

  * 函数原型：


    
    
    ret_t widget_re_translate_text (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_ref 函数

* * *

  * 函数功能：



> 增加控件的引用计数。

  * 函数原型：


    
    
    widget_t* widget_ref (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回控件对象。  
widget | widget_t* | 控件对象。  
  
#### widget_remove_child 函数

* * *

  * 函数功能：



> 移出指定的子控件(并不销毁)。

  * 函数原型：


    
    
    ret_t widget_remove_child (widget_t* widget, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
child | widget_t* | 子控件对象。  
  
#### widget_remove_idle 函数

* * *

  * 函数功能：



> 删除指定的idle。

  * 函数原型：


    
    
    ret_t widget_remove_idle (widget_t* widget, uint32_t idle_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
idle_id | uint32_t | idleID。  
  
#### widget_remove_timer 函数

* * *

  * 函数功能：



> 删除指定的timer。

  * 函数原型：


    
    
    ret_t widget_remove_timer (widget_t* widget, uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
timer_id | uint32_t | timerID。  
  
#### widget_reset_canvas 函数

* * *

  * 函数功能：



> 重置canvas对象。for designer only,调用者需要unload全部图片

  * 函数原型：


    
    
    ret_t widget_reset_canvas (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_resize 函数

* * *

  * 函数功能：



> 调整控件的大小。

  * 函数原型：


    
    
    ret_t widget_resize (widget_t* widget, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### widget_restack 函数

* * *

  * 函数功能：



> 调整控件在父控件中的位置序数。

  * 函数原型：


    
    
    ret_t widget_restack (widget_t* widget, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
index | uint32_t | 位置序数(大于等于总个数，则放到最后)。  
  
#### widget_set_animation 函数

* * *

  * 函数功能：



> 设置控件的动画参数(仅用于在UI文件使用)。 请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

  * 函数原型：


    
    
    ret_t widget_set_animation (widget_t* widget, const char* animation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
animation | const char* | 动画参数。  
  
#### widget_set_animator_time_scale 函数

* * *

  * 函数功能：



> 设置动画的时间倍率，<0: 时间倒退，<1: 时间变慢，>1 时间变快。 请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

  * 1.widget为NULL时，设置所有名称为name的动画的时间倍率。
  * 2.name为NULL时，设置所有widget相关的动画的时间倍率。
  * 3.widget和name均为NULL，设置所有动画的时间倍率。

  * 函数原型：



    
    
    ret_t widget_set_animator_time_scale (widget_t* widget, const char* name, float_t time_scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
time_scale | float_t | 时间倍率。  
  
#### widget_set_as_key_target 函数

* * *

  * 函数功能：



> 递归的把父控件的key_target设置为自己。

  * 函数原型：


    
    
    ret_t widget_set_as_key_target (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_set_auto_adjust_size 函数

* * *

  * 函数功能：



> 设置控件是否根据子控件和文本自动调整控件自身大小。

  * 函数原型：


    
    
    ret_t widget_set_auto_adjust_size (widget_t* widget, bool_t auto_adjust_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
auto_adjust_size | bool_t | 是否根据子控件和文本自动调整控件自身大小。  
  
#### widget_set_child_text_utf8 函数

* * *

  * 函数功能：



> 设置子控件的文本。 只是对widget_set_prop的包装，文本的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_set_child_text_utf8 (widget_t* widget, const char* name, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 子控件的名称。  
text | const char* | 文本。  
  
#### widget_set_child_text_with_double 函数

* * *

  * 函数功能：



> 用一个浮点数去设置子控件的文本。 只是对widget_set_prop的包装，文本的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_set_child_text_with_double (widget_t* widget, const char* name, const char* format, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 子控件的名称。  
format | const char* | 格式字符串(如：”%2.2lf”)。  
value | double | 浮点数值。  
  
#### widget_set_child_text_with_int 函数

* * *

  * 函数功能：



> 用一个整数去设置子控件的文本。 只是对widget_set_prop的包装，文本的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_set_child_text_with_int (widget_t* widget, const char* name, const char* format, int value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 子控件的名称。  
format | const char* | 格式字符串(如：”%d”)。  
value | int | 值。  
  
#### widget_set_children_layout 函数

* * *

  * 函数功能：



> 设置子控件的布局参数。 备注：下一帧才会生效数据

  * 函数原型：


    
    
    ret_t widget_set_children_layout (widget_t* widget, const char* params);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
params | const char* | 布局参数。  
  
#### widget_set_dirty_rect_tolerance 函数

* * *

  * 函数功能：



> 设置控件脏矩形超出控件本身大小的最大范围(一般不用指定)。

  * 函数原型：


    
    
    ret_t widget_set_dirty_rect_tolerance (widget_t* widget, uint16_t dirty_rect_tolerance);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
dirty_rect_tolerance | uint16_t | 控件脏脏矩形超出控件本身大小的最大范。  
  
#### widget_set_enable 函数

* * *

  * 函数功能：



> 设置控件的可用性。

  * 函数原型：


    
    
    ret_t widget_set_enable (widget_t* widget, bool_t enable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
enable | bool_t | 是否可用性。  
  
#### widget_set_feedback 函数

* * *

  * 函数功能：



> 设置控件是否启用反馈。

  * 函数原型：


    
    
    ret_t widget_set_feedback (widget_t* widget, bool_t feedback);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
feedback | bool_t | 是否启用反馈。  
  
#### widget_set_floating 函数

* * *

  * 函数功能：



> 设置控件的floating标志。 floating的控件不受父控件的子控件布局参数的影响。

  * 函数原型：


    
    
    ret_t widget_set_floating (widget_t* widget, bool_t floating);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
floating | bool_t | 是否启用floating布局。  
  
#### widget_set_focusable 函数

* * *

  * 函数功能：



> 设置控件是否可获得焦点。

  * 函数原型：


    
    
    ret_t widget_set_focusable (widget_t* widget, bool_t focusable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
focusable | bool_t | 是否可获得焦点。  
  
#### widget_set_focused 函数

* * *

  * 函数功能：



> 设置控件是否获得焦点。

  * 函数原型：


    
    
    ret_t widget_set_focused (widget_t* widget, bool_t focused);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
focused | bool_t | 是否获得焦点。  
  
#### widget_set_name 函数

* * *

  * 函数功能：



> 设置控件的名称。

  * 函数原型：


    
    
    ret_t widget_set_name (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 名称。  
  
#### widget_set_need_relayout 函数

* * *

  * 函数功能：



> 设置控件需要relayout标识。

  * 函数原型：


    
    
    ret_t widget_set_need_relayout (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回。  
widget | widget_t* | 控件对象。  
  
#### widget_set_need_relayout_children 函数

* * *

  * 函数功能：



> 设置控件需要relayout标识。

  * 函数原型：


    
    
    ret_t widget_set_need_relayout_children (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回。  
widget | widget_t* | 控件对象。  
  
#### widget_set_need_update_style 函数

* * *

  * 函数功能：



> 设置需要更新Style。

  * 函数原型：


    
    
    ret_t widget_set_need_update_style (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_set_need_update_style_recursive 函数

* * *

  * 函数功能：



> 让控件及子控件设置需要更新Style。

  * 函数原型：


    
    
    ret_t widget_set_need_update_style_recursive (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_set_opacity 函数

* * *

  * 函数功能：



> 设置控件的不透明度。
> 
> 在嵌入式平台，半透明效果会使性能大幅下降，请谨慎使用。

  * 函数原型：


    
    
    ret_t widget_set_opacity (widget_t* widget, uint8_t opacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
opacity | uint8_t | 不透明度(取值0-255，0表示完全透明，255表示完全不透明)。  
  
#### widget_set_pointer_cursor 函数

* * *

  * 函数功能：



> 设置鼠标指针的图片名。

  * 函数原型：


    
    
    ret_t widget_set_pointer_cursor (widget_t* widget, const char* cursor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
cursor | const char* | 图片名称(无扩展名)。  
  
#### widget_set_prop 函数

* * *

  * 函数功能：



> 设置控件指定属性的值。

  * 函数原型：


    
    
    ret_t widget_set_prop (widget_t* widget, const char* name, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | const value_t* | 属性的值。  
  
#### widget_set_prop_bool 函数

* * *

  * 函数功能：



> 设置布尔格式的属性。

  * 函数原型：


    
    
    ret_t widget_set_prop_bool (widget_t* widget, const char* name, bool_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | bool_t | 属性的值。  
  
#### widget_set_prop_float 函数

* * *

  * 函数功能：



> 设置浮点数格式的属性。

  * 函数原型：


    
    
    ret_t widget_set_prop_float (widget_t* widget, const char* name, float_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | float_t | 属性的值。  
  
#### widget_set_prop_int 函数

* * *

  * 函数功能：



> 设置整数格式的属性。

  * 函数原型：


    
    
    ret_t widget_set_prop_int (widget_t* widget, const char* name, int32_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | int32_t | 属性的值。  
  
#### widget_set_prop_pointer 函数

* * *

  * 函数功能：



> 设置指针格式的属性。

  * 函数原型：


    
    
    ret_t widget_set_prop_pointer (widget_t* widget, const char* name, void* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | void* | 属性的值。  
  
#### widget_set_prop_pointer_ex 函数

* * *

  * 函数功能：



> 设置指针格式的属性。

  * 函数原型：


    
    
    ret_t widget_set_prop_pointer_ex (widget_t* widget, const char* name, void* v, tk_destroy_t destroy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | void* | 属性的值。  
destroy | tk_destroy_t | 销毁函数。  
  
#### widget_set_prop_str 函数

* * *

  * 函数功能：



> 设置字符串格式的属性。

  * 函数原型：


    
    
    ret_t widget_set_prop_str (widget_t* widget, const char* name, const char* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 属性的名称。  
v | const char* | 属性的值。  
  
#### widget_set_props 函数

* * *

  * 函数功能：



> 设置多个参数。 参数之间用&分隔，名称和值之间用=分隔。如: name=awtk&min=10&max=100

  * 函数原型：


    
    
    ret_t widget_set_props (widget_t* widget, const char* params);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
params | const char* | 参数列表。  
  
#### widget_set_self_layout 函数

* * *

  * 函数功能：



> 设置控件自己的布局参数。 备注：下一帧才会生效数据

  * 函数原型：


    
    
    ret_t widget_set_self_layout (widget_t* widget, const char* params);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
params | const char* | 布局参数。  
  
#### widget_set_self_layout_params 函数

* * *

  * 函数功能：



> 设置控件自己的布局(缺省布局器)参数(建议用widget_set_self_layout)。 备注：下一帧才会生效数据

  * 函数原型：


    
    
    ret_t widget_set_self_layout_params (widget_t* widget, const char* x, const char* y, const char* w, const char* h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
x | const char* | x参数。  
y | const char* | y参数。  
w | const char* | w参数。  
h | const char* | h参数。  
  
#### widget_set_sensitive 函数

* * *

  * 函数功能：



> 设置控件是否接受用户事件。

  * 函数原型：


    
    
    ret_t widget_set_sensitive (widget_t* widget, bool_t sensitive);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
sensitive | bool_t | 是否接受用户事件。  
  
#### widget_set_state 函数

* * *

  * 函数功能：



> 设置控件的状态。

  * 函数原型：


    
    
    ret_t widget_set_state (widget_t* widget, const char* state);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
state | const char* | 状态。  
  
#### widget_set_style 函数

* * *

  * 函数功能：



> 设置widget私有样式。

  * 函数原型：


    
    
    ret_t widget_set_style (widget_t* widget, const char* state_and_name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
state_and_name | const char* | 样式对应类型与名字。  
value | const value_t* | 值。  
  
#### widget_set_style_color 函数

* * *

  * 函数功能：



> 设置颜色类型的style。
> 
>   * [state 的取值](https://github.com/zlgopen/awtk/blob/master/docs/manual/widget_state_t.html)
>   * [name 的取值](https://github.com/zlgopen/awtk/blob/master/docs/theme.html)
> 


在下面这个例子中，R=0x11 G=0x22 B=0x33 A=0xFF
    
    
    widget_set_style_color(label, "normal:bg_color", 0xFF332211);
    

  * 函数原型：


    
    
    ret_t widget_set_style_color (widget_t* widget, const char* state_and_name, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
state_and_name | const char* | 状态和名字，用英文的冒号分隔。  
value | uint32_t | 值。颜色值一般用十六进制表示，每两个数字表示一个颜色通道，从高位到低位，依次是ABGR。  
  
#### widget_set_style_int 函数

* * *

  * 函数功能：



> 设置整数类型的style。
> 
>   * [state 的取值](https://github.com/zlgopen/awtk/blob/master/docs/manual/widget_state_t.html)
>   * [name 的取值](https://github.com/zlgopen/awtk/blob/master/docs/theme.html)
> 


  * 函数原型：


    
    
    ret_t widget_set_style_int (widget_t* widget, const char* state_and_name, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
state_and_name | const char* | 状态和名字，用英文的冒号分隔。  
value | int32_t | 值。  
  
#### widget_set_style_str 函数

* * *

  * 函数功能：



> 设置字符串类型的style。
> 
>   * [state 的取值](https://github.com/zlgopen/awtk/blob/master/docs/manual/widget_state_t.html)
>   * [name 的取值](https://github.com/zlgopen/awtk/blob/master/docs/theme.html)
> 


  * 函数原型：


    
    
    ret_t widget_set_style_str (widget_t* widget, const char* state_and_name, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
state_and_name | const char* | 状态和名字，用英文的冒号分隔。  
value | const char* | 值。  
  
#### widget_set_text 函数

* * *

  * 函数功能：



> 设置控件的文本。（如果字符串相同，则不会重复设置以及触发事件）

  * 函数原型：


    
    
    ret_t widget_set_text (widget_t* widget, const wchar_t* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
text | const wchar_t* | 文本。  
  
#### widget_set_text_ex 函数

* * *

  * 函数功能：



> 设置控件的文本。

  * 函数原型：


    
    
    ret_t widget_set_text_ex (widget_t* widget, const wchar_t* text, bool_t check_diff);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
text | const wchar_t* | 文本。  
check_diff | bool_t | 是否检查设置的文本是否和控件中的文本一样。  
  
#### widget_set_text_utf8 函数

* * *

  * 函数功能：



> 设置控件的文本。（如果字符串相同，则不会重复设置以及触发事件）

  * 函数原型：


    
    
    ret_t widget_set_text_utf8 (widget_t* widget, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
text | const char* | 文本。  
  
#### widget_set_text_utf8_ex 函数

* * *

  * 函数功能：



> 设置控件的文本。

  * 函数原型：


    
    
    ret_t widget_set_text_utf8_ex (widget_t* widget, const char* text, bool_t check_diff);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
text | const char* | 文本。  
check_diff | bool_t | 是否检查设置的文本是否和控件中的文本一样。  
  
#### widget_set_text_with_double 函数

* * *

  * 函数功能：



> 设置控件的文本。

  * 函数原型：


    
    
    ret_t widget_set_text_with_double (widget_t* widget, const char* format, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
format | const char* | 格式。  
value | double | 值。  
  
#### widget_set_theme 函数

* * *

  * 函数功能：



> 设置theme的名称，用于动态切换主题。名称与当前主题名称相同，则重新加载全部资源。

  * 函数原型：


    
    
    ret_t widget_set_theme (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 主题的名称。  
  
#### widget_set_tr_text 函数

* * *

  * 函数功能：



> 获取翻译之后的文本，然后调用widget_set_text。

  * 函数原型：


    
    
    ret_t widget_set_tr_text (widget_t* widget, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
text | const char* | 文本。  
  
#### widget_set_value 函数

* * *

  * 函数功能：



> 设置控件的值。 只是对widget_set_prop的包装，值的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_set_value (widget_t* widget, float_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
value | float_t | 值。  
  
#### widget_set_value_int 函数

* * *

  * 函数功能：



> 设置控件的值。 只是对widget_set_prop的包装，值的意义由子类控件决定。

  * 函数原型：


    
    
    ret_t widget_set_value_int (widget_t* widget, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
value | int32_t | 值。  
  
#### widget_set_visible 函数

* * *

  * 函数功能：



> 设置控件的可见性。

  * 函数原型：


    
    
    ret_t widget_set_visible (widget_t* widget, bool_t visible);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
visible | bool_t | 是否可见。  
  
#### widget_set_visible_only 函数

* * *

  * 函数功能：



> 设置控件的可见性(不触发repaint和relayout)。

  * 函数原型：


    
    
    ret_t widget_set_visible_only (widget_t* widget, bool_t visible);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
visible | bool_t | 是否可见。  
  
#### widget_start_animator 函数

* * *

  * 函数功能：



> 播放动画。 请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

  * 1.widget为NULL时，播放所有名称为name的动画。
  * 2.name为NULL时，播放所有widget相关的动画。
  * 3.widget和name均为NULL，播放所有动画。

  * 函数原型：



    
    
    ret_t widget_start_animator (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_stop_animator 函数

* * *

  * 函数功能：



> 停止动画(控件的相应属性回归原位)。 请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

  * 1.widget为NULL时，停止所有名称为name的动画。
  * 2.name为NULL时，停止所有widget相关的动画。
  * 3.widget和name均为NULL，停止所有动画。

  * 函数原型：



    
    
    ret_t widget_stop_animator (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
name | const char* | 动画名称。  
  
#### widget_stroke_border_rect 函数

* * *

  * 函数功能：



> 根据控件的style绘制边框矩形。

  * 函数原型：


    
    
    ret_t widget_stroke_border_rect (widget_t* widget, canvas_t* c, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
c | canvas_t* | 画布对象。  
r | const rect_t* | 矩形区域。  
  
#### widget_take_snapshot 函数

* * *

  * 函数功能：



> 创建一个bitmap对象，将控件绘制到bitmap上，并返回bitmap对象。

调用者需要调用bitmap_destroy销毁返回的bitmap对象。
    
    
    bitmap_t* bitmap = widget_take_snapshot(window_manager());
    bitmap_save_png(bitmap, "test.png");
    bitmap_destroy(bitmap);
    

  * 函数原型：


    
    
    bitmap_t* widget_take_snapshot (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回位图对象。  
widget | widget_t* | 控件对象。  
  
#### widget_take_snapshot_rect 函数

* * *

  * 函数功能：



> 创建一个bitmap对象，将控件绘制到bitmap上并且可以设置该控件的截屏区域，返回bitmap对象。

调用者需要调用bitmap_destroy销毁返回的bitmap对象。
    
    
    bitmap_t* bitmap = widget_take_snapshot_rect(window_manager(), NULL);
    bitmap_save_png(bitmap, "test.png");
    bitmap_destroy(bitmap);
    

  * 函数原型：


    
    
    bitmap_t* widget_take_snapshot_rect (widget_t* widget, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bitmap_t* | 返回位图对象。  
widget | widget_t* | 控件对象。  
r | const rect_t* | 截屏区域（输入NULL，则为控件全区域截屏）。  
  
#### widget_to_global 函数

* * *

  * 函数功能：



> 将控件内的本地坐标转换成全局坐标。

  * 函数原型：


    
    
    ret_t widget_to_global (widget_t* widget, point_t* p);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
p | point_t* | 坐标点。  
  
#### widget_to_local 函数

* * *

  * 函数功能：



> 将屏幕坐标转换成控件内的本地坐标，即相对于控件左上角的坐标。

  * 函数原型：


    
    
    ret_t widget_to_local (widget_t* widget, point_t* p);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
p | point_t* | 坐标点。  
  
#### widget_to_screen 函数

* * *

  * 函数功能：



> 将控件内的本地坐标转换成屏幕上的坐标。

  * 函数原型：


    
    
    ret_t widget_to_screen (widget_t* widget, point_t* p);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
p | point_t* | 坐标点。  
  
#### widget_to_screen_ex 函数

* * *

  * 函数功能：



> 将控件内的本地坐标根据祖父级控件转换成相对于祖父级控件的屏幕相对坐标。 备注：如果 parent 不是 widget 控件的父级或者祖父级话，该函数会退化为 widget_to_screen 函数。

  * 函数原型：


    
    
    ret_t widget_to_screen_ex (widget_t* widget, widget_t* parent, point_t* p);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
parent | widget_t* | 祖父级控。  
p | point_t* | 坐标点。  
  
#### widget_to_xml 函数

* * *

  * 函数功能：



> 将widget转换成xml。

  * 函数原型：


    
    
    ret_t widget_to_xml (widget_t* widget, str_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
str | str_t* | 用于保存xml结果。  
  
#### widget_ungrab 函数

* * *

  * 函数功能：



> 让指定子控件放弃抓住事件。

  * 函数原型：


    
    
    ret_t widget_ungrab (widget_t* widget, widget_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
child | widget_t* | 子控件对象。  
  
#### widget_unload_asset 函数

* * *

  * 函数功能：



> 卸载资源。

使用示例：
    
    
    const asset_info_t* asset = widget_load_asset(widget, ASSET_TYPE_IMAGE, "mysvg");
    ...
    widget_unload_asset(widget, asset);
    

  * 函数原型：


    
    
    ret_t widget_unload_asset (widget_t* widget, const asset_info_t* asset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
asset | const asset_info_t* | 资源句柄。  
  
#### widget_unload_image 函数

* * *

  * 函数功能：



> 卸载图片。
> 
> 一般不需要调用，只有确认在图片不再需要时才调用本函数卸载。

  * 函数原型：


    
    
    ret_t widget_unload_image (widget_t* widget, bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
bitmap | bitmap_t* | 图片对象。  
  
#### widget_unref 函数

* * *

  * 函数功能：



> 减少控件的引用计数。引用计数为0时销毁控件。

  * 函数原型：


    
    
    ret_t widget_unref (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_update_pointer_cursor 函数

* * *

  * 函数功能：



> 更新鼠标指针。

  * 函数原型：


    
    
    ret_t widget_update_pointer_cursor (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
  
#### widget_update_style 函数

* * *

  * 函数功能：



> 让控件根据自己当前状态更新style。

  * 函数原型：


    
    
    ret_t widget_update_style (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_update_style_recursive 函数

* * *

  * 函数功能：



> 让控件及子控件根据自己当前状态更新style。

  * 函数原型：


    
    
    ret_t widget_update_style_recursive (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
  
#### widget_use_style 函数

* * *

  * 函数功能：



> 启用指定的style。

  * 函数原型：


    
    
    ret_t widget_use_style (widget_t* widget, const char* style);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
style | const char* | style的名称。  
  
#### animation 属性

* * *

> 动画参数。请参考[控件动画](https://github.com/zlgopen/awtk/blob/master/docs/widget_animator.html)

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
  
#### astyle 属性

* * *

> Style对象。

  * 类型：style_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### auto_adjust_size 属性

* * *

> 是否根据子控件和文本自动调整控件自身大小。
> 
> 为true时，最好不要使用 layout 的相关东西，否则可能有冲突。 注意：只是调整控件的本身的宽高，不会修改控件本身的位置。

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
  
#### auto_created 属性

* * *

> 是否由父控件自动创建。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### children 属性

* * *

> 全部子控件。

  * 类型：darray_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### children_layout 属性

* * *

> 子控件布局器。请参考[控件布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)

  * 类型：children_layouter_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### custom_props 属性

* * *

> 自定义属性。

  * 类型：tk_object_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### destroying 属性

* * *

> 标识控件正在被销毁。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### dirty 属性

* * *

> 标识控件是否需要重绘。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### dirty_rect_tolerance 属性

* * *

> 脏矩形超出控件本身大小的最大范围(一般不用指定)。
> 
> 如果 border 太粗或 offset 太大等原因，导致脏矩形超出控件本身大小太多（大于缺省值）时，才需要指定。

  * 类型：uint16_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
可在IDE中设置 | 是  
  
#### emitter 属性

* * *

> 事件发射器。

  * 类型：emitter_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### enable 属性

* * *

> 启用/禁用状态。

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
  
#### feedback 属性

* * *

> 是否启用按键音、触屏音和震动等反馈。

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
  
#### floating 属性

* * *

> 标识控件是否启用浮动布局，不受父控件的children_layout的控制。

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
  
#### focusable 属性

* * *

> 是否支持焦点停留。

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
  
#### focused 属性

* * *

> 是否得到焦点。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### h 属性

* * *

> 高度。

  * 类型：wh_t

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
  
#### initializing 属性

* * *

> 标识控件正在初始化。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### loading 属性

* * *

> 标识控件正在加载。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### name 属性

* * *

> 控件名字。

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
  
#### need_update_style 属性

* * *

> 标识控件是否需要update style。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### opacity 属性

* * *

> 不透明度(0-255)，0完全透明，255完全不透明。

  * 类型：uint8_t

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
  
#### parent 属性

* * *

> 父控件

  * 类型：widget_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### pointer_cursor 属性

* * *

> 鼠标光标图片名称。

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
  
#### ref_count 属性

* * *

> 引用计数，计数为0时销毁。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### self_layout 属性

* * *

> 控件布局器。请参考[控件布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)

  * 类型：self_layouter_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### sensitive 属性

* * *

> 是否接受用户事件。

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
  
#### state 属性

* * *

> 控件的状态(取值参考widget_state_t)。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### style 属性

* * *

> style的名称。

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
  
#### text 属性

* * *

> 文本。用途视具体情况而定。

  * 类型：wstr_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### tr_text 属性

* * *

> 保存用于翻译的字符串。

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
  
#### visible 属性

* * *

> 是否可见。

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
  
#### vt 属性

* * *

> 虚函数表。

  * 类型：const widget_vtable_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### w 属性

* * *

> 宽度。

  * 类型：wh_t

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
  
#### with_focus_state 属性

* * *

> 是否支持焦点状态。 如果希望style支持焦点状态，但又不希望焦点停留，可用本属性。

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
  
#### x 属性

* * *

> x坐标(相对于父控件的x坐标)。

  * 类型：xy_t

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
  
#### y 属性

* * *

> y坐标(相对于父控件的y坐标)。

  * 类型：xy_t

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
