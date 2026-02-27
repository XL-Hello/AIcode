# 参考手册

## 一、GUI 相关组件

### 控件

![widget_overview](images/widget_overview.png)

#### widget

  * [widget](manual/widget_t.html) 所有控件、窗口和窗口管理器的基类。



#### 窗口管理器

  * [window_manager](manual/window_manager_t.html) 窗口管理器。



#### 窗口

  * [window_base](manual/window_base_t.html) 窗口基类。
  * [dialog](manual/dialog_t.html) 对话框。
  * [popup](manual/popup_t.html) 弹出窗口。
  * [window](manual/window_t.html) 普通窗口。
  * [system_bar](manual/system_bar_t.html) 系统状态窗口。
  * [calibration_win](manual/calibration_win_t.html) 电阻屏校准窗口。
  * [overlay](manual/overlay_t.html) 悬浮窗口。



#### 基本控件

  * [button](manual/button_t.html) 按钮控件。
  * [label](manual/label_t.html) 文本控件。
  * [edit](manual/edit_t.html) 单行编辑器控件。
  * [image](manual/image_t.html) 图片控件。
  * [dragger](manual/dragger_t.html) dragger 控件。
  * [draggable](manual/draggable_t.html) draggable 控件。
  * [image_base](manual/image_base_t.html) 图片控件基类。
  * [check_button](manual/check_button_t.html) 多选按钮。
  * [radio_button](manual/check_button_t.html) 单选按钮。
  * [spin_box](manual/spin_box_t.html) 数值编辑器控件。
  * [combo_box](manual/combo_box_t.html) 下拉列表控件。
  * [combo_box_ex](manual/combo_box_ex_t.html) 可滚动的下拉列表控件。
  * [combo_box_item](manual/combo_box_item_t.html) 下拉列表项控件。
  * [color_tile](manual/color_tile_t.html) 色块控件。
  * [dialog_title](manual/dialog_title_t.html) 对话框标题控件。
  * [dialog_client](manual/dialog_client_t.html) 对话框客户区控件。
  * [slider](manual/slider_t.html) 滑块控件。
  * [progress_bar](manual/progress_bar_t.html) 进度条控件。
  * [tab_control](manual/tab_control_t.html) 标签控件。
  * [tab_button](manual/tab_button_t.html) 标签按钮控件。
  * [tab_button_group](manual/tab_button_group_t.html) 标签按钮分组控件。



#### 通用容器控件

  * [row](manual/row_t.html) 行控件。
  * [column](manual/column_t.html) 列控件。
  * [grid](manual/grid_t.html) 网格控件。
  * [view](manual/view_t.html) 通用容器控件。
  * [grid_item](manual/grid_item_t.html) 网格项控件。
  * [group_box](manual/group_box_t.html) 通用分组控件。
  * [app_bar](manual/app_bar_t.html) app_bar 控件。
  * [button_group](manual/button_group_t.html) 按钮分组控件。



#### 扩展控件

  * [candidates](manual/candidates_t.html) 软键盘候选字控件。
  * [canvas_widget](manual/canvas_widget_t.html) 画布控件。
  * [color_picker](manual/color_picker_t.html) 颜色选择器控件。
  * [gif_image](manual/gif_image_t.html) gif_image 控件。
  * [guage](manual/guage_t.html) 仪表控件。
  * [guage_pointer](manual/guage_pointer_t.html) 仪表指针控件。
  * [image_animation](manual/image_animation_t.html) 图片动画控件。
  * [image_value](manual/image_value_t.html) 图片值控件。
  * [keyboard](manual/keyboard_t.html) 软键盘控件。
  * [progress_circle](manual/progress_circle_t.html) 进度圆环控件。
  * [rich_text](manual/rich_text_t.html) 图文混排控件。
  * [rich_text_view](manual/rich_text_view_t.html) 用于协调 rich text 和 scrollbar 控件。
  * [slide_menu](manual/slide_menu_t.html) 左右滑动菜单控件。
  * [slide_view](manual/slide_view_t.html) 滑动视图控件。
  * [slide_view_indicator](manual/slide_indicator_t.html) 滑动视图的指示器控件。
  * [svg_image](manual/svg_image_t.html) SVG 图片控件。
  * [switch](manual/switch_t.html) 开关控件。
  * [text_selector](manual/text_selector_t.html) 文本选择器控件。
  * [time_clock](manual/time_clock_t.html) 模拟时钟控件。
  * [digit_clock](manual/digit_clock_t.html) 数字时钟控件。
  * [list_view](manual/list_view_t.html) 列表视图控件。
  * [list_view_h](manual/list_view_h_t.html) 水平列表视图控件。
  * [list_item](manual/list_item_t.html) 列表项控件。
  * [scroll_bar](manual/scroll_bar_t.html) 滚动条控件。
  * [scroll_view](manual/scroll_view_t.html) 滚动视图控件。
  * [mledit](manual/mledit_t.html) 多行编辑器控件。
  * [line_number](manual/line_number_t.html) 多行编辑器的行号控件。
  * [mutable_image](manual/mutable_image_t.html) mutable 图片控件（用于辅助实现 camera/video）。
  * [file_browser_view](manual/file_browser_view_t.html) 文件浏览控件。



