## darray_t

### 概述

动态数组，根据元素个数动态调整数组的容量。

用darray_init初始化时，用darray_deinit释放。如：
    
    
    darray_t darray;
    darray_init(&darray, 10, destroy, compare);
    ...
    darray_deinit(&darray);
    

用darray_create创建时，用darray_destroy销毁。如：
    
    
    darray_t* darray = darray_create(10, destroy, compare);
    ...
    darray_destroy(darray);
    

* * *

### 函数

函数名称 | 说明  
---|---  
darray_bsearch | 二分查找(确保数组有序)。  
darray_bsearch_index | 二分查找(确保数组有序)。  
darray_bsearch_index_ex | 二分查找(确保数组有序)，元素不存在时，返回low索引。  
darray_clear | 清除全部元素。  
darray_count | 返回满足条件元素的个数。  
darray_create | 创建darray对象。  
darray_deinit | 清除全部元素，并释放elms。  
darray_destroy | 销毁darray对象。  
darray_find | 查找第一个满足条件的元素。  
darray_find_all | 查找全部满足条件的元素。  
darray_find_ex | 查找第一个满足条件的元素。  
darray_find_index | 查找第一个满足条件的元素，并返回位置。  
darray_find_index_ex | 查找第一个满足条件的元素，并返回位置。  
darray_foreach | 遍历元素。  
darray_get | 获取指定序数的元素。  
darray_head | 返回第一个元素。  
darray_init | 初始化darray对象。  
darray_insert | 插入一个元素。  
darray_pop | 弹出最后一个元素。  
darray_push | 在尾巴追加一个元素。  
darray_push_unique | 如果不存在，在尾巴追加一个元素。  
darray_remove | 删除第一个满足条件的元素。  
darray_remove_all | 删除全部满足条件的元素。  
darray_remove_ex | 删除第一个满足条件的元素。  
darray_remove_index | 删除指定位置的元素。  
darray_remove_range | 删除指定范围的元素。  
darray_replace | 设置指定序数的元素(销毁旧的数据)。  
darray_set | 设置指定序数的元素(不销毁旧的数据)。  
darray_sort | 排序。  
darray_sorted_insert | 插入一个元素到有序数组。  
darray_tail | 返回最后一个元素。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
capacity | uint32_t | 数组的容量大小。  
compare | tk_compare_t | 元素比较函数。  
destroy | tk_destroy_t | 元素销毁函数。  
elms | void** | 数组中的元素。  
size | uint32_t | 数组中元素的个数。  
  
#### darray_bsearch 函数

* * *

  * 函数功能：



