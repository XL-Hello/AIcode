## dialog_client_t

### 概述

![image](images/dialog_client_t_0.png)

对话框客户区控件。

它本身不提供布局功能，仅提供具有语义的标签，让xml更具有可读性。 子控件的布局可用layout_children属性指定。 请参考[布局参数](https://github.com/zlgopen/awtk/blob/master/docs/layout.html)。

dialog_client_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于dialog_client_t控件。

在xml中使用”dialog_client”标签创建dialog_client。如：
    
    
    <dialog anim_hint="center_scale(duration=300)" x="c" y="m" w="80%" h="160" text="Dialog">
    <dialog_title x="0" y="0" w="100%" h="30" text="Hello AWTK" />
    <dialog_client x="0" y="bottom" w="100%" h="-30">
    <label name="" x="center" y="middle:-20" w="200" h="30" text="Are you ready?"/>
    <button name="quit" x="10" y="bottom:10" w="40%" h="30" text="确定"/>
    <button name="quit" x="right:10" y="bottom:10" w="40%" h="30" text="取消"/>
    </dialog_client>
    </dialog>
    

## 在c代码中，用dialog_create_simple创建对话框时，自动创建dialog客户区对象。

### 函数

函数名称 | 说明  
---|---  
dialog_client_cast | 转换为dialog_client对象(供脚本语言使用)。  
dialog_client_create | 创建dialog客户区对象。  
dialog_client_get_widget_vtable | 获取 dialog_client 虚表。  
  
#### dialog_client_cast 函数

* * *

  * 函数功能：



> 转换为dialog_client对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* dialog_client_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | dialog_client对象。  
widget | widget_t* | dialog_client对象。  
  
#### dialog_client_create 函数

* * *

  * 函数功能：



> 创建dialog客户区对象。

  * 函数原型：


    
    
    widget_t* dialog_client_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | dialog对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### dialog_client_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 dialog_client 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* dialog_client_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 dialog_client 虚表。
