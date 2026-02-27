## tk_ostream_serial_t

### 概述

基于串口实现的输出流。

## input stream base on fd

### 函数

函数名称 | 说明  
---|---  
tk_ostream_serial_create | 创建ostream对象。  
  
#### tk_ostream_serial_create 函数

* * *

  * 函数功能：



> 创建ostream对象。

  * 函数原型：


    
    
    tk_ostream_t* tk_ostream_serial_create (serial_handle_t fd);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_ostream_t* | 返回ostream对象。  
fd | serial_handle_t | fd.
