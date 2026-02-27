## ui_feedback_t

### 概述

## 提供按键音、触屏音和震动等反馈。

### 函数

函数名称 | 说明  
---|---  
ui_feedback_deinit | ~初始化。  
ui_feedback_init | 初始化。  
ui_feedback_request | 请求反馈。  
  
#### ui_feedback_deinit 函数

* * *

  * 函数功能：



> ~初始化。

  * 函数原型：


    
    
    ret_t ui_feedback_deinit ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### ui_feedback_init 函数

* * *

  * 函数功能：



> 初始化。 设置实际的处理函数。

  * 函数原型：


    
    
    ret_t ui_feedback_init (ui_on_feedback_t on_feedback, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
on_feedback | ui_on_feedback_t | 实际的处理函数。  
ctx | void* | 回调函数的上下文。  
  
#### ui_feedback_request 函数

* * *

  * 函数功能：



> 请求反馈。

  * 函数原型：


    
    
    ret_t ui_feedback_request (widget_t* widget, event_t* evt);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
evt | event_t* | event对象。
