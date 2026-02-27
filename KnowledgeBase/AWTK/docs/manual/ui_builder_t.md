## ui_builder_t

### 概述

界面构造器接口。

负责把ui_loader解析的数据进一步处理，至于具体做什么，由具体实现决定。常见的实现有：

  * 构建widget对象树。

  * 生成二进制的UI描述数据。

  * 生成XML格式的UI描述数据。




![image](images/ui_builder_t_0.png)

* * *

### 函数

函数名称 | 说明  
---|---  
ui_builder_destroy | 销毁builder。  
ui_builder_on_end | ui_loader在解析结束时，调用本函数做些收尾工作。  
ui_builder_on_start | ui_loader在解析开始时，调用本函数做些准备工作。  
ui_builder_on_widget_end | ui_loader在解析到widget结束时，调用本函数进一步处理。  
ui_builder_on_widget_prop | ui_loader在解析到widget的属性时，调用本函数进一步处理。  
ui_builder_on_widget_prop_end | ui_loader在解析到widget全部属性结束时，调用本函数进一步处理。  
ui_builder_on_widget_start | ui_loader在解析到widget时，调用本函数进一步处理。  
  
#### ui_builder_destroy 函数

* * *

  * 函数功能：



> 销毁builder。

  * 函数原型：


    
    
    ret_t ui_builder_destroy (ui_builder_t* builder);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
builder | ui_builder_t* | builder对象。  
  
#### ui_builder_on_end 函数

* * *

  * 函数功能：



> ui_loader在解析结束时，调用本函数做些收尾工作。

  * 函数原型：


    
    
    ret_t ui_builder_on_end (ui_builder_t* builder);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
builder | ui_builder_t* | builder对象。  
  
#### ui_builder_on_start 函数

* * *

  * 函数功能：



> ui_loader在解析开始时，调用本函数做些准备工作。

  * 函数原型：


    
    
    ret_t ui_builder_on_start (ui_builder_t* builder);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
builder | ui_builder_t* | builder对象。  
  
#### ui_builder_on_widget_end 函数

* * *

  * 函数功能：



> ui_loader在解析到widget结束时，调用本函数进一步处理。

  * 函数原型：


    
    
    ret_t ui_builder_on_widget_end (ui_builder_t* builder);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
builder | ui_builder_t* | builder对象。  
  
#### ui_builder_on_widget_prop 函数

* * *

  * 函数功能：



> ui_loader在解析到widget的属性时，调用本函数进一步处理。

  * 函数原型：


    
    
    ret_t ui_builder_on_widget_prop (ui_builder_t* builder, const char* name, const char* value);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
builder | ui_builder_t* | builder对象。  
name | const char* | 属性名。  
value | const char* | 属性值。  
  
#### ui_builder_on_widget_prop_end 函数

* * *

  * 函数功能：



> ui_loader在解析到widget全部属性结束时，调用本函数进一步处理。

  * 函数原型：


    
    
    ret_t ui_builder_on_widget_prop_end (ui_builder_t* builder);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
builder | ui_builder_t* | builder对象。  
  
#### ui_builder_on_widget_start 函数

* * *

  * 函数功能：



> ui_loader在解析到widget时，调用本函数进一步处理。

  * 函数原型：


    
    
    ret_t ui_builder_on_widget_start (ui_builder_t* builder, const widget_desc_t* desc);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
builder | ui_builder_t* | builder对象。  
desc | const widget_desc_t* | widget描述信息。
