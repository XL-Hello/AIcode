## idle_manager_t

### 概述

## idle_manager_t管理器。

### 函数

函数名称 | 说明  
---|---  
idle_manager | 获取缺省的idle_manager_t管理器。  
idle_manager_add | 添加idle。  
idle_manager_add_with_id | 添加 idle（可以指定 idle_id ，如果发现 idle_id 冲突则添加失败）。  
idle_manager_add_with_type | 添加对应类型的idle。  
idle_manager_add_with_type_and_id | 添加对应类型和id的idle。  
idle_manager_append | 追加idle。  
idle_manager_count | 返回idle的个数。  
idle_manager_create | 创建idle_manager_t管理器。  
idle_manager_deinit | 析构idle_manager_t管理器。  
idle_manager_destroy | 析构并释放idle_manager_t管理器。  
idle_manager_dispatch | 检查全部idle的函数，如果时间到期，调用相应的idle函数。  
idle_manager_exist | 对应回调函数和上下文的idle是否存在。  
idle_manager_find | 查找指定ID的idle。  
idle_manager_get_next_idle_id | 获取下一个可用的 idle_id。  
idle_manager_init | 初始化idle_manager_t管理器。  
idle_manager_remove | 根据idle_id删除idle。  
idle_manager_remove_all | 删除全部idle。  
idle_manager_remove_all_by_ctx | 根据上下文删除所有符合条件的idle。  
idle_manager_remove_all_by_ctx_and_type | 移除对应类型和上下文的所有idle。  
idle_manager_set | 设置缺省的idle_manager_t管理器。  
  
#### idle_manager 函数

* * *

  * 函数功能：



> 获取缺省的idle_manager_t管理器。

  * 函数原型：


    
    
    idle_manager_t* idle_manager ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | idle_manager_t* | 返回idle_manager_t管理器对象。  
  
#### idle_manager_add 函数

* * *

  * 函数功能：



> 添加idle。

  * 函数原型：


    
    
    uint32_t idle_manager_add (idle_manager_t* idle_manager, idle_func_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle的ID，TK_INVALID_ID表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | idle回调函数的上下文。  
  
#### idle_manager_add_with_id 函数

* * *

  * 函数功能：



> 添加 idle（可以指定 idle_id ，如果发现 idle_id 冲突则添加失败）。

  * 函数原型：


    
    
    uint32_t idle_manager_add_with_id (idle_manager_t* idle_manager, uint32_t id, idle_func_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle的ID，TK_INVALID_ID表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
id | uint32_t | idle_id。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | idle回调函数的上下文。  
  
#### idle_manager_add_with_type 函数

* * *

  * 函数功能：



> 添加对应类型的idle。

  * 函数原型：


    
    
    uint32_t idle_manager_add_with_type (idle_manager_t* idle_manager, idle_func_t on_idle, void* ctx, uint16_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle_id。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | 上下文。  
type | uint16_t | 类型。  
  
#### idle_manager_add_with_type_and_id 函数

* * *

  * 函数功能：



> 添加对应类型和id的idle。

  * 函数原型：


    
    
    uint32_t idle_manager_add_with_type_and_id (idle_manager_t* idle_manager, uint32_t id, idle_func_t on_idle, void* ctx, uint16_t type, bool_t check_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle_id。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
id | uint32_t | id。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | 上下文。  
type | uint16_t | 类型。  
check_id | bool_t | 是否校验id。  
  
#### idle_manager_append 函数

* * *

  * 函数功能：



> 追加idle。

  * 函数原型：


    
    
    ret_t idle_manager_append (idle_manager_t* idle_manager, idle_info_t* idle);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
idle | idle_info_t* | idle对象。  
  
#### idle_manager_count 函数

* * *

  * 函数功能：



> 返回idle的个数。

  * 函数原型：


    
    
    uint32_t idle_manager_count (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回timer的个数。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
  
#### idle_manager_create 函数

* * *

  * 函数功能：



> 创建idle_manager_t管理器。

  * 函数原型：


    
    
    idle_manager_t* idle_manager_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | idle_manager_t* | 返回idle_manager_t管理器对象。  
  
#### idle_manager_deinit 函数

* * *

  * 函数功能：



> 析构idle_manager_t管理器。

  * 函数原型：


    
    
    ret_t idle_manager_deinit (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
  
#### idle_manager_destroy 函数

* * *

  * 函数功能：



> 析构并释放idle_manager_t管理器。

  * 函数原型：


    
    
    ret_t idle_manager_destroy (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
  
#### idle_manager_dispatch 函数

* * *

  * 函数功能：



> 检查全部idle的函数，如果时间到期，调用相应的idle函数。

  * 函数原型：


    
    
    ret_t idle_manager_dispatch (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
  
#### idle_manager_exist 函数

* * *

  * 函数功能：



> 对应回调函数和上下文的idle是否存在。

  * 函数原型：


    
    
    bool_t idle_manager_exist (idle_manager_t* idle_manager, idle_func_t on_idle, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
on_idle | idle_func_t | idle回调函数。  
ctx | void* | 上下文。  
  
#### idle_manager_find 函数

* * *

  * 函数功能：



> 查找指定ID的idle。

  * 函数原型：


    
    
    const idle_info_t* idle_manager_find (idle_manager_t* idle_manager, uint32_t idle_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const idle_info_t* | 返回idle的信息。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
idle_id | uint32_t | idle_id。  
  
#### idle_manager_get_next_idle_id 函数

* * *

  * 函数功能：



> 获取下一个可用的 idle_id。

  * 函数原型：


    
    
    uint32_t idle_manager_get_next_idle_id (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回idle的ID，TK_INVALID_ID表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
  
#### idle_manager_init 函数

* * *

  * 函数功能：



> 初始化idle_manager_t管理器。

  * 函数原型：


    
    
    idle_manager_t* idle_manager_init (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | idle_manager_t* | 返回idle_manager_t管理器对象。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
  
#### idle_manager_remove 函数

* * *

  * 函数功能：



> 根据idle_id删除idle。

  * 函数原型：


    
    
    ret_t idle_manager_remove (idle_manager_t* idle_manager, uint32_t idle_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
idle_id | uint32_t | idle_id。  
  
#### idle_manager_remove_all 函数

* * *

  * 函数功能：



> 删除全部idle。

  * 函数原型：


    
    
    ret_t idle_manager_remove_all (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
  
#### idle_manager_remove_all_by_ctx 函数

* * *

  * 函数功能：



> 根据上下文删除所有符合条件的idle。

  * 函数原型：


    
    
    ret_t idle_manager_remove_all_by_ctx (idle_manager_t* idle_manager, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
ctx | void* | idle回调函数的上下文。  
  
#### idle_manager_remove_all_by_ctx_and_type 函数

* * *

  * 函数功能：



> 移除对应类型和上下文的所有idle。

  * 函数原型：


    
    
    ret_t idle_manager_remove_all_by_ctx_and_type (idle_manager_t* idle_manager, uint16_t type, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。  
type | uint16_t | 类型。  
ctx | void* | 上下文。  
  
#### idle_manager_set 函数

* * *

  * 函数功能：



> 设置缺省的idle_manager_t管理器。

  * 函数原型：


    
    
    ret_t idle_manager_set (idle_manager_t* idle_manager);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
idle_manager | idle_manager_t* | idle_manager_t管理器对象。
