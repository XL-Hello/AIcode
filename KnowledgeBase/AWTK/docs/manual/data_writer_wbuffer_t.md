## data_writer_wbuffer_t

### 概述

![image](images/data_writer_wbuffer_t_0.png)

基于内存实现的 data_writer。通过 data_writer_factory 创建 writer 时，URL的格式如下(请用函数data_writer_wbuffer_build_url生成)：
    
    
    wbuffer://addr
    

* * *

### 函数

函数名称 | 说明  
---|---  
data_writer_wbuffer_build_url | 构造wbuffer的URL。  
data_writer_wbuffer_create | 创建基于wbuffer的data writer。  
  
#### data_writer_wbuffer_build_url 函数

* * *

  * 函数功能：



> 构造wbuffer的URL。

  * 函数原型：


    
    
    const char* data_writer_wbuffer_build_url (wbuffer_t* wbuffer, char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回URL。  
wbuffer | wbuffer_t* | wbuffer对象。  
url | char* | 生成的URL。  
  
#### data_writer_wbuffer_create 函数

* * *

  * 函数功能：



> 创建基于wbuffer的data writer。
> 
> 不要直接调用，而是注册到 data_writer_factory后，通过data_writer_factory调用

  * 函数原型：


    
    
    data_writer_t* data_writer_wbuffer_create (const char* wbuffer_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | data_writer_t* | 返回data writer对象。  
wbuffer_name | const char* | wbuffer地址的字符串格式表示 。
