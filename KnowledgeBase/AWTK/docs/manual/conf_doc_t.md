## conf_doc_t

### 概述

## 代表整个配置文件。

### 函数

函数名称 | 说明  
---|---  
conf_doc_add_child | 追加一个子节点。  
conf_doc_append_child | 追加一个子节点。  
conf_doc_append_sibling | 追加一个兄弟节点。  
conf_doc_clear | 删除指定路径的节点的全部子节点。  
conf_doc_create | 构造函数。  
conf_doc_create_node | 创建一个空节点。  
conf_doc_destroy | 析构函数。  
conf_doc_destroy_node | 销毁节点对象。  
conf_doc_dup_node | 拷贝一个节点，并追加到其后。  
conf_doc_exists | 判断指定路径的节点是否存在。  
conf_doc_find_node | 根据path查找节点。  
conf_doc_get | 获取指定路径节点的值。  
conf_doc_get_bool | 获取指定路径节点的值。  
conf_doc_get_ex | 获取指定路径节点的值。  
conf_doc_get_float | 获取指定路径节点的值。  
conf_doc_get_int | 获取指定路径节点的值。  
conf_doc_get_str | 获取指定路径节点的值。  
conf_doc_is_first | 检查指定节点是否在兄弟节点中排第一。  
conf_doc_is_last | 检查指定节点是否在兄弟节点中排最后。  
conf_doc_move_down | 和后一个兄弟节点交换位置。  
conf_doc_move_up | 和前一个兄弟节点交换位置。  
conf_doc_remove | 删除指定路径的节点。  
conf_doc_remove_child | 删除指定的子节点。  
conf_doc_remove_child_by_name | 删除指定的子节点。  
conf_doc_remove_children | 删除全部子节点。  
conf_doc_remove_sibling | 删除指定的兄弟节点。  
conf_doc_set | 设置指定路径节点的值。  
conf_doc_set_bool | 设置指定路径节点的值。  
conf_doc_set_float | 设置指定路径节点的值。  
conf_doc_set_int | 设置指定路径节点的值。  
conf_doc_set_node_prop | 设置节点的属性。  
conf_doc_set_str | 设置指定路径节点的值。  
conf_doc_use_extend_type | 使用拓展类型。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
root | conf_node_t* | 根节点。  
use_extend_type | bool_t | 使用拓展类型。  
  
#### conf_doc_add_child 函数

* * *

  * 函数功能：



