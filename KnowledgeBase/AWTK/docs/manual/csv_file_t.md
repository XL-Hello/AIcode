## csv_file_t

### 概述

## 操作CSV文件。

### 函数

函数名称 | 说明  
---|---  
csv_file_append_row | 追加一行。  
csv_file_clear | 保存。  
csv_file_create | 根据文件创建csv对象。  
csv_file_create_empty | 创建空的csv对象。  
csv_file_create_with_buff | 根据buff创建csv对象。  
csv_file_destroy | 销毁csv对象。  
csv_file_find_first | 查找第一个满足条件的行。  
csv_file_get | 获取指定行列的数据。  
csv_file_get_by_name | 根据列名获取数据。  
csv_file_get_checked_rows | 获取checked行数(包括标题)。  
csv_file_get_col_of_name | 根据列名获取列号。  
csv_file_get_cols | 获取列数。  
csv_file_get_first_checked | 获取第一个勾选的行。  
csv_file_get_row | 获取指定行。  
csv_file_get_rows | 获取行数(包括标题)。  
csv_file_get_title | 获取标题(不存在则返回NULL)。  
csv_file_insert_row | 插入一行。  
csv_file_is_row_checked | 判断指定行是否勾选。  
csv_file_load_buff | 从内存加载csv。  
csv_file_load_file | 从文件加载csv。  
csv_file_load_file | 保存。  
csv_file_reload | 丢弃内存中的修改，重新加载当前文件。  
csv_file_remove_checked_rows | 删除全部勾选的行。  
csv_file_remove_row | 删除指定行。  
csv_file_save | 保存。  
csv_file_save_to_buff | 保存。  
csv_file_set | 修改指定行列的数据。  
csv_file_set_filter | 设置过滤函数。  
csv_file_set_max_rows | 设置最大行数。  
csv_file_set_row_checked | 勾选指定行。  
csv_file_set_single_select | 设置是否单选。  
csv_file_uncheck_all | 取消勾选全部行。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
has_title | bool_t | 是否有标题。  
single_select | bool_t | 是否单选。  
  
#### csv_file_append_row 函数

* * *

  * 函数功能：



