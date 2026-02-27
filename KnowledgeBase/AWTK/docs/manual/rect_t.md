## rect_t

### 概述

## 矩形。包括一个x坐标、y坐标、宽度和高度。

### 函数

函数名称 | 说明  
---|---  
rect_cast | 转换为rect对象。  
rect_contains | 判断指定的点在rect范围内。  
rect_create | 创建rect对象。  
rect_destroy | 销毁rect对象。  
rect_diff | 求第一个矩形和第二个矩形的差集。  
rect_fix | 确保rect在指定的大小范围内。  
rect_from_rectf | rectf 类型转换到 rect 类型。  
rect_has_intersect | 判断两个rect的是否存在交集。  
rect_init | 初始化rect对象。  
rect_intersect | 求两个rect的交集。  
rect_merge | 合并两个rect对象。  
rect_scale | 缩放rect对象。  
rect_set | 设置rect对象的xywh。  
rect_to_rectf | rect 类型转换到 rectf 类型。  
rectf_fix | 确保rectf在指定的大小范围内。  
rectf_scale | 缩放rectf对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
h | wh_t | 高度。  
w | wh_t | 宽度。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### rect_cast 函数

* * *

  * 函数功能：



> 转换为rect对象。
> 
> 供脚本语言使用。

  * 函数原型：


    
    
    rect_t* rect_cast (rect_t* rect);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t* | rect对象。  
rect | rect_t* | rect对象。  
  
#### rect_contains 函数

* * *

  * 函数功能：



> 判断指定的点在rect范围内。

  * 函数原型：


    
    
    bool_t rect_contains (const rect_t* r, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回在rect范围内。  
r | const rect_t* | rect对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### rect_create 函数

* * *

  * 函数功能：



> 创建rect对象。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    rect_t* rect_create (xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t* | rect对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### rect_destroy 函数

* * *

  * 函数功能：



> 销毁rect对象。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    ret_t rect_destroy (rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
r | rect_t* | rect对象。  
  
#### rect_diff 函数

* * *

  * 函数功能：



> 求第一个矩形和第二个矩形的差集。

备注：第一个矩形包含第二个矩形的话，就会返回第一个矩形的四个矩形区域。

  * 函数原型：


    
    
    bool_t rect_diff (const rect_t* r1, const rect_t* r2, rect_t* out_r1, rect_t* out_r2, rect_t* out_r3, rect_t* out_r4);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在差集，否则表示不存在差集。  
r1 | const rect_t* | 第一个矩形。  
r2 | const rect_t* | 第二个矩形。  
out_r1 | rect_t* | 返回差集的第一个矩形数据。  
out_r2 | rect_t* | 返回差集的第二个矩形数据。  
out_r3 | rect_t* | 返回差集的第三个矩形数据。  
out_r4 | rect_t* | 返回差集的第四个矩形数据。  
  
#### rect_fix 函数

* * *

  * 函数功能：



> 确保rect在指定的大小范围内。

  * 函数原型：


    
    
    rect_t rect_fix (rect_t* r, wh_t max_w, wh_t max_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t | 返回修复之后的rect对象。  
r | rect_t* | rect对象。  
max_w | wh_t | 最大宽度。  
max_h | wh_t | 最大高度。  
  
#### rect_from_rectf 函数

* * *

  * 函数功能：



> rectf 类型转换到 rect 类型。

  * 函数原型：


    
    
    rect_t rect_from_rectf (const rectf_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t | 返回 rect 对象。  
r | const rectf_t* | rectf 对象。  
  
#### rect_has_intersect 函数

* * *

  * 函数功能：



> 判断两个rect的是否存在交集。

  * 函数原型：


    
    
    bool_t rect_has_intersect (const rect_t* r1, const rect_t* r2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
r1 | const rect_t* | rect对象。  
r2 | const rect_t* | rect对象。  
  
#### rect_init 函数

* * *

  * 函数功能：



> 初始化rect对象。

  * 函数原型：


    
    
    rect_t rect_init (xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t | 返回rect对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### rect_intersect 函数

* * *

  * 函数功能：



> 求两个rect的交集。

  * 函数原型：


    
    
    rect_t rect_intersect (const rect_t* r1, const rect_t* r2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t | 返回交集。  
r1 | const rect_t* | rect对象。  
r2 | const rect_t* | rect对象。  
  
#### rect_merge 函数

* * *

  * 函数功能：



> 合并两个rect对象。

  * 函数原型：


    
    
    ret_t rect_merge (rect_t* dst_r, const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dst_r | rect_t* | rect对象。  
r | const rect_t* | rect对象。  
  
#### rect_scale 函数

* * *

  * 函数功能：



> 缩放rect对象。

  * 函数原型：


    
    
    rect_t* rect_scale (rect_t* r, float_t scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t* | 返回rect对象。  
r | rect_t* | rect对象。  
scale | float_t | 缩放比例。  
  
#### rect_set 函数

* * *

  * 函数功能：



> 设置rect对象的xywh。
> 
> 主要供脚本语言使用。

  * 函数原型：


    
    
    rect_t* rect_set (rect_t* rect, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rect_t* | rect对象。  
rect | rect_t* | rect对象。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
w | wh_t | 宽度。  
h | wh_t | 高度。  
  
#### rect_to_rectf 函数

* * *

  * 函数功能：



> rect 类型转换到 rectf 类型。

  * 函数原型：


    
    
    rectf_t rect_to_rectf (const rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rectf_t | 返回 rectf_t 对象。  
r | const rect_t* | rect对象。  
  
#### rectf_fix 函数

* * *

  * 函数功能：



> 确保rectf在指定的大小范围内。

  * 函数原型：


    
    
    rectf_t rectf_fix (rectf_t* r, wh_t max_w, wh_t max_h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rectf_t | 返回修复之后的rect对象。  
r | rectf_t* | rectf对象。  
max_w | wh_t | 最大宽度。  
max_h | wh_t | 最大高度。  
  
#### rectf_scale 函数

* * *

  * 函数功能：



> 缩放rectf对象。

  * 函数原型：


    
    
    rectf_t* rectf_scale (rectf_t* r, float_t scale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | rectf_t* | 返回rect对象。  
r | rectf_t* | rect对象。  
scale | float_t | 缩放比例。  
  
#### h 属性

* * *

> 高度。

  * 类型：wh_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### w 属性

* * *

> 宽度。

  * 类型：wh_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### x 属性

* * *

> x坐标。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### y 属性

* * *

> y坐标。

  * 类型：xy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
