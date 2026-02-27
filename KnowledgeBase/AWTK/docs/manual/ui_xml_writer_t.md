## ui_xml_writer_t

### 概述

![image](images/ui_xml_writer_t_0.png)

## 生成XML格式的UI描述数据。

### 函数

函数名称 | 说明  
---|---  
ui_xml_writer_init | 初始化ui_xml_writer对象。  
  
#### ui_xml_writer_init 函数

* * *

  * 函数功能：



> 初始化ui_xml_writer对象。

  * 函数原型：


    
    
    ui_builder_t* ui_xml_writer_init (ui_xml_writer_t* writer, str_t* str);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ui_builder_t* | 返回ui\\_builder对象。  
writer | ui_xml_writer_t* | writer对象。  
str | str_t* | 保存结果的str。
