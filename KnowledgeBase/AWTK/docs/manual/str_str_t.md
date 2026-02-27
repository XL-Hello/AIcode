## str_str_t

### 概述

字符串-字符串类型。

负责把一个字符串映射成另外一个字符串。

示例：
    
    
    static const str_str_t color_values[] = {{"1", "red"}, {"2", "black"}, {"3", "blue"}, {"4", "white"}};
    const char* value = str_str_value(color_values, "3");
    const char* name = str_str_name(color_values, "blue", "0");
    printf("value = %s \n", value);
    printf("name = %s \n", name);
    

* * *

### 函数

函数名称 | 说明  
---|---  
str_str_name | 根据value获取对应的name。  
str_str_value | 根据name获取对应的value。  
  
#### str_str_name 函数

* * *

  * 函数功能：



> 根据value获取对应的name。

  * 函数原型：


    
    
    const char* str_str_name (const str_str_t* items, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回name。  
items | const str_str_t* | str_str_t数组。  
value | const char* | value  
  
#### str_str_value 函数

* * *

  * 函数功能：



> 根据name获取对应的value。

  * 函数原型：


    
    
    const char* str_str_value (const str_str_t* items, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回value。  
items | const str_str_t* | str_str_t数组。  
name | const char* | name。
