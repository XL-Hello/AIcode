## conf_obj_t

### 概述

![image](images/conf_obj_t_0.png)

## conf对象。

### 函数

函数名称 | 说明  
---|---  
conf_obj_create |   
conf_obj_create_ex |   
conf_obj_create_sub_object | 根据路径创建一个子对象。  
conf_obj_get_doc | 获取doc对象，用于更高级的操作。  
conf_obj_save | 保存文档。  
conf_obj_set_readonly | 设置为只读模式。  
  
#### conf_obj_create 函数

* * *

  * 函数功能：



>   * 函数原型：


    
    
    tk_object_t* conf_obj_create (conf_doc_save_t save, conf_doc_load_t load, const char* url, bool_t create_if_not_exist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回配置对象。  
save | conf_doc_save_t | 保存函数。  
load | conf_doc_load_t | 加载函数。  
url | const char* | 路径。  
create_if_not_exist | bool_t | 如果不存在是否创建。  
  
#### conf_obj_create_ex 函数

* * *

  * 函数功能：



>   * 函数原型：


    
    
    tk_object_t* conf_obj_create_ex (conf_doc_save_t save, conf_doc_load_t load, const char* url, bool_t create_if_not_exist, bool_t use_extend_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回配置对象。  
save | conf_doc_save_t | 保存函数。  
load | conf_doc_load_t | 加载函数。  
url | const char* | 路径。  
create_if_not_exist | bool_t | 如果不存在是否创建。  
use_extend_type | bool_t | 是否使用拓展类型。  
  
#### conf_obj_create_sub_object 函数

* * *

  * 函数功能：



> 根据路径创建一个子对象。

  * 函数原型：


    
    
    tk_object_t* conf_obj_create_sub_object (tk_object_t* conf, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回配置对象。  
conf | tk_object_t* | 配置对象。  
path | const char* | 路径。  
  
#### conf_obj_get_doc 函数

* * *

  * 函数功能：



> 获取doc对象，用于更高级的操作。

  * 函数原型：


    
    
    conf_doc_t* conf_obj_get_doc (tk_object_t* conf);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | conf_doc_t* | 返回doc对象。  
conf | tk_object_t* | conf对象。  
  
#### conf_obj_save 函数

* * *

  * 函数功能：



> 保存文档。

  * 函数原型：


    
    
    ret_t conf_obj_save (tk_object_t* conf);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败  
conf | tk_object_t* | conf对象。  
  
#### conf_obj_set_readonly 函数

* * *

  * 函数功能：



> 设置为只读模式。

  * 函数原型：


    
    
    ret_t conf_obj_set_readonly (tk_object_t* conf, bool_t readonly);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败  
conf | tk_object_t* | conf对象。  
readonly | bool_t | 只读模式。
