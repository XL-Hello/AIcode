## fs_file_t

### 概述

文件接口。

示例：
    
    
    int32_t ret = 0;
    const char* file_name = "test.txt";
    int32_t len = file_get_size(file_name);
    uint8_t* buff = (uint8_t*)TKMEM_ALLOC(len + 1);
    return_value_if_fail(buff != NULL, NULL);
    
    fs_file_t* fp = fs_open_file(os_fs(), file_name, "rb");
    if (fp != NULL) {
    ret = fs_file_read(fp, buff, len);
    fs_file_close(fp);
    }
    

* * *

### 函数

函数名称 | 说明  
---|---  
fs_file_close | 关闭文件。  
fs_file_eof | 判断文件是否结束。  
fs_file_printf | 写入文件。  
fs_file_read | 读取文件。  
fs_file_read_line | 读取一行文本。  
fs_file_seek | 定位读写指针到指定的位置。  
fs_file_size | 获取文件大小。  
fs_file_stat | 获取文件信息。  
fs_file_sync | 同步文件到磁盘。  
fs_file_tell | 获取文件当前读写位置。  
fs_file_truncate | 清除文件内容。  
fs_file_write | 写入文件。  
  
#### fs_file_close 函数

* * *

  * 函数功能：



> 关闭文件。

  * 函数原型：


    
    
    ret_t fs_file_close (fs_file_t* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
file | fs_file_t* | 文件对象。  
  
#### fs_file_eof 函数

* * *

  * 函数功能：



> 判断文件是否结束。

  * 函数原型：


    
    
    bool_t fs_file_eof (fs_file_t* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示结束，否则表示没结束。  
file | fs_file_t* | 文件对象。  
  
#### fs_file_printf 函数

* * *

  * 函数功能：



> 写入文件。

  * 函数原型：


    
    
    int32_t fs_file_printf (fs_file_t* file, const char* const format_str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际写入的字节数。  
file | fs_file_t* | 文件对象。  
format_str | const char* const | 格式化字符串。  
  
#### fs_file_read 函数

* * *

  * 函数功能：



> 读取文件。

  * 函数原型：


    
    
    int32_t fs_file_read (fs_file_t* file, void* buffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际读取的字节数。  
file | fs_file_t* | 文件对象。  
buffer | void* | 用于返回数据的缓冲区。  
size | uint32_t | 缓冲区大小。  
  
#### fs_file_read_line 函数

* * *

  * 函数功能：



> 读取一行文本。 需要用二进制格式打开，否则Windows下，系统会修改换行符。

  * 函数原型：


    
    
    int32_t fs_file_read_line (fs_file_t* file, char* buffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际读取的字节数。  
file | fs_file_t* | 文件对象。  
buffer | char* | 用于返回数据的缓冲区。  
size | uint32_t | 缓冲区大小。  
  
#### fs_file_seek 函数

* * *

  * 函数功能：



> 定位读写指针到指定的位置。

  * 函数原型：


    
    
    ret_t fs_file_seek (fs_file_t* file, int32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
file | fs_file_t* | 文件对象。  
offset | int32_t | 数据长度。  
  
#### fs_file_size 函数

* * *

  * 函数功能：



> 获取文件大小。

  * 函数原型：


    
    
    int64_t fs_file_size (fs_file_t* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回文件大小。  
file | fs_file_t* | 文件对象。  
  
#### fs_file_stat 函数

* * *

  * 函数功能：



> 获取文件信息。

  * 函数原型：


    
    
    ret_t fs_file_stat (fs_file_t* file, fs_stat_info_t* fst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
file | fs_file_t* | 文件对象。  
fst | fs_stat_info_t* | 文件状态信息。  
  
#### fs_file_sync 函数

* * *

  * 函数功能：



> 同步文件到磁盘。

  * 函数原型：


    
    
    ret_t fs_file_sync (fs_file_t* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
file | fs_file_t* | 文件对象。  
  
#### fs_file_tell 函数

* * *

  * 函数功能：



> 获取文件当前读写位置。

  * 函数原型：


    
    
    int64_t fs_file_tell (fs_file_t* file);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回文件当前读写位置。  
file | fs_file_t* | 文件对象。  
  
#### fs_file_truncate 函数

* * *

  * 函数功能：



> 清除文件内容。

  * 函数原型：


    
    
    ret_t fs_file_truncate (fs_file_t* file, int32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
file | fs_file_t* | 文件对象。  
offset | int32_t | 数据长度。  
  
#### fs_file_write 函数

* * *

  * 函数功能：



> 写入文件。

  * 函数原型：


    
    
    int32_t fs_file_write (fs_file_t* file, const void* buffer, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际写入的字节数。  
file | fs_file_t* | 文件对象。  
buffer | const void* | 数据缓冲区。  
size | uint32_t | 数据长度。
