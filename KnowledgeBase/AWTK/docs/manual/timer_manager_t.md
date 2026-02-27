## timer_manager_t

### 概述

## 定时器管理器。

### 函数

函数名称 | 说明  
---|---  
timer_manager | 获取缺省的定时器管理器。  
timer_manager_add | 添加定时器。  
timer_manager_add_with_id | 添加定时器。（可以指定 timer_id ，如果发现 timer_id 冲突则添加失败）。  
timer_manager_add_with_type | 添加对应类型的定时器。  
timer_manager_add_with_type_and_id | 添加对应类型和id的定时器。  
timer_manager_all_remove_by_ctx | 根据上下文删除所有对应的定时器。  
timer_manager_all_remove_by_ctx_and_type | 移除对应类型和上下文的所有定时器。  
timer_manager_append | 追加定时器。  
timer_manager_count | 返回定时器的个数。  
timer_manager_create | 创建定时器管理器。  
timer_manager_deinit | 析构定时器管理器。  
timer_manager_destroy | 析构并释放定时器管理器。  
timer_manager_dispatch | 检查全部定时器的函数，如果时间到期，调用相应的timer函数。  
timer_manager_find | 查找指定ID的定时器。  
timer_manager_get_next_timer_id | 获取下一个可用的 timer_id。  
timer_manager_init | 初始化定时器管理器。  
timer_manager_next_time | 返回最近的定时器到期时间(毫秒)。  
timer_manager_remove | 根据id删除定时器。  
timer_manager_reset | 重置定时器。  
timer_manager_set | 设置缺省的定时器管理器。  
  
#### timer_manager 函数

* * *

  * 函数功能：



> 获取缺省的定时器管理器。

  * 函数原型：


    
    
    timer_manager_t* timer_manager ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | timer_manager_t* | 返回定时器管理器对象。  
  
#### timer_manager_add 函数

* * *

  * 函数功能：



