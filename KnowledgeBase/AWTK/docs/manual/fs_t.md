## fs_t

### 概述

## 文件系统接口。

### 函数

函数名称 | 说明  
---|---  
dir_exist | 判断目录是否存在。  
file_exist | 判断文件是否存在。  
file_get_size | 获取文件大小。  
file_read | 读取文件的全部内容。  
file_read_part | 从某个位置读取文件。  
file_remove | 刪除文件。  
file_write | 写入文件。  
fs_build_user_storage_file_name | 生成一个保存数据文件的完整路径的文件名。  
fs_change_dir | 修改当前目录。  
fs_copy_dir | 拷贝目录。  
fs_copy_dir_ex | 拷贝目录。  
fs_copy_file | 拷贝文件。  
fs_create_dir | 创建目录。  
fs_create_dir_r | 递归创建目录。  
fs_dir_exist | 判断目录是否存在。  
fs_dir_is_empty | 判断目录是否为空。  
fs_dir_rename | 目录重命名。  
fs_file_equal | 比较二进制文件。  
fs_file_exist | 判断文件是否存在。  
fs_file_rename | 文件重命名。  
fs_foreach_file | 遍历指定目录下全部常规文件。  
fs_get_cwd | 获取当前所在目录。  
fs_get_disk_info | 获取文件系统信息。  
fs_get_exe | 获取可执行文件所在目录。  
fs_get_file_size | 获取文件大小。  
fs_get_temp_path | 获取临时目录。  
fs_get_user_storage_path | 获取home目录或者应用程序可以写入数据的目录。  
fs_open_dir | 打开目录。  
fs_open_file | 打开文件。  
fs_remove_dir | 刪除目录。  
fs_remove_dir_r | 递归刪除目录。  
fs_remove_file | 刪除文件。  
fs_stat | 获取文件信息。  
os_fs | 获取缺省的文件系统对象。  
  
#### dir_exist 函数

* * *

  * 函数功能：



