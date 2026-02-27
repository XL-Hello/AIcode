## data_reader_asset_t

### 概述

![image](images/data_reader_asset_t_0.png)

基于资源实现的 data_reader。通过 data_reader_factory 创建 reader 时，URL的格式如下(请用函数data_reader_asset_build_url生成)：
    
    
    asset://type/name
    

* * *

### 函数

函数名称 | 说明  
---|---  
data_reader_asset_build_url | 构造内存URL。  
data_reader_asset_create | 创建基于asset的data reader。  
  
#### data_reader_asset_build_url 函数

* * *

  * 函数功能：



> 构造内存URL。

  * 函数原型：


    
    
    const char* data_reader_asset_build_url (const char* name, asset_type_t type, char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回URL。  
name | const char* | 资源的名称。  
type | asset_type_t | 资源的类型。  
url | char* | 生成的URL。  
  
#### data_reader_asset_create 函数

* * *

  * 函数功能：



> 创建基于asset的data reader。
> 
> 不要直接调用，而是注册到 data_reader_factory后，通过data_reader_factory调用。

  * 函数原型：


    
    
    data_reader_t* data_reader_asset_create (const char* assetname);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | data_reader_t* | 返回data reader对象。  
assetname | const char* | 资源的名称。