> 添加定时器。

  * 函数原型：


    
    
    uint32_t timer_manager_add (timer_manager_t* timer_manager, timer_func_t on_timer, void* ctx, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回timer的ID，TK_INVALID_ID表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
on_timer | timer_func_t | timer回调函数。  
ctx | void* | timer回调函数的上下文。  
duration | uint32_t | 时间(毫秒)。  
  
#### timer_manager_add_with_id 函数

* * *

  * 函数功能：



> 添加定时器。（可以指定 timer_id ，如果发现 timer_id 冲突则添加失败）。

  * 函数原型：


    
    
    uint32_t timer_manager_add_with_id (timer_manager_t* timer_manager, uint32_t id, timer_func_t on_timer, void* ctx, uint32_t duration);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回timer的ID，TK_INVALID_ID表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
id | uint32_t | timer_id。  
on_timer | timer_func_t | timer回调函数。  
ctx | void* | timer回调函数的上下文。  
duration | uint32_t | 时间(毫秒)。  
  
#### timer_manager_add_with_type 函数

* * *

  * 函数功能：



> 添加对应类型的定时器。

  * 函数原型：


    
    
    uint32_t timer_manager_add_with_type (timer_manager_t* timer_manager, timer_func_t on_timer, void* ctx, uint32_t duration, uint16_t timer_info_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回定时器id。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
on_timer | timer_func_t | 定时器回调函数。  
ctx | void* | 上下文。  
duration | uint32_t | 时间(毫秒)。  
timer_info_type | uint16_t | timer_info_type。  
  
#### timer_manager_add_with_type_and_id 函数

* * *

  * 函数功能：



> 添加对应类型和id的定时器。

  * 函数原型：


    
    
    uint32_t timer_manager_add_with_type_and_id (timer_manager_t* timer_manager, uint32_t id, timer_func_t on_timer, void* ctx, uint32_t duration, uint16_t timer_info_type, bool_t is_check_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回定时器id。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
id | uint32_t | id。  
on_timer | timer_func_t | 定时器回调函数。  
ctx | void* | 上下文。  
duration | uint32_t | 时间(毫秒)。  
timer_info_type | uint16_t | timer_info_type。  
is_check_id | bool_t | 是否校验id。  
  
#### timer_manager_all_remove_by_ctx 函数

* * *

  * 函数功能：



> 根据上下文删除所有对应的定时器。

  * 函数原型：


    
    
    ret_t timer_manager_all_remove_by_ctx (timer_manager_t* timer_manager, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
ctx | void* | timer回调函数的上下文。  
  
#### timer_manager_all_remove_by_ctx_and_type 函数

* * *

  * 函数功能：



> 移除对应类型和上下文的所有定时器。

  * 函数原型：


    
    
    ret_t timer_manager_all_remove_by_ctx_and_type (timer_manager_t* timer_manager, uint16_t type, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
type | uint16_t | 类型。  
ctx | void* | 上下文。  
  
#### timer_manager_append 函数

* * *

  * 函数功能：



> 追加定时器。

  * 函数原型：


    
    
    ret_t timer_manager_append (timer_manager_t* timer_manager, timer_info_t* timer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。。  
timer | timer_info_t* | timer对象。  
  
#### timer_manager_count 函数

* * *

  * 函数功能：



> 返回定时器的个数。

  * 函数原型：


    
    
    uint32_t timer_manager_count (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回timer的个数。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
  
#### timer_manager_create 函数

* * *

  * 函数功能：



> 创建定时器管理器。

  * 函数原型：


    
    
    timer_manager_t* timer_manager_create (timer_get_time_t get_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | timer_manager_t* | 返回定时器管理器对象。  
get_time | timer_get_time_t | 获取当前时间的函数。  
  
#### timer_manager_deinit 函数

* * *

  * 函数功能：



> 析构定时器管理器。

  * 函数原型：


    
    
    ret_t timer_manager_deinit (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
  
#### timer_manager_destroy 函数

* * *

  * 函数功能：



> 析构并释放定时器管理器。

  * 函数原型：


    
    
    ret_t timer_manager_destroy (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
  
#### timer_manager_dispatch 函数

* * *

  * 函数功能：



> 检查全部定时器的函数，如果时间到期，调用相应的timer函数。

  * 函数原型：


    
    
    ret_t timer_manager_dispatch (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
  
#### timer_manager_find 函数

* * *

  * 函数功能：



> 查找指定ID的定时器。

  * 函数原型：


    
    
    const timer_info_t* timer_manager_find (timer_manager_t* timer_manager, uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const timer_info_t* | 返回timer的信息。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
timer_id | uint32_t | timer_id  
  
#### timer_manager_get_next_timer_id 函数

* * *

  * 函数功能：



> 获取下一个可用的 timer_id。

  * 函数原型：


    
    
    uint32_t timer_manager_get_next_timer_id (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle的ID，TK_INVALID_ID表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
  
#### timer_manager_init 函数

* * *

  * 函数功能：



> 初始化定时器管理器。

  * 函数原型：


    
    
    timer_manager_t* timer_manager_init (timer_manager_t* timer_manager, timer_get_time_t get_time);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | timer_manager_t* | 返回定时器管理器对象。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
get_time | timer_get_time_t | 获取当前时间的函数。  
  
#### timer_manager_next_time 函数

* * *

  * 函数功能：



> 返回最近的定时器到期时间(毫秒)。

  * 函数原型：


    
    
    uint64_t timer_manager_next_time (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回最近的timer到期时间(毫秒)。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
  
#### timer_manager_remove 函数

* * *

  * 函数功能：



> 根据id删除定时器。

  * 函数原型：


    
    
    ret_t timer_manager_remove (timer_manager_t* timer_manager, uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
timer_id | uint32_t | timer_id。  
  
#### timer_manager_reset 函数

* * *

  * 函数功能：



> 重置定时器。

  * 函数原型：


    
    
    ret_t timer_manager_reset (timer_manager_t* timer_manager, uint32_t timer_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。  
timer_id | uint32_t | timer_id。  
  
#### timer_manager_set 函数

* * *

  * 函数功能：



> 设置缺省的定时器管理器。

  * 函数原型：


    
    
    ret_t timer_manager_set (timer_manager_t* timer_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
timer_manager | timer_manager_t* | 定时器管理器对象。
