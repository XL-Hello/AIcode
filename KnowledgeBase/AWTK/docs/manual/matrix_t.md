## matrix_t

### 概述

## 2D矩阵对象。

### 函数

函数名称 | 说明  
---|---  
matrix_identity | 重置矩阵对象为单位矩阵。  
matrix_init | 初始化矩阵对象。  
matrix_invert | 求矩阵的逆。  
matrix_is_invertible | 判断matrix是否可逆。  
matrix_multiply | 矩阵相乘。  
matrix_rotate | 旋转。  
matrix_scale | 缩放。  
matrix_set | 设置矩阵的参数。  
matrix_transform_point | 对点进行变换。  
matrix_transform_pointf | 对点进行变换。  
matrix_translate | 平移。  
  
#### matrix_identity 函数

* * *

  * 函数功能：



> 重置矩阵对象为单位矩阵。

  * 函数原型：


    
    
    matrix_t* matrix_identity (matrix_t* m);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
  
#### matrix_init 函数

* * *

  * 函数功能：



> 初始化矩阵对象。

  * 函数原型：


    
    
    matrix_t* matrix_init (matrix_t* m);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
  
#### matrix_invert 函数

* * *

  * 函数功能：



> 求矩阵的逆。

  * 函数原型：


    
    
    matrix_t* matrix_invert (matrix_t* m);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
  
#### matrix_is_invertible 函数

* * *

  * 函数功能：



> 判断matrix是否可逆。

  * 函数原型：


    
    
    bool_t matrix_is_invertible (matrix_t* m);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示可逆，否则表示不可逆。  
m | matrix_t* | 矩阵对象。  
  
#### matrix_multiply 函数

* * *

  * 函数功能：



> 矩阵相乘。

  * 函数原型：


    
    
    matrix_t* matrix_multiply (matrix_t* m, matrix_t* b);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
b | matrix_t* | 矩阵对象。  
  
#### matrix_rotate 函数

* * *

  * 函数功能：



> 旋转。

  * 函数原型：


    
    
    matrix_t* matrix_rotate (matrix_t* m, float rad);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
rad | float | 角度。  
  
#### matrix_scale 函数

* * *

  * 函数功能：



> 缩放。

  * 函数原型：


    
    
    matrix_t* matrix_scale (matrix_t* m, float sx, float sy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
sx | float | sx  
sy | float | sy  
  
#### matrix_set 函数

* * *

  * 函数功能：



> 设置矩阵的参数。

  * 函数原型：


    
    
    matrix_t* matrix_set (matrix_t* m, float a0, float a1, float a2, float a3, float a4, float a5);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
a0 | float | a0  
a1 | float | a1  
a2 | float | a2  
a3 | float | a3  
a4 | float | a4  
a5 | float | a5  
  
#### matrix_transform_point 函数

* * *

  * 函数功能：



> 对点进行变换。

  * 函数原型：


    
    
    matrix_t* matrix_transform_point (matrix_t* m, xy_t x, xy_t y, xy_t* out_x, xy_t* out_y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
x | xy_t | x  
y | xy_t | y  
out_x | xy_t* | out_x  
out_y | xy_t* | out_y  
  
#### matrix_transform_pointf 函数

* * *

  * 函数功能：



> 对点进行变换。

  * 函数原型：


    
    
    matrix_t* matrix_transform_pointf (matrix_t* m, float x, float y, float* ox, float* oy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
x | float | x  
y | float | y  
ox | float* | out_x  
oy | float* | out_y  
  
#### matrix_translate 函数

* * *

  * 函数功能：



> 平移。

  * 函数原型：


    
    
    matrix_t* matrix_translate (matrix_t* m, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | matrix_t* | 矩阵对象。  
m | matrix_t* | 矩阵对象。  
x | xy_t | x  
y | xy_t | y
