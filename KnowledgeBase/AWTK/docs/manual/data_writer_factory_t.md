## data_writer_factory_t

### 概述

## data writer工厂。

### 函数

函数名称 | 说明  
---|---  
data_writer_factory | 获取缺省的data writer工厂对象。  
data_writer_factory_create | 创建data writer工厂对象。  
data_writer_factory_create_writer | 创建指定类型的data writer对象。  
data_writer_factory_destroy | 析构并释放data writer工厂对象。  
data_writer_factory_register | 注册data writer创建函数。  
data_writer_factory_set | 设置缺省的data writer工厂对象。  
  
#### data_writer_factory 函数

* * *

  * 函数功能：



> 获取缺省的data writer工厂对象。

  * 函数原型：


    
    
    data_writer_factory_t* data_writer_factory ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | data_writer_factory_t* | 返回data writer工厂对象。  
  
#### data_writer_factory_create 函数

* * *

  * 函数功能：



> 创建data writer工厂对象。

  * 函数原型：


    
    
    data_writer_factory_t* data_writer_factory_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | data_writer_factory_t* | 返回data writer工厂对象。  
  
#### data_writer_factory_create_writer 函数

* * *

  * 函数功能：



> 创建指定类型的data writer对象。

  * 函数原型：


    
    
    data_writer_t* data_writer_factory_create_writer (data_writer_factory_t* factory, const char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | data_writer_t* | 返回data writer对象。  
factory | data_writer_factory_t* | data writer工厂对象。  
url | const char* | URL。  
  
#### data_writer_factory_destroy 函数

* * *

  * 函数功能：



> 析构并释放data writer工厂对象。

  * 函数原型：


    
    
    ret_t data_writer_factory_destroy (data_writer_factory_t* factory);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | data_writer_factory_t* | data writer工厂对象。  
  
#### data_writer_factory_register 函数

* * *

  * 函数功能：



> 注册data writer创建函数。

  * 函数原型：


    
    
    ret_t data_writer_factory_register (data_writer_factory_t* factory, const char* protocol, data_writer_create_t create);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | data_writer_factory_t* | writer工厂对象。  
protocol | const char* | 协议(如file)。  
create | data_writer_create_t | data writer创建函数。  
  
#### data_writer_factory_set 函数

* * *

  * 函数功能：



> 设置缺省的data writer工厂对象。

  * 函数原型：


    
    
    ret_t data_writer_factory_set (data_writer_factory_t* factory);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
factory | data_writer_factory_t* | data writer工厂对象。
