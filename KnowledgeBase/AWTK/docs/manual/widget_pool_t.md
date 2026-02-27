## widget_pool_t

### 概述

有时需要频繁创建和销毁控件，widget pool把销毁的控件缓存起来，再次使用时直接拿回来用。

  * 优点：速度快，内存碎片少。
  * 缺点：占用一点内存空间。



通过宏WITH_WIDGET_POOL来指定最大缓存控件的数量。

控件可以通过vt->enable_pool参数决定该类控件是否启用缓存。

* * *

### 函数

函数名称 | 说明  
---|---  
widget_pool | 获取缺省widget pool对象。  
widget_pool_clear_cache | 清除全部缓存控件。  
widget_pool_count | 计算缓存控件个数。  
widget_pool_create | 创建widget pool对象。  
widget_pool_create_widget | 创建widget对象。  
widget_pool_destroy | 清除全部缓存控件并销毁widget pool对象。  
widget_pool_destroy_widget | 销毁或回收widget对象。  
widget_pool_set | 设置缺省widget pool对象。  
  
#### widget_pool 函数

* * *

  * 函数功能：



> 获取缺省widget pool对象。

  * 函数原型：


    
    
    widget_pool_t* widget_pool ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_pool_t* | 返回widget pool对象。  
  
#### widget_pool_clear_cache 函数

* * *

  * 函数功能：



> 清除全部缓存控件。

  * 函数原型：


    
    
    ret_t widget_pool_clear_cache (widget_pool_t* pool);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
pool | widget_pool_t* | widget pool对象。  
  
#### widget_pool_count 函数

* * *

  * 函数功能：



> 计算缓存控件个数。

  * 函数原型：


    
    
    int32_t widget_pool_count (widget_pool_t* pool);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回缓存控件个数。  
pool | widget_pool_t* | widget pool对象。  
  
#### widget_pool_create 函数

* * *

  * 函数功能：



> 创建widget pool对象。

  * 函数原型：


    
    
    widget_pool_t* widget_pool_create (uint32_t max_cache_nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_pool_t* | 返回widget pool对象。  
max_cache_nr | uint32_t | 最大缓存对象个数。  
  
#### widget_pool_create_widget 函数

* * *

  * 函数功能：



> 创建widget对象。

  * 函数原型：


    
    
    widget_t widget_pool_create_widget (widget_pool_t* pool, const widget_vtable_t* vt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t | 返回控件对象。  
pool | widget_pool_t* | widget pool对象。  
vt | const widget_vtable_t* | 控件虚表。  
  
#### widget_pool_destroy 函数

* * *

  * 函数功能：



> 清除全部缓存控件并销毁widget pool对象。

  * 函数原型：


    
    
    ret_t widget_pool_destroy (widget_pool_t* pool);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
pool | widget_pool_t* | widget pool对象。  
  
#### widget_pool_destroy_widget 函数

* * *

  * 函数功能：



> 销毁或回收widget对象。

  * 函数原型：


    
    
    ret_t widget_pool_destroy_widget (widget_pool_t* pool, widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
pool | widget_pool_t* | widget pool对象。  
widget | widget_t* | 控件对象。  
  
#### widget_pool_set 函数

* * *

  * 函数功能：



> 设置缺省widget pool对象。

  * 函数原型：


    
    
    ret_t widget_pool_set (widget_pool_t* pool);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
pool | widget_pool_t* | widget pool对象。
