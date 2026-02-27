## ui_loader_t

### 概述

UI加载器。

负责从资源加载界面描述数据，然后分发给ui_builder，由ui_builder进一步处理。

常见的实现有两种：

  * XML格式的加载器。

  * 二进制格式的加载器。




![image](images/ui_loader_t_0.png)

* * *

### 函数

函数名称 | 说明  
---|---  
ui_loader_load | 加载界面描述数据，然后分发给ui_builder，由ui_builder进一步处理。  
ui_loader_load_widget | 从指定的资源加载widget对象，通常用于加载非窗口的widget。  
ui_loader_load_widget_from_xml | 从xml数据创建widget。  
ui_loader_load_widget_with_parent | 从指定的资源加载widget对象，并为widget对象指定父控件对象，通常用于加载非窗口的widget。  
  
#### ui_loader_load 函数

* * *

  * 函数功能：



> 加载界面描述数据，然后分发给ui_builder，由ui_builder进一步处理。

  * 函数原型：


    
    
    ret_t ui_loader_load (ui_loader_t* loader, const uint8_t* data, uint32_t size, ui_builder_t* builder);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
loader | ui_loader_t* | loader对象。  
data | const uint8_t* | 数据。  
size | uint32_t | 数据长度。  
builder | ui_builder_t* | 负责进一步处理，比如构建UI界面。  
  
#### ui_loader_load_widget 函数

* * *

  * 函数功能：



> 从指定的资源加载widget对象，通常用于加载非窗口的widget。
> 
> 需要自己将widget加入窗口后，再调用widget_layout。

  * 函数原型：


    
    
    widget_t* ui_loader_load_widget (const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回widget对象。  
name | const char* | 资源名。  
  
#### ui_loader_load_widget_from_xml 函数

* * *

  * 函数功能：



> 从xml数据创建widget。
> 
> 需要自己将widget加入窗口后，再调用widget_layout。

  * 函数原型：


    
    
    widget_t* ui_loader_load_widget_from_xml (widget_t* parent, const char* xml, uint32_t size);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回widget对象。  
parent | widget_t* | 父控件对象。  
xml | const char* | XML数据。  
size | uint32_t | XML数据长度。  
  
#### ui_loader_load_widget_with_parent 函数

* * *

  * 函数功能：



> 从指定的资源加载widget对象，并为widget对象指定父控件对象，通常用于加载非窗口的widget。

  * 函数原型：


    
    
    widget_t* ui_loader_load_widget_with_parent (const char* name, widget_t* parent);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 返回widget对象。  
name | const char* | 资源名。  
parent | widget_t* | 父控件对象。
