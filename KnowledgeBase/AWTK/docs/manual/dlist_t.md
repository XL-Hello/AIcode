## dlist_t

### 概述

双向链表

用dlist_init初始化时，用dlist_deinit释放。如：
    
    
    dlist_t dlist;
    dlist_init(&dlist, destroy, compare);
    ...
    dlist_deinit(&dlist);
    

用dlist_create创建时，用dlist_destroy销毁。如：
    
    
    dlist_t* dlist = dlist_create(destroy, compare);
    ...
    dlist_destroy(dlist);
    

* * *

### 函数

函数名称 | 说明  
---|---  
dlist_append | 在尾巴追加一个元素。  
dlist_count | 返回满足条件元素的个数。  
dlist_create | 创建dlist对象  
dlist_deinit | 清除双向链表中的元素。  
dlist_destroy | 清除双向链表中的元素，并释放双向链表对象。  
dlist_find | 查找第一个满足条件的元素。  
dlist_find_ex | 查找第一个满足条件的元素。  
dlist_find_last | 查找最后一个满足条件的元素。  
dlist_foreach | 遍历元素。  
dlist_foreach_reverse | 反向遍历元素。  
dlist_head | 返回第一个元素。  
dlist_head_pop | 弹出第一个元素。  
dlist_init | 初始化dlist对象  
dlist_insert | 插入一个元素。  
dlist_is_empty | 列表是否为空。  
dlist_prepend | 在头部追加一个元素。  
dlist_remove | 删除第一个满足条件的元素。  
dlist_remove_all | 删除全部元素。  
dlist_remove_ex | 删除满足条件的元素。  
dlist_remove_last | 删除最后一个满足条件的元素。  
dlist_reverse | 反转链表。  
dlist_size | 返回元素个数。  
dlist_tail | 返回最后一个元素。  
dlist_tail_pop | 弹出最后一个元素。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
compare | tk_compare_t | 元素比较函数。  
destroy | tk_destroy_t | 元素销毁函数。  
first | dlist_node_t* | 首节点。  
last | dlist_node_t* | 尾节点。  
size | int32_t | 元素个数。  
  
#### dlist_append 函数

* * *

  * 函数功能：



