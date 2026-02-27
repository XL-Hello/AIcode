## style_factory_t

### 概述

style工厂接口，主要用于创建style。

## > 在特殊情况下，可以实现自己的style工厂，比如支持CSS和可实时修改的style。

### 函数

函数名称 | 说明  
---|---  
style_factory | 获取缺省的style factory。  
style_factory_create_style | 创建style。  
style_factory_set | 设置缺省的style factory(需要自定义的style factory才设置)。  
  
#### style_factory 函数

* * *

  * 函数功能：



> 获取缺省的style factory。

  * 函数原型：


    
    
    style_factory_t* style_factory ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | style_factory_t* | 返回style factory对象。  
  
#### style_factory_create_style 函数

* * *

  * 函数功能：



> 创建style。

  * 函数原型：


    
    
    style_t* style_factory_create_style (style_factory_t* factory, const char* style_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | style_t* | 返回style对象。  
factory | style_factory_t* | factory对象。  
style_type | const char* | style类型。  
  
#### style_factory_set 函数

* * *

  * 函数功能：



> 设置缺省的style factory(需要自定义的style factory才设置)。

  * 函数原型：


    
    
    ret_t style_factory_set (style_factory_t* factory);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | style_factory_t* | factory对象。
