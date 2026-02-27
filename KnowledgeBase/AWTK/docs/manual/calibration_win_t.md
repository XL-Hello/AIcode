## calibration_win_t

### 概述

![image](images/calibration_win_t_0.png)

电阻屏校准窗口。

calibration_win_t是[window_base_t](window_base_t.html)的子类控件， window_base_t的函数均适用于calibration_win_t控件。

在xml中使用”calibration_win”标签创建电阻屏校准窗口。如：
    
    
    <calibration_win name="cali" w="100%" h="100%" text="Please click the center of cross">
    </calibration_win>
    

> 更多用法请参考： [window.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/calibration_win.xml)

在c代码中使用函数calibration_win_create创建窗口。如：
    
    
    widget_t* win = calibration_win_create(NULL, 0, 0, 320, 480);
    

## 通过calibration_win_set_on_done注册回调函数，用于保存校准数据。

### 函数

函数名称 | 说明  
---|---  
calibration_win_cast | 转换为calibration_win对象(供脚本语言使用)。  
calibration_win_create | 创建calibration_win对象  
calibration_win_get_widget_vtable | 获取 calibration_win 虚表。  
calibration_win_set_on_click | 设置校准点击事件的处理函数。  
calibration_win_set_on_done | 设置校准完成的处理函数。  
  
#### calibration_win_cast 函数

* * *

  * 函数功能：



> 转换为calibration_win对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* calibration_win_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | calibration_win对象。  
widget | widget_t* | calibration_win对象。  
  
#### calibration_win_create 函数

* * *

  * 函数功能：



> 创建calibration_win对象

  * 函数原型：


    
    
    widget_t* calibration_win_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### calibration_win_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 calibration_win 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* calibration_win_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 calibration_win 虚表。  
  
#### calibration_win_set_on_click 函数

* * *

  * 函数功能：



> 设置校准点击事件的处理函数。

  * 函数原型：


    
    
    ret_t calibration_win_set_on_click (widget_t* widget, calibration_win_on_click_t on_click, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
on_click | calibration_win_on_click_t | 回调函数。  
ctx | void* | 回调函数的上下文。  
  
#### calibration_win_set_on_done 函数

* * *

  * 函数功能：



> 设置校准完成的处理函数。

  * 函数原型：


    
    
    ret_t calibration_win_set_on_done (widget_t* widget, calibration_win_on_done_t on_done, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | widget对象。  
on_done | calibration_win_on_done_t | 回调函数。  
ctx | void* | 回调函数的上下文。
