## conf_json_t

### 概述

![image](images/conf_json_t_0.png)

conf json对象。

示例
    
    
    char filename[MAX_PATH + 1] = {0};
    path_prepend_temp_path(filename, "test.json");
    
    const char *json_data1 = "{"
    "{\"root\":{"
    "\"name\":\"awplc\","
    "\"age\":18,"
    "\"weight\":60.5"
    "}"
    "}";
    ENSURE(file_write(filename, json_data1, strlen(json_data1)) == RET_OK);
    
    // 从文件加载
    tk_object_t *json = conf_json_load(filename, FALSE);
    
    // 获取数据。
    ENSURE(tk_str_eq(tk_object_get_prop_str(json, "root.name"), "awplc"));
    ENSURE(tk_object_get_prop_int(json, "root.age", 0) == 18);
    ENSURE(tk_object_get_prop_double(json, "root.weight", 0) == 60.5);
    
    // 销毁对象
    TK_OBJECT_UNREF(json);
    
    // 从内存加载
    json = conf_json_load_from_buff(json_data1, strlen(json_data1), FALSE);
    
    // 获取数据
    ENSURE(tk_str_eq(tk_object_get_prop_str(json, "root.name"), "awplc"));
    ENSURE(tk_object_get_prop_int(json, "root.age", 0) == 18);
    ENSURE(tk_object_get_prop_double(json, "root.weight", 0) == 60.5);
    
    // 设置数据
    ENSURE(tk_object_set_prop_int(json, "root.age", 20) == RET_OK);
    ENSURE(tk_object_get_prop_int(json, "root.age", 0) == 20);
    
    // 保存到文件
    ENSURE(conf_json_save_as(json, filename) == RET_OK);
    ENSURE(file_exist(filename) == TRUE);
    
    // 销毁对象
    TK_OBJECT_UNREF(json);
    

* * *

### 函数

函数名称 | 说明  
---|---  
conf_doc_save_json_ex | 功能描述  
conf_json_create | 创建一个空的conf对象。  
conf_json_load | 从指定URL加载JSON对象。  
conf_json_load_ex | 从指定URL加载JSON对象。  
conf_json_load_from_buff | 从内存加载JSON对象。  
conf_json_save_as | 将doc对象保存到指定URL。  
conf_json_save_to_buff | 将obj保存为JSON格式到内存。  
  
#### conf_doc_save_json_ex 函数

* * *

  * 函数功能：



> 功能描述

  * 函数原型：


    
    
    ret_t conf_doc_save_json_ex (conf_doc_t* doc, str_t* str, uint32_t indent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回 ret_t值  
doc | conf_doc_t* | doc对象  
str | str_t* | 保存结果  
indent | uint32_t | 缩进  
  
#### conf_json_create 函数

* * *

  * 函数功能：



> 创建一个空的conf对象。

  * 函数原型：


    
    
    tk_object_t* conf_json_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回配置对象。  
  
#### conf_json_load 函数

* * *

  * 函数功能：



> 从指定URL加载JSON对象。

  * 函数原型：


    
    
    tk_object_t* conf_json_load (const char* url, bool_t create_if_not_exist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回配置对象。  
url | const char* | 路径(通常是文件路径)。  
create_if_not_exist | bool_t | 如果不存在是否创建。  
  
#### conf_json_load_ex 函数

* * *

  * 函数功能：



> 从指定URL加载JSON对象。

  * 函数原型：


    
    
    tk_object_t* conf_json_load_ex (const char* url, bool_t create_if_not_exist, bool_t use_extend_type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回配置对象。  
url | const char* | 路径(通常是文件路径)。  
create_if_not_exist | bool_t | 如果不存在是否创建。  
use_extend_type | bool_t | 是否使用拓展类型。  
  
#### conf_json_load_from_buff 函数

* * *

  * 函数功能：



> 从内存加载JSON对象。

  * 函数原型：


    
    
    tk_object_t* conf_json_load_from_buff (const void* buff, uint32_t size, bool_t create_if_not_exist);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回配置对象。  
buff | const void* | 数据。  
size | uint32_t | 数据长度。  
create_if_not_exist | bool_t | 如果不存在是否创建。  
  
#### conf_json_save_as 函数

* * *

  * 函数功能：



> 将doc对象保存到指定URL。

  * 函数原型：


    
    
    ret_t conf_json_save_as (tk_object_t* obj, const char* url);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败  
obj | tk_object_t* | doc对象。  
url | const char* | 保存的位置。  
  
#### conf_json_save_to_buff 函数

* * *

  * 函数功能：



> 将obj保存为JSON格式到内存。

  * 函数原型：


    
    
    ret_t conf_json_save_to_buff (tk_object_t* obj, wbuffer_t* wb);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败  
obj | tk_object_t* | doc对象。  
wb | wbuffer_t* | 返回结果(不要初始化，使用完成后要调用wbuffer_deinit)。
