## object_widget_t

### 概述

![image](images/object_widget_t_0.png)

将widget包装成object。

> 备注：主要用于 fscript 实现 widget.prop 方式访问控件属性。

* * *

### 函数

函数名称 | 说明  
---|---  
object_widget_cast | 类型转换。  
object_widget_create | 创建widget对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
widget | widget_t* | widget对象。  
  
#### object_widget_cast 函数

* * *

  * 函数功能：



> 类型转换。

  * 函数原型：


    
    
    object_widget_t* object_widget_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_widget_t* | 返回object_widget对象。  
obj | tk_object_t* | object对象。  
  
#### object_widget_create 函数

* * *

  * 函数功能：



> 创建widget对象。

  * 函数原型：


    
    
    tk_object_t* object_widget_create (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
widget | widget_t* | 控件。  
  
#### widget 属性

* * *

> widget对象。

  * 类型：widget_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
