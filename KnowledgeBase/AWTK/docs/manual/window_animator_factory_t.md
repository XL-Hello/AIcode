## window_animator_factory_t

### 概述

窗口动画工厂对象。

提供通过类型创建窗口动画的能力。 让用户可以自定义窗口动画，并获得内置窗口动画同等待遇。

* * *

### 函数

函数名称 | 说明  
---|---  
window_animator_create_for_close | 为关闭窗口创建动画。  
window_animator_create_for_open | 为打开窗口创建动画。  
window_animator_factory | 获取缺省的窗口动画工厂对象。  
window_animator_factory_create | 创建窗口动画工厂对象。  
window_animator_factory_create_animator | 创建指定类型的窗口动画。  
window_animator_factory_destroy | 析构并释放窗口动画工厂对象。  
window_animator_factory_register | 注册窗口动画创建函数。  
window_animator_factory_set | 设置缺省的窗口动画工厂对象。  
  
#### window_animator_create_for_close 函数

* * *

  * 函数功能：



> 为关闭窗口创建动画。

  * 函数原型：


    
    
    window_animator_t* window_animator_create_for_close (const char* type, canvas_t* c, widget_t* prev_win, widget_t* curr_win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | window_animator_t* | 窗口动画对象。  
type | const char* | 动画类型。  
c | canvas_t* | canvas。  
prev_win | widget_t* | 前一窗口。  
curr_win | widget_t* | 当前窗口。  
  
#### window_animator_create_for_open 函数

* * *

  * 函数功能：



> 为打开窗口创建动画。

  * 函数原型：


    
    
    window_animator_t* window_animator_create_for_open (const char* type, canvas_t* c, widget_t* prev_win, widget_t* curr_win);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | window_animator_t* | 窗口动画对象。  
type | const char* | 动画类型。  
c | canvas_t* | canvas。  
prev_win | widget_t* | 前一窗口。  
curr_win | widget_t* | 当前窗口。  
  
#### window_animator_factory 函数

* * *

  * 函数功能：



> 获取缺省的窗口动画工厂对象。

  * 函数原型：


    
    
    window_animator_factory_t* window_animator_factory ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | window_animator_factory_t* | 返回窗口动画工厂对象。  
  
#### window_animator_factory_create 函数

* * *

  * 函数功能：



> 创建窗口动画工厂对象。

  * 函数原型：


    
    
    window_animator_factory_t* window_animator_factory_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | window_animator_factory_t* | 返回窗口动画工厂对象。  
  
#### window_animator_factory_create_animator 函数

* * *

  * 函数功能：



> 创建指定类型的窗口动画。

  * 函数原型：


    
    
    window_animator_t* window_animator_factory_create_animator (window_animator_factory_t* factory, bool_t open, tk_object_t* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | window_animator_t* | 返回窗口动画对象。  
factory | window_animator_factory_t* | 窗口动画工厂对象。  
open | bool_t | TRUE表示打开窗口时的动画，FALSE表示关闭窗口时的动画。  
args | tk_object_t* | 参数。  
  
#### window_animator_factory_destroy 函数

* * *

  * 函数功能：



> 析构并释放窗口动画工厂对象。

  * 函数原型：


    
    
    ret_t window_animator_factory_destroy (window_animator_factory_t* factory);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | window_animator_factory_t* | 窗口动画工厂对象。  
  
#### window_animator_factory_register 函数

* * *

  * 函数功能：



> 注册窗口动画创建函数。

  * 函数原型：


    
    
    ret_t window_animator_factory_register (window_animator_factory_t* factory, const char* type, window_animator_create_t create);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | window_animator_factory_t* | 窗口动画工厂对象。  
type | const char* | 窗口动画类型。  
create | window_animator_create_t | 创建函数。  
  
#### window_animator_factory_set 函数

* * *

  * 函数功能：



> 设置缺省的窗口动画工厂对象。

  * 函数原型：


    
    
    ret_t window_animator_factory_set (window_animator_factory_t* factory);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | window_animator_factory_t* | 窗口动画工厂对象。
