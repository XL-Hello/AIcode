## im_commit_event_t

### 概述

![image](images/im_commit_event_t_0.png)

## 输入法提交输入的文本事件。

### 函数

函数名称 | 说明  
---|---  
im_commit_event_init | 初始化im_commit事件。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
replace | bool_t | 是否替换原来的文本。  
text | const char* | 提交的文本。  
  
#### im_commit_event_init 函数

* * *

  * 函数功能：



> 初始化im_commit事件。

  * 函数原型：


    
    
    event_t* im_commit_event_init (im_commit_event_t* e, const char* text, bool_t replace);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_t* | 返回事件对象。  
e | im_commit_event_t* | 事件对象。  
text | const char* | 文本。  
replace | bool_t | 是否替代当前的内容。  
  
#### replace 属性

* * *

> 是否替换原来的文本。

  * 类型：bool_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### text 属性

* * *

> 提交的文本。

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
