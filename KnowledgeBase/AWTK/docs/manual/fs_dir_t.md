## fs_dir_t

### 概述

## 文件夹接口。

### 函数

函数名称 | 说明  
---|---  
fs_dir_close | 关闭文件夹对象。  
fs_dir_read | 读取文件夹对象。  
fs_dir_rewind | 重置文件夹读取位置到开始。  
  
#### fs_dir_close 函数

* * *

  * 函数功能：



> 关闭文件夹对象。

  * 函数原型：


    
    
    ret_t fs_dir_close (fs_dir_t* dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dir | fs_dir_t* | 文件夹对象。  
  
#### fs_dir_read 函数

* * *

  * 函数功能：



> 读取文件夹对象。

  * 函数原型：


    
    
    ret_t fs_dir_read (fs_dir_t* dir, fs_item_t* item);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dir | fs_dir_t* | 文件夹对象。  
item | fs_item_t* | 返回一项。  
  
#### fs_dir_rewind 函数

* * *

  * 函数功能：



> 重置文件夹读取位置到开始。

  * 函数原型：


    
    
    ret_t fs_dir_rewind (fs_dir_t* dir);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dir | fs_dir_t* | 文件夹对象。
