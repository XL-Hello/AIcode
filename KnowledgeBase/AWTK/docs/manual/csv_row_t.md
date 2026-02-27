## csv_row_t

### 概述

## 行对象。

### 函数

函数名称 | 说明  
---|---  
csv_row_count_cols | 获取列数。  
csv_row_get | 获取指定列的数据。  
csv_row_get_col | 根据列名获取列号。  
csv_row_set | 修改指定列的数据。  
  
#### csv_row_count_cols 函数

* * *

  * 函数功能：



> 获取列数。

  * 函数原型：


    
    
    uint32_t csv_row_count_cols (csv_row_t* row);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回列数。  
row | csv_row_t* | 行对象。  
  
#### csv_row_get 函数

* * *

  * 函数功能：



> 获取指定列的数据。

  * 函数原型：


    
    
    const char* csv_row_get (csv_row_t* row, uint32_t col);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回数据。  
row | csv_row_t* | 行对象。  
col | uint32_t | 列号。  
  
#### csv_row_get_col 函数

* * *

  * 函数功能：



> 根据列名获取列号。

  * 函数原型：


    
    
    int32_t csv_row_get_col (csv_row_t* row, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回列号。  
row | csv_row_t* | 行对象。  
value | const char* | 列名。  
  
#### csv_row_set 函数

* * *

  * 函数功能：



> 修改指定列的数据。

  * 函数原型：


    
    
    ret_t csv_row_set (csv_row_t* row, uint32_t col, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
row | csv_row_t* | 行对象。  
col | uint32_t | 列号。  
value | const char* | 值。