> 二分查找(确保数组有序)。

  * 函数原型：


    
    
    void* darray_bsearch (darray_t* darray, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 如果找到，返回满足条件的对象，否则返回NULL。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### darray_bsearch_index 函数

* * *

  * 函数功能：



> 二分查找(确保数组有序)。

  * 函数原型：


    
    
    int32_t darray_bsearch_index (darray_t* darray, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果找到，返回满足条件的对象的位置，否则返回-1。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### darray_bsearch_index_ex 函数

* * *

  * 函数功能：



> 二分查找(确保数组有序)，元素不存在时，返回low索引。

  * 函数原型：


    
    
    int32_t darray_bsearch_index_ex (darray_t* darray, tk_compare_t cmp, void* ctx, int32_t* ret_low);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果找到，返回满足条件的对象的位置，否则返回-1。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
ret_low | int32_t* | low索引。  
  
#### darray_clear 函数

* * *

  * 函数功能：



> 清除全部元素。

  * 函数原型：


    
    
    ret_t darray_clear (darray_t* darray);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
  
#### darray_count 函数

* * *

  * 函数功能：



> 返回满足条件元素的个数。

  * 函数原型：


    
    
    int32_t darray_count (darray_t* darray, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回元素个数。  
darray | darray_t* | 单向链表对象。  
ctx | void* | 比较函数的上下文。  
  
#### darray_create 函数

* * *

  * 函数功能：



> 创建darray对象。

  * 函数原型：


    
    
    darray_t* darray_create (uint32_t capacity, tk_destroy_t destroy, tk_compare_t compare);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | darray_t* | 数组对象。  
capacity | uint32_t | 数组的初始容量。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
  
#### darray_deinit 函数

* * *

  * 函数功能：



> 清除全部元素，并释放elms。

  * 函数原型：


    
    
    ret_t darray_deinit (darray_t* darray);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
  
#### darray_destroy 函数

* * *

  * 函数功能：



> 销毁darray对象。

  * 函数原型：


    
    
    ret_t darray_destroy (darray_t* darray);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
  
#### darray_find 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素。

  * 函数原型：


    
    
    void* darray_find (darray_t* darray, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 如果找到，返回满足条件的对象，否则返回NULL。  
darray | darray_t* | 数组对象。  
ctx | void* | 比较函数的上下文。  
  
#### darray_find_all 函数

* * *

  * 函数功能：



> 查找全部满足条件的元素。
    
    
    darray_t matched;
    darray_init(&matched, 0, NULL, NULL);
    darray_find_all(darray, mycmp, myctx, &matched);
    ...
    darray_deinit(&matched);
    

  * 函数原型：


    
    
    ret_t darray_find_all (darray_t* darray, tk_compare_t cmp, void* ctx, darray_t* matched);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
matched | darray_t* | 返回满足条件的元素。  
  
#### darray_find_ex 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素。

  * 函数原型：


    
    
    void* darray_find_ex (darray_t* darray, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 如果找到，返回满足条件的对象，否则返回NULL。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### darray_find_index 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素，并返回位置。

  * 函数原型：


    
    
    int32_t darray_find_index (darray_t* darray, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果找到，返回满足条件的对象的位置，否则返回-1。  
darray | darray_t* | 数组对象。  
ctx | void* | 比较函数的上下文。  
  
#### darray_find_index_ex 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素，并返回位置。

  * 函数原型：


    
    
    int32_t darray_find_index_ex (darray_t* darray, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 如果找到，返回满足条件的对象的位置，否则返回-1。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### darray_foreach 函数

* * *

  * 函数功能：



> 遍历元素。

  * 函数原型：


    
    
    ret_t darray_foreach (darray_t* darray, tk_visit_t visit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
visit | tk_visit_t | 遍历函数。  
ctx | void* | 遍历函数的上下文。  
  
#### darray_get 函数

* * *

  * 函数功能：



> 获取指定序数的元素。

  * 函数原型：


    
    
    void* darray_get (darray_t* darray, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回满足条件的对象，否则返回NULL。  
darray | darray_t* | 数组对象。  
index | uint32_t | 序数。  
  
#### darray_head 函数

* * *

  * 函数功能：



> 返回第一个元素。

  * 函数原型：


    
    
    void* darray_head (darray_t* darray);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
darray | darray_t* | 数组对象。  
  
#### darray_init 函数

* * *

  * 函数功能：



> 初始化darray对象。

  * 函数原型：


    
    
    darray_t* darray_init (darray_t* darray, uint32_t capacity, tk_destroy_t destroy, tk_compare_t compare);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | darray_t* | 数组对象。  
darray | darray_t* | 数组对象。  
capacity | uint32_t | 数组的初始容量。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
  
#### darray_insert 函数

* * *

  * 函数功能：



> 插入一个元素。

  * 函数原型：


    
    
    ret_t darray_insert (darray_t* darray, uint32_t index, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
index | uint32_t | 位置序数。  
data | void* | 待插入的元素。  
  
#### darray_pop 函数

* * *

  * 函数功能：



> 弹出最后一个元素。

  * 函数原型：


    
    
    void* darray_pop (darray_t* darray);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
darray | darray_t* | 数组对象。  
  
#### darray_push 函数

* * *

  * 函数功能：



> 在尾巴追加一个元素。

  * 函数原型：


    
    
    ret_t darray_push (darray_t* darray, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
data | void* | 待追加的元素。  
  
#### darray_push_unique 函数

* * *

  * 函数功能：



> 如果不存在，在尾巴追加一个元素。

  * 函数原型：


    
    
    ret_t darray_push_unique (darray_t* darray, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
data | void* | 待追加的元素。  
  
#### darray_remove 函数

* * *

  * 函数功能：



> 删除第一个满足条件的元素。

  * 函数原型：


    
    
    ret_t darray_remove (darray_t* darray, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
ctx | void* | 比较函数的上下文。  
  
#### darray_remove_all 函数

* * *

  * 函数功能：



> 删除全部满足条件的元素。

  * 函数原型：


    
    
    ret_t darray_remove_all (darray_t* darray, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### darray_remove_ex 函数

* * *

  * 函数功能：



> 删除第一个满足条件的元素。

  * 函数原型：


    
    
    ret_t darray_remove_ex (darray_t* darray, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### darray_remove_index 函数

* * *

  * 函数功能：



> 删除指定位置的元素。

  * 函数原型：


    
    
    ret_t darray_remove_index (darray_t* darray, uint32_t index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
index | uint32_t | 位置序数。  
  
#### darray_remove_range 函数

* * *

  * 函数功能：



> 删除指定范围的元素。 删除范围为[start, end)

  * 函数原型：


    
    
    ret_t darray_remove_range (darray_t* darray, uint32_t start, uint32_t end);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
start | uint32_t | 起始位置。  
end | uint32_t | 结束位置。  
  
#### darray_replace 函数

* * *

  * 函数功能：



> 设置指定序数的元素(销毁旧的数据)。

  * 函数原型：


    
    
    ret_t darray_replace (darray_t* darray, uint32_t index, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
index | uint32_t | 序数。  
data | void* | 数据。  
  
#### darray_set 函数

* * *

  * 函数功能：



> 设置指定序数的元素(不销毁旧的数据)。

  * 函数原型：


    
    
    ret_t darray_set (darray_t* darray, uint32_t index, void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
index | uint32_t | 序数。  
data | void* | 数据。  
  
#### darray_sort 函数

* * *

  * 函数功能：



> 排序。

  * 函数原型：


    
    
    ret_t darray_sort (darray_t* darray, tk_compare_t cmp);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
  
#### darray_sorted_insert 函数

* * *

  * 函数功能：



> 插入一个元素到有序数组。

  * 函数原型：


    
    
    ret_t darray_sorted_insert (darray_t* darray, void* data, tk_compare_t cmp, bool_t replace_if_exist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
darray | darray_t* | 数组对象。  
data | void* | 待插入的元素。  
cmp | tk_compare_t | 元素比较函数。  
replace_if_exist | bool_t | 如果存在是否替换。  
  
#### darray_tail 函数

* * *

  * 函数功能：



> 返回最后一个元素。

  * 函数原型：


    
    
    void* darray_tail (darray_t* darray);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 成功返回最后一个元素，失败返回NULL。  
darray | darray_t* | 数组对象。  
  
#### capacity 属性

* * *

> 数组的容量大小。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
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
  
#### elms 属性

* * *

> 数组中的元素。

  * 类型：void**

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
  
#### size 属性

* * *

> 数组中元素的个数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
