## combo_box_ex_t

### 概述

![image](images/combo_box_ex_t_0.png)

扩展combo_box控件。支持以下功能： * 支持滚动。项目比较多时显示滚动条。 * 自动调整弹出窗口的宽度。根据最长文本自动调整弹出窗口的宽度。 * 支持分组显示。如果item的文本以”seperator.”开头，视为一个分组开始，其后的文本为分组的标题。比如: “seperator.basic”，会创建一个basic为标题的分组。

* * *

### 函数

函数名称 | 说明  
---|---  
combo_box_ex_create | 创建combo_box_ex对象  
combo_box_ex_get_widget_vtable | 获取 combo_box_ex 虚表。  
  
#### combo_box_ex_create 函数

* * *

  * 函数功能：



> 创建combo_box_ex对象

  * 函数原型：


    
    
    widget_t* combo_box_ex_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### combo_box_ex_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 combo_box_ex 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* combo_box_ex_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 combo_box_ex 虚表。
