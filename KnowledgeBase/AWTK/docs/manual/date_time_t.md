## date_time_t

### 概述

日期时间。

## > 在嵌入式平台中，在系统初始时，需要调用date_time_global_init设置实际获取/设置系统时间的函数。

### 函数

函数名称 | 说明  
---|---  
date_time_add_delta | 加上一个偏移量(s)。  
date_time_create | 创建date_time对象，并初始为当前日期和时间(一般供脚本语言中使用)。  
date_time_destroy | 销毁date_time对象(一般供脚本语言中使用)。  
date_time_from_time | 从time转换而来(按GMT转换)。  
date_time_get_days | 获取指定年份月份的天数。  
date_time_get_month_name | 获取指定月份的英文名称(简写)。  
date_time_get_wday | 获取指定日期是周几(0-6, Sunday = 0)。。  
date_time_get_wday_name | 获取周几的英文名称(简写)。  
date_time_global_init_ex | 时间日期全局初始化。  
date_time_init | 初始为当前日期和时间。  
date_time_is_leap | 是否是闰年。  
date_time_parse_date | 解析日期。  
date_time_parse_date_time | 解析日期和时间。  
date_time_parse_time | 解析时间。  
date_time_set | 设置当前时间。  
date_time_set_day | 设置日。  
date_time_set_hour | 设置小时。  
date_time_set_minute | 设置分钟。  
date_time_set_month | 设置月。  
date_time_set_second | 设置秒。  
date_time_set_year | 设置年。  
date_time_to_time | 转换成time(按GMT转换)。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
day | int32_t | 日(1-31)。  
hour | int32_t | 时(0 - 23)。  
minute | int32_t | 分(0 - 59)。  
month | int32_t | 月(1-12)。  
second | int32_t | 秒(0 - 59)。  
wday | int32_t | 星期几(0-6, Sunday = 0)。  
year | int32_t | 年。  
  
#### date_time_add_delta 函数

* * *

  * 函数功能：



> 加上一个偏移量(s)。

  * 函数原型：


    
    
    ret_t date_time_add_delta (date_time_t* dt, int64_t delta);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
delta | int64_t | 偏移量(s)。  
  
#### date_time_create 函数

* * *

  * 函数功能：



> 创建date_time对象，并初始为当前日期和时间(一般供脚本语言中使用)。

  * 函数原型：


    
    
    date_time_t* date_time_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | date_time_t* | 返回date_time对象。  
  
#### date_time_destroy 函数

* * *

  * 函数功能：



