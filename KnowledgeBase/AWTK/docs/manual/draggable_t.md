## draggable_t

### 概述

![image](images/draggable_t_0.png)

将draggable放入目标控件，即可让目标控件或当前窗口可以被拖动。

draggable_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于draggable_t控件。

在xml中使用”draggable”标签创建draggable控件。如：
    
    
    <button text="Drag Me" w="80" h="40" x="10" y="10">
    <draggable />
    </button>
    

拖动对话框标题时移动对话框：
    
    
    <dialog_title x="0" y="0" w="100%" h="30" text="Hello AWTK" >
    <draggable drag_window="true"/>
    </dialog_title>
    

> 更多用法请参考： [draggable.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/draggable.xml)

在c代码中使用函数draggable_create创建按钮控件。如：
    
    
    widget_t* draggable = draggable_create(target, 0, 0, 0, 0);
    

## > draggable本身不可见，故无需style。

### 函数

函数名称 | 说明  
---|---  
draggable_cast | 转换为draggable对象(供脚本语言使用)。  
draggable_create | 创建draggable对象  
draggable_get_widget_vtable | 获取 draggable 虚表。  
draggable_set_allow_out_of_screen | 设置是否无范围限制拖动。  
draggable_set_bottom | 设置bottom。  
draggable_set_drag_native_window | 设置drag_native_window。  
draggable_set_drag_parent | 设置drag_parent。  
draggable_set_drag_window | 设置drag_window。  
draggable_set_horizontal_only | 设置horizontal_only。  
draggable_set_left | 设置left。  
draggable_set_right | 设置right。  
draggable_set_top | 设置top。  
draggable_set_vertical_only | 设置vertical_only。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
allow_out_of_screen | bool_t | 支持超出原生窗口边界拖动。（无法完全移出原生窗口，同时优先受到拖动范围限制的影响）  
bottom | int32_t | 拖动范围的底部限制。缺省为父控件的底部。  
drag_native_window | bool_t | 拖动原生窗口。  
drag_parent | uint32_t | 拖动父控件。0表示直系父控件，1表示父控件的父控件，依次类推。  
drag_window | bool_t | 拖动窗口而不是父控件。比如放在对话框的titlebar上，拖动titlebar其实是希望拖动对话框。  
horizontal_only | bool_t | 只允许水平拖动。  
left | int32_t | 拖动范围的左边限制。缺省为父控件的左边。  
right | int32_t | 拖动范围的右边限制。缺省为父控件的右边边。  
top | int32_t | 拖动范围的顶部限制。缺省为父控件的顶部。  
vertical_only | bool_t | 只允许垂直拖动。  
  
#### draggable_cast 函数

* * *

  * 函数功能：



> 转换为draggable对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* draggable_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | draggable对象。  
widget | widget_t* | draggable对象。  
  
#### draggable_create 函数

* * *

  * 函数功能：



> 创建draggable对象

  * 函数原型：


    
    
    widget_t* draggable_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### draggable_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 draggable 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* draggable_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 draggable 虚表。  
  
#### draggable_set_allow_out_of_screen 函数

* * *

  * 函数功能：



> 设置是否无范围限制拖动。 备注：可以让窗口拖动到外面去。

  * 函数原型：


    
    
    ret_t draggable_set_allow_out_of_screen (widget_t* widget, bool_t allow_out_of_screen);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
allow_out_of_screen | bool_t | 是否无范围限制拖动。  
  
#### draggable_set_bottom 函数

* * *

  * 函数功能：



> 设置bottom。

  * 函数原型：


    
    
    ret_t draggable_set_bottom (widget_t* widget, int32_t bottom);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
bottom | int32_t | 拖动范围的底部限制。缺省为父控件的底部。  
  
#### draggable_set_drag_native_window 函数

* * *

  * 函数功能：



> 设置drag_native_window。

  * 函数原型：


    
    
    ret_t draggable_set_drag_native_window (widget_t* widget, bool_t drag_native_window);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
drag_native_window | bool_t | 是否拖动原生窗口。  
  
#### draggable_set_drag_parent 函数

* * *

  * 函数功能：



> 设置drag_parent。 拖动窗口而不是父控件。比如放在对话框的titlebar上，拖动titlebar其实是希望拖动对话框。

  * 函数原型：


    
    
    ret_t draggable_set_drag_parent (widget_t* widget, uint32_t drag_parent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
drag_parent | uint32_t | 0表示直系父控件，1表示父控件的父控件，依次类推。  
  
#### draggable_set_drag_window 函数

* * *

  * 函数功能：



> 设置drag_window。 拖动窗口而不是父控件。比如放在对话框的titlebar上，拖动titlebar其实是希望拖动对话框。

  * 函数原型：


    
    
    ret_t draggable_set_drag_window (widget_t* widget, bool_t drag_window);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
drag_window | bool_t | 是否拖动窗口。  
  
#### draggable_set_horizontal_only 函数

* * *

  * 函数功能：



> 设置horizontal_only。

  * 函数原型：


    
    
    ret_t draggable_set_horizontal_only (widget_t* widget, bool_t horizontal_only);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
horizontal_only | bool_t | 只允许水平拖动。  
  
#### draggable_set_left 函数

* * *

  * 函数功能：



> 设置left。

  * 函数原型：


    
    
    ret_t draggable_set_left (widget_t* widget, int32_t left);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
left | int32_t | 拖动范围的左边限制。缺省为父控件的左边。  
  
#### draggable_set_right 函数

* * *

  * 函数功能：



> 设置right。

  * 函数原型：


    
    
    ret_t draggable_set_right (widget_t* widget, int32_t right);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
right | int32_t | 拖动范围的右边限制。缺省为父控件的右边边。  
  
#### draggable_set_top 函数

* * *

  * 函数功能：



> 设置top。

  * 函数原型：


    
    
    ret_t draggable_set_top (widget_t* widget, int32_t top);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
top | int32_t | 拖动范围的顶部限制。缺省为父控件的顶部。  
  
#### draggable_set_vertical_only 函数

* * *

  * 函数功能：



> 设置vertical_only。

  * 函数原型：


    
    
    ret_t draggable_set_vertical_only (widget_t* widget, bool_t vertical_only);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
vertical_only | bool_t | 只允许垂直拖动。  
  
#### allow_out_of_screen 属性

* * *

> 支持超出原生窗口边界拖动。（无法完全移出原生窗口，同时优先受到拖动范围限制的影响）

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
  
#### bottom 属性

* * *

> 拖动范围的底部限制。缺省为父控件的底部。

  * 类型：int32_t

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
  
#### drag_native_window 属性

* * *

> 拖动原生窗口。

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
  
#### drag_parent 属性

* * *

> 拖动父控件。0表示直系父控件，1表示父控件的父控件，依次类推。

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
  
#### drag_window 属性

* * *

> 拖动窗口而不是父控件。比如放在对话框的titlebar上，拖动titlebar其实是希望拖动对话框。

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
  
#### horizontal_only 属性

* * *

> 只允许水平拖动。

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
  
#### left 属性

* * *

> 拖动范围的左边限制。缺省为父控件的左边。

  * 类型：int32_t

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
  
#### right 属性

* * *

> 拖动范围的右边限制。缺省为父控件的右边边。

  * 类型：int32_t

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
  
#### top 属性

* * *

> 拖动范围的顶部限制。缺省为父控件的顶部。

  * 类型：int32_t

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
  
#### vertical_only 属性

* * *

> 只允许垂直拖动。

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
