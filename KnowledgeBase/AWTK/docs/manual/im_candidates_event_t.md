## im_candidates_event_t

### 概述

![image](images/im_candidates_event_t_0.png)

## 输入法请求显示候选字的事件。

### 属性

属性名称 | 类型 | 说明  
---|---|---  
candidates | const char* | 可选的文本，多个文本以\0分隔。如：里\0李\0力\0离\0  
candidates_nr | uint32_t | 可选的文本的个数。  
selected | int32_t | 缺省选中某个候选字，小于0不选择任何候选字。  
  
#### candidates 属性

* * *

> 可选的文本，多个文本以\0分隔。如：里\0李\0力\0离\0

  * 类型：const char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### candidates_nr 属性

* * *

> 可选的文本的个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### selected 属性

* * *

> 缺省选中某个候选字，小于0不选择任何候选字。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
