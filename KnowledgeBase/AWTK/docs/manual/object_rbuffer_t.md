## object_rbuffer_t

### 概述

![image](images/object_rbuffer_t_0.png)

## 将rbuffer包装成object。

### 函数

函数名称 | 说明  
---|---  
object_rbuffer_cast | 转换为object_rbuffer对象。  
object_rbuffer_create | 创建rbuffer对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
rbuffer | rbuffer_t* | rbuffer对象。  
  
#### object_rbuffer_cast 函数

* * *

  * 函数功能：



> 转换为object_rbuffer对象。

  * 函数原型：


    
    
    object_rbuffer_t* object_rbuffer_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_rbuffer_t* | object_rbuffer对象。  
obj | tk_object_t* | object_rbuffer对象。  
  
#### object_rbuffer_create 函数

* * *

  * 函数功能：



> 创建rbuffer对象。

  * 函数原型：


    
    
    tk_object_t* object_rbuffer_create (const uint8_t* data, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
data | const uint8_t* | 缓冲区。  
capacity | uint32_t | 缓冲区的容量。  
  
#### rbuffer 属性

* * *

> rbuffer对象。

  * 类型：rbuffer_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
