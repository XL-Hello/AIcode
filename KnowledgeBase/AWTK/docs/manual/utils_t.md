## utils_t

### 概述

## 工具类。

### 函数

函数名称 | 说明  
---|---  
bits_stream_get | 从buff中获取第index位的值。  
bits_stream_set | 设置buff中第index位的值。  
compare_always_equal | 始终返回相等。  
data_url_copy | 将数据从源URL拷贝到目标URL。  
default_destroy | 缺省的destroy函数。释放data指向的内存。  
dummy_destroy | 空的destroy函数。  
file_read_as_unix_text | 读取文本文件。并将windows换行(\r\n)或macos换行(\r)转换为unix换行(\n)。  
filename_to_name | 从完整文件名中获取文件名。  
filename_to_name_ex | 从完整文件名中获取文件名。  
image_region_parse | 解析子图的区域信息。  
object_to_json | 将对象转换成json字符串。  
pointer_compare | 指针比较。  
ret_code_from_name | 将ret_t的文本名称转换成对应的值。  
ret_code_to_name | 将ret_t转换成对应的文本名称。  
tk_angle | 计算两点之间的角度(逆时针方向为正，GUI坐标)。  
tk_atob | 将字符串转换为布尔类型。  
tk_atof | 将字符串转换为浮点类型。  
tk_atoi | 将字符串转换为整型数。  
tk_atol | 将字符串转换为整型。  
tk_atoul | 将字符串转换为整型。  
tk_basic_type_from_name | 将类型名称转换成对应的类型。  
tk_bits_data_from_bytes_data | 将bytes数据转换成bits数据(每个字节对应一位)。  
tk_bits_data_to_bytes_data | 将bits数据转换成bytes数据(每个字节对应一位)。  
tk_bits_to_bytes | 将bits数转换成bytes数。  
tk_buffer_get_value | 获取buffer中的值。  
tk_buffer_set_value | 设置buffer中的值。  
tk_count_char | 统计字符串中某个字符出现的次数。  
tk_date_time_format | 格式化时间。  
tk_distance | 计算两点之间的距离。  
tk_eval_ratio_or_px | 如果expr以px/PX结束，直接返回expr前面的数值。  
tk_free_utf8_argv | 释放utf8字符串数组。  
tk_ftoa | 将浮点型转换为字符串。  
tk_int_is_in_array | 检查整数是否在整数数组中。  
tk_is_ui_thread | 判断当前线程是否是UI线程。  
tk_is_valid_name | 判断是否是有效的属性名。  
tk_itoa | 将整型转换为字符串。  
tk_levelize | 将value转换成level。  
tk_lltoa | 将整型转换为字符串。  
tk_memcpy | 内存拷贝。  
tk_memcpy16 | 拷贝数据2字节。  
tk_memcpy32 | 拷贝数据4字节。  
tk_memdup | 内存拷贝。  
tk_memset16 | 设置数据2字节。  
tk_memset24 | 设置数据3字节。  
tk_memset32 | 设置数据4字节。  
tk_mergesort | 归并排序(如果需要稳定的排序，可以选择归并排序，而不是快速排序)。  
tk_normalize_key_name | 标准化key_name  
tk_pixel_copy | 已bpp字节为标准拷贝数据。  
tk_pointer_from_int | 将int转换成指针。  
tk_pointer_from_long | 将long转换成指针。  
tk_pointer_to_int | 将指针转换成int。  
tk_pointer_to_long | 将指针转换成long。  
tk_qsort | 快速排序。  
tk_replace_char | 替换字符。  
tk_replace_locale | 将文本中的$locale$替换为对应的语言。  
tk_set_ui_thread | 设置UI线程的ID。  
tk_size_of_basic_type | 获取基本类型的大小(字节数)。  
tk_skip_chars | 跳过字符串中的字符。  
tk_skip_to_chars | 跳到字符串中的字符。  
tk_skip_to_num | 跳过字符串函数，如：字符串”hello123world”，返回的结果是”123world”。  
tk_snprintf | 将可变参数(…)按照format格式化字符串，并将字符串复制到str中。  
tk_sscanf | 从字符串读取格式化输入。  
tk_sscanf_simple | 从字符串读取格式化输入。  
tk_str_append | 字符串追加函数。  
tk_str_case_end_with | 检查字符串是否以指定的字符串appendix结尾(忽略大小写)。  
tk_str_case_start_with | 检查字符串是否以指定的字符串prefix开头(忽略大小写)。  
tk_str_copy | 字符串拷贝函数。  
tk_str_end_with | 检查字符串是否以指定的字符串appendix结尾。  
tk_str_is_in_array | 检查字符串是否在字符串数组中。  
tk_str_start_with | 检查字符串是否以指定的字符串prefix开头。  
tk_str_tolower | 将大写字母转换为小写字母。  
tk_str_totitle | 将单词首字母转换为大写字母。  
tk_str_toupper | 将小写字母转换为大写字母。  
tk_strcmp | 字符串比较函数。  
tk_strcpy | 将src所指向的字符串复制到dst。  
tk_strdup | 字符串拷贝函数。  
tk_stricmp | 字符串比较函数（不区分大小写）。  
tk_strlen | 获取字符串的长度。str为空时返回0。  
tk_strncpy | 将src所指向的字符串复制到dst，最多复制len个字符串，并在[len]位置添加’\0’。  
tk_strncpy_s | 将src所指向的字符串复制到dst，最多复制min(dst_len-1, src_len)个字符串，并在[len]位置添加’\0’。  
tk_strndup | 字符串拷贝函数，最多复制len个字符串。  
tk_strnlen | 获取字符串的长度。str为空时返回0。  
tk_strrstr | 从后往前查找指定的字符串。  
tk_strs_bsearch | 在字符串数组中查找字符串。  
tk_strtoi | 将字符串转换为整型。  
tk_strtol | 将字符串转换为长整型。  
tk_strtoll | 将字符串转换为长整型。  
tk_to_utf8_argv | 将宽字符串数组转换成utf8字符串数组。  
tk_under_score_to_camel | 将下划线名字转成驼峰名字。  
tk_utf8_dup_wstr | 将UCS字符串拷贝为utf8字符串。  
tk_value_to_angle | 将value转换成角度。  
tk_vsnprintf | 将可变参数ap按照format格式化字符串，并将字符串复制到str中。  
tk_watob | 将宽字符串转换为布尔类型。  
tk_watof | 将宽字符串转换为浮点类型。  
tk_watoi | 将宽字符串转换为整型。  
tk_watoi_n | 将宽字符串转换为整型。  
tk_wild_card_match | 简单的通配符匹配。*匹配0到多个字符，?匹配1个字符。  
tk_wstr_count_c | 统计UCS字符串中某个字符出现的次数。  
tk_wstr_dup_utf8 | 将utf8字符串拷贝为UCS字符串。  
tk_wstr_select_word | 获取字符串中距离某个位置最近的单词（中文或英文字符）或数字字符的范围，选取的范围由标点符号或空格分隔开，得到的范围由left与right两个指针获取。  
tk_wstrcmp | 字符串比较函数。  
tk_wstrdup | 宽字符串拷贝函数。  
tk_wstricmp | 字符串比较函数（不区分大小写）。  
xml_file_expand_read | expand include process instruction to file content: <?include filename=”view_me.inc” ?>  
xml_file_expand_subfilenames_get | 从xml文件中获取所有使用 <?include filename=”” ?> 导入的文件名称  
  
