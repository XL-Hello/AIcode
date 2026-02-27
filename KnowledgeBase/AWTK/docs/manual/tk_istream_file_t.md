## tk_istream_file_t

### 概述

![image](images/tk_istream_file_t_0.png)

## 基于文件实现的输入流。

### 函数

函数名称 | 说明  
---|---  
tk_istream_file_create | 创建istream对象。  
tk_istream_file_create_ex | 创建istream对象。  
  
#### tk_istream_file_create 函数

* * *

  * 函数功能：



> 创建istream对象。

  * 函数原型：


    
    
    tk_istream_t* tk_istream_file_create (const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_istream_t* | 返回istream对象。  
filename | const char* | 文件名。  
  
#### tk_istream_file_create_ex 函数

* * *

  * 函数功能：



> 创建istream对象。

  * 函数原型：


    
    
    tk_istream_t* tk_istream_file_create_ex (const char* filename, const char* mode);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_istream_t* | 返回istream对象。  
filename | const char* | 文件名。  
mode | const char* | 模式。
