## csv_row_object_t

### 概述

![image](images/csv_row_object_t_0.png)

## 将cvs row包装成object对象。

### 函数

函数名称 | 说明  
---|---  
csv_row_object_create | 将csv_row对象包装成object。  
  
#### csv_row_object_create 函数

* * *

  * 函数功能：



> 将csv_row对象包装成object。

  * 函数原型：


    
    
    tk_object_t* csv_row_object_create (tk_object_t* csv, const char* init);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回对象。  
csv | tk_object_t* | csv对象。  
init | const char* | 初始化数据。
