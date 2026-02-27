## tk_dl_t

### 概述

## 动态链接库对象。

### 函数

函数名称 | 说明  
---|---  
tk_dl_close | 关闭dl对象。  
tk_dl_error | 获取最后的错误信息。  
tk_dl_open | 打开动态链接库。  
tk_dl_sym | 获取指定名称函数的地址。  
  
#### tk_dl_close 函数

* * *

  * 函数功能：



> 关闭dl对象。

  * 函数原型：


    
    
    ret_t tk_dl_close (tk_dl_t* dl);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
dl | tk_dl_t* | dl对象。  
  
#### tk_dl_error 函数

* * *

  * 函数功能：



> 获取最后的错误信息。

  * 函数原型：


    
    
    const char* tk_dl_error ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const char* | 返回error message.  
  
#### tk_dl_open 函数

* * *

  * 函数功能：



> 打开动态链接库。

  * 函数原型：


    
    
    tk_dl_t* tk_dl_open (const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_dl_t* | 动态链接库对象。  
filename | const char* | 文件名。  
  
#### tk_dl_sym 函数

* * *

  * 函数功能：



> 获取指定名称函数的地址。

  * 函数原型：


    
    
    void* tk_dl_sym (tk_dl_t* dl, const char* name);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void* | 返回函数的地址。  
dl | tk_dl_t* | dl对象。  
name | const char* | 函数名。
