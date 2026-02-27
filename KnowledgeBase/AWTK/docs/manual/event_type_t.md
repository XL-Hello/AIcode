## event_type_t

### 概述

类型常量定义。

### 常量

名称 | 说明  
---|---  
EVT_POINTER_DOWN | 指针按下事件名(pointer_event_t)。  
EVT_POINTER_DOWN_BEFORE_CHILDREN | 指针按下事件名，在子控件处理之前触发(pointer_event_t)。  
EVT_POINTER_MOVE | 指针移动事件名(pointer_event_t)。  
EVT_POINTER_MOVE_BEFORE_CHILDREN | 指针移动事件名，在子控件处理之前触发(pointer_event_t)。  
EVT_POINTER_UP | 指针抬起事件名(pointer_event_t)。  
EVT_POINTER_UP_BEFORE_CHILDREN | 指针抬起事件名，在子控件处理之前触发(pointer_event_t)。  
EVT_WHEEL | 滚轮事件名(wheel_event_t)。  
EVT_WHEEL_BEFORE_CHILDREN | 鼠标滚轮事件名，在子控件处理之前触发(wheel_event_t)。  
EVT_POINTER_DOWN_ABORT | 取消前一个指针按下事件名(pointer_event_t)。  
EVT_CONTEXT_MENU | 右键/长按弹出上下文菜单的事件名(pointer_event_t)。  
EVT_POINTER_ENTER | 指针进入事件名(pointer_event_t)。  
EVT_POINTER_LEAVE | 指针离开事件名(pointer_event_t)。  
EVT_LONG_PRESS | 长按事件名(pointer_event_t)。  
EVT_CLICK | 点击事件名(pointer_event_t)。  
EVT_DOUBLE_CLICK | 双击事件名(pointer_event_t)。  
EVT_FOCUS | 得到焦点事件名(event_t)。  
EVT_BLUR | 失去焦点事件名(event_t)。  
EVT_KEY_DOWN | 键按下事件名(key_event_t)。  
EVT_KEY_LONG_PRESS | 键长按事件名(key_event_t)。  
EVT_KEY_DOWN_BEFORE_CHILDREN | 键按下事件名，在子控件处理之前触发(key_event_t)。  
EVT_KEY_REPEAT | 按键repeat事件名(key_event_t)。  
EVT_KEY_UP | 键抬起事件名(key_event_t)。  
EVT_KEY_UP_BEFORE_CHILDREN | 键抬起事件名，在子控件处理之前触发(key_event_t)。  
EVT_WILL_MOVE | 即将移动Widget的事件名(event_t)。  
EVT_MOVE | 移动Widget的事件名(event_t)。  
EVT_WILL_RESIZE | 即将调整Widget大小的事件名(event_t)。  
EVT_RESIZE | 调整Widget大小的事件名(event_t)。  
EVT_WILL_MOVE_RESIZE | 即将调整Widget大小/位置的事件名(event_t)。  
EVT_MOVE_RESIZE | 调整Widget大小/位置的事件名(event_t)。  
EVT_PAINT | 绘制的事件名(paint_event_t)。  
EVT_BEFORE_PAINT | 即将绘制的事件名(paint_event_t)。  
EVT_AFTER_PAINT | 绘制完成的事件名(paint_event_t)。  
EVT_PAINT_DONE | 绘制完成(canvas状态已经恢复)的事件名(paint_event_t)。  
EVT_LOCALE_CHANGED | locale改变的事件(event_t)。  
EVT_ANIM_START | 控件动画开始事件(event_t)。  
EVT_ANIM_STOP | 控件动画被主动停止的事件(event_t)。  
EVT_ANIM_PAUSE | 控件动画被暂停的事件(event_t)。  
EVT_ANIM_ONCE | 控件动画yoyo/repeat时，完成一次的事件(event_t)。  
EVT_ANIM_END | 控件动画完成事件(event_t)。  
EVT_WINDOW_LOAD | 窗口加载完成事件(event_t)。  
EVT_WIDGET_LOAD | 控件加载完成事件(event_t)。  
EVT_WINDOW_WILL_OPEN | 窗口即将打开事件(event_t)。如果有窗口动画，在窗口动画开始前触发。如果没有窗口动画，在窗口被加载后的下一次循环中触发。  
EVT_WINDOW_OPEN | 窗口打开事件(event_t)。如果有窗口动画，在窗口动画完成时触发。如果没有窗口动画，在窗口被加载后的下一次循环中触发。  
EVT_WINDOW_TO_BACKGROUND | 窗口被切换到后台事件(event_t)。打开新窗口时，当前窗口被切换到后台时，对当前窗口触发本事件。  
EVT_WINDOW_TO_FOREGROUND | 窗口被切换到前台事件(event_t)。关闭当前窗口时，前一个窗口被切换到前台时，对前一个窗口触发本事件。  
EVT_WINDOW_CLOSE | 窗口关闭事件。  
EVT_REQUEST_CLOSE_WINDOW | 请求关闭窗口的事件(event_t)。  
EVT_TOP_WINDOW_CHANGED | 顶层窗口改变的事件(window_event_t)。  
EVT_IM_START | 输入法启动(event_t)。  
EVT_IM_STOP | 输入法停止(event_t)。  
EVT_IM_COMMIT | 输入法提交输入的文本事件(im_commit_event_t)。  
EVT_IM_CLEAR | 清除编辑器内容(event_t)。  
EVT_IM_CANCEL | 取消编辑，恢复之前的内容(event_t)。  
EVT_IM_PREEDIT | 进入预编辑状态(event_t)。  
EVT_IM_PREEDIT_CONFIRM | 确认预编辑内容，退出预编辑状态(event_t)。  
EVT_IM_PREEDIT_ABORT | 删除预编辑内容，退出预编辑状态event_t)。  
EVT_IM_SHOW_CANDIDATES | 输入法请求显示候选字事件(im_candidates_event_t)。  
EVT_IM_SHOW_PRE_CANDIDATES | 输入法请求显示预候选字事件(im_candidates_event_t)。  
EVT_IM_LANG_CHANGED | 输入法语言改变事件(event_t)。  
EVT_IM_ACTION | 软键盘Action点击事件(event_t)。  
EVT_IM_ACTION_INFO | 请求更新软键盘上的Action按钮的信息(im_action_button_info_event_t)。  
EVT_DRAG_START | 开始拖动(event_t)。  
EVT_DRAG | 拖动(event_t)。  
EVT_DRAG_END | 结束拖动(event_t)。  
EVT_RESET | Reset(event_t)。  
EVT_SCREEN_SAVER | 在指定的时间内，没有用户输入事件，由窗口管理器触发。  
EVT_LOW_MEMORY | 内存不足(event_t)。  
EVT_OUT_OF_MEMORY | 内存耗尽(event_t)。  
EVT_ORIENTATION_WILL_CHANGED | 屏幕即将旋转(event_t)。  
EVT_ORIENTATION_CHANGED | 屏幕旋转(event_t)。  
EVT_WIDGET_CREATED | 控件创建事件(event_t)。  
EVT_REQUEST_QUIT_APP | 请求退出应用程序事件。点击原生窗口关闭按钮时，通过窗口管理器触发，注册该事件并返回RET_STOP，可以阻止窗口关闭。  
EVT_THEME_WILL_CHANGE | 即将改变主题(event_t)。  
EVT_THEME_CHANGED | 主题变化(event_t)。  
EVT_WIDGET_WILL_UPDATE_STYLE | 控件根据自己当前状态即将更新style(event_t)。  
EVT_WIDGET_UPDATE_STYLE | 控件根据自己当前状态更新style(event_t)。  
EVT_WIDGET_ADD_CHILD | 控件加载新的子控件(event_t)。  
EVT_WIDGET_REMOVE_CHILD | 控件移除子控件(event_t)。  
EVT_SCROLL_START | scroll view开始滚动(event_t)。  
EVT_SCROLL | scroll view滚动(event_t)。  
EVT_SCROLL_END | scroll view结束滚动(event_t)。  
EVT_MULTI_GESTURE | 多点触摸手势(multi_gesture_event_t)。  
EVT_PAGE_CHANGED | 当前看到的页面改变了(event_t)。  
EVT_PAGE_CHANGING | 当前看到的页面正在改变(offset_change_event_t)。  
EVT_ASSET_MANAGER_LOAD_ASSET | 资源管理加载某个资源(assets_event_t)。  
EVT_ASSET_MANAGER_UNLOAD_ASSET | 资源管理卸载某个资源(assets_event_t)。  
EVT_ASSET_MANAGER_CLEAR_CACHE | 资源管理移除同种资源缓存(assets_event_t)。  
EVT_TIMER | 定时器(event_t)。  
EVT_DATA | 数据到来(event_t)。  
EVT_CONNECT | 客户连接到来(event_t)。  
EVT_MODEL_CHANGE | 模型变化。用于fscript实现窗口间通讯(model_event_t)。  
EVT_SYSTEM | SDL系统事件(system_event_t)。  
EVT_DROP_FILE | SDL文件拖入事件(drop_file_event_t)。  
EVT_LOCALE_INFOS_LOAD_INFO | locale_infos加载某个本地化信息(event_t)。  
EVT_LOCALE_INFOS_UNLOAD_INFO | locale_infos卸载某个本地化信息(event_t)。  
EVT_ACTIVATED | 控件进入激活状态(event_t)。  
EVT_UNACTIVATED | 控件退出激活状态(event_t)。  
EVT_UI_LOAD | UI加载完成事件(event_t)。  
EVT_TOUCH_DOWN | 触摸按下事件名(touch_event_t)。  
EVT_TOUCH_MOVE | 触摸移动事件名(touch_event_t)。  
EVT_TOUCH_UP | 触摸抬起事件名(touch_event_t)。  
EVT_REQ_START | event queue其它请求编号起始值。  
EVT_USER_START | 用户定义事件起始值。  
EVT_NONE | 无效事件名称。  
EVT_PROP_WILL_CHANGE | 对象的属性即将改变的事件名(prop_change_event_t)。  
EVT_PROP_CHANGED | 对象的属性改变的事件名(prop_change_event_t)。  
EVT_CMD_WILL_EXEC | 对象即将执行命令(cmd_exec_event_t)。  
EVT_CMD_EXECED | 对象完成执行命令(cmd_exec_event_t)。  
EVT_CMD_CAN_EXEC | 对象命令是否能执行指定的命令(cmd_exec_event_t)。  
EVT_ITEMS_WILL_CHANGE | 即将增加和删除集合中的项目(event_t)。  
EVT_ITEMS_CHANGED | 完成增加和删除集合中的项目(event_t)。  
EVT_PROPS_CHANGED | 对象的属性改变的事件名(props_event_t)。  
EVT_PROGRESS | 进度状态(progress_event_t)。  
EVT_DONE | 完成(done_event_t)。  
EVT_ERROR | 错误(error_event_t)。  
EVT_DESTROY | 对象销毁事件名(event_t)。  
EVT_VALUE_WILL_CHANGE | 值即将改变的事件名(value_change_event_t)。  
EVT_VALUE_CHANGED | 值改变的事件名(value_change_event_t)。  
EVT_VALUE_CHANGING | 值持续改变(如编辑器正在编辑)的事件名(value_change_event_t)。  
EVT_LOG_MESSAGE | 日志信息。
