## wstr_t

### 概述

可变长度的宽字符字符串。

示例：
    
    
    wstr_t s;
    wstr_init(&s, 0);
    
    wstr_append(&s, L"abc");
    wstr_append(&s, L"123");
    
    wstr_reset(&s);
    

## > 先调wstr_init进行初始化，最后调用wstr_reset释放内存。

### 函数

函数名称 | 说明  
---|---  
wstr_add_float | 将字符串转成浮点数，加上delta，再转换回来。  
wstr_append | 追加字符串。  
wstr_append_int | 追加整数到字符串。  
wstr_append_more | 追加多个字符串。以NULL结束。  
wstr_append_utf8 | 追加UTF8字符串。  
wstr_append_with_len | 追加字符串。  
wstr_attach | 通过附加到一个buff来初始化str。  
wstr_clear | 清除字符串内容。  
wstr_count_char | 统计指定字符的个数。  
wstr_create | 创建str对象。  
wstr_destroy | 销毁str对象。  
wstr_eq | 判断两个字符串是否相等。  
wstr_equal | 判断两个字符是否相同。  
wstr_extend | 扩展字符串到指定的容量。  
wstr_from_float | 用浮点数初始化字符串。  
wstr_from_int | 用整数初始化字符串。  
wstr_from_int64 | 用整数初始化字符串。  
wstr_from_value | 用value初始化字符串。  
wstr_get_utf8 | 获取UTF8字符串。  
wstr_init | 初始化字符串对象。  
wstr_insert | 在指定位置插入字符串。  
wstr_modify_wchar | 修改字符。  
wstr_normalize_newline | 规范化换行符。  
wstr_pop | 删除尾部字符。  
wstr_push | 追加一个字符。  
wstr_push_int | 追加一个整数。  
wstr_remove | 删除指定范围的字符。  
wstr_reset | 重置字符串为空。  
wstr_set | 设置字符串。  
wstr_set_utf8 | 设置UTF8字符串。  
wstr_set_utf8_with_len | 设置UTF8字符串。  
wstr_set_with_len | 设置字符串。  
wstr_shrink | 如果字符串长度大于指定长度，收缩字符串到指定的长度。  
wstr_to_float | 将字符串转成浮点数。  
wstr_to_int | 将字符串转成整数。  
wstr_to_int64 | 将字符串转成整数。  
wstr_trim_float_zero | 去掉浮点数小数点尾部的零。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
capacity | uint32_t | 容量。  
size | uint32_t | 长度。  
str | wchar_t* | 字符串。  
  
#### wstr_add_float 函数

* * *

  * 函数功能：



