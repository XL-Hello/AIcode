## fps_t

### 概述

## 用于计算FPS(帧率)。

### 函数

函数名称 | 说明  
---|---  
fps_get | 获取FPS(帧率)。  
fps_inc | 增加帧数。  
fps_init | 初始化。  
  
#### fps_get 函数

* * *

  * 函数功能：



> 获取FPS(帧率)。

  * 函数原型：


    
    
    uint32_t fps_get (fps_t* fps);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回FPS(帧率)。  
fps | fps_t* | fps对象。  
  
#### fps_inc 函数

* * *

  * 函数功能：



> 增加帧数。

  * 函数原型：


    
    
    ret_t fps_inc (fps_t* fps);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fps | fps_t* | fps对象。  
  
#### fps_init 函数

* * *

  * 函数功能：



> 初始化。

  * 函数原型：


    
    
    ret_t fps_init (fps_t* fps);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
fps | fps_t* | fps对象。
