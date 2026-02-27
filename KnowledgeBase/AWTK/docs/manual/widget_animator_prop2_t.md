## widget_animator_prop2_t

### 概述

## 通过修改对象的两个指定属性形成动画效果。

### 函数

函数名称 | 说明  
---|---  
widget_animator_prop2_create | 创建双属性动画对象。  
widget_animator_prop2_set_params | 设置动画对象的参数。  
  
#### widget_animator_prop2_create 函数

* * *

  * 函数功能：



> 创建双属性动画对象。

  * 函数原型：


    
    
    widget_animator_t* widget_animator_prop2_create (widget_t* widget, uint32_t duration, uint32_t delay, easing_type_t easing, const char* prop1_name, const char* prop2_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_animator_t* | 成功返回动画对象，失败返回NULL。  
widget | widget_t* | 控件对象。  
duration | uint32_t | 动画持续时间(毫秒)。  
delay | uint32_t | 动画执行时间(毫秒)。  
easing | easing_type_t | 插值函数类型。  
prop1_name | const char* | 属性1的名称。  
prop2_name | const char* | 属性2的名称。  
  
#### widget_animator_prop2_set_params 函数

* * *

  * 函数功能：



> 设置动画对象的参数。

  * 函数原型：


    
    
    ret_t widget_animator_prop2_set_params (widget_animator_t* animator, double from1, double from2, double to1, double to2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
animator | widget_animator_t* | 动画对象本身。  
from1 | double | x的初值。  
from2 | double | y的初值。  
to1 | double | x的终值。  
to2 | double | y的终值。