> 将字符串转成浮点数，加上delta，再转换回来。

  * 函数原型：


    
    
    ret_t wstr_add_float (wstr_t* str, double delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
delta | double | 要加上的值。  
  
#### wstr_append 函数

* * *

  * 函数功能：



> 追加字符串。

  * 函数原型：


    
    
    ret_t wstr_append (wstr_t* str, const wchar_t* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const wchar_t* | 要追加的字符串。  
  
#### wstr_append_int 函数

* * *

  * 函数功能：



> 追加整数到字符串。

  * 函数原型：


    
    
    ret_t wstr_append_int (wstr_t* str, int32_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | int32_t | 整数。  
  
#### wstr_append_more 函数

* * *

  * 函数功能：



> 追加多个字符串。以NULL结束。

示例：
    
    
    wstr_t s;
    wstr_init(&s, 0);
    
    wstr_append_more(&s, L"abc", L"123", NULL);
    log_debug("%s\n", s.str);
    
    wstr_reset(&s);
    

  * 函数原型：


    
    
    ret_t wstr_append_more (wstr_t* str, const wchar_t* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const wchar_t* | 要追加的字符串。  
  
#### wstr_append_utf8 函数

* * *

  * 函数功能：



> 追加UTF8字符串。

  * 函数原型：


    
    
    ret_t wstr_append_utf8 (wstr_t* str, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const char* | 要设置的字符串。  
  
#### wstr_append_with_len 函数

* * *

  * 函数功能：



> 追加字符串。

  * 函数原型：


    
    
    ret_t wstr_append_with_len (wstr_t* str, const wchar_t* text, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const wchar_t* | 要追加的字符串。  
len | uint32_t | 字符串长度。  
  
#### wstr_attach 函数

* * *

  * 函数功能：



> 通过附加到一个buff来初始化str。 可以避免str动态分配内存，同时也不会自动扩展内存，使用完成后无需调用str_reset。
    
    
    wstr_t s;
    wchar_t buff[32];
    wstr_attach(&s, buff, ARRAY_SIZE(buff));
    wstr_set(&s, L"abc");
    wstr_append(&s, L"123");
    

  * 函数原型：


    
    
    wstr_t* wstr_attach (wstr_t* str, wchar_t* buff, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wstr_t* | str对象本身。  
str | wstr_t* | str对象。  
buff | wchar_t* | 缓冲区。  
capacity | uint32_t | 初始容量。  
  
#### wstr_clear 函数

* * *

  * 函数功能：



> 清除字符串内容。

  * 函数原型：


    
    
    ret_t wstr_clear (wstr_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
  
#### wstr_count_char 函数

* * *

  * 函数功能：



> 统计指定字符的个数。

  * 函数原型：


    
    
    uint32_t wstr_count_char (wstr_t* str, wchar_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回指定字符的个数。  
str | wstr_t* | str对象。  
c | wchar_t | 字符。  
  
#### wstr_create 函数

* * *

  * 函数功能：



> 创建str对象。 备注：最后调用wstr_destroy释放内存

  * 函数原型：


    
    
    wstr_t* wstr_create (uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wstr_t* | str对象。  
capacity | uint32_t | 初始容量。  
  
#### wstr_destroy 函数

* * *

  * 函数功能：



> 销毁str对象。

  * 函数原型：


    
    
    ret_t wstr_destroy (wstr_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
  
#### wstr_eq 函数

* * *

  * 函数功能：



> 判断两个字符串是否相等。

  * 函数原型：


    
    
    bool_t wstr_eq (wstr_t* str, const wchar_t* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回是否相等。  
str | wstr_t* | str对象。  
text | const wchar_t* | 待比较的字符串。  
  
#### wstr_equal 函数

* * *

  * 函数功能：



> 判断两个字符是否相同。

  * 函数原型：


    
    
    bool_t wstr_equal (wstr_t* str, wstr_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示相同，否则表示不同。  
str | wstr_t* | str对象。  
other | wstr_t* | str对象。  
  
#### wstr_extend 函数

* * *

  * 函数功能：



> 扩展字符串到指定的容量。

  * 函数原型：


    
    
    ret_t wstr_extend (wstr_t* str, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | wstr对象。  
capacity | uint32_t | 新的容量。  
  
#### wstr_from_float 函数

* * *

  * 函数功能：



> 用浮点数初始化字符串。

  * 函数原型：


    
    
    ret_t wstr_from_float (wstr_t* str, double v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | double | 浮点数。  
  
#### wstr_from_int 函数

* * *

  * 函数功能：



> 用整数初始化字符串。

  * 函数原型：


    
    
    ret_t wstr_from_int (wstr_t* str, int32_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | int32_t | 整数。  
  
#### wstr_from_int64 函数

* * *

  * 函数功能：



> 用整数初始化字符串。

  * 函数原型：


    
    
    ret_t wstr_from_int64 (wstr_t* str, int64_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | int64_t | 整数。  
  
#### wstr_from_value 函数

* * *

  * 函数功能：



> 用value初始化字符串。

  * 函数原型：


    
    
    ret_t wstr_from_value (wstr_t* str, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | const value_t* | value。  
  
#### wstr_get_utf8 函数

* * *

  * 函数功能：



> 获取UTF8字符串。

  * 函数原型：


    
    
    ret_t wstr_get_utf8 (wstr_t* str, char* text, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | char* | 返回的字符串。  
size | uint32_t | text最大长度。  
  
#### wstr_init 函数

* * *

  * 函数功能：



> 初始化字符串对象。 备注：最后调用wstr_reset释放内存

  * 函数原型：


    
    
    wstr_t* wstr_init (wstr_t* str, uint32_t capacity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | wstr_t* | str对象本身。  
str | wstr_t* | str对象。  
capacity | uint32_t | 初始容量。  
  
#### wstr_insert 函数

* * *

  * 函数功能：



> 在指定位置插入字符串。

  * 函数原型：


    
    
    ret_t wstr_insert (wstr_t* str, uint32_t offset, const wchar_t* text, uint32_t nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
offset | uint32_t | 指定的位置。  
text | const wchar_t* | 待插入的文本。  
nr | uint32_t | 要插入的字符数。  
  
#### wstr_modify_wchar 函数

* * *

  * 函数功能：



> 修改字符。

  * 函数原型：


    
    
    ret_t wstr_modify_wchar (wstr_t* str, uint32_t pos, wchar_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
pos | uint32_t | 修改的位置。  
c | wchar_t | 修改的字符。  
  
#### wstr_normalize_newline 函数

* * *

  * 函数功能：



> 规范化换行符。

  * 函数原型：


    
    
    ret_t wstr_normalize_newline (wstr_t* str, wchar_t newline);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
newline | wchar_t | 换行符。  
  
#### wstr_pop 函数

* * *

  * 函数功能：



> 删除尾部字符。

  * 函数原型：


    
    
    ret_t wstr_pop (wstr_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
  
#### wstr_push 函数

* * *

  * 函数功能：



> 追加一个字符。

  * 函数原型：


    
    
    ret_t wstr_push (wstr_t* str, const wchar_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
c | const wchar_t | 字符。  
  
#### wstr_push_int 函数

* * *

  * 函数功能：



> 追加一个整数。

  * 函数原型：


    
    
    ret_t wstr_push_int (wstr_t* str, const char* format, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
format | const char* | 格式(用于snprintf格式化数值)  
value | int32_t | 数值。  
  
#### wstr_remove 函数

* * *

  * 函数功能：



> 删除指定范围的字符。

  * 函数原型：


    
    
    ret_t wstr_remove (wstr_t* str, uint32_t offset, uint32_t nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
offset | uint32_t | 指定的位置。  
nr | uint32_t | 要删除的字符数。  
  
#### wstr_reset 函数

* * *

  * 函数功能：



> 重置字符串为空。

  * 函数原型：


    
    
    ret_t wstr_reset (wstr_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
  
#### wstr_set 函数

* * *

  * 函数功能：



> 设置字符串。

  * 函数原型：


    
    
    ret_t wstr_set (wstr_t* str, const wchar_t* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const wchar_t* | 要设置的字符串。  
  
#### wstr_set_utf8 函数

* * *

  * 函数功能：



> 设置UTF8字符串。

  * 函数原型：


    
    
    ret_t wstr_set_utf8 (wstr_t* str, const char* text);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const char* | 要设置的字符串。  
  
#### wstr_set_utf8_with_len 函数

* * *

  * 函数功能：



> 设置UTF8字符串。

  * 函数原型：


    
    
    ret_t wstr_set_utf8_with_len (wstr_t* str, const char* text, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const char* | 要设置的字符串。  
len | uint32_t | 长度。  
  
#### wstr_set_with_len 函数

* * *

  * 函数功能：



> 设置字符串。

  * 函数原型：


    
    
    ret_t wstr_set_with_len (wstr_t* str, const wchar_t* text, uint32_t len);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
text | const wchar_t* | 要设置的字符串。  
len | uint32_t | 字符串长度。  
  
#### wstr_shrink 函数

* * *

  * 函数功能：



> 如果字符串长度大于指定长度，收缩字符串到指定的长度。

  * 函数原型：


    
    
    ret_t wstr_shrink (wstr_t* str, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | wstr对象。  
size | uint32_t | 新的长度。  
  
#### wstr_to_float 函数

* * *

  * 函数功能：



> 将字符串转成浮点数。

  * 函数原型：


    
    
    ret_t wstr_to_float (wstr_t* str, double* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | double* | 用于返回浮点数。  
  
#### wstr_to_int 函数

* * *

  * 函数功能：



> 将字符串转成整数。

  * 函数原型：


    
    
    ret_t wstr_to_int (wstr_t* str, int32_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | int32_t* | 用于返回整数。  
  
#### wstr_to_int64 函数

* * *

  * 函数功能：



> 将字符串转成整数。

  * 函数原型：


    
    
    ret_t wstr_to_int64 (wstr_t* str, int64_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
v | int64_t* | 用于返回整数。  
  
#### wstr_trim_float_zero 函数

* * *

  * 函数功能：



> 去掉浮点数小数点尾部的零。

  * 函数原型：


    
    
    ret_t wstr_trim_float_zero (wstr_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
str | wstr_t* | str对象。  
  
#### capacity 属性

* * *

> 容量。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 长度。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### str 属性

* * *

> 字符串。

  * 类型：wchar_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
