## self_layouter_t

### 概述

控件自身排版布局器的接口。

## 按特定算法对控件进行排版布局，子类需要实现vtable中的函数。

### 函数

函数名称 | 说明  
---|---  
self_layouter_clone | 克隆layouter对象。  
self_layouter_create | 创建layouter对象。  
self_layouter_destroy | 销毁layouter对象。  
self_layouter_get_param | 获取指定的参数。  
self_layouter_get_param_float | 获取指定的浮点格式的参数。  
self_layouter_get_param_int | 获取指定的整数格式的参数。  
self_layouter_layout | 对控件自身进行布局。  
self_layouter_reinit | 重新计算layouter对象中的数据。  
self_layouter_set_param | 获取指定的参数。  
self_layouter_set_param_str | 设置字符串格式的参数。  
self_layouter_to_string | 获取全部参数。  
  
#### self_layouter_clone 函数

* * *

  * 函数功能：



> 克隆layouter对象。

  * 函数原型：


    
    
    self_layouter_t* self_layouter_clone (self_layouter_t* layouter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | self_layouter_t* | 返回layouter对象。  
layouter | self_layouter_t* | 被克隆的对象。  
  
#### self_layouter_create 函数

* * *

  * 函数功能：



> 创建layouter对象。

  * 函数原型：


    
    
    self_layouter_t* self_layouter_create (const char* params);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | self_layouter_t* | 返回layouter对象。  
params | const char* | 参数。  
  
#### self_layouter_destroy 函数

* * *

  * 函数功能：



> 销毁layouter对象。

  * 函数原型：


    
    
    ret_t self_layouter_destroy (self_layouter_t* layouter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
layouter | self_layouter_t* | layouter对象。  
  
#### self_layouter_get_param 函数

* * *

  * 函数功能：



> 获取指定的参数。

  * 函数原型：


    
    
    ret_t self_layouter_get_param (self_layouter_t* layouter, const char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
layouter | self_layouter_t* | layouter对象。  
name | const char* | 参数名。  
v | value_t* | 返回参数的值。  
  
#### self_layouter_get_param_float 函数

* * *

  * 函数功能：



> 获取指定的浮点格式的参数。

  * 函数原型：


    
    
    float_t self_layouter_get_param_float (self_layouter_t* layouter, const char* name, float_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 成功返回参数的值，失败返回缺省值。  
layouter | self_layouter_t* | layouter对象。  
name | const char* | 参数名。  
defval | float_t | 缺省值。  
  
#### self_layouter_get_param_int 函数

* * *

  * 函数功能：



> 获取指定的整数格式的参数。

  * 函数原型：


    
    
    int32_t self_layouter_get_param_int (self_layouter_t* layouter, const char* name, int32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 成功返回参数的值，失败返回缺省值。  
layouter | self_layouter_t* | layouter对象。  
name | const char* | 参数名。  
defval | int32_t | 缺省值。  
  
#### self_layouter_layout 函数

* * *

  * 函数功能：



> 对控件自身进行布局。

  * 函数原型：


    
    
    ret_t self_layouter_layout (self_layouter_t* layouter, widget_t* widget, rect_t* area);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
layouter | self_layouter_t* | layouter对象。  
widget | widget_t* | 控件。  
area | rect_t* | 可以使用的区域。  
  
#### self_layouter_reinit 函数

* * *

  * 函数功能：



> 重新计算layouter对象中的数据。

  * 函数原型：


    
    
    ret_t self_layouter_reinit (self_layouter_t* layouter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
layouter | self_layouter_t* | layouter对象。  
  
#### self_layouter_set_param 函数

* * *

  * 函数功能：



> 获取指定的参数。

  * 函数原型：


    
    
    ret_t self_layouter_set_param (self_layouter_t* layouter, const char* name, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
layouter | self_layouter_t* | layouter对象。  
name | const char* | 参数名。  
v | const value_t* | 参数的值。  
  
#### self_layouter_set_param_str 函数

* * *

  * 函数功能：



> 设置字符串格式的参数。

  * 函数原型：


    
    
    ret_t self_layouter_set_param_str (self_layouter_t* layouter, const char* name, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
layouter | self_layouter_t* | layouter对象。  
name | const char* | 参数名。  
value | const char* | 参数值。  
  
#### self_layouter_to_string 函数

* * *

  * 函数功能：



> 获取全部参数。

  * 函数原型：


    
    
    const char* self_layouter_to_string (self_layouter_t* layouter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回字符串格式的参数。  
layouter | self_layouter_t* | layouter对象。
