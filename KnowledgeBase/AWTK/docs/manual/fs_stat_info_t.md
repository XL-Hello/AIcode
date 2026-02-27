## fs_stat_info_t

### 概述

## 文件状态信息。

### 函数

函数名称 | 说明  
---|---  
fs_stat_info_create | 创建文件状态信息对象。  
fs_stat_info_destroy | 销毁文件状态信息对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
atime | uint64_t | 最后访问时间。  
ctime | uint64_t | 创建时间。  
is_dir | bool_t | 是否为目录。  
is_link | bool_t | 是否为链接。  
is_reg_file | bool_t | 是否普通文件。  
mtime | uint64_t | 最后修改时间。  
size | uint64_t | 文件大小。  
  
#### fs_stat_info_create 函数

* * *

  * 函数功能：



> 创建文件状态信息对象。

  * 函数原型：


    
    
    fs_stat_info_t* fs_stat_info_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fs_stat_info_t* | 返回文件状态信息对象。  
  
#### fs_stat_info_destroy 函数

* * *

  * 函数功能：



> 销毁文件状态信息对象。

  * 函数原型：


    
    
    ret_t fs_stat_info_destroy (fs_stat_info_t* fst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fst | fs_stat_info_t* | 文件状态信息对象。  
  
#### atime 属性

* * *

> 最后访问时间。

  * 类型：uint64_t



#### ctime 属性

* * *

> 创建时间。

  * 类型：uint64_t



#### is_dir 属性

* * *

> 是否为目录。

  * 类型：bool_t



#### is_link 属性

* * *

> 是否为链接。

  * 类型：bool_t



#### is_reg_file 属性

* * *

> 是否普通文件。

  * 类型：bool_t



#### mtime 属性

* * *

> 最后修改时间。

  * 类型：uint64_t



#### size 属性

* * *

> 文件大小。

  * 类型：uint64_t


