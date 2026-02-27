## slist_t

### 概述

单向链表

用slist_init初始化时，用slist_deinit释放。如：
    
    
    slist_t slist;
    slist_init(&slist, destroy, compare);
    ...
    slist_deinit(&slist);
    

用slist_create创建时，用slist_destroy销毁。如：
    
    
    slist_t* slist = slist_create(destroy, compare);
    ...
    slist_destroy(slist);
    

* * *

### 函数

函数名称 | 说明  
---|---  
slist_append | 在尾巴追加一个元素。  
slist_count | 返回满足条件元素的个数。  
slist_create | 创建slist对象  
slist_deinit | 清除单向链表中的元素。  
slist_destroy | 清除单向链表中的元素，并释放单向链表对象。  
slist_find | 查找第一个满足条件的元素。  
slist_find_ex | 查找第一个满足条件的元素。  
slist_foreach | 遍历元素。  
slist_head | 返回第一个元素。  
slist_head_pop | 弹出第一个元素。  
slist_init | 初始化slist对象  
slist_insert | 插入一个元素。  
slist_is_empty | 列表是否为空。  
slist_prepend | 在头部追加一个元素。  
slist_remove | 删除第一个满足条件的元素。  
slist_remove_all | 删除全部元素。  
slist_remove_ex | 删除满足条件的元素。  
slist_reverse | 反转链表。  
slist_size | 返回元素个数。  
slist_tail | 返回最后一个元素。  
slist_tail_pop | 弹出最后一个元素。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
compare | tk_compare_t | 元素比较函数。  
destroy | tk_destroy_t | 元素销毁函数。  
first | slist_node_t* | 首节点。  
last | slist_node_t* | 尾节点。  
size | int32_t | 元素个数。  
  
#### slist_append 函数

* * *

  * 函数功能：



> 在尾巴追加一个元素。

  * 函数原型：


    
    
    ret_t slist_append (slist_t* slist, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
data | void* | 待追加的元素。  
  
#### slist_count 函数

* * *

  * 函数功能：



> 返回满足条件元素的个数。

  * 函数原型：


    
    
    int32_t slist_count (slist_t* slist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回元素个数。  
slist | slist_t* | 单向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### slist_create 函数

* * *

  * 函数功能：



> 创建slist对象

  * 函数原型：


    
    
    slist_t* slist_create (tk_destroy_t destroy, tk_compare_t compare);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | slist_t* | 单向链表对象。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
  
#### slist_deinit 函数

* * *

  * 函数功能：



> 清除单向链表中的元素。

  * 函数原型：


    
    
    ret_t slist_deinit (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
  
#### slist_destroy 函数

* * *

  * 函数功能：



> 清除单向链表中的元素，并释放单向链表对象。

  * 函数原型：


    
    
    ret_t slist_destroy (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
  
#### slist_find 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素。

  * 函数原型：


    
    
    void* slist_find (slist_t* slist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 如果找到，返回满足条件的对象，否则返回NULL。  
slist | slist_t* | 单向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### slist_find_ex 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素。

  * 函数原型：


    
    
    void* slist_find_ex (slist_t* slist, tk_compare_t compare, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回节点。  
slist | slist_t* | 单向链表对象。  
compare | tk_compare_t | 元素比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### slist_foreach 函数

* * *

  * 函数功能：



> 遍历元素。

  * 函数原型：


    
    
    ret_t slist_foreach (slist_t* slist, tk_visit_t visit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
visit | tk_visit_t | 遍历函数。  
ctx | void* | 遍历函数的上下文。  
  
#### slist_head 函数

* * *

  * 函数功能：



> 返回第一个元素。

  * 函数原型：


    
    
    void* slist_head (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
slist | slist_t* | 单向链表对象。  
  
#### slist_head_pop 函数

* * *

  * 函数功能：



> 弹出第一个元素。

  * 函数原型：


    
    
    void* slist_head_pop (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
slist | slist_t* | 单向链表对象。  
  
#### slist_init 函数

* * *

  * 函数功能：



> 初始化slist对象

  * 函数原型：


    
    
    slist_t* slist_init (slist_t* slist, tk_destroy_t destroy, tk_compare_t compare);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | slist_t* | 单向链表对象。  
slist | slist_t* | 单向链表对象。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
  
#### slist_insert 函数

* * *

  * 函数功能：



> 插入一个元素。

  * 函数原型：


    
    
    ret_t slist_insert (slist_t* slist, uint32_t index, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
index | uint32_t | 位置序数。  
data | void* | 待追加的元素。  
  
#### slist_is_empty 函数

* * *

  * 函数功能：



> 列表是否为空。

  * 函数原型：


    
    
    bool_t slist_is_empty (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回 TRUE 表示空列表，返回 FALSE 表示列表有数据。  
slist | slist_t* | 单向链表对象。  
  
#### slist_prepend 函数

* * *

  * 函数功能：



> 在头部追加一个元素。

  * 函数原型：


    
    
    ret_t slist_prepend (slist_t* slist, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
data | void* | 待追加的元素。  
  
#### slist_remove 函数

* * *

  * 函数功能：



> 删除第一个满足条件的元素。

  * 函数原型：


    
    
    ret_t slist_remove (slist_t* slist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### slist_remove_all 函数

* * *

  * 函数功能：



> 删除全部元素。

  * 函数原型：


    
    
    ret_t slist_remove_all (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
  
#### slist_remove_ex 函数

* * *

  * 函数功能：



> 删除满足条件的元素。 备注： 如果队列中符合条件的元素不足 remove_size，移除最后一个符合条件的元素后返回 RET_OK。 如果队列中符合条件的元素大于 remove_size，在队列中移除 remove_size 个元素后返回 RET_OK。 remove_size 为负数则会移除所有符合条件的元素。

  * 函数原型：


    
    
    ret_t slist_remove_ex (slist_t* slist, tk_compare_t compare, void* ctx, int32_t remove_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
compare | tk_compare_t | 元素比较函数。  
ctx | void* | 比较函数的上下文。  
remove_size | int32_t | 删除个数。  
  
#### slist_reverse 函数

* * *

  * 函数功能：



> 反转链表。

  * 函数原型：


    
    
    ret_t slist_reverse (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
slist | slist_t* | 单向链表对象。  
  
#### slist_size 函数

* * *

  * 函数功能：



> 返回元素个数。

  * 函数原型：


    
    
    int32_t slist_size (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回元素个数。  
slist | slist_t* | 单向链表对象。  
  
#### slist_tail 函数

* * *

  * 函数功能：



> 返回最后一个元素。

  * 函数原型：


    
    
    void* slist_tail (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
slist | slist_t* | 单向链表对象。  
  
#### slist_tail_pop 函数

* * *

  * 函数功能：



> 弹出最后一个元素。

  * 函数原型：


    
    
    void* slist_tail_pop (slist_t* slist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
slist | slist_t* | 单向链表对象。  
  
#### compare 属性

* * *

> 元素比较函数。

  * 类型：tk_compare_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### destroy 属性

* * *

> 元素销毁函数。

  * 类型：tk_destroy_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### first 属性

* * *

> 首节点。

  * 类型：slist_node_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### last 属性

* * *

> 尾节点。

  * 类型：slist_node_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 元素个数。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
