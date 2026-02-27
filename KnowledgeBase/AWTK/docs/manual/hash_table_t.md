## hash_table_t

### 概述

哈希表。

用hash_table_init初始化时，用hash_table_deinit释放。如：
    
    
    hash_table_t hash_table;
    hash_table_init(&hash_table, 10, destroy, compare, hash);
    ...
    hash_table_deinit(&hash_table);
    

用hash_table_create创建时，用hash_table_destroy销毁。如：
    
    
    hash_table_t* hash_table = hash_table_create(10, destroy, compare, hash);
    ...
    hash_table_destroy(hash_table);
    

示例
    
    
    typedef struct _motor_t
    {
    int id;
    int position;
    int velocity;
    int acceleration;
    } motor_t;
    
    motor_t *motor_create(int id)
    {
    motor_t *motor = new motor_t;
    motor->id = id;
    motor->position = 0;
    motor->velocity = 0;
    motor->acceleration = 0;
    return motor;
    }
    
    ret_t motor_destroy(motor_t *motor)
    {
    delete motor;
    return RET_OK;
    }
    
    int motor_compare(const void *a, const void *b)
    {
    motor_t *motor_a = (motor_t *)a;
    motor_t *motor_b = (motor_t *)b;
    
    return motor_a->id - motor_b->id;
    }
    
    ret_t visist_motor(void *ctx, const void *data)
    {
    motor_t *motor = (motor_t *)data;
    log_debug("motor id: %d\n", motor->id);
    return RET_OK;
    }
    
    uint32_t motor_hash(const void *data)
    {
    motor_t *motor = (motor_t *)data;
    return motor->id;
    }
    
    void demo(void)
    {
    hash_table_t motors;
    motor_t *motor = NULL;
    
    // 初始化哈希表
    hash_table_init(&motors, 10, (tk_destroy_t)motor_destroy, (tk_compare_t)motor_compare, motor_hash);
    
    motor = motor_create(1);
    // 将motor添加到哈希表
    hash_table_add(&motors, motor, TRUE);
    ENSURE(hash_table_find(&motors, NULL, motor) == motor);
    
    motor = motor_create(2);
    // 将motor添加到哈希表
    hash_table_add(&motors, motor, TRUE);
    ENSURE(hash_table_find(&motors, NULL, motor) == motor);
    
    // 遍历哈希表
    log_debug("motors size: %d\n", hash_table_size(&motors));
    hash_table_foreach(&motors, visist_motor, NULL);
    
    // 释放哈希表
    hash_table_deinit(&motors);
    }
    

* * *

### 函数

函数名称 | 说明  
---|---  
hash_table_add | 加入一个元素。  
hash_table_clear | 清除全部元素。  
hash_table_count | 返回满足条件元素的个数。  
hash_table_create | 创建hash_table对象。  
hash_table_deinit | 清除全部元素，并释放elms。  
hash_table_destroy | 销毁hash_table对象。  
hash_table_find | 查找第一个满足条件的元素。  
hash_table_foreach | 遍历元素。  
hash_table_hash_int | 计算int的hash值。  
hash_table_hash_str | 计算字符串hash值。  
hash_table_init | 初始化hash_table对象。  
hash_table_remove | 删除第一个满足条件的元素。  
hash_table_remove_all | 删除全部满足条件的元素。  
hash_table_size | 返回全部元素个数。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
buckets | darray_t | buckets。  
compare | tk_compare_t | 元素比较函数。  
destroy | tk_destroy_t | 元素销毁函数。  
hash | tk_hash_t | 元素哈希函数。  
  
#### hash_table_add 函数

* * *

  * 函数功能：



