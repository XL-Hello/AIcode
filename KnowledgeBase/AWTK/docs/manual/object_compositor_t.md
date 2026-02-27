## object_compositor_t

### 概述

![image](images/object_compositor_t_0.png)

## 将两个对象包装为一个对象，优先访问第一个对象，如果访问失败则访问第二个对象。

### 函数

函数名称 | 说明  
---|---  
object_compositor_cast | 转换为object_compositor对象。  
object_compositor_create | 创建对象。  
  
#### object_compositor_cast 函数

* * *

  * 函数功能：



> 转换为object_compositor对象。

  * 函数原型：


    
    
    object_compositor_t* object_compositor_cast (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | object_compositor_t* | object_compositor对象。  
obj | tk_object_t* | object_compositor对象。  
  
#### object_compositor_create 函数

* * *

  * 函数功能：



> 创建对象。

  * 函数原型：


    
    
    tk_object_t* object_compositor_create (tk_object_t* obj1, tk_object_t* obj2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
obj1 | tk_object_t* | 对象1。  
obj2 | tk_object_t* | 对象2。
