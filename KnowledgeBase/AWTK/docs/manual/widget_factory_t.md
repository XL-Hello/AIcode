## widget_factory_t

### 概述

![image](images/widget_factory_t_0.png)

控件工厂对象。

提供通过类型创建控件的能力。 用户注册自定义控件，可以获得内置控件同等待遇。

* * *

### 函数

函数名称 | 说明  
---|---  
widget_factory | 获取缺省的控件工厂对象。  
widget_factory_create | 创建控件工厂对象。  
widget_factory_create_widget | 创建指定类型的控件。  
widget_factory_destroy | 析构并释放控件工厂对象。  
widget_factory_register | 注册控件创建函数。  
widget_factory_register_multi | 注册控件创建函数。  
widget_factory_set | 设置缺省的控件工厂对象。  
  
#### widget_factory 函数

* * *

  * 函数功能：



> 获取缺省的控件工厂对象。

  * 函数原型：


    
    
    widget_factory_t* widget_factory ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_factory_t* | 返回控件工厂对象。  
  
#### widget_factory_create 函数

* * *

  * 函数功能：



> 创建控件工厂对象。

  * 函数原型：


    
    
    widget_factory_t* widget_factory_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_factory_t* | 返回控件工厂对象。  
  
#### widget_factory_create_widget 函数

* * *

  * 函数功能：



> 创建指定类型的控件。

  * 函数原型：


    
    
    widget_t* widget_factory_create_widget (widget_factory_t* factory, const char* type, widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回控件对象。  
factory | widget_factory_t* | 控件工厂对象。  
type | const char* | 控件类型。  
parent | widget_t* | 父控件。  
x | xy_t | 初始X坐标。  
y | xy_t | 初始Y坐标。  
w | wh_t | 初始宽度。  
h | wh_t | 初始高度。  
  
#### widget_factory_destroy 函数

* * *

  * 函数功能：



> 析构并释放控件工厂对象。

  * 函数原型：


    
    
    ret_t widget_factory_destroy (widget_factory_t* factory);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | widget_factory_t* | 控件工厂对象。  
  
#### widget_factory_register 函数

* * *

  * 函数功能：



> 注册控件创建函数。

  * 函数原型：


    
    
    ret_t widget_factory_register (widget_factory_t* factory, const char* type, widget_create_t create);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | widget_factory_t* | 控件工厂对象。  
type | const char* | 控件类型。  
create | widget_create_t | 创建函数。  
  
#### widget_factory_register_multi 函数

* * *

  * 函数功能：



> 注册控件创建函数。

  * 函数原型：


    
    
    ret_t widget_factory_register_multi (widget_factory_t* factory, const general_factory_table_t* table);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | widget_factory_t* | 控件工厂对象。  
table | const general_factory_table_t* | 表。  
  
#### widget_factory_set 函数

* * *

  * 函数功能：



> 设置缺省的控件工厂对象。

  * 函数原型：


    
    
    ret_t widget_factory_set (widget_factory_t* factory);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | widget_factory_t* | 控件工厂对象。