> 加入一个元素。

  * 函数原型：


    
    
    ret_t hash_table_add (hash_table_t* hash_table, void* data, bool_t replace_if_exist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash_table | hash_table_t* | 哈希表对象。  
data | void* | 数据。  
replace_if_exist | bool_t | 如果存在是否替换。  
  
#### hash_table_clear 函数

* * *

  * 函数功能：



> 清除全部元素。

  * 函数原型：


    
    
    ret_t hash_table_clear (hash_table_t* hash_table);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash_table | hash_table_t* | 哈希表对象。  
  
#### hash_table_count 函数

* * *

  * 函数功能：



> 返回满足条件元素的个数。

  * 函数原型：


    
    
    int32_t hash_table_count (hash_table_t* hash_table, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回元素个数。  
hash_table | hash_table_t* | 哈希表对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### hash_table_create 函数

* * *

  * 函数功能：



> 创建hash_table对象。

  * 函数原型：


    
    
    hash_table_t* hash_table_create (uint32_t capacity, tk_destroy_t destroy, tk_compare_t compare, tk_hash_t hash);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | hash_table_t* | 哈希表对象。  
capacity | uint32_t | 哈希表桶数。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
hash | tk_hash_t | 元素哈希函数。  
  
#### hash_table_deinit 函数

* * *

  * 函数功能：



> 清除全部元素，并释放elms。

  * 函数原型：


    
    
    ret_t hash_table_deinit (hash_table_t* hash_table);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash_table | hash_table_t* | 哈希表对象。  
  
#### hash_table_destroy 函数

* * *

  * 函数功能：



> 销毁hash_table对象。

  * 函数原型：


    
    
    ret_t hash_table_destroy (hash_table_t* hash_table);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash_table | hash_table_t* | 哈希表对象。  
  
#### hash_table_find 函数

* * *

  * 函数功能：



> 查找第一个满足条件的元素。

  * 函数原型：


    
    
    void* hash_table_find (hash_table_t* hash_table, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 如果找到，返回满足条件的对象，否则返回NULL。  
hash_table | hash_table_t* | 哈希表对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### hash_table_foreach 函数

* * *

  * 函数功能：



> 遍历元素。

  * 函数原型：


    
    
    ret_t hash_table_foreach (hash_table_t* hash_table, tk_visit_t visit, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash_table | hash_table_t* | 哈希表对象。  
visit | tk_visit_t | 遍历函数。  
ctx | void* | 遍历函数的上下文。  
  
#### hash_table_hash_int 函数

* * *

  * 函数功能：



> 计算int的hash值。

  * 函数原型：


    
    
    uint32_t hash_table_hash_int (const void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回hash值。  
data | const void* | 数据。  
  
#### hash_table_hash_str 函数

* * *

  * 函数功能：



> 计算字符串hash值。

  * 函数原型：


    
    
    uint32_t hash_table_hash_str (const void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回hash值。  
data | const void* | 数据。  
  
#### hash_table_init 函数

* * *

  * 函数功能：



> 初始化hash_table对象。

  * 函数原型：


    
    
    hash_table_t* hash_table_init (hash_table_t* hash_table, uint32_t capacity, tk_destroy_t destroy, tk_compare_t compare, tk_hash_t hash);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | hash_table_t* | 哈希表对象。  
hash_table | hash_table_t* | 哈希表对象。  
capacity | uint32_t | 哈希表桶数。  
destroy | tk_destroy_t | 元素销毁函数。  
compare | tk_compare_t | 元素比较函数。  
hash | tk_hash_t | 元素哈希函数。  
  
#### hash_table_remove 函数

* * *

  * 函数功能：



> 删除第一个满足条件的元素。

  * 函数原型：


    
    
    ret_t hash_table_remove (hash_table_t* hash_table, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash_table | hash_table_t* | 哈希表对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### hash_table_remove_all 函数

* * *

  * 函数功能：



> 删除全部满足条件的元素。

  * 函数原型：


    
    
    ret_t hash_table_remove_all (hash_table_t* hash_table, tk_compare_t cmp, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
hash_table | hash_table_t* | 哈希表对象。  
cmp | tk_compare_t | 比较函数，为NULL则使用内置的比较函数。  
ctx | void* | 比较函数的上下文。  
  
#### hash_table_size 函数

* * *

  * 函数功能：



> 返回全部元素个数。

  * 函数原型：


    
    
    int32_t hash_table_size (hash_table_t* hash_table);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回元素个数。  
hash_table | hash_table_t* | 哈希表对象。  
  
#### buckets 属性

* * *

> buckets。

  * 类型：darray_t

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
  
#### hash 属性

* * *

> 元素哈希函数。

  * 类型：tk_hash_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
