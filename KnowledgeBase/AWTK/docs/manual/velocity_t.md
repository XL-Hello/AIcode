## velocity_t

### 概述

## velocity。

### 函数

函数名称 | 说明  
---|---  
velocity_reset | 重置状态。  
velocity_update | 更新位置。  
  
#### velocity_reset 函数

* * *

  * 函数功能：



> 重置状态。

  * 函数原型：


    
    
    velocity_t* velocity_reset (velocity_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | velocity_t* | 返回velocity对象。  
v | velocity_t* | velocity对象。  
  
#### velocity_update 函数

* * *

  * 函数功能：



> 更新位置。

  * 函数原型：


    
    
    ret_t velocity_update (velocity_t* v, uint64_t time, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
v | velocity_t* | velocity对象。  
time | uint64_t | 时间(毫秒)。  
x | xy_t | x坐标。  
y | xy_t | y坐标。
