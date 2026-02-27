## svg_helper_t

### 概述

* * *

### 函数

函数名称 | 说明  
---|---  
bsvg_to_svg | bsvg to svg  
svg_file_to_bsvg | svg to bsvg  
svg_to_bsvg | svg to bsvg  
  
#### bsvg_to_svg 函数

* * *

  * 函数功能：



> bsvg to svg

  * 函数原型：


    
    
    ret_t bsvg_to_svg (const uint32_t* data, uint32_t size, str_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
data | const uint32_t* | bsvg数据。  
size | uint32_t | bsvg数据长度。  
str | str_t* | 用于返回svg数据。  
  
#### svg_file_to_bsvg 函数

* * *

  * 函数功能：



> svg to bsvg

  * 函数原型：


    
    
    ret_t svg_file_to_bsvg (const char* ifilename, const char* ofilename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ifilename | const char* | svg文件名。  
ofilename | const char* | bsvg文件名。  
  
#### svg_to_bsvg 函数

* * *

  * 函数功能：



> svg to bsvg

  * 函数原型：


    
    
    ret_t svg_to_bsvg (const char* xml, uint32_t size, uint32_t** out, uint32_t* out_size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
xml | const char* | svg数据。  
size | uint32_t | svg数据长度。  
out | uint32_t** | 用于返回bsvg数据。  
out_size | uint32_t* | bsvg数据长度。
