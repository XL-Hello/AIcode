## combo_box_item_t

### 概述

![image](images/combo_box_item_t_0.png)

ComboBox Item控件。

## 本类仅供combo_box控件内部使用。

### 函数

函数名称 | 说明  
---|---  
combo_box_item_cast | 转换combo_box_item对象(供脚本语言使用)。  
combo_box_item_create | 创建combo_box_item对象  
combo_box_item_get_widget_vtable | 获取 combo_box_item 虚表。  
combo_box_item_set_checked | 设置控件是否被选中。  
combo_box_item_set_value | 设置控件的值。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
checked | bool_t | 是否被选中。  
value | int32_t | 值。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_CLICK | pointer_event_t | 点击事件。  
EVT_VALUE_WILL_CHANGE | value_change_event_t | 值(勾选状态)即将改变事件。  
EVT_VALUE_CHANGED | value_change_event_t | 值(勾选状态)改变事件。  
  
#### combo_box_item_cast 函数

* * *

  * 函数功能：



> 转换combo_box_item对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* combo_box_item_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | combo_box_item对象。  
widget | widget_t* | combo_box_item对象。  
  
#### combo_box_item_create 函数

* * *

  * 函数功能：



> 创建combo_box_item对象

  * 函数原型：


    
    
    widget_t* combo_box_item_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### combo_box_item_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 combo_box_item 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* combo_box_item_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 combo_box_item 虚表。  
  
#### combo_box_item_set_checked 函数

* * *

  * 函数功能：



> 设置控件是否被选中。

  * 函数原型：


    
    
    ret_t combo_box_item_set_checked (widget_t* widget, bool_t checked);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | combo_box_item对象。  
checked | bool_t | 是否被选中。  
  
#### combo_box_item_set_value 函数

* * *

  * 函数功能：



> 设置控件的值。

  * 函数原型：


    
    
    ret_t combo_box_item_set_value (widget_t* widget, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | combo_box_item对象。  
value | int32_t | 值  
  
#### checked 属性

* * *

> 是否被选中。

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
  
#### value 属性

* * *

> 值。

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
