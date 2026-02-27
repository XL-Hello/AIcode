## suggest_words_t

### 概述

## 输入法联想字词。

### 函数

函数名称 | 说明  
---|---  
suggest_words_create | 创建联想字对象。  
suggest_words_destroy | @deconstructor  
suggest_words_find | 查找prefix对应的联想字列表，成功后会更新words/words_nr。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
|  |   
  
#### suggest_words_create 函数

* * *

  * 函数功能：



> 创建联想字对象。

  * 函数原型：


    
    
    suggest_words_t* suggest_words_create (const asset_info_t* res);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | suggest_words_t* | 返回联想字对象。  
res | const asset_info_t* | 数据资源。  
  
#### suggest_words_destroy 函数

* * *

  * 函数功能：



> @deconstructor 销毁联想字对象。

  * 函数原型：


    
    
    ret_t suggest_words_destroy (suggest_words_t* suggest_words);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
suggest_words | suggest_words_t* | 联想字对象。  
  
#### suggest_words_find 函数

* * *

  * 函数功能：



> 查找prefix对应的联想字列表，成功后会更新words/words_nr。

  * 函数原型：


    
    
    ret_t suggest_words_find (suggest_words_t* suggest_words, wchar_t c);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
suggest_words | suggest_words_t* | 联想字对象。  
c | wchar_t | 字符。
