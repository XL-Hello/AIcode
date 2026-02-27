## zip_file_t

### 概述

## zip文件。

### 函数

函数名称 | 说明  
---|---  
zip_file_extract | 解压zip文件。  
  
#### zip_file_extract 函数

* * *

  * 函数功能：



> 解压zip文件。

  * 函数原型：


    
    
    ret_t zip_file_extract (const char* zipfile, const char* dst_dir, const char* password);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
zipfile | const char* | zip文件名。  
dst_dir | const char* | 目录。  
password | const char* | 密码(可选)
