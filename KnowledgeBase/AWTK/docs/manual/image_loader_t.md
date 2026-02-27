## image_loader_t

### 概述

## 图片加载接口。

### 函数

函数名称 | 说明  
---|---  
image_loader_load | 加载图片。  
image_loader_load_image | 查找满足条件加载器并加载图片。  
image_loader_register | 注册图片加载器。  
image_loader_unregister | 注销图片加载器。  
  
#### image_loader_load 函数

* * *

  * 函数功能：



> 加载图片。

  * 函数原型：


    
    
    ret_t image_loader_load (image_loader_t* loader, const asset_info_t* asset, bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
loader | image_loader_t* | loader对象。  
asset | const asset_info_t* | 资源。  
bitmap | bitmap_t* | 用于返回位图对象。  
  
#### image_loader_load_image 函数

* * *

  * 函数功能：



> 查找满足条件加载器并加载图片。

  * 函数原型：


    
    
    ret_t image_loader_load_image (const asset_info_t* asset, bitmap_t* bitmap);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
asset | const asset_info_t* | 资源。  
bitmap | bitmap_t* | 用于返回位图对象。  
  
#### image_loader_register 函数

* * *

  * 函数功能：



> 注册图片加载器。

  * 函数原型：


    
    
    ret_t image_loader_register (image_loader_t* loader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
loader | image_loader_t* | loader对象。  
  
#### image_loader_unregister 函数

* * *

  * 函数功能：



> 注销图片加载器。

  * 函数原型：


    
    
    ret_t image_loader_unregister (image_loader_t* loader);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
loader | image_loader_t* | loader对象。