> 销毁date_time对象(一般供脚本语言中使用)。

  * 函数原型：


    
    
    ret_t date_time_destroy (date_time_t* dt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
  
#### date_time_from_time 函数

* * *

  * 函数功能：



> 从time转换而来(按GMT转换)。

  * 函数原型：


    
    
    ret_t date_time_from_time (date_time_t* dt, int64_t time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
time | int64_t | 时间。  
  
#### date_time_get_days 函数

* * *

  * 函数功能：



> 获取指定年份月份的天数。

  * 函数原型：


    
    
    int32_t date_time_get_days (uint32_t year, uint32_t month);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回大于0表示天数，否则表示失败。  
year | uint32_t | 年份。  
month | uint32_t | 月份(1-12)。  
  
#### date_time_get_month_name 函数

* * *

  * 函数功能：



> 获取指定月份的英文名称(简写)。

  * 函数原型：


    
    
    const char* date_time_get_month_name (uint32_t month);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回指定月份的英文名称(简写)。  
month | uint32_t | 月份(1-12)。  
  
#### date_time_get_wday 函数

* * *

  * 函数功能：



> 获取指定日期是周几(0-6, Sunday = 0)。。

  * 函数原型：


    
    
    int32_t date_time_get_wday (uint32_t year, uint32_t month, uint32_t day);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回大于等于0表示周几(0-6)，否则表示失败。  
year | uint32_t | 年份。  
month | uint32_t | 月份(1-12)。  
day | uint32_t | 日(1-31)。  
  
#### date_time_get_wday_name 函数

* * *

  * 函数功能：



> 获取周几的英文名称(简写)。

  * 函数原型：


    
    
    const char* date_time_get_wday_name (uint32_t wday);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回指定周几的英文名称(简写)。  
wday | uint32_t | 星期几(0-6, Sunday = 0)。  
  
#### date_time_global_init_ex 函数

* * *

  * 函数功能：



> 时间日期全局初始化。
> 
> 嵌入式平台需要提供并设置获取当前日期和时间的函数，否则相关的功能(如时钟控件)将无法正常工作。

  * 函数原型：


    
    
    ret_t date_time_global_init_ex (const date_time_vtable_t* vt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
vt | const date_time_vtable_t* | 日期和时间的相关函数的实现。  
  
#### date_time_init 函数

* * *

  * 函数功能：



> 初始为当前日期和时间。

  * 函数原型：


    
    
    date_time_t* date_time_init (date_time_t* dt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | date_time_t* | 返回date_time对象。  
dt | date_time_t* | date_time对象。  
  
#### date_time_is_leap 函数

* * *

  * 函数功能：



> 是否是闰年。

  * 函数原型：


    
    
    bool_t date_time_is_leap (uint32_t year);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示否。  
year | uint32_t | 年份。  
  
#### date_time_parse_date 函数

* * *

  * 函数功能：



> 解析日期。

  * 函数原型：


    
    
    ret_t date_time_parse_date (date_time_t* dt, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
str | const char* | 日期字符串。  
  
#### date_time_parse_date_time 函数

* * *

  * 函数功能：



> 解析日期和时间。

  * 函数原型：


    
    
    ret_t date_time_parse_date_time (date_time_t* dt, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
str | const char* | 日期和时间字符串。  
  
#### date_time_parse_time 函数

* * *

  * 函数功能：



> 解析时间。

  * 函数原型：


    
    
    ret_t date_time_parse_time (date_time_t* dt, const char* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
str | const char* | 时间字符串。  
  
#### date_time_set 函数

* * *

  * 函数功能：



> 设置当前时间。

  * 函数原型：


    
    
    ret_t date_time_set (date_time_t* dt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
  
#### date_time_set_day 函数

* * *

  * 函数功能：



> 设置日。

  * 函数原型：


    
    
    ret_t date_time_set_day (date_time_t* dt, uint32_t day);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
day | uint32_t | 日。  
  
#### date_time_set_hour 函数

* * *

  * 函数功能：



> 设置小时。

  * 函数原型：


    
    
    ret_t date_time_set_hour (date_time_t* dt, uint32_t hour);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
hour | uint32_t | 小时。  
  
#### date_time_set_minute 函数

* * *

  * 函数功能：



> 设置分钟。

  * 函数原型：


    
    
    ret_t date_time_set_minute (date_time_t* dt, uint32_t minute);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
minute | uint32_t | 分钟。  
  
#### date_time_set_month 函数

* * *

  * 函数功能：



> 设置月。

  * 函数原型：


    
    
    ret_t date_time_set_month (date_time_t* dt, uint32_t month);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
month | uint32_t | 月。  
  
#### date_time_set_second 函数

* * *

  * 函数功能：



> 设置秒。

  * 函数原型：


    
    
    ret_t date_time_set_second (date_time_t* dt, uint32_t second);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
second | uint32_t | 秒。  
  
#### date_time_set_year 函数

* * *

  * 函数功能：



> 设置年。

  * 函数原型：


    
    
    ret_t date_time_set_year (date_time_t* dt, uint32_t year);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dt | date_time_t* | date_time对象。  
year | uint32_t | 年。  
  
#### date_time_to_time 函数

* * *

  * 函数功能：



> 转换成time(按GMT转换)。

  * 函数原型：


    
    
    int64_t date_time_to_time (date_time_t* dt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回time。  
dt | date_time_t* | date_time对象。  
  
#### day 属性

* * *

> 日(1-31)。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### hour 属性

* * *

> 时(0 - 23)。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### minute 属性

* * *

> 分(0 - 59)。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### month 属性

* * *

> 月(1-12)。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### second 属性

* * *

> 秒(0 - 59)。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### wday 属性

* * *

> 星期几(0-6, Sunday = 0)。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### year 属性

* * *

> 年。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