> 在尾巴追加一个元素。

  * 函数原型：


    
    
    ret_t dlist_append (dlist_t* dlist, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
data | void* | 待追加的元素。  
  
#### dlist_count 函数

* * *

  * 函数功能：



> 返回满足条件元素的个数。

  * 函数原型：


    
    
    int32_t dlist_count (dlist_t* dlist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回元素个数。  
dlist | dlist_t* | 双向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### dlist_create 函数

* * *

  * 函数功能：



> 创建dlist对象

  * 函数原型：


    
    
    dlist_t* dlist_create (tk_destroy_t destroy, tk_compare_t compare);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | dlist_t* | 双向链表对象。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
  
#### dlist_deinit 函数

* * *

  * 函数功能：



> 清除双向链表中的元素。

  * 函数原型：


    
    
    ret_t dlist_deinit (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_destroy 函数

* * *

  * 函数功能：



> 清除双向链表中的元素，并释放双向链表对象。

  * 函数原型：


    
    
    ret_t dlist_destroy (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_find 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素。

  * 函数原型：


    
    
    void* dlist_find (dlist_t* dlist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 如果找到，返回满足条件的对象，否则返回NULL。  
dlist | dlist_t* | 双向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### dlist_find_ex 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素。

  * 函数原型：


    
    
    void* dlist_find_ex (dlist_t* dlist, tk_compare_t compare, void* ctx, bool_t reverse);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回节点。  
dlist | dlist_t* | 双向链表对象。  
compare | tk_compare_t | 元素比较函数。  
ctx | void* | 比较函数的上下文。  
reverse | bool_t | 逆序查找。  
  
#### dlist_find_last 函数

* * *

  * 函数功能：



> 查找最后一个满足条件的元素。

  * 函数原型：


    
    
    void* dlist_find_last (dlist_t* dlist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 如果找到，返回满足条件的对象，否则返回NULL。  
dlist | dlist_t* | 双向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### dlist_foreach 函数

* * *

  * 函数功能：



> 遍历元素。

  * 函数原型：


    
    
    ret_t dlist_foreach (dlist_t* dlist, tk_visit_t visit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
visit | tk_visit_t | 遍历函数。  
ctx | void* | 遍历函数的上下文。  
  
#### dlist_foreach_reverse 函数

* * *

  * 函数功能：



> 反向遍历元素。

  * 函数原型：


    
    
    ret_t dlist_foreach_reverse (dlist_t* dlist, tk_visit_t visit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
visit | tk_visit_t | 遍历函数。  
ctx | void* | 遍历函数的上下文。  
  
#### dlist_head 函数

* * *

  * 函数功能：



> 返回第一个元素。

  * 函数原型：


    
    
    void* dlist_head (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_head_pop 函数

* * *

  * 函数功能：



> 弹出第一个元素。

  * 函数原型：


    
    
    void* dlist_head_pop (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_init 函数

* * *

  * 函数功能：



> 初始化dlist对象

  * 函数原型：


    
    
    dlist_t* dlist_init (dlist_t* dlist, tk_destroy_t destroy, tk_compare_t compare);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | dlist_t* | 双向链表对象。  
dlist | dlist_t* | 双向链表对象。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
  
#### dlist_insert 函数

* * *

  * 函数功能：



> 插入一个元素。

  * 函数原型：


    
    
    ret_t dlist_insert (dlist_t* dlist, uint32_t index, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
index | uint32_t | 位置序数。  
data | void* | 待追加的元素。  
  
#### dlist_is_empty 函数

* * *

  * 函数功能：



> 列表是否为空。

  * 函数原型：


    
    
    bool_t dlist_is_empty (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回 TRUE 表示空列表，返回 FALSE 表示列表有数据。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_prepend 函数

* * *

  * 函数功能：



> 在头部追加一个元素。

  * 函数原型：


    
    
    ret_t dlist_prepend (dlist_t* dlist, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
data | void* | 待追加的元素。  
  
#### dlist_remove 函数

* * *

  * 函数功能：



> 删除第一个满足条件的元素。

  * 函数原型：


    
    
    ret_t dlist_remove (dlist_t* dlist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### dlist_remove_all 函数

* * *

  * 函数功能：



> 删除全部元素。

  * 函数原型：


    
    
    ret_t dlist_remove_all (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_remove_ex 函数

* * *

  * 函数功能：



> 删除满足条件的元素。 备注： 如果队列中符合条件的元素不足 remove_size，移除最后一个符合条件的元素后返回 RET_OK。 如果队列中符合条件的元素大于 remove_size，在队列中移除 remove_size 个元素后返回 RET_OK。 remove_size 为负数则会移除所有符合条件的元素。

  * 函数原型：


    
    
    ret_t dlist_remove_ex (dlist_t* dlist, tk_compare_t compare, void* ctx, int32_t remove_size, bool_t reverse);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
compare | tk_compare_t | 元素比较函数。  
ctx | void* | 比较函数的上下文。  
remove_size | int32_t | 删除个数。  
reverse | bool_t | 逆序删除。  
  
#### dlist_remove_last 函数

* * *

  * 函数功能：



> 删除最后一个满足条件的元素。

  * 函数原型：


    
    
    ret_t dlist_remove_last (dlist_t* dlist, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### dlist_reverse 函数

* * *

  * 函数功能：



> 反转链表。

  * 函数原型：


    
    
    ret_t dlist_reverse (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_size 函数

* * *

  * 函数功能：



> 返回元素个数。

  * 函数原型：


    
    
    int32_t dlist_size (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回元素个数。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_tail 函数

* * *

  * 函数功能：



> 返回最后一个元素。

  * 函数原型：


    
    
    void* dlist_tail (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
dlist | dlist_t* | 双向链表对象。  
  
#### dlist_tail_pop 函数

* * *

  * 函数功能：



> 弹出最后一个元素。

  * 函数原型：


    
    
    void* dlist_tail_pop (dlist_t* dlist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
dlist | dlist_t* | 双向链表对象。  
  
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

  * 类型：dlist_node_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### last 属性

* * *

> 尾节点。

  * 类型：dlist_node_t*

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