#### bits_stream_get 函数

* * *

  * 函数功能：



> 从buff中获取第index位的值。

  * 函数原型：


    
    
    ret_t bits_stream_get (const uint8_t* buff, uint32_t size, uint32_t index, bool_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buff | const uint8_t* | 数据。  
size | uint32_t | 数据长度。  
index | uint32_t | 位索引。  
value | bool_t* | 返回值。  
  
#### bits_stream_set 函数

* * *

  * 函数功能：



> 设置buff中第index位的值。

  * 函数原型：


    
    
    ret_t bits_stream_set (uint8_t* buff, uint32_t size, uint32_t index, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buff | uint8_t* | 数据。  
size | uint32_t | 数据长度。  
index | uint32_t | 位索引。  
value | bool_t | 值。  
  
#### compare_always_equal 函数

* * *

  * 函数功能：



> 始终返回相等。

  * 函数原型：


    
    
    int compare_always_equal (const void* a, const void* b);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 始终返回0。  
a | const void* | 数据a。  
b | const void* | 数据b。  
  
#### data_url_copy 函数

* * *

  * 函数功能：



> 将数据从源URL拷贝到目标URL。

  * 函数原型：


    
    
    ret_t data_url_copy (const char* dst_url, const char* src_url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dst_url | const char* | 目标URL。  
src_url | const char* | 源URL。  
  
#### default_destroy 函数

* * *

  * 函数功能：



> 缺省的destroy函数。释放data指向的内存。

  * 函数原型：


    
    
    ret_t default_destroy (void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
data | void* | 数据。  
  
#### dummy_destroy 函数

* * *

  * 函数功能：



> 空的destroy函数。

  * 函数原型：


    
    
    ret_t dummy_destroy (void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
data | void* | 数据。  
  
#### file_read_as_unix_text 函数

* * *

  * 函数功能：



> 读取文本文件。并将windows换行(\r\n)或macos换行(\r)转换为unix换行(\n)。

  * 函数原型：


    
    
    char* file_read_as_unix_text (const char* filename, uint32_t* size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回读取的数据，需要调用TKMEM_FREE释放。  
filename | const char* | 文件名。  
size | uint32_t* | 返回实际读取的长度。  
  
#### filename_to_name 函数

* * *

  * 函数功能：



> 从完整文件名中获取文件名。

  * 函数原型：


    
    
    ret_t filename_to_name (const char* filename, char* str, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | const char* | 完整的文件名。  
str | char* | 用于返回文件名。  
size | uint32_t | 文件名(str参数)的最大长度。  
  
#### filename_to_name_ex 函数

* * *

  * 函数功能：



> 从完整文件名中获取文件名。

  * 函数原型：


    
    
    ret_t filename_to_name_ex (const char* filename, char* str, uint32_t size, bool_t remove_extname);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | const char* | 完整的文件名。  
str | char* | 用于返回文件名。  
size | uint32_t | 文件名(str参数)的最大长度。  
remove_extname | bool_t | 是否移除扩展名。  
  
#### image_region_parse 函数

* * *

  * 函数功能：



> 解析子图的区域信息。

  * 函数原型：


    
    
    ret_t image_region_parse (uint32_t img_w, uint32_t img_h, const char* region, rect_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
img_w | uint32_t | 图片宽度。  
img_h | uint32_t | 图片宽度。  
region | const char* | region。  
r | rect_t* | 返回具体位置。  
  
#### object_to_json 函数

* * *

  * 函数功能：



> 将对象转换成json字符串。

  * 函数原型：


    
    
    ret_t object_to_json (tk_object_t* obj, str_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
str | str_t* | 用于返回结果。  
  
#### pointer_compare 函数

* * *

  * 函数功能：



> 指针比较。

  * 函数原型：


    
    
    int pointer_compare (const void* a, const void* b);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回0表示相等，返回负数表示小于，返回整数表示大于。  
a | const void* | 数据a。  
b | const void* | 数据b。  
  
#### ret_code_from_name 函数

* * *

  * 函数功能：



> 将ret_t的文本名称转换成对应的值。

  * 函数原型：


    
    
    ret_t ret_code_from_name (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回对应的值。  
name | const char* | 字符串。  
  
#### ret_code_to_name 函数

* * *

  * 函数功能：



> 将ret_t转换成对应的文本名称。

  * 函数原型：


    
    
    const char* ret_code_to_name (ret_t ret);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回对应的名称。  
ret | ret_t | 代码。  
  
#### tk_angle 函数

* * *

  * 函数功能：



> 计算两点之间的角度(逆时针方向为正，GUI坐标)。

  * 函数原型：


    
    
    double tk_angle (int cx, int cy, int x, int y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回角度。  
cx | int | cx。  
cy | int | cy。  
x | int | x。  
y | int | y。  
  
#### tk_atob 函数

* * *

  * 函数功能：



> 将字符串转换为布尔类型。

  * 函数原型：


    
    
    bool_t tk_atob (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回转换后的布尔类型。  
str | const char* | 要转换为布尔类型的字符串。  
  
#### tk_atof 函数

* * *

  * 函数功能：



> 将字符串转换为浮点类型。

  * 函数原型：


    
    
    double tk_atof (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回转换后的浮点类型。  
str | const char* | 要转换为浮点类型的字符串。  
  
#### tk_atoi 函数

* * *

  * 函数功能：



> 将字符串转换为整型数。

  * 函数原型：


    
    
    int32_t tk_atoi (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回转换后的整型。  
str | const char* | 要转换为整型数的字符串。  
  
#### tk_atol 函数

* * *

  * 函数功能：



> 将字符串转换为整型。

  * 函数原型：


    
    
    int64_t tk_atol (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回转换后的整型。  
str | const char* | 要转换为整型的字符串。  
  
#### tk_atoul 函数

* * *

  * 函数功能：



> 将字符串转换为整型。

  * 函数原型：


    
    
    uint64_t tk_atoul (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回转换后的整型。  
str | const char* | 要转换为整型的字符串。  
  
#### tk_basic_type_from_name 函数

* * *

  * 函数功能：



> 将类型名称转换成对应的类型。

  * 函数原型：


    
    
    value_type_t tk_basic_type_from_name (const char* type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_type_t | 返回对应的类型。  
type | const char* | 类型名称。  
  
#### tk_bits_data_from_bytes_data 函数

* * *

  * 函数功能：



> 将bytes数据转换成bits数据(每个字节对应一位)。

  * 函数原型：


    
    
    ret_t tk_bits_data_from_bytes_data (uint8_t* bits, uint32_t bits_size, uint8_t* bytes, uint32_t bytes_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bits | uint8_t* | bits。  
bits_size | uint32_t | bits内存的长度(字节数)。  
bytes | uint8_t* | bytes。  
bytes_size | uint32_t | bytes内存的长度(字节数)。  
  
#### tk_bits_data_to_bytes_data 函数

* * *

  * 函数功能：



> 将bits数据转换成bytes数据(每个字节对应一位)。

  * 函数原型：


    
    
    ret_t tk_bits_data_to_bytes_data (uint8_t* bits, uint32_t bits_size, uint8_t* bytes, uint32_t bytes_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
bits | uint8_t* | bits。  
bits_size | uint32_t | bits内存的长度(字节数)。  
bytes | uint8_t* | bytes。  
bytes_size | uint32_t | bytes内存的长度(字节数)。  
  
#### tk_bits_to_bytes 函数

* * *

  * 函数功能：



> 将bits数转换成bytes数。

  * 函数原型：


    
    
    uint32_t tk_bits_to_bytes (uint32_t bits);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回bytes。  
bits | uint32_t | bits。  
  
#### tk_buffer_get_value 函数

* * *

  * 函数功能：



> 获取buffer中的值。

  * 函数原型：


    
    
    ret_t tk_buffer_get_value (uint8_t* buffer, uint32_t size, value_type_t type, int16_t offset, int16_t bit_offset, value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | uint8_t* | buffer。  
size | uint32_t | buffer的长度。  
type | value_type_t | 类型。  
offset | int16_t | 偏移。  
bit_offset | int16_t | 位偏移。  
value | value_t* | 值。  
  
#### tk_buffer_set_value 函数

* * *

  * 函数功能：



> 设置buffer中的值。

  * 函数原型：


    
    
    ret_t tk_buffer_set_value (uint8_t* buffer, uint32_t size, value_type_t type, int16_t offset, int16_t bit_offset, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
buffer | uint8_t* | buffer。  
size | uint32_t | buffer的长度。  
type | value_type_t | 类型。  
offset | int16_t | 偏移。  
bit_offset | int16_t | 位偏移。  
value | const value_t* | 值。  
  
#### tk_count_char 函数

* * *

  * 函数功能：



> 统计字符串中某个字符出现的次数。

  * 函数原型：


    
    
    uint32_t tk_count_char (const char* str, char c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回字符出现的次数。  
str | const char* | 字符串。  
c | char | 字符。  
  
#### tk_date_time_format 函数

* * *

  * 函数功能：



> 格式化时间。 格式规则： * Y 代表年(完整显示) * M 代表月(1-12) * D 代表日(1-31) * h 代表时(0-23) * H 代表时(1-12) * m 代表分(0-59) * s 代表秒(0-59) * w 代表星期(0-6) * W 代表星期的英文缩写 * T 代表时段AM/PM * YY 代表年(只显示末两位) * MM 代表月(01-12) * DD 代表日(01-31) * hh 代表时(00-23) * HH 代表时(01-12) * mm 代表分(00-59) * ss 代表秒(00-59) * MMM 代表月的英文缩写

如 日期时间为：2018/11/12 9:10:20 * “Y/M/D”显示为”2018/11/12” * “Y-M-D”显示为”2018-11-12” * “Y-M-D h:m:s”显示为”2018-11-12 9:10:20” * “Y-M-D hh:mm:ss”显示为”2018-11-12 09:10:20”

  * 函数原型：


    
    
    ret_t tk_date_time_format (uint64_t time, const char* format, str_t* result);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
time | uint64_t | 时间。  
format | const char* | 格式化字符串。  
result | str_t* | 用于返回结果。  
  
#### tk_distance 函数

* * *

  * 函数功能：



> 计算两点之间的距离。

  * 函数原型：


    
    
    uint32_t tk_distance (int x1, int y1, int x2, int y2);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回距离。  
x1 | int | x1。  
y1 | int | y1。  
x2 | int | x2。  
y2 | int | y2。  
  
#### tk_eval_ratio_or_px 函数

* * *

  * 函数功能：



> 如果expr以px/PX结束，直接返回expr前面的数值。 如果expr以%结束，而且数值大于1，返回(数值 * value)/100。 否则将数值当作比例，返回(数值 * value)。
> 
> 为了兼容以前的处理，如果expr以%结束，但是数值在0到1之间，此时忽略%。
    
    
    tk_eval_ratio_or_px("0.5", 100) => 50
    tk_eval_ratio_or_px("20px", 100) => 20
    tk_eval_ratio_or_px("20%", 100) => 20
    tk_eval_ratio_or_px("0.5%", 100) => 50
    

  * 函数原型：


    
    
    float_t tk_eval_ratio_or_px (const char* expr, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回计算结果。  
expr | const char* | 表达式(如100px, 0.5等)  
value | int32_t | 值。  
  
#### tk_free_utf8_argv 函数

* * *

  * 函数功能：



> 释放utf8字符串数组。

  * 函数原型：


    
    
    ret_t tk_free_utf8_argv (int argc, char** argv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
argc | int | 参数个数。  
argv | char** | 参数。  
  
#### tk_ftoa 函数

* * *

  * 函数功能：



> 将浮点型转换为字符串。

  * 函数原型：


    
    
    const char* tk_ftoa (char* str, int len, double f);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回字符串。  
str | char* | 保存字符串缓冲区。  
len | int | 缓冲区大小。  
f | double | 要转换的浮点型。  
  
#### tk_int_is_in_array 函数

* * *

  * 函数功能：



> 检查整数是否在整数数组中。

  * 函数原型：


    
    
    bool_t tk_int_is_in_array (int32_t v, const int32_t* array, uint32_t array_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示在，否则表示不在。  
v | int32_t | 整数。  
array | const int32_t* | 整数数组。  
array_size | uint32_t | 整数数组中整数的个数。  
  
#### tk_is_ui_thread 函数

* * *

  * 函数功能：



> 判断当前线程是否是UI线程。

  * 函数原型：


    
    
    bool_t tk_is_ui_thread ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示否。  
  
#### tk_is_valid_name 函数

* * *

  * 函数功能：



> 判断是否是有效的属性名。

  * 函数原型：


    
    
    bool_t tk_is_valid_name (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 如果名称有效返回TRUE，否则返回FALSE。  
name | const char* | 名字字符串。  
  
#### tk_itoa 函数

* * *

  * 函数功能：



> 将整型转换为字符串。

  * 函数原型：


    
    
    const char* tk_itoa (char* str, int len, int n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回字符串。  
str | char* | 保存字符串缓冲区。  
len | int | 缓冲区大小。  
n | int | 要转换的整型。  
  
#### tk_levelize 函数

* * *

  * 函数功能：



> 将value转换成level。 比如levels为”0-20;21-40;41-60;61-80;81-100”，value为50，那么返回2。

  * 函数原型：


    
    
    int32_t tk_levelize (const char* levels, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回level。  
levels | const char* | 级别字符串。  
value | int32_t | 值。  
  
#### tk_lltoa 函数

* * *

  * 函数功能：



> 将整型转换为字符串。

  * 函数原型：


    
    
    const char* tk_lltoa (char* str, int len, int64_t n);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回字符串。  
str | char* | 保存字符串缓冲区。  
len | int | 缓冲区大小。  
n | int64_t | 要转换的整型。  
  
#### tk_memcpy 函数

* * *

  * 函数功能：



> 内存拷贝。 在地址对齐的情况下并且少于 64 个字节，效率会比 memcpy 要快，否则会退化为 memcpy。

  * 函数原型：


    
    
    void* tk_memcpy (void* dst, const void* src, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回成功返回 dst 地址，失败返回 NULL。  
dst | void* | 目标字符串。  
src | const void* | 源字符串。  
len | uint32_t | 拷贝长度。  
  
#### tk_memcpy16 函数

* * *

  * 函数功能：



> 拷贝数据2字节。

  * 函数原型：


    
    
    uint16_t* tk_memcpy16 (uint16_t* dst, uint16_t* src, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t* | 返回设置好的buff。  
dst | uint16_t* | 目标  
src | uint16_t* | 源。  
size | uint32_t | 个数。  
  
#### tk_memcpy32 函数

* * *

  * 函数功能：



> 拷贝数据4字节。

  * 函数原型：


    
    
    uint32_t* tk_memcpy32 (uint32_t* dst, uint32_t* src, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t* | 返回设置好的buff。  
dst | uint32_t* | 目标  
src | uint32_t* | 源。  
size | uint32_t | 个数。  
  
#### tk_memdup 函数

* * *

  * 函数功能：



> 内存拷贝。

  * 函数原型：


    
    
    void* tk_memdup (const void* data, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回指向的向新的内存指针，如果失败则返回NULL。  
data | const void* | 原内存。  
len | uint32_t | 长度。  
  
#### tk_memset16 函数

* * *

  * 函数功能：



> 设置数据2字节。

  * 函数原型：


    
    
    uint16_t* tk_memset16 (uint16_t* buff, uint16_t val, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t* | 返回设置好的buff。  
buff | uint16_t* | buff  
val | uint16_t | 值。  
size | uint32_t | 个数。  
  
#### tk_memset24 函数

* * *

  * 函数功能：



> 设置数据3字节。

  * 函数原型：


    
    
    uint32_t* tk_memset24 (uint32_t* buff, void* val, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t* | 返回设置好的buff。  
buff | uint32_t* | buff。  
val | void* | 值。  
size | uint32_t | 个数。  
  
#### tk_memset32 函数

* * *

  * 函数功能：



> 设置数据4字节。

  * 函数原型：


    
    
    uint32_t* tk_memset32 (uint32_t* buff, uint32_t val, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t* | 返回设置好的buff。  
buff | uint32_t* | buff。  
val | uint32_t | 值。  
size | uint32_t | 个数。  
  
#### tk_mergesort 函数

* * *

  * 函数功能：



> 归并排序(如果需要稳定的排序，可以选择归并排序，而不是快速排序)。

  * 函数原型：


    
    
    ret_t tk_mergesort (void* base, size_t nmemb, size_t size, tk_compare_t cmp);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
base | void* | 数据。  
nmemb | size_t | 元素个数。  
size | size_t | 元素大小。  
cmp | tk_compare_t | 比较函数。  
  
#### tk_normalize_key_name 函数

* * *

  * 函数功能：



> 标准化key_name

  * 函数原型：


    
    
    const char* tk_normalize_key_name (const char* name, char* fixed_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回标准化后的字符串。  
name | const char* | key_name。  
fixed_name | char* | 保存标准化后的字符串。  
  
#### tk_pixel_copy 函数

* * *

  * 函数功能：



> 已bpp字节为标准拷贝数据。

  * 函数原型：


    
    
    void* tk_pixel_copy (void* dst, const void* src, uint32_t size, uint8_t bpp);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回设置好的buff。  
dst | void* | 目标  
src | const void* | 源。  
size | uint32_t | 个数。  
bpp | uint8_t | 单个数据的字节数。  
  
#### tk_pointer_from_int 函数

* * *

  * 函数功能：



> 将int转换成指针。
> 
> 常用于将int类型的数据作为回调函数的ctx。

  * 函数原型：


    
    
    void* tk_pointer_from_int (int32_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回对应的指针。  
v | int32_t | 整数。  
  
#### tk_pointer_from_long 函数

* * *

  * 函数功能：



> 将long转换成指针。
> 
> 常用于将long类型的数据作为回调函数的ctx。

  * 函数原型：


    
    
    void* tk_pointer_from_long (uint64_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回对应的指针。  
v | uint64_t | 整数。  
  
#### tk_pointer_to_int 函数

* * *

  * 函数功能：



> 将指针转换成int。
> 
> 与tk_pointer_from_int配套使用，也就是pointer本身必须就是整数，而不是指针，否则pointer会被截断。

  * 函数原型：


    
    
    int32_t tk_pointer_to_int (const void* p);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回对应的int数据。  
p | const void* | 指针。  
  
#### tk_pointer_to_long 函数

* * *

  * 函数功能：



> 将指针转换成long。
> 
> 与tk_pointer_from_long配套使用，也就是pointer本身必须就是整数，而不是指针，否则pointer会被截断。

  * 函数原型：


    
    
    uint64_t tk_pointer_to_long (const void* p);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回对应的long数据。  
p | const void* | 指针。  
  
#### tk_qsort 函数

* * *

  * 函数功能：



> 快速排序。

  * 函数原型：


    
    
    ret_t tk_qsort (void** array, size_t nr, tk_compare_t cmp);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
array | void** | 数据。  
nr | size_t | 元素个数。  
cmp | tk_compare_t | 比较函数。  
  
#### tk_replace_char 函数

* * *

  * 函数功能：



> 替换字符。

  * 函数原型：


    
    
    char* tk_replace_char (char* str, char from, char to);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回str。  
str | char* | 原字符串。  
from | char | 被替换的字符。  
to | char | 替换成的字符。  
  
#### tk_replace_locale 函数

* * *

  * 函数功能：



> 将文本中的$locale$替换为对应的语言。

  * 函数原型：


    
    
    ret_t tk_replace_locale (const char* name, char* out, const char* locale);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
name | const char* | 文本。  
out | char* | 替换后保存的字符串。  
locale | const char* | 语言。  
  
#### tk_set_ui_thread 函数

* * *

  * 函数功能：



> 设置UI线程的ID。

  * 函数原型：


    
    
    ret_t tk_set_ui_thread (uint64_t ui_thread_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ui_thread_id | uint64_t | UI线程的ID。  
  
#### tk_size_of_basic_type 函数

* * *

  * 函数功能：



> 获取基本类型的大小(字节数)。

  * 函数原型：


    
    
    uint32_t tk_size_of_basic_type (value_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回大小。  
type | value_type_t | 类型。  
  
#### tk_skip_chars 函数

* * *

  * 函数功能：



> 跳过字符串中的字符。

  * 函数原型：


    
    
    const char* tk_skip_chars (const char* str, const char* chars);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回跳过后的字符串。  
str | const char* | 字符串。  
chars | const char* | 字符集。  
  
#### tk_skip_to_chars 函数

* * *

  * 函数功能：



> 跳到字符串中的字符。

  * 函数原型：


    
    
    const char* tk_skip_to_chars (const char* str, const char* chars);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回跳到的字符串。  
str | const char* | 字符串。  
chars | const char* | 字符集。  
  
#### tk_skip_to_num 函数

* * *

  * 函数功能：



> 跳过字符串函数，如：字符串”hello123world”，返回的结果是”123world”。

  * 函数原型：


    
    
    const char* tk_skip_to_num (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回转换后的字符串。  
str | const char* | 要输入的原始字符串。  
  
#### tk_snprintf 函数

* * *

  * 函数功能：



> 将可变参数(…)按照format格式化字符串，并将字符串复制到str中。

  * 函数原型：


    
    
    int tk_snprintf (char* str, size_t size, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回格式化后的字符串长度。  
str | char* | 目标字符串。  
size | size_t | 拷贝字节数。  
format | const char* | 格式化字符串。  
  
#### tk_sscanf 函数

* * *

  * 函数功能：



> 从字符串读取格式化输入。

  * 函数原型：


    
    
    int tk_sscanf (const char* str, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回成功匹配和赋值的个数。  
str | const char* | 要输入的字符串。  
format | const char* | 格式化字符串。  
  
#### tk_sscanf_simple 函数

* * *

  * 函数功能：



> 从字符串读取格式化输入。 TKC自己实现的，只支持几种简单的格式，在没有sscanf函数时使用。

  * 函数原型：


    
    
    int tk_sscanf_simple (const char* str, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回成功匹配和赋值的个数。  
str | const char* | 要输入的字符串。  
format | const char* | 格式化字符串。  
  
#### tk_str_append 函数

* * *

  * 函数功能：



> 字符串追加函数。

  * 函数原型：


    
    
    ret_t tk_str_append (char* str, uint32_t max_len, const char* s);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | char* | 被追加字符串。  
max_len | uint32_t | 字符串的最大长度。  
s | const char* | 要追加的字符串。  
  
#### tk_str_case_end_with 函数

* * *

  * 函数功能：



> 检查字符串是否以指定的字符串appendix结尾(忽略大小写)。

  * 函数原型：


    
    
    bool_t tk_str_case_end_with (const char* str, const char* appendix);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是；否则表示不是。  
str | const char* | 要检查字符串。  
appendix | const char* | 被检查的字符串。  
  
#### tk_str_case_start_with 函数

* * *

  * 函数功能：



> 检查字符串是否以指定的字符串prefix开头(忽略大小写)。

  * 函数原型：


    
    
    bool_t tk_str_case_start_with (const char* str, const char* prefix);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是；否则表示不是。  
str | const char* | 要检查字符串。  
prefix | const char* | 被检查的字符串。  
  
#### tk_str_copy 函数

* * *

  * 函数功能：



> 字符串拷贝函数。 XXX: 要求dst为NULL或内存块的首地址，本函数调用之后，dst可能无效，请保留返回的地址 该函数会自动申请内存，调用后需要使用TKMEM_FREE释放。

  * 函数原型：


    
    
    char* tk_str_copy (char* dst, const char* src);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回指向的复制字符串指针，如果失败则返回NULL。  
dst | char* | 目标字符串。  
src | const char* | 源字符串。  
  
#### tk_str_end_with 函数

* * *

  * 函数功能：



> 检查字符串是否以指定的字符串appendix结尾。

  * 函数原型：


    
    
    bool_t tk_str_end_with (const char* str, const char* appendix);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是；否则表示不是。  
str | const char* | 要检查字符串。  
appendix | const char* | 被检查的字符串。  
  
#### tk_str_is_in_array 函数

* * *

  * 函数功能：



> 检查字符串是否在字符串数组中。

  * 函数原型：


    
    
    bool_t tk_str_is_in_array (const char* str, const char** str_array, uint32_t array_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示在，否则表示不在。  
str | const char* | 字符串。  
str_array | const char** | 字符串数组。  
array_size | uint32_t | 字符串数组中字符串的个数。  
  
#### tk_str_start_with 函数

* * *

  * 函数功能：



> 检查字符串是否以指定的字符串prefix开头。

  * 函数原型：


    
    
    bool_t tk_str_start_with (const char* str, const char* prefix);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是；否则表示不是。  
str | const char* | 要检查字符串。  
prefix | const char* | 被检查的字符串。  
  
#### tk_str_tolower 函数

* * *

  * 函数功能：



> 将大写字母转换为小写字母。 修改传入的字符串。

  * 函数原型：


    
    
    char* tk_str_tolower (char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回转换后的小写字母字符串。  
str | char* | 要被转换成小写字母的字符串。  
  
#### tk_str_totitle 函数

* * *

  * 函数功能：



> 将单词首字母转换为大写字母。 修改传入的字符串。

  * 函数原型：


    
    
    char* tk_str_totitle (char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回转换后的字符串。  
str | char* | 被转换的字符串。  
  
#### tk_str_toupper 函数

* * *

  * 函数功能：



> 将小写字母转换为大写字母。 修改传入的字符串。

  * 函数原型：


    
    
    char* tk_str_toupper (char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回转换后的大写字母字符串。  
str | char* | 要被转换成大写字母的字符串。  
  
#### tk_strcmp 函数

* * *

  * 函数功能：



> 字符串比较函数。

  * 函数原型：


    
    
    int32_t tk_strcmp (const char* a, const char* b);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果返回值=-1，则表示a为NULL；如果返回值=1，则表示b为NULL；如果返回值<0，则表示a小于b；如果返回值>0，则表示a大于b；如果返回值=0，则表示a等于b。  
a | const char* | 要进行比较的第一个字符串。  
b | const char* | 要进行比较的第二个字符串。  
  
#### tk_strcpy 函数

* * *

  * 函数功能：



> 将src所指向的字符串复制到dst。

  * 函数原型：


    
    
    char* tk_strcpy (char* dst, const char* src);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回目标字符串。  
dst | char* | 目标字符串。  
src | const char* | 原字符串。  
  
#### tk_strdup 函数

* * *

  * 函数功能：



> 字符串拷贝函数。

  * 函数原型：


    
    
    char* tk_strdup (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回指向的复制字符串指针，如果失败则返回NULL。  
str | const char* | 原字符串。  
  
#### tk_stricmp 函数

* * *

  * 函数功能：



> 字符串比较函数（不区分大小写）。

  * 函数原型：


    
    
    int32_t tk_stricmp (const char* a, const char* b);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果返回值=-1，则表示a为NULL；如果返回值=1，则表示b为NULL；如果返回值<0，则表示a小于b；如果返回值>0，则表示a大于b；如果返回值=0，则表示a等于b。  
a | const char* | 要进行比较的第一个字符串。  
b | const char* | 要进行比较的第二个字符串。  
  
#### tk_strlen 函数

* * *

  * 函数功能：



> 获取字符串的长度。str为空时返回0。

  * 函数原型：


    
    
    uint32_t tk_strlen (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回字符串的长度。  
str | const char* | 字符串。  
  
#### tk_strncpy 函数

* * *

  * 函数功能：



> 将src所指向的字符串复制到dst，最多复制len个字符串，并在[len]位置添加’\0’。
> 
> 请确保dst的长度>=(len+1)

  * 函数原型：


    
    
    char* tk_strncpy (char* dst, const char* src, size_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回目标字符串。  
dst | char* | 目标字符串。  
src | const char* | 源字符串。  
len | size_t | 要复制的字符串个数。  
  
#### tk_strncpy_s 函数

* * *

  * 函数功能：



> 将src所指向的字符串复制到dst，最多复制min(dst_len-1, src_len)个字符串，并在[len]位置添加’\0’。 如果 dst 和 src 的地址对齐的话，效率会比 strncpy 高，如果小于 64 个字节的话，效率是最高的。

  * 函数原型：


    
    
    char* tk_strncpy_s (char* dst, size_t dst_len, const char* src, size_t src_len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回目标字符串。  
dst | char* | 目标字符串。  
dst_len | size_t | 目标字符串内存长度。  
src | const char* | 源字符串。  
src_len | size_t | 要复制的字符串个数。  
  
#### tk_strndup 函数

* * *

  * 函数功能：



> 字符串拷贝函数，最多复制len个字符串。

  * 函数原型：


    
    
    char* tk_strndup (const char* str, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回指向的复制字符串指针，如果失败则返回NULL。  
str | const char* | 原字符串。  
len | uint32_t | 要复制的字符串个数。  
  
#### tk_strnlen 函数

* * *

  * 函数功能：



> 获取字符串的长度。str为空时返回0。

  * 函数原型：


    
    
    uint32_t tk_strnlen (const char* str, uint32_t maxlen);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回字符串的长度。  
str | const char* | 字符串。  
maxlen | uint32_t | 最大长度。  
  
#### tk_strrstr 函数

* * *

  * 函数功能：



> 从后往前查找指定的字符串。

  * 函数原型：


    
    
    const char* tk_strrstr (const char* str, const char* substr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回字符串的位置或者NULL。  
str | const char* | 字符串。  
substr | const char* | 子字符串。  
  
#### tk_strs_bsearch 函数

* * *

  * 函数功能：



> 在字符串数组中查找字符串。

  * 函数原型：


    
    
    const char* tk_strs_bsearch (const char** strs, uint32_t nr, const char* str, bool_t case_sensitive);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回找到的字符串。  
strs | const char** | 字符串数组(已排序)。  
nr | uint32_t | 字符串个数。  
str | const char* | 字符串。  
case_sensitive | bool_t | 是否区分大小写。  
  
#### tk_strtoi 函数

* * *

  * 函数功能：



> 将字符串转换为整型。

  * 函数原型：


    
    
    int32_t tk_strtoi (const char* str, const char** end, int base);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回转换后的整型。  
str | const char* | 要转换为整型的字符串。  
end | const char** | 对类型char*的对象的引用。  
base | int | 基数。  
  
#### tk_strtol 函数

* * *

  * 函数功能：



> 将字符串转换为长整型。

  * 函数原型：


    
    
    long tk_strtol (const char* str, const char** end, int base);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | long | 返回转换后的长整型。  
str | const char* | 要转换为长整型的字符串。  
end | const char** | 对类型char*的对象的引用。  
base | int | 基数。  
  
#### tk_strtoll 函数

* * *

  * 函数功能：



> 将字符串转换为长整型。

  * 函数原型：


    
    
    int64_t tk_strtoll (const char* str, const char** end, int base);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回转换后的长整型。  
str | const char* | 要转换为长整型的字符串。  
end | const char** | 对类型char*的对象的引用。  
base | int | 基数。  
  
#### tk_to_utf8_argv 函数

* * *

  * 函数功能：



> 将宽字符串数组转换成utf8字符串数组。

  * 函数原型：


    
    
    char** tk_to_utf8_argv (int argc, wchar_t** argv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char** | 返回utf8字符串数组。  
argc | int | 参数个数。  
argv | wchar_t** | 参数。  
  
#### tk_under_score_to_camel 函数

* * *

  * 函数功能：



> 将下划线名字转成驼峰名字。

  * 函数原型：


    
    
    const char* tk_under_score_to_camel (const char* name, char* out, uint32_t max_out_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回T驼峰名字。  
name | const char* | 下划线名字。  
out | char* | 驼峰名字(保存结果)。  
max_out_size | uint32_t | 结果最大长度。  
  
#### tk_utf8_dup_wstr 函数

* * *

  * 函数功能：



> 将UCS字符串拷贝为utf8字符串。

  * 函数原型：


    
    
    char* tk_utf8_dup_wstr (const wchar_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char* | 返回UTF-8字符串(需要调用TKMEM_FREE释放)。  
str | const wchar_t* | 字符串。  
  
#### tk_value_to_angle 函数

* * *

  * 函数功能：



> 将value转换成角度。

  * 函数原型：


    
    
    double tk_value_to_angle (double value, double min, double max, double start_angle, double end_angle, bool_t counter_clock_wise);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回角度。  
value | double | 值。  
min | double | 最小值。  
max | double | 最大值。  
start_angle | double | 开始角度。  
end_angle | double | 结束角度。  
counter_clock_wise | bool_t | 是否逆时针。  
  
#### tk_vsnprintf 函数

* * *

  * 函数功能：



> 将可变参数ap按照format格式化字符串，并将字符串复制到str中。

  * 函数原型：


    
    
    int tk_vsnprintf (char* str, size_t size, const char* format, va_list ap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回格式化后的字符串长度。  
str | char* | 目标字符串。  
size | size_t | 拷贝字节数。  
format | const char* | 格式化字符串。  
ap | va_list | 可变参数。  
  
#### tk_watob 函数

* * *

  * 函数功能：



> 将宽字符串转换为布尔类型。

  * 函数原型：


    
    
    bool_t tk_watob (const wchar_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回转换后的布尔类型。  
str | const wchar_t* | 要转换为布尔类型的宽字符串。  
  
#### tk_watof 函数

* * *

  * 函数功能：



> 将宽字符串转换为浮点类型。

  * 函数原型：


    
    
    double tk_watof (const wchar_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回转换后的浮点类型。  
str | const wchar_t* | 要转换为浮点类型的宽字符串。  
  
#### tk_watoi 函数

* * *

  * 函数功能：



> 将宽字符串转换为整型。

  * 函数原型：


    
    
    int tk_watoi (const wchar_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回转换后的整型。  
str | const wchar_t* | 要转换为整型的宽字符串。  
  
#### tk_watoi_n 函数

* * *

  * 函数功能：



> 将宽字符串转换为整型。

  * 函数原型：


    
    
    int tk_watoi_n (const wchar_t* str, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 返回转换后的整型。  
str | const wchar_t* | 要转换为整型的宽字符串。  
len | uint32_t | 字符串长度。  
  
#### tk_wild_card_match 函数

* * *

  * 函数功能：



> 简单的通配符匹配。*匹配0到多个字符，?匹配1个字符。 示例：
    
    
    tk_wild_card_match("*c", "abc");
    tk_wild_card_match("a?c", "abc");
    

  * 函数原型：


    
    
    bool_t tk_wild_card_match (const char* pattern, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示匹配，否则表示不匹配。  
pattern | const char* | 字符串。  
str | const char* | 字符串。  
  
#### tk_wstr_count_c 函数

* * *

  * 函数功能：



> 统计UCS字符串中某个字符出现的次数。

  * 函数原型：


    
    
    uint32_t tk_wstr_count_c (const wchar_t* str, wchar_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回字符出现的次数。  
str | const wchar_t* | 字符串。  
c | wchar_t | 字符。  
  
#### tk_wstr_dup_utf8 函数

* * *

  * 函数功能：



> 将utf8字符串拷贝为UCS字符串。

  * 函数原型：


    
    
    wchar_t* tk_wstr_dup_utf8 (const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wchar_t* | 返回UCS字符串(需要调用TKMEM_FREE释放)。  
str | const char* | utf8编码的字符串。  
  
#### tk_wstr_select_word 函数

* * *

  * 函数功能：



> 获取字符串中距离某个位置最近的单词（中文或英文字符）或数字字符的范围，选取的范围由标点符号或空格分隔开，得到的范围由left与right两个指针获取。

  * 函数原型：


    
    
    ret_t tk_wstr_select_word (const wchar_t* str, uint32_t len, uint32_t index, int32_t* left, int32_t* right);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | const wchar_t* | 字符串。  
len | uint32_t | 字符串的长度。  
index | uint32_t | 字符串中某个位置的下标。  
left | int32_t* | int32_t指针，用来获取范围结果的左边界值  
right | int32_t* | int32_t指针，用来获取范围结果的右边界值  
  
#### tk_wstrcmp 函数

* * *

  * 函数功能：



> 字符串比较函数。

  * 函数原型：


    
    
    int32_t tk_wstrcmp (const wchar_t* a, const wchar_t* b);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果返回值=-1，则表示a为NULL；如果返回值=1，则表示b为NULL；如果返回值<0，则表示a小于b；如果返回值>0，则表示a大于b；如果返回值=0，则表示a等于b。  
a | const wchar_t* | 要进行比较的第一个字符串。  
b | const wchar_t* | 要进行比较的第二个字符串。  
  
#### tk_wstrdup 函数

* * *

  * 函数功能：



> 宽字符串拷贝函数。

  * 函数原型：


    
    
    wchar_t* tk_wstrdup (const wchar_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wchar_t* | 返回指向的复制宽字符串指针，如果失败则返回NULL。  
str | const wchar_t* | 原宽字符串。  
  
#### tk_wstricmp 函数

* * *

  * 函数功能：



> 字符串比较函数（不区分大小写）。

  * 函数原型：


    
    
    int32_t tk_wstricmp (const wchar_t* a, const wchar_t* b);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果返回值=-1，则表示a为NULL；如果返回值=1，则表示b为NULL；如果返回值<0，则表示a小于b；如果返回值>0，则表示a大于b；如果返回值=0，则表示a等于b。  
a | const wchar_t* | 要进行比较的第一个字符串。  
b | const wchar_t* | 要进行比较的第二个字符串。  
  
#### xml_file_expand_read 函数

* * *

  * 函数功能：



> expand include process instruction to file content: <?include filename=”view_me.inc” ?>

  * 函数原型：


    
    
    ret_t xml_file_expand_read (const char* filename, str_t* s);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | const char* | 文件名。  
s | str_t* | 用于返回内容。  
  
#### xml_file_expand_subfilenames_get 函数

* * *

  * 函数功能：



> 从xml文件中获取所有使用 <?include filename=”” ?> 导入的文件名称

  * 函数原型：


    
    
    ret_t xml_file_expand_subfilenames_get (const char* filename, char*** subfilenames, uint32_t* size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | const char* | 文件名。  
subfilenames | char*** | 用于返回文件名称集合。  
size | uint32_t* | 用于返回文件名称集合的大小。
