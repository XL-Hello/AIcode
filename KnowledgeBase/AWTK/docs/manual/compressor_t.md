## compressor_t

### 概述

## 压缩解压接口。

### 函数

函数名称 | 说明  
---|---  
compressor_compress | 压缩数据。  
compressor_destroy | 销毁compressor对象。  
compressor_uncompress | 解压数据。  
  
#### compressor_compress 函数

* * *

  * 函数功能：



> 压缩数据。

  * 函数原型：


    
    
    ret_t compressor_compress (compressor_t* compressor, const void* data, uint32_t size, wbuffer_t* out);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
compressor | compressor_t* | compressor对象。  
data | const void* | 待压缩的数据。  
size | uint32_t | 数据长度。  
out | wbuffer_t* | 压缩之后的数据。  
  
#### compressor_destroy 函数

* * *

  * 函数功能：



> 销毁compressor对象。

  * 函数原型：


    
    
    ret_t compressor_destroy (compressor_t* compressor);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
compressor | compressor_t* | compressor对象。  
  
#### compressor_uncompress 函数

* * *

  * 函数功能：



> 解压数据。

  * 函数原型：


    
    
    ret_t compressor_uncompress (compressor_t* compressor, const void* data, uint32_t size, wbuffer_t* out);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
compressor | compressor_t* | compressor对象。  
data | const void* | 待解压的数据。  
size | uint32_t | 数据长度。  
out | wbuffer_t* | 解压之后的数据。