> 追加一行。

  * 函数原型：


    
    
    ret_t csv_file_append_row (csv_file_t* csv, const char* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
data | const char* | 数据。  
  
#### csv_file_clear 函数

* * *

  * 函数功能：



> 保存。

  * 函数原型：


    
    
    ret_t csv_file_clear (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_create 函数

* * *

  * 函数功能：



> 根据文件创建csv对象。

  * 函数原型：


    
    
    csv_file_t* csv_file_create (const char* filename, char sep);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | csv_file_t* | 返回csv对象。  
filename | const char* | 文件名。  
sep | char | 分隔符。  
  
#### csv_file_create_empty 函数

* * *

  * 函数功能：



> 创建空的csv对象。

  * 函数原型：


    
    
    csv_file_t* csv_file_create_empty (char sep, csv_file_filter_t filter, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | csv_file_t* | 返回csv对象。  
sep | char | 分隔符。  
filter | csv_file_filter_t | 过滤函数。  
ctx | void* | 过滤函数的上下文。  
  
#### csv_file_create_with_buff 函数

* * *

  * 函数功能：



> 根据buff创建csv对象。

  * 函数原型：


    
    
    csv_file_t* csv_file_create_with_buff (const char* buff, uint32_t size, char sep);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | csv_file_t* | 返回csv对象。  
buff | const char* | 数据。  
size | uint32_t | 数据长度。  
sep | char | 分隔符。  
  
#### csv_file_destroy 函数

* * *

  * 函数功能：



> 销毁csv对象。

  * 函数原型：


    
    
    ret_t csv_file_destroy (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_find_first 函数

* * *

  * 函数功能：



> 查找第一个满足条件的行。

  * 函数原型：


    
    
    csv_row_t* csv_file_find_first (csv_file_t* csv, tk_compare_t compare, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | csv_row_t* | 返回行对象。  
csv | csv_file_t* | csv对象。  
compare | tk_compare_t | 比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### csv_file_get 函数

* * *

  * 函数功能：



> 获取指定行列的数据。

  * 函数原型：


    
    
    const char* csv_file_get (csv_file_t* csv, uint32_t row, uint32_t col);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回数据。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
col | uint32_t | 列号。  
  
#### csv_file_get_by_name 函数

* * *

  * 函数功能：



> 根据列名获取数据。

  * 函数原型：


    
    
    const char* csv_file_get_by_name (csv_file_t* csv, uint32_t row, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回数据。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
name | const char* | 列名。  
  
#### csv_file_get_checked_rows 函数

* * *

  * 函数功能：



> 获取checked行数(包括标题)。

  * 函数原型：


    
    
    uint32_t csv_file_get_checked_rows (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回checked行数。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_get_col_of_name 函数

* * *

  * 函数功能：



> 根据列名获取列号。

  * 函数原型：


    
    
    int32_t csv_file_get_col_of_name (csv_file_t* csv, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回列号。  
csv | csv_file_t* | csv对象。  
name | const char* | 列名。  
  
#### csv_file_get_cols 函数

* * *

  * 函数功能：



> 获取列数。

  * 函数原型：


    
    
    uint32_t csv_file_get_cols (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回列数。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_get_first_checked 函数

* * *

  * 函数功能：



> 获取第一个勾选的行。

  * 函数原型：


    
    
    int32_t csv_file_get_first_checked (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回行号。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_get_row 函数

* * *

  * 函数功能：



> 获取指定行。

  * 函数原型：


    
    
    csv_row_t* csv_file_get_row (csv_file_t* csv, uint32_t row);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | csv_row_t* | 返回行对象。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
  
#### csv_file_get_rows 函数

* * *

  * 函数功能：



> 获取行数(包括标题)。

  * 函数原型：


    
    
    uint32_t csv_file_get_rows (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回行数。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_get_title 函数

* * *

  * 函数功能：



> 获取标题(不存在则返回NULL)。

  * 函数原型：


    
    
    const char* csv_file_get_title (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回标题。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_insert_row 函数

* * *

  * 函数功能：



> 插入一行。

  * 函数原型：


    
    
    ret_t csv_file_insert_row (csv_file_t* csv, uint32_t row, const char* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
data | const char* | 数据。  
  
#### csv_file_is_row_checked 函数

* * *

  * 函数功能：



> 判断指定行是否勾选。

  * 函数原型：


    
    
    bool_t csv_file_is_row_checked (csv_file_t* csv, uint32_t row);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示勾选，否则表示没勾选。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
  
#### csv_file_load_buff 函数

* * *

  * 函数功能：



> 从内存加载csv。

  * 函数原型：


    
    
    ret_t csv_file_load_buff (csv_file_t* csv, const char* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
buff | const char* | 数据。  
size | uint32_t | 数据长度。  
  
#### csv_file_load_file 函数

* * *

  * 函数功能：



> 从文件加载csv。

  * 函数原型：


    
    
    ret_t csv_file_load_file (csv_file_t* csv, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
filename | const char* | 文件名。  
  
#### csv_file_load_file 函数

* * *

  * 函数功能：



> 保存。

  * 函数原型：


    
    
    ret_t csv_file_load_file (csv_file_t* csv, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
filename | const char* | 文件名。  
  
#### csv_file_reload 函数

* * *

  * 函数功能：



> 丢弃内存中的修改，重新加载当前文件。

  * 函数原型：


    
    
    ret_t csv_file_reload (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_remove_checked_rows 函数

* * *

  * 函数功能：



> 删除全部勾选的行。

  * 函数原型：


    
    
    ret_t csv_file_remove_checked_rows (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
  
#### csv_file_remove_row 函数

* * *

  * 函数功能：



> 删除指定行。

  * 函数原型：


    
    
    ret_t csv_file_remove_row (csv_file_t* csv, uint32_t row);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
  
#### csv_file_save 函数

* * *

  * 函数功能：



> 保存。

  * 函数原型：


    
    
    ret_t csv_file_save (csv_file_t* csv, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
filename | const char* | 文件名。  
  
#### csv_file_save_to_buff 函数

* * *

  * 函数功能：



> 保存。

  * 函数原型：


    
    
    ret_t csv_file_save_to_buff (csv_file_t* csv, wbuffer_t* buff);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
buff | wbuffer_t* | 保存结果数据。  
  
#### csv_file_set 函数

* * *

  * 函数功能：



> 修改指定行列的数据。

  * 函数原型：


    
    
    ret_t csv_file_set (csv_file_t* csv, uint32_t row, uint32_t col, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
col | uint32_t | 列号。  
value | const char* | 值。  
  
#### csv_file_set_filter 函数

* * *

  * 函数功能：



> 设置过滤函数。

  * 函数原型：


    
    
    ret_t csv_file_set_filter (csv_file_t* csv, csv_file_filter_t filter, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
filter | csv_file_filter_t | 过滤函数。  
ctx | void* | 过滤函数的上下文。  
  
#### csv_file_set_max_rows 函数

* * *

  * 函数功能：



> 设置最大行数。

  * 函数原型：


    
    
    ret_t csv_file_set_max_rows (csv_file_t* csv, uint32_t max_rows);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
max_rows | uint32_t | 最大行数。  
  
#### csv_file_set_row_checked 函数

* * *

  * 函数功能：



> 勾选指定行。

  * 函数原型：


    
    
    ret_t csv_file_set_row_checked (csv_file_t* csv, uint32_t row, bool_t checked);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
row | uint32_t | 行号。  
checked | bool_t | 是否勾选。  
  
#### csv_file_set_single_select 函数

* * *

  * 函数功能：



> 设置是否单选。

  * 函数原型：


    
    
    ret_t csv_file_set_single_select (csv_file_t* csv, bool_t single_select);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
single_select | bool_t | 是否单选。  
  
#### csv_file_uncheck_all 函数

* * *

  * 函数功能：



> 取消勾选全部行。

  * 函数原型：


    
    
    ret_t csv_file_uncheck_all (csv_file_t* csv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
csv | csv_file_t* | csv对象。  
  
#### has_title 属性

* * *

> 是否有标题。

  * 类型：bool_t



#### single_select 属性

* * *

> 是否单选。

  * 类型：bool_t