### 常用常量

  * [控件状态定义](manual/widget_state_t.html)

  * [控件属性定义](manual/widget_prop_t.html)




### 画布

#### 普通画布

  * [canvas](manual/canvas_t.html)

  * [canvas offline](manual/canvas_offline_t.html)




#### 矢量图画布

![vgcanvas_overview](manual/images/vgcanvas_t_0.png)

  * [vgcanvas](manual/vgcanvas_t.html)



### 资源相关组件

![assets overview](images/assets_overview.png)

  * [asset_info](manual/asset_info_t.html) 资源信息。
  * [assets_manager](manual/assets_manager_t.html) 资源管理器。



#### 1\. 字体

![font_overview](images/font_overview.png)

  * [glyph](manual/glyph_t.html) 字模。
  * [font](manual/font_t.html) 字体。
  * [font_loader](manual/font_loader_t.html) 字体加载器。
  * [font_loader_ft](manual/font_loader_ft_t.html) 基于 freetype 实现的字体加载器。
  * [font_loader_stb](manual/font_loader_stb_t.html) 基于 stb 实现的字体加载器。
  * [font_loader_bitmap](manual/font_loader_bitmap_t.html) 基于位图实现的字体加载器。
  * [font_manager](manual/font_manager_t.html) 字体管理器。



#### 2\. 图片

![image_overview](images/image_overview.png)

  * [bitmap](manual/bitmap_t.html) 位图。
  * [image_loader](manual/image_loader_t.html) 图片加载器。
  * [image_loader_stb](manual/image_loader_stb_t.html) stb 图片加载器。
  * [image_manager](manual/image_manager_t.html) 图片管理器。



#### 3\. 字符串资源

  * [locale_info](manual/locale_info_t.html) 本地化信息。



#### 4\. 窗体样式

![style_overview](images/style_overview.png)

  * [style](manual/style_t.html) style 接口。
  * [theme](manual/theme_t.html) 常量窗体样式数据。
  * [style_factory](manual/style_factory_t.html) style 工厂。
  * [style_const](manual/style_const_t.html) 只读的 style。
  * [style_mutable](manual/style_mutable_t.html) 可修改的 style。



#### 5.UI 描述数据

![ui_loader_overview](images/ui_loader_overview.png)

  * [ui_loader](manual/ui_loader_t.html) loader 接口。
  * [ui_builder](manual/ui_builder_t.html) builder 接口。

  * [ui_builder_default](manual/ui_builder_default_t.html) 缺省 builder 实现，负责构建 widget 树。

  * [ui_xml_writer](manual/ui_xml_writer_t.html) 生成 XML 格式的 UI 描述数据。 
  * [ui_binary_writer](manual/ui_binary_writer_t.html) 生成二进制格式的 UI 描述数据。 

  * [ui_loader_default](manual/ui_loader_default_t.html) 二进制格式的 UI 资源加载器。 

  * [ui_loader_xml](manual/ui_loader_xml_t.html) XML 格式的 UI 资源加载器。



### 输入法

![input_method_overview](images/input_method_overview.png)

  * [input_type](manual/input_type_t.html) 输入类型（用于控制软键盘和输入格式）
  * [input_method](manual/input_method_t.html) 输入法接口。
  * [input_method_default](manual/input_method_default_t.html) 输入法缺省实现。
  * [input_method_sdl](manual/input_method_sdl_t.html) 输入法 SDL 实现。
  * [input_method_null](manual/input_method_null_t.html) 输入法空实现。

  * [input_engine](manual/input_engine_t.html) 输入法引擎接口。

  * [input_engine_null](manual/input_engine_null_t.html) 空输入法引擎实现。
  * [input_engine_pinyin](manual/input_engine_pinyin_t.html) 拼音输入法引擎实现。



### 定时器/IDLE

![timer_overview](images/timer_overview.png)

  * [timer](manual/timer_t.html) 定时器。

  * [timer_info](manual/timer_info_t.html) 单个 timer 的信息。




![idle_overview](images/idle_overview.png)

  * [idle](manual/idle_t.html) 用于异步执行一些函数。 

  * [idle_info](manual/idle_info_t.html) 单个 idle 的信息。 




### 布局器

![self_layouter](images/layout_self_layouter.png)

