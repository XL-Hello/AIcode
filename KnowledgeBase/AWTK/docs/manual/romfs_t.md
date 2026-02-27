## romfs_t

### 概述

## 一个简单的ROMFS(目前用于WEB加载配置文件)

### 函数

函数名称 | 说明  
---|---  
romfs_deinit | ~初始化。  
romfs_get | 获取fs对象。  
romfs_init | 初始化。  
  
#### romfs_deinit 函数

* * *

  * 函数功能：



> ~初始化。

  * 函数原型：


    
    
    ret_t romfs_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### romfs_get 函数

* * *

  * 函数功能：



> 获取fs对象。

  * 函数原型：


    
    
    fs_t* romfs_get ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | fs_t* | 返回fs对象。  
  
#### romfs_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    ret_t romfs_init (const uint8_t* header_data, uint32_t header_size, const uint8_t* body_data, uint32_t body_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
header_data | const uint8_t* | 文件信息数据。  
header_size | uint32_t | 文件信息数据长度。  
body_data | const uint8_t* | 文件数据。  
body_size | uint32_t | 文件数据长度。
