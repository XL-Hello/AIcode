## candidates_t

### 概述

![image](images/candidates_t_0.png)

输入法候选字词控件。

如果希望启用用数字选择对应的候选字，请设置属性grab_keys=”true”。如：
    
    
    <candidates x="0" y="0" w="100%" h="30" grab_keys="true"/>
    

> 相关文件： assets/default/raw/ui/kb_default.xml

如果希望通过左右键切换不同的候选字，除了设置属性grab_keys=”true”，还需要设置按钮的focused状态的style。
    
    
    <style name="candidates" text_color="black">
    <normal  />
    <pressed    bg_color="#c0c0c0" border_color="#a0a0a0"/>
    <over       bg_color="#e0e0e0" border_color="#a0a0a0"/>
    <focused    border_color="#a0a0a0"/>
    </style>
    

## >相关文件：assets/default/raw/styles/keyboard.xml

### 函数

函数名称 | 说明  
---|---  
candidates_cast | 转换为candidates对象(供脚本语言使用)。  
candidates_create | 创建candidates对象  
candidates_get_widget_vtable | 获取 candidates 虚表。  
candidates_set_auto_hide | 设置是否自动隐藏。  
candidates_set_button_style | 设置按钮的style名称。  
candidates_set_pre | 设置是否为预候选字列表。  
candidates_set_select_by_num | 设置是否启用用数字选择候选字。  
candidates_set_visible_num | 设置可见候选词个数。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
auto_hide | bool_t | 没有候选字时，是否自动隐藏控件。  
button_style | char* | 按钮的style名称。  
enable_preview | bool_t | 是否启用候选字预览。  
pre | bool_t | 是否为预候选字。  
select_by_num | bool_t | 是否启用用数字选择候选字。比如按下1选择第1个候选字，按下2选择第2个候选字。  
visible_num | uint32_t | 候选字可见个数。  
  
#### candidates_cast 函数

* * *

  * 函数功能：



> 转换为candidates对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* candidates_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | candidates对象。  
widget | widget_t* | candidates对象。  
  
#### candidates_create 函数

* * *

  * 函数功能：



> 创建candidates对象

  * 函数原型：


    
    
    widget_t* candidates_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### candidates_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 candidates 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* candidates_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 candidates 虚表。  
  
#### candidates_set_auto_hide 函数

* * *

  * 函数功能：



> 设置是否自动隐藏。

  * 函数原型：


    
    
    ret_t candidates_set_auto_hide (widget_t* widget, bool_t auto_hide);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
auto_hide | bool_t | 是否自动隐藏。  
  
#### candidates_set_button_style 函数

* * *

  * 函数功能：



> 设置按钮的style名称。

  * 函数原型：


    
    
    ret_t candidates_set_button_style (widget_t* widget, const char* button_style);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
button_style | const char* | 按钮的style名称。  
  
#### candidates_set_pre 函数

* * *

  * 函数功能：



> 设置是否为预候选字列表。
> 
> 为预候选字列表则注册EVT_IM_SHOW_PRE_CANDIDATES，否则注册EVT_IM_SHOW_CANDIDATES事件。

  * 函数原型：


    
    
    ret_t candidates_set_pre (widget_t* widget, bool_t pre);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
pre | bool_t | 是否为预候选字列表。  
  
#### candidates_set_select_by_num 函数

* * *

  * 函数功能：



> 设置是否启用用数字选择候选字。

  * 函数原型：


    
    
    ret_t candidates_set_select_by_num (widget_t* widget, bool_t select_by_num);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
select_by_num | bool_t | 是否启用用数字选择候选字。  
  
#### candidates_set_visible_num 函数

* * *

  * 函数功能：



> 设置可见候选词个数。

  * 函数原型：


    
    
    ret_t candidates_set_visible_num (widget_t* widget, uint32_t visible_num);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
widget | widget_t* | 控件对象。  
visible_num | uint32_t | 可见个数。  
  
#### auto_hide 属性

* * *

> 没有候选字时，是否自动隐藏控件。

  * 类型：bool_t

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
  
#### button_style 属性

* * *

> 按钮的style名称。

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
  
#### enable_preview 属性

* * *

> 是否启用候选字预览。

  * 类型：bool_t

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
  
#### pre 属性

* * *

> 是否为预候选字。
> 
> 预候选字: 在有的输入法中，比如T9硬键盘输入时，按下12两个键时，预候选字会显示可用的拼音列表。 从预候选字列表中选择拼音，再查询拼音对应的候选字列表。

  * 类型：bool_t

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
  
#### select_by_num 属性

* * *

> 是否启用用数字选择候选字。比如按下1选择第1个候选字，按下2选择第2个候选字。

  * 类型：bool_t

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
  
#### visible_num 属性

* * *

> 候选字可见个数。

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
