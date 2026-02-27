## ui_binary_writer_t

### 概述

![image](images/ui_binary_writer_t_0.png)

## 生成二进制格式的UI描述数据。

### 函数

函数名称 | 说明  
---|---  
ui_binary_writer_init | 初始化ui_binary_writer对象。  
  
#### ui_binary_writer_init 函数

* * *

  * 函数功能：



> 初始化ui_binary_writer对象。

  * 函数原型：


    
    
    ui_builder_t* ui_binary_writer_init (ui_binary_writer_t* writer, wbuffer_t* wbuffer);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ui_builder_t* | 返回ui\\_builder对象。  
writer | ui_binary_writer_t* | writer对象。  
wbuffer | wbuffer_t* | 保存结果的buffer。
