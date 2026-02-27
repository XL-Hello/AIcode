## object_wbuffer_t

### 概述

![image](images/object_wbuffer_t_0.png)

## 将wbuffer包装成object。

### 函数

函数名称 | 说明  
---|---  
object_wbuffer_cast | 转换为object_wbuffer对象。  
object_wbuffer_create | 创建wbuffer对象。  
object_wbuffer_create_extendable | 创建可扩展的wbuffer对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
wbuffer | wbuffer_t* | wbuffer对象。  
  
#### object_wbuffer_cast 函数

* * *

  * 函数功能：



> 转换为object_wbuffer对象。

  * 函数原型：


    
    
    object_wbuffer_t* object_wbuffer_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_wbuffer_t* | object_wbuffer对象。  
obj | tk_object_t* | object_wbuffer对象。  
  
#### object_wbuffer_create 函数

* * *

  * 函数功能：



> 创建wbuffer对象。

  * 函数原型：


    
    
    tk_object_t* object_wbuffer_create (uint8_t* data, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
data | uint8_t* | 缓冲区。  
capacity | uint32_t | 缓冲区的容量。  
  
#### object_wbuffer_create_extendable 函数

* * *

  * 函数功能：



> 创建可扩展的wbuffer对象。

  * 函数原型：


    
    
    tk_object_t* object_wbuffer_create_extendable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
  
#### wbuffer 属性

* * *

> wbuffer对象。

  * 类型：wbuffer_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
