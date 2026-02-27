## serial_widget_t

### 概述

![image](images/serial_widget_t_0.png)

用于串口通信的控件 在xml中使用”serial”标签创建控件。如：
    
    
    <!-- ui -->
    <serial device="COM1" baudrate="115200"/>
    

可用通过style来设置控件的显示风格，如字体的大小和颜色等等。如：

> 本控件默认不可见，无需指定style。
    
    
    <!-- style -->
    <serial>
    <style name="default" font_size="32">
    <normal text_color="black" />
    </style>
    </serial>
    

* * *

### 函数

函数名称 | 说明  
---|---  
serial_widget_cast | 转换为serial_widget对象(供脚本语言使用)。  
serial_widget_create | 创建serial_widget对象  
serial_widget_get_widget_vtable | 获取 serial_widget 虚表。  
serial_widget_set_baudrate | 设置 波特率。  
serial_widget_set_bytesize | 设置 字节位数。  
serial_widget_set_check_interval | 设置 轮询时间(毫秒)。  
serial_widget_set_device | 设置 设备。  
serial_widget_set_flowcontrol | 设置 流控。  
serial_widget_set_parity | 设置 奇偶校验。  
serial_widget_set_stopbits | 设置 停止位。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
baudrate | uint32_t | 波特率。  
bytesize | uint32_t | 字节位数。  
check_interval | uint32_t | 轮询时间（单位：ms）。  
device | char* | 设备(文件)名。  
flowcontrol | uint32_t | 流控。  
iostream | tk_iostream_t* | 输入/出流。  
istream | tk_istream_t* | 输入流。  
ostream | tk_ostream_t* | 输出流。  
parity | uint32_t | 奇偶校验。  
stopbits | uint32_t | 停止位。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_DATA | event_t | 数据到来事件。  
  
#### serial_widget_cast 函数

* * *

  * 函数功能：



> 转换为serial_widget对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* serial_widget_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | serial_widget对象。  
widget | widget_t* | serial_widget对象。  
  
#### serial_widget_create 函数

* * *

  * 函数功能：



> 创建serial_widget对象

  * 函数原型：


    
    
    widget_t* serial_widget_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | serial_widget对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### serial_widget_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 serial_widget 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* serial_widget_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 serial_widget 虚表。  
  
#### serial_widget_set_baudrate 函数

* * *

  * 函数功能：



> 设置 波特率。

  * 函数原型：


    
    
    ret_t serial_widget_set_baudrate (widget_t* widget, uint32_t baudrate);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
baudrate | uint32_t | 波特率。  
  
#### serial_widget_set_bytesize 函数

* * *

  * 函数功能：



> 设置 字节位数。

  * 函数原型：


    
    
    ret_t serial_widget_set_bytesize (widget_t* widget, uint32_t bytesize);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
bytesize | uint32_t | 字节位数。  
  
#### serial_widget_set_check_interval 函数

* * *

  * 函数功能：



> 设置 轮询时间(毫秒)。

  * 函数原型：


    
    
    ret_t serial_widget_set_check_interval (widget_t* widget, uint32_t check_interval);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
check_interval | uint32_t | 轮询时间（单位：ms）。  
  
#### serial_widget_set_device 函数

* * *

  * 函数功能：



> 设置 设备。

  * 函数原型：


    
    
    ret_t serial_widget_set_device (widget_t* widget, const char* device);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
device | const char* | 设备。  
  
#### serial_widget_set_flowcontrol 函数

* * *

  * 函数功能：



> 设置 流控。

  * 函数原型：


    
    
    ret_t serial_widget_set_flowcontrol (widget_t* widget, uint32_t flowcontrol);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
flowcontrol | uint32_t | 流控。  
  
#### serial_widget_set_parity 函数

* * *

  * 函数功能：



> 设置 奇偶校验。

  * 函数原型：


    
    
    ret_t serial_widget_set_parity (widget_t* widget, uint32_t parity);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
parity | uint32_t | 奇偶校验。  
  
#### serial_widget_set_stopbits 函数

* * *

  * 函数功能：



> 设置 停止位。

  * 函数原型：


    
    
    ret_t serial_widget_set_stopbits (widget_t* widget, uint32_t stopbits);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
stopbits | uint32_t | 停止位。  
  
#### baudrate 属性

* * *

> 波特率。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### bytesize 属性

* * *

> 字节位数。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### check_interval 属性

* * *

> 轮询时间（单位：ms）。 仅在不支持用select等待串口数据的嵌入式设备上有效。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### device 属性

* * *

> 设备(文件)名。

  * 类型：char*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### flowcontrol 属性

* * *

> 流控。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### iostream 属性

* * *

> 输入/出流。

  * 类型：tk_iostream_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### istream 属性

* * *

> 输入流。

  * 类型：tk_istream_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### ostream 属性

* * *

> 输出流。

  * 类型：tk_ostream_t*

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### parity 属性

* * *

> 奇偶校验。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是  
  
#### stopbits 属性

* * *

> 停止位。

  * 类型：uint32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否  
可持久化 | 是  
可脚本化 | 是  
可在IDE中设置 | 是  
可在XML中设置 | 是  
可通过widget_get_prop读取 | 是  
可通过widget_set_prop修改 | 是
