## object_locker_t

### 概述

![image](images/object_locker_t_0.png)

## 对现有的object对象进行装饰，添加访问互斥功能。

### 函数

函数名称 | 说明  
---|---  
object_locker_cast | 转换为object_locker对象。  
object_locker_create | 创建对象。  
  
#### object_locker_cast 函数

* * *

  * 函数功能：



> 转换为object_locker对象。

  * 函数原型：


    
    
    object_locker_t* object_locker_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_locker_t* | object_locker对象。  
obj | tk_object_t* | object_locker对象。  
  
#### object_locker_create 函数

* * *

  * 函数功能：



> 创建对象。

  * 函数原型：


    
    
    tk_object_t* object_locker_create (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
obj | tk_object_t* | 待装饰的对象。