![children_layouter](images/layout_children_layouter.png)

  * [self_layouter](manual/self_layouter_t.html) 控件自身排版布局器的接口

  * [children_layouter](manual/children_layouter_t.html) 子控件排版布局器的接口

  * [self_layouter_factory](manual/self_layouter_factory_t.html) 控件自身排版布局器的工厂。

  * [children_layouter_factory](manual/children_layouter_factory_t.html) 子控件排版布局器的的工厂。

  * [self_layouter_default](manual/self_layouter_default_t.html) 缺省的控件自身布局算法实现。

  * [self_layouter_menu](manual/self_layouter_menu_t.html) 菜单控件自身布局算法实现。

  * [children_layouter_default](manual/children_layouter_default_t.html) 缺省的子控件布局算法实现。

  * [children_layouter_list_view](manual/children_layouter_list_view_t.html) 列表视图的子控件布局算法实现。




### lcd

![lcd](images/lcd.png)

  * [lcd](manual/lcd_t.html) LCD 接口

  * [lcd_type](manual/lcd_type_t.html) LCD 类型定义

  * [lcd_draw_mode](manual/lcd_draw_mode_t.html) LCD 绘制模式

  * [lcd_mem_fragment](manual/lcd_mem_fragment_t.html) 片段 LCD

  * [lcd_orientation](manual/lcd_orientation_t.html) LCD 旋转常量

  * [lcd_mem_bgr565](manual/lcd_mem_bgr565_t.html) bgr565 格式的 LCD

  * [lcd_mem_bgr888](manual/lcd_mem_bgr888_t.html) bgr888 格式的 LCD

  * [lcd_mem_bgra8888](manual/lcd_mem_bgra8888_t.html) bgra8888 格式的 LCD

  * [lcd_mem_rgb565](manual/lcd_mem_rgb565_t.html) rgb565 格式的 LCD

  * [lcd_mem_rgb888](manual/lcd_mem_rgb888_t.html) rgb888 格式的 LCD

  * [lcd_mem_rgba8888](manual/lcd_mem_rgba8888_t.html) bgra8888 格式的 LCD

  * [lcd_mem_special](manual/lcd_mem_special_t.html) 特殊格式的 LCD

  * [lcd_mono](manual/lcd_mono_t.html) 单色 LCD

  * [lcd_profile](manual/lcd_profile_t.html) 用于 profile 性能的 LCD




### 杂项

  * [system_info](manual/system_info_t.html) 系统信息。



## 二、基本函数库

### 容器与基本数据结构

  * [darray](manual/darray_t.html) 动态数组。
  * [slist](manual/slist_t.html) 单向链表。
  * [wbuffer](manual/wbuffer_t.html) Write Buffer。
  * [rbuffer](manual/rbuffer_t.html) Read Buffer。
  * [ring_buffer](manual/ring_buffer_t.html) 循环缓存区。
  * [str](manual/str_t.html) 可变长度的 UTF8 字符串。
  * [wstr](manual/wstr_t.html) 可变长度的宽字符字符串。
  * [object](manual/object_t.html) 对象接口。
  * [object_default](manual/object_default_t.html) 对象接口的缺省实现。
  * [object_array](manual/object_array_t.html) 简单的动态数组，内部存放 value 对象。

  * [point](manual/point_t.html) 点。

  * [rect](manual/rect_t.html) 矩形。
  * [color](manual/color_t.html) 颜色对象。
  * [pointf](manual/pointf_t.html) 点（浮点数格式）。
  * [int_str](manual/int_str_t.html) 数字-字符串类型
  * [str_str](manual/str_str_t.html) 字符串-字符串类型
  * [named_value](manual/named_value_t.html) 命名的值。
  * [value](manual/value_t.html) 一个通用数据类型，用来存放整数、浮点数、字符串和其它对象。
  * [emitter](manual/emitter_t.html) 事件分发器，用于实现观察者模式。
  * [rgba](manual/rgba_t.html) RGBA 颜色值。
  * [asset_info](manual/asset_info_t.html) 资源类型定义。



