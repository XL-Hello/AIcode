## data_reader_file_t

### 概述

![image](images/data_reader_file_t_0.png)

基于文件实现的 data_reader。通过 data_reader_factory 创建 reader 时，URL的格式如下(请用函数data_reader_file_build_url生成)：
    
    
    file://filename
    

* * *

### 函数

函数名称 | 说明  
---|---  
data_reader_file_create | 创建基于文件的data reader。  
  
#### data_reader_file_create 函数

* * *

  * 函数功能：



> 创建基于文件的data reader。 不要直接调用，而是注册到 data_reader_factory后，通过data_reader_factory调用。

  * 函数原型：


    
    
    data_reader_t* data_reader_file_create (const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | data_reader_t* | 返回data reader对象。  
filename | const char* | 文件名。
