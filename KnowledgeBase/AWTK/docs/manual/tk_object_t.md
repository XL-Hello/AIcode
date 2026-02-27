## tk_object_t

### 概述

![image](images/tk_object_t_0.png)

## 对象接口。

### 函数

函数名称 | 说明  
---|---  
tk_object_can_exec | 检查是否可以执行指定的命令。  
tk_object_can_exec_by_path | 检查是否可以执行指定的命令。  
tk_object_clear_props | 清除全部属性。  
tk_object_clone | clone对象。  
tk_object_compare | 比较两个对象。  
tk_object_compare_name_without_nullptr | 根据名称比较两个对象，如果两个对象的名称都为NULL，则比较两个对象的地址。  
tk_object_copy_prop | 拷贝指定的属性。  
tk_object_copy_props | 拷贝全部的属性。  
tk_object_create | 创建对象。  
tk_object_create_ex | 创建对象。  
tk_object_eval | 计算一个表达式，表达式中引用的变量从prop中获取。  
tk_object_exec | 执行指定的命令。  
tk_object_exec_by_path | 执行指定的命令。  
tk_object_find_prop | 查找满足条件的属性，并返回它的值。  
tk_object_find_props | 查找全部满足条件的属性。  
tk_object_foreach_prop | 遍历所有属性。  
tk_object_get_child_object | 获取下一级子对象。  
tk_object_get_desc | 获取对象的描述信息。  
tk_object_get_prop | 获取指定属性的值。  
tk_object_get_prop_bool | 获取指定属性的bool类型的值。  
tk_object_get_prop_bool_by_path | 获取指定属性的bool类型的值。  
tk_object_get_prop_by_path | 获取指定path属性的值。  
tk_object_get_prop_double | 获取指定属性的浮点数类型的值。  
tk_object_get_prop_float | 获取指定属性的浮点数类型的值。  
tk_object_get_prop_float_by_path | 获取指定属性的浮点数类型的值。  
tk_object_get_prop_int | 获取指定属性的整数类型的值。  
tk_object_get_prop_int_by_path | 获取指定属性的整数类型的值。  
tk_object_get_prop_int16 | 获取指定属性的int16类型的值。  
tk_object_get_prop_int32 | 获取指定属性的int32类型的值。  
tk_object_get_prop_int64 | 获取指定属性的int64类型的值。  
tk_object_get_prop_int8 | 获取指定属性的int8类型的值。  
tk_object_get_prop_object | 获取指定属性的object类型的值。  
tk_object_get_prop_object_by_path | 获取指定属性的object类型的值。  
tk_object_get_prop_pointer | 获取指定属性的指针类型的值。  
tk_object_get_prop_pointer_by_path | 获取指定属性的指针类型的值。  
tk_object_get_prop_str | 获取指定属性的字符串类型的值。  
tk_object_get_prop_str_by_path | 获取指定属性的字符串类型的值。  
tk_object_get_prop_uint16 | 获取指定属性的uint16类型的值。  
tk_object_get_prop_uint32 | 获取指定属性的uint32类型的值。  
tk_object_get_prop_uint64 | 获取指定属性的uint64类型的值。  
tk_object_get_prop_uint8 | 获取指定属性的uint8类型的值。  
tk_object_get_size | 获取对象占用内存的大小。  
tk_object_get_type | 获取对象的类型名称。  
tk_object_has_prop | 检查是否存在指定的属性。  
tk_object_has_prop_by_path | 检查是否存在指定的属性。  
tk_object_is_collection | 判断对象是否是集合。  
tk_object_is_instance_of | 检查对象是否是指定类型的实例。  
tk_object_notify_changed | 触发EVT_PROPS_CHANGED事件。  
tk_object_ref | 引用计数加1。  
tk_object_remove_prop | 删除指定属性。  
tk_object_set_name | 设置对象的名称。  
tk_object_set_prop | 设置指定属性的值。  
tk_object_set_prop_bool | 设置指定属性的bool类型的值。  
tk_object_set_prop_bool_by_path | 设置指定属性的bool类型的值。  
tk_object_set_prop_by_path | 设置指定属性的值。  
tk_object_set_prop_double | 设置指定属性的浮点数类型的值。  
tk_object_set_prop_float | 设置指定属性的浮点数类型的值。  
tk_object_set_prop_float_by_path | 设置指定属性的浮点数类型的值。  
tk_object_set_prop_int | 设置指定属性的整数类型的值。  
tk_object_set_prop_int_by_path | 设置指定属性的整数类型的值。  
tk_object_set_prop_int16 | 设置指定属性的int16类型的值。  
tk_object_set_prop_int32 | 设置指定属性的int32类型的值。  
tk_object_set_prop_int64 | 设置指定属性的int64类型的值。  
tk_object_set_prop_int8 | 设置指定属性的int8类型的值。  
tk_object_set_prop_object | 设置指定属性的object类型的值。  
tk_object_set_prop_object_by_path | 设置指定属性的object类型的值。  
tk_object_set_prop_pointer | 设置指定属性的指针类型的值。  
tk_object_set_prop_pointer_by_path | 设置指定属性的指针类型的值。  
tk_object_set_prop_pointer_ex | 设置指定属性的指针类型的值。  
tk_object_set_prop_str | 设置指定属性的字符串类型的值。  
tk_object_set_prop_str_by_path | 设置指定属性的字符串类型的值。  
tk_object_set_prop_str_with_format | 设置指定属性的字符串类型的值。  
tk_object_set_prop_uint16 | 设置指定属性的uint16类型的值。  
tk_object_set_prop_uint32 | 设置指定属性的uint32类型的值。  
tk_object_set_prop_uint64 | 设置指定属性的uint64类型的值。  
tk_object_set_prop_uint8 | 设置指定属性的uint8类型的值。  
tk_object_to_json | 转换成JSON字符串。  
tk_object_unref | 引用计数减1。引用计数为0时，销毁对象。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
name | char* | 对象的名称。  
ref_count | int32_t | 引用计数。  
  
