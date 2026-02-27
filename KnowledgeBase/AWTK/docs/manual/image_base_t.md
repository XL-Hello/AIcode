## image_base_t

### 概述

![image](images/image_base_t_0.png)

图片控件基类。

本类把图片相关控件的公共行为进行抽象，放到一起方便重用。目前已知的具体实现如下图：

![image](images/image_base_t_1.png)

> 本类是一个抽象类，不能进行实例化。请在应用程序中使用具体的类，如image_t。

如果需要显示文件系统中的图片，只需将图片名称换成实际的文件名，并加上”file://”前缀即可。如：
    
    
    <image draw_type="center" image="file://./design/default/images/xx/flag_CN.png" />
    <gif image="file://./design/default/images/x2/bee.gif" />
    <svg image="file://./design/default/images/svg/china.bsvg" />
    

* * *

### 函数

函数名称 | 说明  
---|---  
image_base_cast | 转换为image_base对象(供脚本语言使用)。  
image_base_get_widget_vtable | 获取 image_base 虚表。  
image_base_set_anchor | 设置控件的锚点(仅在WITH_VGCANVAS定义时生效)。  
image_base_set_clickable | 设置控件是否可以被点击。  
image_base_set_image | 设置控件的图片名称。  
image_base_set_rotation | 设置控件的旋转角度(仅在WITH_VGCANVAS定义时生效)。  
image_base_set_scale | 设置控件的缩放比例(仅在WITH_VGCANVAS定义时生效)。  
image_base_set_selectable | 设置控件是否可以被选中。  
image_base_set_selected | 设置控件的选中状态。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
anchor_x | float_t | 锚点X(0-1)。0在控件左边，0.5在控件中间，1在控件右边。  
anchor_y | float_t | 锚点Y(0-1)。0在控件顶部，0.5在控件中间，1在控件底部。  
clickable | bool_t | 点击时，是否触发EVT_CLICK事件。  
image | char* | 图片的名称。  
rotation | float_t | 控件的旋转角度(幅度)。  
scale_x | float_t | 控件在X方向上的缩放比例。  
scale_y | float_t | 控件在Y方向上的缩放比例。  
selectable | bool_t | 是否设置选中状态。  
selected | bool_t | 当前是否被选中。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_CLICK | pointer_event_t | 点击事件。  
  
#### image_base_cast 函数

* * *

  * 函数功能：



> 转换为image_base对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* image_base_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | image_base对象。  
widget | widget_t* | image_base对象。  
  
#### image_base_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 image_base 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* image_base_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 image_base 虚表。  
  
#### image_base_set_anchor 函数

* * *

  * 函数功能：



> 设置控件的锚点(仅在WITH_VGCANVAS定义时生效)。

  * 函数原型：


    
    
    ret_t image_base_set_anchor (widget_t* widget, float_t anchor_x, float_t anchor_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
anchor_x | float_t | 锚点X(0-1)。0在控件左边，0.5在控件中间，1在控件右边。  
anchor_y | float_t | 锚点Y(0-1)。0在控件顶部，0.5在控件中间，1在控件底部。  
  
#### image_base_set_clickable 函数

* * *

  * 函数功能：



> 设置控件是否可以被点击。

  * 函数原型：


    
    
    ret_t image_base_set_clickable (widget_t* widget, bool_t clickable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
clickable | bool_t | 是否可以被点击。  
  
#### image_base_set_image 函数

* * *

  * 函数功能：



> 设置控件的图片名称。
> 
> 如果需要显示文件系统中的图片，只需将图片名称换成实际的文件名，并加上”file://”前缀即可。

  * 函数原型：


    
    
    ret_t image_base_set_image (widget_t* widget, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | image对象。  
name | const char* | 图片名称，该图片必须存在于资源管理器。  
  
#### image_base_set_rotation 函数

* * *

  * 函数功能：



> 设置控件的旋转角度(仅在WITH_VGCANVAS定义时生效)。

  * 函数原型：


    
    
    ret_t image_base_set_rotation (widget_t* widget, float_t rotation);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
rotation | float_t | 旋转角度(幅度)。  
  
#### image_base_set_scale 函数

* * *

  * 函数功能：



> 设置控件的缩放比例(仅在WITH_VGCANVAS定义时生效)。

  * 函数原型：


    
    
    ret_t image_base_set_scale (widget_t* widget, float_t scale_x, float_t scale_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
scale_x | float_t | X方向缩放比例。  
scale_y | float_t | Y方向缩放比例。  
  
#### image_base_set_selectable 函数

* * *

  * 函数功能：



> 设置控件是否可以被选中。

  * 函数原型：


    
    
    ret_t image_base_set_selectable (widget_t* widget, bool_t selectable);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
selectable | bool_t | 是否可以被选中。  
  
#### image_base_set_selected 函数

* * *

  * 函数功能：



> 设置控件的选中状态。

  * 函数原型：


    
    
    ret_t image_base_set_selected (widget_t* widget, bool_t selected);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
selected | bool_t | 是否被选中。  
  
#### anchor_x 属性

* * *

> 锚点X(0-1)。0在控件左边，0.5在控件中间，1在控件右边。

  * 类型：float_t

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
  
#### anchor_y 属性

* * *

> 锚点Y(0-1)。0在控件顶部，0.5在控件中间，1在控件底部。

  * 类型：float_t

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
  
#### clickable 属性

* * *

> 点击时，是否触发EVT_CLICK事件。

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
  
#### image 属性

* * *

> 图片的名称。

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
  
#### rotation 属性

* * *

> 控件的旋转角度(幅度)。

  * 类型：float_t

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
  
#### scale_x 属性

* * *

> 控件在X方向上的缩放比例。

  * 类型：float_t

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
  
#### scale_y 属性

* * *

> 控件在Y方向上的缩放比例。

  * 类型：float_t

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
  
#### selectable 属性

* * *

> 是否设置选中状态。

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
  
#### selected 属性

* * *

> 当前是否被选中。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