> 判断目录是否存在。

  * 函数原型：


    
    
    bool_t dir_exist (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示成功，否则表示失败。  
name | const char* | 目录名。  
  
#### file_exist 函数

* * *

  * 函数功能：



> 判断文件是否存在。

  * 函数原型：


    
    
    bool_t file_exist (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示成功，否则表示失败。  
name | const char* | 文件名。  
  
#### file_get_size 函数

* * *

  * 函数功能：



> 获取文件大小。

  * 函数原型：


    
    
    int32_t file_get_size (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回非负表示文件大小，否则表示失败。  
name | const char* | 文件名。  
  
#### file_read 函数

* * *

  * 函数功能：



> 读取文件的全部内容。

  * 函数原型：


    
    
    void* file_read (const char* name, uint32_t* size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回读取的数据，需要调用TKMEM_FREE释放。  
name | const char* | 文件名。  
size | uint32_t* | 返回实际读取的长度。  
  
#### file_read_part 函数

* * *

  * 函数功能：



> 从某个位置读取文件。

  * 函数原型：


    
    
    int32_t file_read_part (const char* name, void* buff, uint32_t size, uint32_t offset);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回实际读取的字节数。  
name | const char* | 文件名。  
buff | void* | 数据缓冲区。  
size | uint32_t | 数据长度。  
offset | uint32_t | 偏移量。  
  
#### file_remove 函数

* * *

  * 函数功能：



> 刪除文件。

  * 函数原型：


    
    
    ret_t file_remove (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 文件名。  
  
#### file_write 函数

* * *

  * 函数功能：



> 写入文件。

  * 函数原型：


    
    
    ret_t file_write (const char* name, const void* buff, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 文件名。  
buff | const void* | 数据缓冲区。  
size | uint32_t | 数据长度。  
  
#### fs_build_user_storage_file_name 函数

* * *

  * 函数功能：



> 生成一个保存数据文件的完整路径的文件名。

  * 函数原型：


    
    
    ret_t fs_build_user_storage_file_name (char* filename, const char* appname, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | char* | 用于返回完整路径的文件名。  
appname | const char* | 应用程序的名称。  
name | const char* | 文件名(不包括路径)。  
  
#### fs_change_dir 函数

* * *

  * 函数功能：



> 修改当前目录。

  * 函数原型：


    
    
    ret_t fs_change_dir (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_copy_dir 函数

* * *

  * 函数功能：



> 拷贝目录。

  * 函数原型：


    
    
    ret_t fs_copy_dir (fs_t* fs, const char* src, const char* dst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
src | const char* | 源目录。  
dst | const char* | 目标目录。  
  
#### fs_copy_dir_ex 函数

* * *

  * 函数功能：



> 拷贝目录。

  * 函数原型：


    
    
    ret_t fs_copy_dir_ex (fs_t* fs, const char* src, const char* dst, bool_t overwrite);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
src | const char* | 源目录。  
dst | const char* | 目标目录。  
overwrite | bool_t | 是否覆盖。  
  
#### fs_copy_file 函数

* * *

  * 函数功能：



> 拷贝文件。

  * 函数原型：


    
    
    ret_t fs_copy_file (fs_t* fs, const char* src, const char* dst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
src | const char* | 源文件名。  
dst | const char* | 目标文件名。  
  
#### fs_create_dir 函数

* * *

  * 函数功能：



> 创建目录。

  * 函数原型：


    
    
    ret_t fs_create_dir (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_create_dir_r 函数

* * *

  * 函数功能：



> 递归创建目录。

  * 函数原型：


    
    
    ret_t fs_create_dir_r (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_dir_exist 函数

* * *

  * 函数功能：



> 判断目录是否存在。

  * 函数原型：


    
    
    bool_t fs_dir_exist (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_dir_is_empty 函数

* * *

  * 函数功能：



> 判断目录是否为空。

  * 函数原型：


    
    
    bool_t fs_dir_is_empty (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示目录为空，否则表示目录不为空。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_dir_rename 函数

* * *

  * 函数功能：



> 目录重命名。

  * 函数原型：


    
    
    ret_t fs_dir_rename (fs_t* fs, const char* name, const char* new_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 旧目录名称。  
new_name | const char* | 新目录名称。  
  
#### fs_file_equal 函数

* * *

  * 函数功能：



> 比较二进制文件。

  * 函数原型：


    
    
    bool_t fs_file_equal (fs_t* fs, const char* src, const char* dst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示相同，否则表示不同。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
src | const char* | 源文件名。  
dst | const char* | 目标文件名。  
  
#### fs_file_exist 函数

* * *

  * 函数功能：



> 判断文件是否存在。

  * 函数原型：


    
    
    bool_t fs_file_exist (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 文件名。  
  
#### fs_file_rename 函数

* * *

  * 函数功能：



> 文件重命名。

  * 函数原型：


    
    
    ret_t fs_file_rename (fs_t* fs, const char* name, const char* new_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 旧文件名。  
new_name | const char* | 新文件名。  
  
#### fs_foreach_file 函数

* * *

  * 函数功能：



> 遍历指定目录下全部常规文件。 示例:
    
    
    static ret_t on_file(void* ctx, const void* data) {
    const char* filename = (const char*)data;
    const char* extname = (const char*)ctx;
    
    if (tk_str_end_with(filename, extname)) {
    log_debug("%s\n", filename);
    }
    return RET_OK;
    }
    ...
    fs_foreach_file("tests/testdata", on_file, (void*)".json");
    

  * 函数原型：


    
    
    ret_t fs_foreach_file (const char* path, tk_visit_t on_file, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回TRUE表示成功，否则表示失败。  
path | const char* | 目录。  
on_file | tk_visit_t | 回调函数(完整文件名通过data参数传入)。  
ctx | void* | 回调函数上下文。  
  
#### fs_get_cwd 函数

* * *

  * 函数功能：



> 获取当前所在目录。

  * 函数原型：


    
    
    ret_t fs_get_cwd (fs_t* fs, char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
path | char* | 保存当前所在目录的路径。  
  
#### fs_get_disk_info 函数

* * *

  * 函数功能：



> 获取文件系统信息。

  * 函数原型：


    
    
    ret_t fs_get_disk_info (fs_t* fs, const char* volume, int32_t* free_kb, int32_t* total_kb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回不是-1表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
volume | const char* | 卷名。  
free_kb | int32_t* | 用于返回空闲空间大小(KB)  
total_kb | int32_t* | 用于返回总共空间大小(KB)  
  
#### fs_get_exe 函数

* * *

  * 函数功能：



> 获取可执行文件所在目录。

  * 函数原型：


    
    
    ret_t fs_get_exe (fs_t* fs, char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
path | char* | 保存可执行文件的路径。  
  
#### fs_get_file_size 函数

* * *

  * 函数功能：



> 获取文件大小。

  * 函数原型：


    
    
    int32_t fs_get_file_size (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回不是-1表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 文件名。  
  
#### fs_get_temp_path 函数

* * *

  * 函数功能：



> 获取临时目录。

  * 函数原型：


    
    
    ret_t fs_get_temp_path (fs_t* fs, char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
path | char* | 保存路径。  
  
#### fs_get_user_storage_path 函数

* * *

  * 函数功能：



> 获取home目录或者应用程序可以写入数据的目录。

  * 函数原型：


    
    
    ret_t fs_get_user_storage_path (fs_t* fs, char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
path | char* | 保存路径。  
  
#### fs_open_dir 函数

* * *

  * 函数功能：



> 打开目录。

  * 函数原型：


    
    
    fs_dir_t* fs_open_dir (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fs_dir_t* | 返回非NULL表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_open_file 函数

* * *

  * 函数功能：



> 打开文件。

  * 函数原型：


    
    
    fs_file_t* fs_open_file (fs_t* fs, const char* name, const char* mode);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fs_file_t* | 返回非NULL表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 文件名。  
mode | const char* | 打开方式，取值请参考POSIX的[fopen函数](https://www.runoob.com/cprogramming/c-function-fopen.html)相应的参数。  
  
#### fs_remove_dir 函数

* * *

  * 函数功能：



> 刪除目录。

  * 函数原型：


    
    
    ret_t fs_remove_dir (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_remove_dir_r 函数

* * *

  * 函数功能：



> 递归刪除目录。

  * 函数原型：


    
    
    ret_t fs_remove_dir_r (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 目录名称。  
  
#### fs_remove_file 函数

* * *

  * 函数功能：



> 刪除文件。

  * 函数原型：


    
    
    ret_t fs_remove_file (fs_t* fs, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 文件名。  
  
#### fs_stat 函数

* * *

  * 函数功能：



> 获取文件信息。

  * 函数原型：


    
    
    ret_t fs_stat (fs_t* fs, const char* name, fs_stat_info_t* fst);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fs | fs_t* | 文件系统对象，一般赋值为os_fs()。  
name | const char* | 文件名。  
fst | fs_stat_info_t* | 文件状态信息。  
  
#### os_fs 函数

* * *

  * 函数功能：



> 获取缺省的文件系统对象。

  * 函数原型：


    
    
    fs_t* os_fs ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fs_t* | 返回文件系统对象。
