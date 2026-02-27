## data_reader_mem_t

### 概述

![image](images/data_reader_mem_t_0.png)

基于内存实现的 data_reader。通过 data_reader_factory 创建 reader 时，URL的格式如下(请用函数data_reader_mem_build_url生成)：
    
    
    mem://addr:size
    

* * *

### 函数

函数名称 | 说明  
---|---  
data_reader_mem_build_url | 构造内存URL。  
data_reader_mem_create | 创建基于内存的 data reader。  
  
#### data_reader_mem_build_url 函数

* * *

  * 函数功能：



> 构造内存URL。

  * 函数原型：


    
    
    const char* data_reader_mem_build_url (const void* buffer, uint32_t size, char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回URL。  
buffer | const void* | 内存的地址。  
size | uint32_t | 内存的长度。  
url | char* | 生成的URL。  
  
#### data_reader_mem_create 函数

* * *

  * 函数功能：



> 创建基于内存的 data reader。
> 
> 不要直接调用，而是注册到 data_reader_factory后，通过data_reader_factory调用。

  * 函数原型：


    
    
    data_reader_t* data_reader_mem_create (const char* memname);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | data_reader_t* | 返回data reader对象。  
memname | const char* | 内存地址和大小的字符串格式表示 。
