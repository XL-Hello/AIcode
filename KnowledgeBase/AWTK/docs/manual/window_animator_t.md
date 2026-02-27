## window_animator_t

### 概述

## 窗口动画。

### 函数

函数名称 | 说明  
---|---  
window_animator_begin_frame | begin frame  
window_animator_create | 创建窗口动画对象。  
window_animator_destroy | 销毁窗口动画对象。  
window_animator_end_frame | end frame  
window_animator_update | 更新动画。  
  
#### window_animator_begin_frame 函数

* * *

  * 函数功能：



> begin frame

  * 函数原型：


    
    
    ret_t window_animator_begin_frame (window_animator_t* wa);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wa | window_animator_t* | 窗口动画对象。  
  
#### window_animator_create 函数

* * *

  * 函数功能：



> 创建窗口动画对象。
> 
> 供子类构造函数用。

  * 函数原型：


    
    
    window_animator_t* window_animator_create (bool_t open, const window_animator_vtable_t* vt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | window_animator_t* | 返回窗口动画对象。  
open | bool_t | TRUE表示打开窗口的动画，FALSE表示关闭窗口的动画。  
vt | const window_animator_vtable_t* | 虚表对象。  
  
#### window_animator_destroy 函数

* * *

  * 函数功能：



> 销毁窗口动画对象。

  * 函数原型：


    
    
    ret_t window_animator_destroy (window_animator_t* wa);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wa | window_animator_t* | 窗口动画对象。  
  
#### window_animator_end_frame 函数

* * *

  * 函数功能：



> end frame

  * 函数原型：


    
    
    ret_t window_animator_end_frame (window_animator_t* wa);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wa | window_animator_t* | 窗口动画对象。  
  
#### window_animator_update 函数

* * *

  * 函数功能：



> 更新动画。

  * 函数原型：


    
    
    ret_t window_animator_update (window_animator_t* wa, uint64_t time_ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
wa | window_animator_t* | 窗口动画对象。  
time_ms | uint64_t | 当前时间(毫秒)。
