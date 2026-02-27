## grid_t

### 概述

![image](images/grid_t_0.png)

网格。 在xml中使用”grid”标签创建控件。如：
    
    
    <!-- ui -->
    <grid x="c" y="50" w="100" h="100"/>
    

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：
    
    
    <!-- style -->
    <grid>
    <style name="default" grid_color="gray" border_color="black" odd_bg_color="#f5f5f5" even_bg_color="#eeeeee">
    <normal />
    </style>
    </grid>
    

* * *

### 函数

函数名称 | 说明  
---|---  
grid_cast | 转换为grid对象(供脚本语言使用)。  
grid_create | 创建grid对象  
grid_get_widget_vtable | 获取 grid 虚表。  
grid_set_columns_definition | 设置 各列的参数。  
grid_set_rows | 设置 行数。  
grid_set_show_grid | 设置 是否显示网格。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
columns_definition | char* | 各列的参数。  
rows | uint32_t | 行数。  
show_grid | bool_t | 是否显示网格。  
  
#### grid_cast 函数

* * *

  * 函数功能：



> 转换为grid对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* grid_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | grid对象。  
widget | widget_t* | grid对象。  
  
#### grid_create 函数

* * *

  * 函数功能：



> 创建grid对象

  * 函数原型：


    
    
    widget_t* grid_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | grid对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### grid_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 grid 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* grid_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 grid 虚表。  
  
#### grid_set_columns_definition 函数

* * *

  * 函数功能：



> 设置 各列的参数。

  * 函数原型：


    
    
    ret_t grid_set_columns_definition (widget_t* widget, const char* columns_definition);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
columns_definition | const char* | 各列的参数。  
  
#### grid_set_rows 函数

* * *

  * 函数功能：



> 设置 行数。

  * 函数原型：


    
    
    ret_t grid_set_rows (widget_t* widget, uint32_t rows);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
rows | uint32_t | 行数。  
  
#### grid_set_show_grid 函数

* * *

  * 函数功能：



> 设置 是否显示网格。

  * 函数原型：


    
    
    ret_t grid_set_show_grid (widget_t* widget, bool_t show_grid);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
show_grid | bool_t | 是否显示网格。  
  
#### columns_definition 属性

* * *

> 各列的参数。 各列的参数之间用英文的分号(;)分隔，每列参数的格式为：

col(w=?,left_margin=?,right_margin=?,top_maorgin=?,bottom_margin=?)

  * w 为列的宽度（必须存在）。取值在 (0-1] 区间时，视为 grid 控件宽度的比例，否则为像素宽度。 （如果为负数，将计算结果加上控件的宽度）
  * left_margin（可选，可缩写为 l）该列左边的边距。
  * right_margin（可选，可缩写为 r）该列右边的边距。
  * top_margin（可选，可缩写为 t）该列顶部的边距。
  * bottom_margin（可选，可缩写为 b）该列底部的边距。
  * margin（可选，可缩写为 m）同时指定上面 4 个边距。
  * fill_available（可选，可缩写为f）填充剩余宽度（只有一列可以指定）。

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
  
#### rows 属性

* * *

> 行数。

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
  
#### show_grid 属性

* * *

> 是否显示网格。

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
