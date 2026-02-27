## widget_prop_t

### 概述

控件的属性。

### 常量

名称 | 说明  
---|---  
WIDGET_PROP_EXEC | 用于执行某些特殊的命令（比如控制动画的启停），主要是方便MVVM通过属性来控制动画。  
WIDGET_PROP_X | X坐标。  
WIDGET_PROP_Y | Y坐标。  
WIDGET_PROP_W | 宽度。  
WIDGET_PROP_H | 高度。  
WIDGET_PROP_MAX_H | 最大高度。  
WIDGET_PROP_DESIGN_W | 窗口设计时宽度。  
WIDGET_PROP_DESIGN_H | 窗口设计时宽度。  
WIDGET_PROP_AUTO_SCALE_CHILDREN_X | 窗口大小与设计时大小不同时，是否自动调整子控件的x坐标。  
WIDGET_PROP_AUTO_SCALE_CHILDREN_Y | 窗口大小与设计时大小不同时，是否自动调整子控件的y坐标。  
WIDGET_PROP_AUTO_SCALE_CHILDREN_W | 窗口大小与设计时大小不同时，是否自动调整子控件的宽度。  
WIDGET_PROP_AUTO_SCALE_CHILDREN_H | 窗口大小与设计时大小不同时，是否自动调整子控件的高度。  
WIDGET_PROP_INPUTING | inputing。  
WIDGET_PROP_ALWAYS_ON_TOP | always on top。  
WIDGET_PROP_CARET_X | caret x。  
WIDGET_PROP_CARET_Y | caret y。  
WIDGET_PROP_LINE_HEIGHT | 行高。  
WIDGET_PROP_DIRTY_RECT_TOLERANCE | 脏矩形超出控件本身大小的最大范围。  
WIDGET_PROP_BIDI | bidi type(rtl,ltr,auto,wrtl,wltr,lro,rlo)。  
WIDGET_PROP_CANVAS | Canvas。  
WIDGET_PROP_LOCALIZE_OPTIONS | Canvas。  
WIDGET_PROP_NATIVE_WINDOW | Native Window。  
WIDGET_PROP_HIGHLIGHT | dialog highlight。  
WIDGET_PROP_BAR_SIZE | slider中的bar的的宽度或高度。  
WIDGET_PROP_OPACITY | 不透明度。  
WIDGET_PROP_MIN_W | 最小宽度。  
WIDGET_PROP_MAX_W | 最大宽度。  
WIDGET_PROP_AUTO_ADJUST_SIZE | 根据子控件和文本自动调整大小。  
WIDGET_PROP_SINGLE_INSTANCE | 窗口是否保持单例。  
WIDGET_PROP_STRONGLY_FOCUS | 点击非focusable控件时，是否让当前焦点控件失去焦点。比如点击窗口空白区域，是否让编辑器失去焦点。  
WIDGET_PROP_CHILDREN_LAYOUT | 子控件布局参数。  
WIDGET_PROP_LAYOUT | 子控件布局参数(过时)。  
WIDGET_PROP_SELF_LAYOUT | 控件布局参数。  
WIDGET_PROP_LAYOUT_W | layout宽度。  
WIDGET_PROP_LAYOUT_H | layout高度。  
WIDGET_PROP_VIRTUAL_W | 虚拟宽度。  
WIDGET_PROP_VIRTUAL_H | 虚拟高度。  
WIDGET_PROP_LOADING | 控件正在加载。  
WIDGET_PROP_NAME | 名称。  
WIDGET_PROP_TYPE | 类型。  
WIDGET_PROP_CLOSABLE | 是否可以关闭。  
WIDGET_PROP_POINTER_CURSOR | 鼠标指针。  
WIDGET_PROP_VALUE | 值。  
WIDGET_PROP_EASY_TOUCH_MODE | 容易点击模式(目前用于spinbox)。  
WIDGET_PROP_RADIO | CheckButton是否单选。  
WIDGET_PROP_REVERSE | 进度条反向显示。  
WIDGET_PROP_LENGTH | 长度。  
WIDGET_PROP_LINE_WRAP | 自动换行。  
WIDGET_PROP_WORD_WRAP | 是否允许单词中换行。  
WIDGET_PROP_ELLIPSES | 是否省略。  
WIDGET_PROP_VISIBLE_REVEAL_IN_SCROLL | 可见控件在滚动控件中的可见处理方案。（影响 widget_ensure_visible_in_viewport 函数）  
WIDGET_PROP_TEXT | 文本。  
WIDGET_PROP_TR_TEXT | 待翻译文本。  
WIDGET_PROP_STYLE | style。  
WIDGET_PROP_STATE | 状态。  
WIDGET_PROP_ENABLE | 是否启用。  
WIDGET_PROP_FEEDBACK | 是否启用按键音等反馈。  
WIDGET_PROP_FLOATING | 是否启用floating布局。  
WIDGET_PROP_MARGIN | 边距。  
WIDGET_PROP_SPACING | 间距。  
WIDGET_PROP_LEFT_MARGIN | 左边距。  
WIDGET_PROP_RIGHT_MARGIN | 右边距。  
WIDGET_PROP_TOP_MARGIN | 顶边距。  
WIDGET_PROP_BOTTOM_MARGIN | 底边距。  
WIDGET_PROP_STEP | 步长。  
WIDGET_PROP_VISIBLE | 是否可见。  
WIDGET_PROP_SENSITIVE | 是否接受用户事件。  
WIDGET_PROP_APPLET_NAME | 窗口所属的小应用程序(applet)名称。  
WIDGET_PROP_ANIMATION | 控件动画。  
WIDGET_PROP_ANIM_HINT | 窗口动画。  
WIDGET_PROP_FULLSCREEN | 窗口设置为全部大小。  
WIDGET_PROP_DISABLE_ANIM | 禁用窗口动画。  
WIDGET_PROP_OPEN_ANIM_HINT | 打开窗口时的动画。  
WIDGET_PROP_CLOSE_ANIM_HINT | 关闭窗口时的动画。  
WIDGET_PROP_MIN | 最小值。  
WIDGET_PROP_ACTION_TEXT | 软键盘上action按钮的文本。  
WIDGET_PROP_TIPS | 提示信息。  
WIDGET_PROP_TR_TIPS | 需要翻译的提示信息。  
WIDGET_PROP_INPUT_TYPE | 输入类型。  
WIDGET_PROP_KEYBOARD | 自定义软键盘资源名称。  
WIDGET_PROP_DEFAULT_FOCUSED_CHILD | 缺省获得焦点的子控件(可用控件名或类型)。  
WIDGET_PROP_READONLY | 只读模式。  
WIDGET_PROP_CANCELABLE | 是否可取消。  
WIDGET_PROP_PASSWORD_VISIBLE | 密码是否可见。  
WIDGET_PROP_ACTIVE | 是否处于active状态。  
WIDGET_PROP_CURR_PAGE | 当前页。  
WIDGET_PROP_PAGE_MAX_NUMBER | 页面最大个数。  
WIDGET_PROP_VERTICAL | 是否为垂直模式。  
WIDGET_PROP_SHOW_TEXT | 是否显示文本。  
WIDGET_PROP_XOFFSET | X方向的偏移。（如果控件有继承 get_offset 函数指针的话，一定要和 get_offset 返回值保持一致，否则容易出现问题）详情请看 docs/how_to_use_offset_in_custom_widget.md  
WIDGET_PROP_YOFFSET | Y方向的偏移。（如果控件有继承 get_offset 函数指针的话，一定要和 get_offset 返回值保持一致，否则容易出现问题）详情请看 docs/how_to_use_offset_in_custom_widget.md  
WIDGET_PROP_ALIGN_V | 垂直对齐模式。  
WIDGET_PROP_ALIGN_H | 水平对齐模式。  
WIDGET_PROP_AUTO_PLAY | 是否自动播放或指定播放的时间(毫秒)。  
WIDGET_PROP_LOOP | 是否循环播放或循环播放的次数。  
WIDGET_PROP_RUNNING | 是否正在运行(播放)。  
WIDGET_PROP_AUTO_FIX | 是否启用自动更正功能。  
WIDGET_PROP_SELECT_NONE_WHEN_FOCUSED | 编辑器在获得焦点时是否不选中文本。  
WIDGET_PROP_OPEN_IM_WHEN_FOCUSED | 编辑器在获得焦点时是否打开输入法。  
WIDGET_PROP_CLOSE_IM_WHEN_BLURED | 编辑器在失去焦点时是否关闭输入法。  
WIDGET_PROP_X_MIN | X最小值。  
WIDGET_PROP_X_MAX | X最大值。  
WIDGET_PROP_Y_MIN | Y最小值。  
WIDGET_PROP_Y_MAX | Y最大值。  
WIDGET_PROP_MAX | 最大值。  
WIDGET_PROP_GRAB_KEYS | 让窗口管理器直接把按键发给自己。  
WIDGET_PROP_ROW | 行数或每行的高度。  
WIDGET_PROP_STATE_FOR_STYLE | 控件状态。  
WIDGET_PROP_THEME | 窗体样式名称。  
WIDGET_PROP_STAGE | window stage  
WIDGET_PROP_IMAGE_MANAGER | 图片管理器。  
WIDGET_PROP_ASSETS_MANAGER | 资源管理器。  
WIDGET_PROP_LOCALE_INFO | locale_info。  
WIDGET_PROP_FONT_MANAGER | 字体管理器。  
WIDGET_PROP_THEME_OBJ | 窗口的窗体样式对象。  
WIDGET_PROP_DEFAULT_THEME_OBJ | 缺省的窗体样式对象。  
WIDGET_PROP_ITEM_WIDTH | 项的宽度。  
WIDGET_PROP_ITEM_HEIGHT | 项的高度。  
WIDGET_PROP_DEFAULT_ITEM_HEIGHT | 项的缺省高度。  
WIDGET_PROP_XSLIDABLE | X方向是否可拖动。  
WIDGET_PROP_YSLIDABLE | Y方向是否可拖动。  
WIDGET_PROP_REPEAT | 重复次数。  
WIDGET_PROP_LONG_PRESS_TIME | 触发长按事件的时间(毫秒)。  
WIDGET_PROP_ENABLE_LONG_PRESS | 是否启用长按。  
WIDGET_PROP_ENABLE_PREVIEW | 是否启用预览。  
WIDGET_PROP_CLICK_THROUGH | 是否启用点击穿透。  
WIDGET_PROP_ANIMATABLE | 是否启用动画。  
WIDGET_PROP_AUTO_HIDE | 是否自动隐藏。  
WIDGET_PROP_AUTO_HIDE_SCROLL_BAR | 是否自动隐藏滚动条。  
WIDGET_PROP_IMAGE | 图片名称。  
WIDGET_PROP_FORMAT | 显示格式。  
WIDGET_PROP_DRAW_TYPE | 图片绘制类型。  
WIDGET_PROP_SELECTABLE | 是否可选择。  
WIDGET_PROP_CLICKABLE | 是否可点击。  
WIDGET_PROP_SCALE_X | X方向缩放比例。  
WIDGET_PROP_SCALE_Y | Y方向缩放比例。  
WIDGET_PROP_ANCHOR_X | x锚点。  
WIDGET_PROP_ANCHOR_Y | y锚点。  
WIDGET_PROP_ROTATION | 选中角度(幅度)  
WIDGET_PROP_COMPACT | 紧凑模式。  
WIDGET_PROP_SCROLLABLE | 是否支持滚动。  
WIDGET_PROP_ICON | 图标名称。  
WIDGET_PROP_OPTIONS | 选项集合。  
WIDGET_PROP_SELECTED | 是否被选中。  
WIDGET_PROP_CHECKED | 是否被勾选。  
WIDGET_PROP_ACTIVE_ICON | active状态下的图标。  
WIDGET_PROP_LOAD_UI | 动态加载UI名字。  
WIDGET_PROP_OPEN_WINDOW | 要打开窗口的名称。  
WIDGET_PROP_THEME_OF_POPUP | ComboBox打开弹出窗口的主题。  
WIDGET_PROP_SELECTED_INDEX | 被选中项的索引。  
WIDGET_PROP_CLOSE_WHEN_CLICK | 点击窗口时关闭窗口。  
WIDGET_PROP_CLOSE_WHEN_CLICK_OUTSIDE | 点击窗口外部时关闭窗口。  
WIDGET_PROP_CLOSE_WHEN_TIMEOUT | 超时后关闭窗口。  
WIDGET_PROP_LINE_GAP | 行间距。  
WIDGET_PROP_BG_COLOR | 背景颜色(仅仅使用于color tile)。  
WIDGET_PROP_BORDER_COLOR | 边框颜色(仅仅使用于color tile)。  
WIDGET_PROP_DELAY | 延迟时间(毫秒)  
WIDGET_PROP_IS_KEYBOARD | 是否为键盘。  
WIDGET_PROP_FOCUSED | 是否为焦点控件。  
WIDGET_PROP_FOCUS | (过时请用focused)。  
WIDGET_PROP_FOCUSABLE | 是否支持焦点停留。  
WIDGET_PROP_WITH_FOCUS_STATE | 是否支持焦点状态(如果希望style支持焦点状态，但又不希望焦点停留，可用本属性)。  
WIDGET_PROP_MOVE_FOCUS_PREV_KEY | 将焦点移到前一个的键值。  
WIDGET_PROP_MOVE_FOCUS_NEXT_KEY | 将焦点移到后一个的键值。  
WIDGET_PROP_MOVE_FOCUS_UP_KEY | 将焦点向上移动的键值。  
WIDGET_PROP_MOVE_FOCUS_DOWN_KEY | 将焦点向下移动的键值。  
WIDGET_PROP_MOVE_FOCUS_LEFT_KEY | 将焦点向左移动的键值。  
WIDGET_PROP_MOVE_FOCUS_RIGHT_KEY | 将焦点向右移动的键值。  
WIDGET_PROP_ROWS | 行数。  
WIDGET_PROP_SHOW_GRID | 是否显示网格线。  
WIDGET_PROP_COLUMNS_DEFINITION | 各列的定义。  
WIDGET_PROP_DRAG_THRESHOLD | 拖拽临界值。  
WIDGET_PROP_ANIMATING_TIME | 动画时间(毫秒)。  
WIDGET_PROP_ANIMATE_PREFIX | 改变控件属性时附带动画的前缀。  
WIDGET_PROP_ANIMATE_ANIMATING_TIME | 改变控件属性时附带动画的播放时间(毫秒)。  
WIDGET_PROP_DIRTY_RECT | 控件脏矩形区域。  
WIDGET_PROP_SCREEN_SAVER_TIME | 屏幕保护时间(毫秒)。  
WIDGET_PROP_SHOW_FPS | 是否显示FPS。  
WIDGET_PROP_MAX_FPS | 最大FPS。  
WIDGET_PROP_VALIDATOR | 数据校验脚本。
