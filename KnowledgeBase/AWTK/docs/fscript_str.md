## 字符串扩展函数

### 1.ulen

## > 获取 unicode 字符个数。

#### 原型
    
    
    ulen(str) => int
    

#### 示例
    
    
    print(ulen('致远电子'))
    

### 2.char_at

## > 获取指定位置的字符。

#### 原型
    
    
    char_at(str, index) => str
    

> index 为负数时，从后往前取。比如-1 表示最后一个元素。

#### 示例
    
    
    print(char_at('致远电子', 1))
    print(char_at('ZLG', 1))
    

### 3.index_of

## > 查找指定子串的位置，如果没有找到返回-1。

#### 原型
    
    
    index_of(str, substr) => int
    

#### 示例
    
    
    print(index_of('hello AWTK and AWTK', 'AWTK'))
    

### 4.last_index_of

## > 反向查找指定子串的位置，如果没有找到返回-1。

#### 原型
    
    
    last_index_of(str, substr) => int
    

#### 示例
    
    
    print(last_index_of('hello AWTK and AWTK', 'AWTK'))
    

### 5.trim_left

## > 去掉字符串左边的空白字符。

#### 原型
    
    
    trim_left(str) => str
    

#### 示例
    
    
    print(trim_left('   AWTK  '))
    

### 6.trim_right

## > 去掉字符串右边的空白字符。

#### 原型
    
    
    trim_right(str) => str
    

#### 示例
    
    
    print(trim_right('   AWTK  ') + "1234")
    

### 7.totitle

> 将字符串中单词的首字母转换成大写。

* * *

#### 原型
    
    
    totitle(str) => str
    

#### 示例
    
    
    print(totitle("it is ok!"))
    

### 8.prompt

## > 在控制台提示用户输入字符串（仅当定义了 HAS_STIOD 时有效）。

#### 原型
    
    
    prompt(tips) => str
    

#### 示例
    
    
    var a = prompt('input a number:');
    print(int(a)+100);
    

### 9.usubstr

## > 取子字符串(unicode)。

#### 原型
    
    
    usubstr(str, start, end) => str
    

>   * 不包括end
>   * start 为负数时，从后往前取。比如-1 表示最后一个元素。
>   * end 为负数时，从后往前取。比如-1 表示最后一个元素。
>   * end 省略表示到最后全部元素。
> 


#### 示例
    
    
    var a="致远电子"
    assert(usubstr(a) == '致远电子');
    assert(usubstr(a,0) == '致远电子');
    assert(usubstr(a,0,1) == '致');
    assert(usubstr(a,0,-1) == '致远电');
    assert(usubstr(a,-2,-1) == '电');
    assert(usubstr(a, -3) == '远电子');
    

### 10.text_reverse

## > 字符串反向

#### 原型
    
    
    text_reverse(str) => str
    

#### 示例
    
    
    print(text_reverse("hello"));
    

### 11.text_count

## > 统计子串出现的次数。

#### 原型
    
    
    text_count(str, substr) => int
    

#### 示例
    
    
    print(text_count("hello zlg!", "zlg"));
    

### 12.str_len

## > 计算字符串的长度。

#### 原型
    
    
    str_len(str) => uint32
    

#### 示例
    
    
    print(str_len("hello"));
    

### 13.str_is_empty

## > 判断字符串是否为空。

#### 原型
    
    
    str_is_empty(str) => bool
    

#### 示例
    
    
    print(str_is_empty(""));
    print(str_is_empty("zlg"));
    

### 14.str_append

## > 追加字符串。

#### 原型
    
    
    str_append(str, append_str) => str
    

#### 示例
    
    
    print(str_append("hello ", "zlg"));
    

### 15.char_at_first

## > 获取首字符。

#### 原型
    
    
    char_at_first(str) => str
    

#### 示例
    
    
    print(char_at_first("hello"));
    

### 16.char_at_last

## > 获取尾字符。

#### 原型
    
    
    char_at_last(str) => str
    

#### 示例
    
    
    print(char_at_last("hello"));
    

### 17.char_at_random

## > 获取随机位置的字符。

#### 原型
    
    
    char_at_random(str) => str
    

#### 示例
    
    
    print(char_at_random("hello"));
    

### 18.str_start_with

## > 检查字符串是否以指定的字符串开头。

#### 原型
    
    
    str_start_with(str, prefix) => bool
    

#### 示例
    
    
    str_start_with('AWTK', 'AW')
    

### 19.str_end_with

## > 检查字符串是否以指定的字符串结尾。

#### 原型
    
    
    str_end_with(str, prefix) => bool
    

#### 示例
    
    
    str_end_with('AWTK', 'TK')
    