> 追加一个子节点。

  * 函数原型：


    
    
    ret_t conf_doc_add_child (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_append_child 函数

* * *

  * 函数功能：



> 追加一个子节点。

  * 函数原型：


    
    
    ret_t conf_doc_append_child (conf_doc_t* doc, conf_node_t* node, conf_node_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
child | conf_node_t* | 待追加节点对象。  
  
#### conf_doc_append_sibling 函数

* * *

  * 函数功能：



> 追加一个兄弟节点。

  * 函数原型：


    
    
    ret_t conf_doc_append_sibling (conf_doc_t* doc, conf_node_t* node, conf_node_t* sibling);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
sibling | conf_node_t* | 待追加节点对象。  
  
#### conf_doc_clear 函数

* * *

  * 函数功能：



> 删除指定路径的节点的全部子节点。

  * 函数原型：


    
    
    ret_t conf_doc_clear (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_create 函数

* * *

  * 函数功能：



> 构造函数。

  * 函数原型：


    
    
    conf_doc_t* conf_doc_create (uint32_t prealloc_nodes_nr);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | conf_doc_t* | 返回doc对象。  
prealloc_nodes_nr | uint32_t | 预先分配的节点数。  
  
#### conf_doc_create_node 函数

* * *

  * 函数功能：



> 创建一个空节点。

  * 函数原型：


    
    
    conf_node_t* conf_doc_create_node (conf_doc_t* doc, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | conf_node_t* | 返回节点对象。  
doc | conf_doc_t* | 文档对象。  
name | const char* | 节点名称。  
  
#### conf_doc_destroy 函数

* * *

  * 函数功能：



> 析构函数。

  * 函数原型：


    
    
    ret_t conf_doc_destroy (conf_doc_t* doc);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
  
#### conf_doc_destroy_node 函数

* * *

  * 函数功能：



> 销毁节点对象。

  * 函数原型：


    
    
    ret_t conf_doc_destroy_node (conf_doc_t* doc, conf_node_t* node);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
  
#### conf_doc_dup_node 函数

* * *

  * 函数功能：



> 拷贝一个节点，并追加到其后。

  * 函数原型：


    
    
    conf_node_t* conf_doc_dup_node (conf_doc_t* doc, conf_node_t* node, const char* new_name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | conf_node_t* | 返回新节点。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
new_name | const char* | 节点名称。  
  
#### conf_doc_exists 函数

* * *

  * 函数功能：



> 判断指定路径的节点是否存在。

  * 函数原型：


    
    
    bool_t conf_doc_exists (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示成功，FALSE表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_find_node 函数

* * *

  * 函数功能：



> 根据path查找节点。

  * 函数原型：


    
    
    conf_node_t* conf_doc_find_node (conf_doc_t* doc, conf_node_t* node, const char* path, bool_t create_if_not_exist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | conf_node_t* | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 从该节点查找。  
path | const char* | 路径。  
create_if_not_exist | bool_t | 不存在是否创建。  
  
#### conf_doc_get 函数

* * *

  * 函数功能：



> 获取指定路径节点的值。

  * 函数原型：


    
    
    ret_t conf_doc_get (conf_doc_t* doc, const char* path, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
v | value_t* | 用于返回值。  
  
#### conf_doc_get_bool 函数

* * *

  * 函数功能：



> 获取指定路径节点的值。

  * 函数原型：


    
    
    bool_t conf_doc_get_bool (conf_doc_t* doc, const char* path, bool_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回值。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
defval | bool_t | 缺省值。  
  
#### conf_doc_get_ex 函数

* * *

  * 函数功能：



> 获取指定路径节点的值。

  * 函数原型：


    
    
    ret_t conf_doc_get_ex (conf_doc_t* doc, conf_node_t* node, const char* path, value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 从该节点查找。  
path | const char* | 节点的路径。  
v | value_t* | 用于返回值。  
  
#### conf_doc_get_float 函数

* * *

  * 函数功能：



> 获取指定路径节点的值。

  * 函数原型：


    
    
    float conf_doc_get_float (conf_doc_t* doc, const char* path, float defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | float | 返回值。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
defval | float | 缺省值。  
  
#### conf_doc_get_int 函数

* * *

  * 函数功能：



> 获取指定路径节点的值。

  * 函数原型：


    
    
    int32_t conf_doc_get_int (conf_doc_t* doc, const char* path, int32_t defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 返回值。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
defval | int32_t | 缺省值。  
  
#### conf_doc_get_str 函数

* * *

  * 函数功能：



> 获取指定路径节点的值。

  * 函数原型：


    
    
    const char* conf_doc_get_str (conf_doc_t* doc, const char* path, const char* defval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回值。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
defval | const char* | 缺省值。  
  
#### conf_doc_is_first 函数

* * *

  * 函数功能：



> 检查指定节点是否在兄弟节点中排第一。

  * 函数原型：


    
    
    bool_t conf_doc_is_first (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示不是。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_is_last 函数

* * *

  * 函数功能：



> 检查指定节点是否在兄弟节点中排最后。

  * 函数原型：


    
    
    bool_t conf_doc_is_last (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示是，否则表示不是。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_move_down 函数

* * *

  * 函数功能：



> 和后一个兄弟节点交换位置。

  * 函数原型：


    
    
    ret_t conf_doc_move_down (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_move_up 函数

* * *

  * 函数功能：



> 和前一个兄弟节点交换位置。

  * 函数原型：


    
    
    ret_t conf_doc_move_up (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_remove 函数

* * *

  * 函数功能：



> 删除指定路径的节点。

  * 函数原型：


    
    
    ret_t conf_doc_remove (conf_doc_t* doc, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
  
#### conf_doc_remove_child 函数

* * *

  * 函数功能：



> 删除指定的子节点。

  * 函数原型：


    
    
    ret_t conf_doc_remove_child (conf_doc_t* doc, conf_node_t* node, conf_node_t* child);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
child | conf_node_t* | 待删除节点对象。  
  
#### conf_doc_remove_child_by_name 函数

* * *

  * 函数功能：



> 删除指定的子节点。

  * 函数原型：


    
    
    ret_t conf_doc_remove_child_by_name (conf_doc_t* doc, conf_node_t* node, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
name | const char* | 待删除节点的名称。  
  
#### conf_doc_remove_children 函数

* * *

  * 函数功能：



> 删除全部子节点。

  * 函数原型：


    
    
    ret_t conf_doc_remove_children (conf_doc_t* doc, conf_node_t* node);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
  
#### conf_doc_remove_sibling 函数

* * *

  * 函数功能：



> 删除指定的兄弟节点。

  * 函数原型：


    
    
    ret_t conf_doc_remove_sibling (conf_doc_t* doc, conf_node_t* node, conf_node_t* sibling);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
sibling | conf_node_t* | 待删除节点对象。  
  
#### conf_doc_set 函数

* * *

  * 函数功能：



> 设置指定路径节点的值。

  * 函数原型：


    
    
    ret_t conf_doc_set (conf_doc_t* doc, const char* path, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
v | const value_t* | 值。  
  
#### conf_doc_set_bool 函数

* * *

  * 函数功能：



> 设置指定路径节点的值。

  * 函数原型：


    
    
    ret_t conf_doc_set_bool (conf_doc_t* doc, const char* path, bool_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
v | bool_t | 值。  
  
#### conf_doc_set_float 函数

* * *

  * 函数功能：



> 设置指定路径节点的值。

  * 函数原型：


    
    
    ret_t conf_doc_set_float (conf_doc_t* doc, const char* path, float v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
v | float | 值。  
  
#### conf_doc_set_int 函数

* * *

  * 函数功能：



> 设置指定路径节点的值。

  * 函数原型：


    
    
    ret_t conf_doc_set_int (conf_doc_t* doc, const char* path, int32_t v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
v | int32_t | 值。  
  
#### conf_doc_set_node_prop 函数

* * *

  * 函数功能：



> 设置节点的属性。

  * 函数原型：


    
    
    ret_t conf_doc_set_node_prop (conf_doc_t* doc, conf_node_t* node, const char* name, const value_t* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
node | conf_node_t* | 节点对象。  
name | const char* | 名称。  
v | const value_t* | 值。  
  
#### conf_doc_set_str 函数

* * *

  * 函数功能：



> 设置指定路径节点的值。

  * 函数原型：


    
    
    ret_t conf_doc_set_str (conf_doc_t* doc, const char* path, const char* v);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
path | const char* | 节点的路径。  
v | const char* | 值。  
  
#### conf_doc_use_extend_type 函数

* * *

  * 函数功能：



> 使用拓展类型。

  * 函数原型：


    
    
    ret_t conf_doc_use_extend_type (conf_doc_t* doc, bool_t use);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
doc | conf_doc_t* | 文档对象。  
use | bool_t | 是否使用拓展类型。  
  
#### root 属性

* * *

> 根节点。

  * 类型：conf_node_t*



#### use_extend_type 属性

* * *

> 使用拓展类型。

  * 类型：bool_t


