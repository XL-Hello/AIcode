## object_date_time_t

### 概述

![image](images/object_date_time_t_0.png)

## 将date_time包装成object。

### 函数

函数名称 | 说明  
---|---  
object_date_time_cast | 转换为object_date_time对象。  
object_date_time_create | 创建对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
dt | date_time_t* | date time对象。  
  
#### object_date_time_cast 函数

* * *

  * 函数功能：



> 转换为object_date_time对象。

  * 函数原型：


    
    
    object_date_time_t* object_date_time_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_date_time_t* | object_date_time对象。  
obj | tk_object_t* | object_date_time对象。  
  
#### object_date_time_create 函数

* * *

  * 函数功能：



> 创建对象。

  * 函数原型：


    
    
    tk_object_t* object_date_time_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
  
#### dt 属性

* * *

> date time对象。

  * 类型：date_time_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