### 流

  * [istream](manual/tk_istream_t.html) 输入流的接口。
  * [ostream](manual/tk_ostream_t.html) 输出流的接口。
  * [iostream](manual/tk_iostream_t.html) 输入/出流的接口。

  * [iostream_mem](manual/tk_iostream_mem_t.html) 内存输入输出流。

  * [istream_mem](manual/tk_istream_mem_t.html) 内存输入流。
  * [ostream_mem](manual/tk_ostream_mem_t.html) 内存输出流。

  * [istream_file](manual/tk_istream_file_t.html) 文件输入流。

  * [ostream_file](manual/tk_ostream_file_t.html) 文件输出流。

  * [iostream_tcp](manual/tk_iostream_tcp_t.html) TCP 输入输出流。

  * [istream_tcp](manual/tk_istream_tcp_t.html) TCP 输入流。
  * [ostream_tcp](manual/tk_ostream_tcp_t.html) TCP 输出流。

  * [iostream_udp](manual/tk_iostream_udp_t.html) UDP 输入输出流。

  * [istream_udp](manual/tk_istream_udp_t.html) UDP 输入流。
  * [ostream_udp](manual/tk_ostream_udp_t.html) UDP 输出流。

  * [iostream_serial](manual/tk_iostream_serial_t.html) 串口输入输出流。

  * [istream_serial](manual/tk_istream_serial_t.html) 串口输入流。
  * [ostream_serial](manual/tk_ostream_serial_t.html) 串口输出流。

  * [istream_buffered](manual/tk_istream_buffered_t.html) 缓冲输入流。

  * [ostream_buffered](manual/tk_ostream_buffered_t.html) 缓冲输出流。

  * [iostream_noisy](manual/tk_iostream_noisy_t.html) 故障注入流。

  * [ostream_noisy](manual/tk_ostream_noisy_t.html) 故障注入输出流。

  * [iostream_shdlc](manual/tk_iostream_shdlc_t.html) SHDLC 输入输出流。

  * [istream_shdlc](manual/tk_istream_shdlc_t.html) SHDLC 输入流。
  * [ostream_shdlc](manual/tk_ostream_shdlc_t.html) SHDLC 输出流。

  * [ostream_retry](manual/tk_ostream_retry_t.html) 重传输出流。




### 并发

  * [mutex](manual/tk_mutex_t.html) 互斥锁。
  * [thread](manual/tk_thread_t.html) 线程。
  * [semaphor](manual/tk_semaphore_t.html) 信号量。
  * [cond_var](manual/tk_cond_var_t.html) 简化版条件变量。



### 事件与事件源

  * [event](manual/emitter_t.html) 事件基类。
  * [timer_info](manual/timer_info_t.html) 单个定时器的信息。
  * [timer_manager](manual/timer_manager_t.html) 定时器管理器
  * [idle_info](manual/idle_info_t.html) 单个 idle 的信息。
  * [idle_manager](manual/idle_manager_t.html) idle_manager_t 管理器
  * [event_source](manual/event_source_t.html) 事件源接口。
  * [event_source_fd](manual/event_source_fd_t.html) 基于文件描述符的事件源实现。
  * [event_source_idle](manual/event_source_idle_t.html) 基于 IDLE 的事件源实现。
  * [event_source_timer](manual/event_source_timer_t.html) 基于 Time 的事件源实现。
  * [event_source_manager](manual/event_source_manager_t.html) 事件源管理器的接口。
  * [event_source_manager_default](manual/event_source_manager_default_t.html) 创建事件源管理器。



### 压缩解压

  * [compressor](manual/compressor_t.html) 压缩解压接口。
  * [compressor_miniz](manual/compressor_miniz_t.html) 基于 miniz 实现的压缩解压接口。



### 平台相关

  * [fs](manual/fs_t.html) 文件系统
  * [fs_dir](manual/fs_dir_t.html) 目录
  * [fs_file](manual/fs_file_t.html) 文件
  * [fs_item](manual/fs_item_t.html) 目录或目录。
  * [path](manual/path_t.html) 路径相关的工具函数。
  * [memory](manual/tk_mem_t.html) 内存管理相关函数和宏。
  * [date_time](manual/date_time_t.html) 时间日期函数。
  * [time_now](manual/time_now_t.html) 获取当前时间的函数。
  * [platform](manual/platform_t.html) 平台接口，包括：获取时间、休眠等函数
  * [socket_pair](manual/socketpair_t.html) 生成两个可以互相通信的 socket 句柄。



### 数据格式

  * [ubjson_parser](manual/ubjson_parser_t.html)
  * [ubjson_writer](manual/ubjson_writer_t.html)
  * [xml_parser](manual/XmlParser.html)



### 工具类

  * [easing](manual/easing_type_t.html) 缓动作常量定义。
  * [utils](manual/utils_t.html) 工具类
  * [utf8](manual/utf8_t.html) wchar_t 和 char 类型转换接口
  * [matrix](manual/matrix_t.html) 2D 阵变换。
  * [func_desc](manual/func_desc_t.html) 函数描述。
  * [value_desc](manual/value_desc_t.html) 属性描述。
  * [func_call_parser](manual/func_call_parser_t.html) 从字符串中解析出函数调用需要的参数。
  * [tokenizer](manual/tokenizer_t.html) 从字符串中解析出一个一个的 token。
  * [color_parse](manual/color_parser_t.html) 颜色解析对象。