#### tk_object_can_exec 函数

* * *

  * 函数功能：



> 检查是否可以执行指定的命令。

  * 函数原型：


    
    
    bool_t tk_object_can_exec (tk_object_t* obj, const char* name, const char* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示可以执行，否则表示不可以执行。  
obj | tk_object_t* | object对象。  
name | const char* | 命令的名称。  
args | const char* | 命令的参数。  
  
#### tk_object_can_exec_by_path 函数

* * *

  * 函数功能：



> 检查是否可以执行指定的命令。

  * 函数原型：


    
    
    bool_t tk_object_can_exec_by_path (tk_object_t* obj, const char* path, const char* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示可以执行，否则表示不可以执行。  
obj | tk_object_t* | object对象。  
path | const char* | 命令的path。  
args | const char* | 命令的参数。  
  
#### tk_object_clear_props 函数

* * *

  * 函数功能：



> 清除全部属性。

  * 函数原型：


    
    
    ret_t tk_object_clear_props (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
  
#### tk_object_clone 函数

* * *

  * 函数功能：



> clone对象。

  * 函数原型：


    
    
    tk_object_t* tk_object_clone (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
obj | tk_object_t* | object对象。  
  
#### tk_object_compare 函数

* * *

  * 函数功能：



> 比较两个对象。

  * 函数原型：


    
    
    int32_t tk_object_compare (tk_object_t* obj, tk_object_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回比较结果。  
obj | tk_object_t* | object对象。  
other | tk_object_t* | 比较的object对象。  
  
#### tk_object_compare_name_without_nullptr 函数

* * *

  * 函数功能：



> 根据名称比较两个对象，如果两个对象的名称都为NULL，则比较两个对象的地址。

  * 函数原型：


    
    
    int32_t tk_object_compare_name_without_nullptr (tk_object_t* obj, tk_object_t* other);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回比较结果。  
obj | tk_object_t* | object对象。  
other | tk_object_t* | 比较的object对象。  
  
#### tk_object_copy_prop 函数

* * *

  * 函数功能：



> 拷贝指定的属性。

  * 函数原型：


    
    
    ret_t tk_object_copy_prop (tk_object_t* obj, tk_object_t* src, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 目标对象。  
src | tk_object_t* | 源对象。  
name | const char* | 属性的名称。  
  
#### tk_object_copy_props 函数

* * *

  * 函数功能：



> 拷贝全部的属性。

  * 函数原型：


    
    
    ret_t tk_object_copy_props (tk_object_t* obj, tk_object_t* src, bool_t overwrite);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 目标对象。  
src | tk_object_t* | 源对象。  
overwrite | bool_t | 如果属性存在是否覆盖。  
  
#### tk_object_create 函数

* * *

  * 函数功能：



> 创建对象。
> 
> 仅供子类调用。

  * 函数原型：


    
    
    tk_object_t* tk_object_create (const object_vtable_t* vt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
vt | const object_vtable_t* | 虚函数表。  
  
#### tk_object_create_ex 函数

* * *

  * 函数功能：



> 创建对象。
> 
> 仅供子类调用。

  * 函数原型：


    
    
    tk_object_t* tk_object_create_ex (const object_vtable_t* vt, uint32_t extra_data_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
vt | const object_vtable_t* | 虚函数表。  
extra_data_size | uint32_t | 额外的内存大小。  
  
#### tk_object_eval 函数

* * *

  * 函数功能：



> 计算一个表达式，表达式中引用的变量从prop中获取。

  * 函数原型：


    
    
    ret_t tk_object_eval (tk_object_t* obj, const char* expr, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
expr | const char* | 表达式。  
v | value_t* | 返回计算结果。  
  
#### tk_object_exec 函数

* * *

  * 函数功能：



> 执行指定的命令。

  * 函数原型：


    
    
    ret_t tk_object_exec (tk_object_t* obj, const char* name, const char* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 命令的名称。  
args | const char* | 命令的参数。  
  
#### tk_object_exec_by_path 函数

* * *

  * 函数功能：



> 执行指定的命令。

  * 函数原型：


    
    
    ret_t tk_object_exec_by_path (tk_object_t* obj, const char* path, const char* args);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 命令的path。  
args | const char* | 命令的参数。  
  
#### tk_object_find_prop 函数

* * *

  * 函数功能：



> 查找满足条件的属性，并返回它的值。

  * 函数原型：


    
    
    value_t* tk_object_find_prop (tk_object_t* obj, tk_compare_t cmp, const void* data);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | value_t* | 返回属性的值。  
obj | tk_object_t* | 对象。  
cmp | tk_compare_t | 比较函数。  
data | const void* | 要比较的数据。  
  
#### tk_object_find_props 函数

* * *

  * 函数功能：



> 查找全部满足条件的属性。
    
    
    darray_t matched;
    darray_init(&matched, 0, NULL, NULL);
    tk_object_find_props(obj, my_cmp, my_data, &matched);
    ...
    darray_deinit(&matched);
    

  * 函数原型：


    
    
    ret_t tk_object_find_props (tk_object_t* obj, tk_compare_t cmp, const void* data, darray_t* matched);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | 对象。  
cmp | tk_compare_t | 比较函数。  
data | const void* | 要比较的数据。  
matched | darray_t* | 返回满足条件的属性。  
  
#### tk_object_foreach_prop 函数

* * *

  * 函数功能：



> 遍历所有属性。

  * 函数原型：


    
    
    ret_t tk_object_foreach_prop (tk_object_t* obj, tk_visit_t on_prop, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
on_prop | tk_visit_t | 回调函数(data参数为named_value_t类型)。  
ctx | void* | 回调函数上下文。  
  
#### tk_object_get_child_object 函数

* * *

  * 函数功能：



> 获取下一级子对象。 属性路径之间使用符号”.”分割，例如：name.sub_name。

  * 函数原型：


    
    
    tk_object_t* tk_object_get_child_object (tk_object_t* obj, const char* path, const char** next_path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回下一级子对象，如果找不到则返回 NULL。  
obj | tk_object_t* | object对象。  
path | const char* | 属性路径。  
next_path | const char** | 返回下一级属性路径。  
  
#### tk_object_get_desc 函数

* * *

  * 函数功能：



> 获取对象的描述信息。

  * 函数原型：


    
    
    const char* tk_object_get_desc (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回对象的描述信息。  
obj | tk_object_t* | object对象。  
  
#### tk_object_get_prop 函数

* * *

  * 函数功能：



> 获取指定属性的值。

  * 函数原型：


    
    
    ret_t tk_object_get_prop (tk_object_t* obj, const char* name, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
v | value_t* | 返回属性的值。  
  
#### tk_object_get_prop_bool 函数

* * *

  * 函数功能：



> 获取指定属性的bool类型的值。

  * 函数原型：


    
    
    bool_t tk_object_get_prop_bool (tk_object_t* obj, const char* name, bool_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回指定属性的bool类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | bool_t | 缺省值。  
  
#### tk_object_get_prop_bool_by_path 函数

* * *

  * 函数功能：



> 获取指定属性的bool类型的值。

  * 函数原型：


    
    
    bool_t tk_object_get_prop_bool_by_path (tk_object_t* obj, const char* path, bool_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回指定属性的bool类型的值。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
defval | bool_t | 缺省值。  
  
#### tk_object_get_prop_by_path 函数

* * *

  * 函数功能：



> 获取指定path属性的值。

  * 函数原型：


    
    
    ret_t tk_object_get_prop_by_path (tk_object_t* obj, const char* path, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path，各级之间用.分隔。  
v | value_t* | 返回属性的值。  
  
#### tk_object_get_prop_double 函数

* * *

  * 函数功能：



> 获取指定属性的浮点数类型的值。

  * 函数原型：


    
    
    double tk_object_get_prop_double (tk_object_t* obj, const char* name, double defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | double | 返回指定属性的浮点数类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | double | 缺省值。  
  
#### tk_object_get_prop_float 函数

* * *

  * 函数功能：



> 获取指定属性的浮点数类型的值。

  * 函数原型：


    
    
    float_t tk_object_get_prop_float (tk_object_t* obj, const char* name, float_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回指定属性的浮点数类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | float_t | 缺省值。  
  
#### tk_object_get_prop_float_by_path 函数

* * *

  * 函数功能：



> 获取指定属性的浮点数类型的值。

e

  * 函数原型：


    
    
    float_t tk_object_get_prop_float_by_path (tk_object_t* obj, const char* path, float_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float_t | 返回指定属性的浮点数类型的值。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
defval | float_t | 缺省值。  
  
#### tk_object_get_prop_int 函数

* * *

  * 函数功能：



> 获取指定属性的整数类型的值。

  * 函数原型：


    
    
    int32_t tk_object_get_prop_int (tk_object_t* obj, const char* name, int32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回指定属性的整数类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | int32_t | 缺省值。  
  
#### tk_object_get_prop_int_by_path 函数

* * *

  * 函数功能：



> 获取指定属性的整数类型的值。

  * 函数原型：


    
    
    int32_t tk_object_get_prop_int_by_path (tk_object_t* obj, const char* path, int32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回指定属性的整数类型的值。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
defval | int32_t | 缺省值。  
  
#### tk_object_get_prop_int16 函数

* * *

  * 函数功能：



> 获取指定属性的int16类型的值。

  * 函数原型：


    
    
    int16_t tk_object_get_prop_int16 (tk_object_t* obj, const char* name, int16_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int16_t | 返回指定属性的int16类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | int16_t | 缺省值。  
  
#### tk_object_get_prop_int32 函数

* * *

  * 函数功能：



> 获取指定属性的int32类型的值。

  * 函数原型：


    
    
    int32_t tk_object_get_prop_int32 (tk_object_t* obj, const char* name, int32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回指定属性的int32类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | int32_t | 缺省值。  
  
#### tk_object_get_prop_int64 函数

* * *

  * 函数功能：



> 获取指定属性的int64类型的值。

  * 函数原型：


    
    
    int64_t tk_object_get_prop_int64 (tk_object_t* obj, const char* name, int64_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int64_t | 返回指定属性的int64类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | int64_t | 缺省值。  
  
#### tk_object_get_prop_int8 函数

* * *

  * 函数功能：



> 获取指定属性的int8类型的值。

  * 函数原型：


    
    
    int8_t tk_object_get_prop_int8 (tk_object_t* obj, const char* name, int8_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int8_t | 返回指定属性的int8类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | int8_t | 缺省值。  
  
#### tk_object_get_prop_object 函数

* * *

  * 函数功能：



> 获取指定属性的object类型的值。

  * 函数原型：


    
    
    tk_object_t* tk_object_get_prop_object (tk_object_t* obj, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回指定属性的object类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
  
#### tk_object_get_prop_object_by_path 函数

* * *

  * 函数功能：



> 获取指定属性的object类型的值。

  * 函数原型：


    
    
    tk_object_t* tk_object_get_prop_object_by_path (tk_object_t* obj, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回指定属性的object类型的值。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
  
#### tk_object_get_prop_pointer 函数

* * *

  * 函数功能：



> 获取指定属性的指针类型的值。

  * 函数原型：


    
    
    void* tk_object_get_prop_pointer (tk_object_t* obj, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回指定属性的指针类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
  
#### tk_object_get_prop_pointer_by_path 函数

* * *

  * 函数功能：



> 获取指定属性的指针类型的值。

  * 函数原型：


    
    
    void* tk_object_get_prop_pointer_by_path (tk_object_t* obj, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回指定属性的指针类型的值。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
  
#### tk_object_get_prop_str 函数

* * *

  * 函数功能：



> 获取指定属性的字符串类型的值。

  * 函数原型：


    
    
    const char* tk_object_get_prop_str (tk_object_t* obj, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回指定属性的字符串类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
  
#### tk_object_get_prop_str_by_path 函数

* * *

  * 函数功能：



> 获取指定属性的字符串类型的值。

  * 函数原型：


    
    
    const char* tk_object_get_prop_str_by_path (tk_object_t* obj, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回指定属性的字符串类型的值。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
  
#### tk_object_get_prop_uint16 函数

* * *

  * 函数功能：



> 获取指定属性的uint16类型的值。

  * 函数原型：


    
    
    uint16_t tk_object_get_prop_uint16 (tk_object_t* obj, const char* name, uint16_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint16_t | 返回指定属性的uint16类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | uint16_t | 缺省值。  
  
#### tk_object_get_prop_uint32 函数

* * *

  * 函数功能：



> 获取指定属性的uint32类型的值。

  * 函数原型：


    
    
    uint32_t tk_object_get_prop_uint32 (tk_object_t* obj, const char* name, uint32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回指定属性的uint32类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | uint32_t | 缺省值。  
  
#### tk_object_get_prop_uint64 函数

* * *

  * 函数功能：



> 获取指定属性的uint64类型的值。

  * 函数原型：


    
    
    uint64_t tk_object_get_prop_uint64 (tk_object_t* obj, const char* name, uint64_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 返回指定属性的uint64类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | uint64_t | 缺省值。  
  
#### tk_object_get_prop_uint8 函数

* * *

  * 函数功能：



> 获取指定属性的uint8类型的值。

  * 函数原型：


    
    
    uint8_t tk_object_get_prop_uint8 (tk_object_t* obj, const char* name, uint8_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint8_t | 返回指定属性的uint8类型的值。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
defval | uint8_t | 缺省值。  
  
#### tk_object_get_size 函数

* * *

  * 函数功能：



> 获取对象占用内存的大小。

  * 函数原型：


    
    
    uint32_t tk_object_get_size (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回对象占用内存的大小。  
obj | tk_object_t* | object对象。  
  
#### tk_object_get_type 函数

* * *

  * 函数功能：



> 获取对象的类型名称。

  * 函数原型：


    
    
    const char* tk_object_get_type (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回对象的类型名称。  
obj | tk_object_t* | object对象。  
  
#### tk_object_has_prop 函数

* * *

  * 函数功能：



> 检查是否存在指定的属性。

  * 函数原型：


    
    
    bool_t tk_object_has_prop (tk_object_t* obj, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
  
#### tk_object_has_prop_by_path 函数

* * *

  * 函数功能：



> 检查是否存在指定的属性。

  * 函数原型：


    
    
    bool_t tk_object_has_prop_by_path (tk_object_t* obj, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示存在，否则表示不存在。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path，各级之间用.分隔。  
  
#### tk_object_is_collection 函数

* * *

  * 函数功能：



> 判断对象是否是集合。

  * 函数原型：


    
    
    bool_t tk_object_is_collection (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是集合，否则不是。  
obj | tk_object_t* | object对象。  
  
#### tk_object_is_instance_of 函数

* * *

  * 函数功能：



> 检查对象是否是指定类型的实例。
    
    
    if(tk_object_is_instance_of(obj, OBJECT_ARRAY_TYPE)) {
    }
    

  * 函数原型：


    
    
    bool_t tk_object_is_instance_of (tk_object_t* obj, const char* type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是指定类型的实例，否则表示不是。  
obj | tk_object_t* | object对象。  
type | const char* | 类型。  
  
#### tk_object_notify_changed 函数

* * *

  * 函数功能：



> 触发EVT_PROPS_CHANGED事件。

  * 函数原型：


    
    
    ret_t tk_object_notify_changed (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
  
#### tk_object_ref 函数

* * *

  * 函数功能：



> 引用计数加1。

  * 函数原型：


    
    
    tk_object_t* tk_object_ref (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回object对象。  
obj | tk_object_t* | object对象。  
  
#### tk_object_remove_prop 函数

* * *

  * 函数功能：



> 删除指定属性。

  * 函数原型：


    
    
    ret_t tk_object_remove_prop (tk_object_t* obj, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
  
#### tk_object_set_name 函数

* * *

  * 函数功能：



> 设置对象的名称。

  * 函数原型：


    
    
    ret_t tk_object_set_name (tk_object_t* obj, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 对象的名称。  
  
#### tk_object_set_prop 函数

* * *

  * 函数功能：



> 设置指定属性的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop (tk_object_t* obj, const char* name, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | const value_t* | 属性的值。  
  
#### tk_object_set_prop_bool 函数

* * *

  * 函数功能：



> 设置指定属性的bool类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_bool (tk_object_t* obj, const char* name, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | bool_t | 属性的值。  
  
#### tk_object_set_prop_bool_by_path 函数

* * *

  * 函数功能：



> 设置指定属性的bool类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_bool_by_path (tk_object_t* obj, const char* path, bool_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
value | bool_t | 属性的值。  
  
#### tk_object_set_prop_by_path 函数

* * *

  * 函数功能：



> 设置指定属性的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_by_path (tk_object_t* obj, const char* path, const value_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
value | const value_t* | 属性的值。  
  
#### tk_object_set_prop_double 函数

* * *

  * 函数功能：



> 设置指定属性的浮点数类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_double (tk_object_t* obj, const char* name, double value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | double | 属性的值。  
  
#### tk_object_set_prop_float 函数

* * *

  * 函数功能：



> 设置指定属性的浮点数类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_float (tk_object_t* obj, const char* name, float_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | float_t | 属性的值。  
  
#### tk_object_set_prop_float_by_path 函数

* * *

  * 函数功能：



> 设置指定属性的浮点数类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_float_by_path (tk_object_t* obj, const char* path, float_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
value | float_t | 属性的值。  
  
#### tk_object_set_prop_int 函数

* * *

  * 函数功能：



> 设置指定属性的整数类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_int (tk_object_t* obj, const char* name, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | int32_t | 属性的值。  
  
#### tk_object_set_prop_int_by_path 函数

* * *

  * 函数功能：



> 设置指定属性的整数类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_int_by_path (tk_object_t* obj, const char* path, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
value | int32_t | 属性的值。  
  
#### tk_object_set_prop_int16 函数

* * *

  * 函数功能：



> 设置指定属性的int16类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_int16 (tk_object_t* obj, const char* name, int16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | int16_t | 属性的值。  
  
#### tk_object_set_prop_int32 函数

* * *

  * 函数功能：



> 设置指定属性的int32类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_int32 (tk_object_t* obj, const char* name, int32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | int32_t | 属性的值。  
  
#### tk_object_set_prop_int64 函数

* * *

  * 函数功能：



> 设置指定属性的int64类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_int64 (tk_object_t* obj, const char* name, int64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | int64_t | 属性的值。  
  
#### tk_object_set_prop_int8 函数

* * *

  * 函数功能：



> 设置指定属性的int8类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_int8 (tk_object_t* obj, const char* name, int8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | int8_t | 属性的值。  
  
#### tk_object_set_prop_object 函数

* * *

  * 函数功能：



> 设置指定属性的object类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_object (tk_object_t* obj, const char* name, tk_object_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | tk_object_t* | 属性的值。  
  
#### tk_object_set_prop_object_by_path 函数

* * *

  * 函数功能：



> 设置指定属性的object类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_object_by_path (tk_object_t* obj, const char* path, tk_object_t* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
value | tk_object_t* | 属性的值。  
  
#### tk_object_set_prop_pointer 函数

* * *

  * 函数功能：



> 设置指定属性的指针类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_pointer (tk_object_t* obj, const char* name, void* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | void* | 属性的值。  
  
#### tk_object_set_prop_pointer_by_path 函数

* * *

  * 函数功能：



> 设置指定属性的指针类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_pointer_by_path (tk_object_t* obj, const char* path, void* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
value | void* | 属性的值。  
  
#### tk_object_set_prop_pointer_ex 函数

* * *

  * 函数功能：



> 设置指定属性的指针类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_pointer_ex (tk_object_t* obj, const char* name, void* value, tk_destroy_t destroy);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | void* | 属性的值。  
destroy | tk_destroy_t | 销毁函数。  
  
#### tk_object_set_prop_str 函数

* * *

  * 函数功能：



> 设置指定属性的字符串类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_str (tk_object_t* obj, const char* name, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | const char* | 属性的值。  
  
#### tk_object_set_prop_str_by_path 函数

* * *

  * 函数功能：



> 设置指定属性的字符串类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_str_by_path (tk_object_t* obj, const char* path, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
path | const char* | 属性的path。  
value | const char* | 属性的值。  
  
#### tk_object_set_prop_str_with_format 函数

* * *

  * 函数功能：



> 设置指定属性的字符串类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_str_with_format (tk_object_t* obj, const char* name, const char* format);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
format | const char* | 格式字符串。  
  
#### tk_object_set_prop_uint16 函数

* * *

  * 函数功能：



> 设置指定属性的uint16类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_uint16 (tk_object_t* obj, const char* name, uint16_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | uint16_t | 属性的值。  
  
#### tk_object_set_prop_uint32 函数

* * *

  * 函数功能：



> 设置指定属性的uint32类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_uint32 (tk_object_t* obj, const char* name, uint32_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | uint32_t | 属性的值。  
  
#### tk_object_set_prop_uint64 函数

* * *

  * 函数功能：



> 设置指定属性的uint64类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_uint64 (tk_object_t* obj, const char* name, uint64_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | uint64_t | 属性的值。  
  
#### tk_object_set_prop_uint8 函数

* * *

  * 函数功能：



> 设置指定属性的uint8类型的值。

  * 函数原型：


    
    
    ret_t tk_object_set_prop_uint8 (tk_object_t* obj, const char* name, uint8_t value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
name | const char* | 属性的名称。  
value | uint8_t | 属性的值。  
  
#### tk_object_to_json 函数

* * *

  * 函数功能：



> 转换成JSON字符串。

  * 函数原型：


    
    
    ret_t tk_object_to_json (tk_object_t* obj, str_t* json, uint32_t indent, uint32_t level, bool_t oneline);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
json | str_t* | 返回JSON字符串。  
indent | uint32_t | 缩进空格数。  
level | uint32_t | 初始缩进层级。  
oneline | bool_t | 是否不换行。  
  
#### tk_object_unref 函数

* * *

  * 函数功能：



> 引用计数减1。引用计数为0时，销毁对象。

  * 函数原型：


    
    
    ret_t tk_object_unref (tk_object_t* obj);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
obj | tk_object_t* | object对象。  
  
#### name 属性

* * *

> 对象的名称。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是  
  
#### ref_count 属性

* * *

> 引用计数。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可脚本化 | 是
