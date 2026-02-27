## platform

### 概述

平台接口，包括：获取时间、休眠等函数。

* * *

### 函数

函数名称 | 说明  
---|---  
get_time_ms64 | 获取当前时间。  
platform_prepare |   
sleep_ms |   
  
#### get_time_ms64 函数

* * *

  * 函数功能：



> 获取当前时间。

  * 函数原型：


    
    
    uint64_t get_time_ms64 ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 成功返回当前时间。  
  
#### platform_prepare 函数

* * *

  * 函数功能：



> 平台准备函数。

  * 函数原型：


    
    
    ret_t platform_prepare ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### sleep_ms 函数

* * *

  * 函数功能：



> 睡眠毫秒。

  * 函数原型：


    
    
    void sleep_ms (uint32_t ms);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 无。  
ms | uint32_t | 毫秒。
