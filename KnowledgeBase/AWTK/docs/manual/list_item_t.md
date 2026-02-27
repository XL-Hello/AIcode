## list_item_t

### 概述

![image](images/list_item_t_0.png)

列表项控件。

列表项控件是一个简单的容器控件，一般作为列表视图中滚动视图的子控件。

list_item_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于list_item_t控件。

在xml中使用”list_item”标签创建列表项控件。如：
    
    
    <list_view x="0"  y="30" w="100%" h="-80" item_height="60">
    <scroll_view name="view" x="0"  y="0" w="100%" h="100%">
    <list_item style="odd" children_layout="default(rows=1,cols=0)">
    <image draw_type="icon" w="30" image="earth"/>
    <label w="-30" text="1.Hello AWTK !">
    <switch x="r:10" y="m" w="60" h="20"/>
    </label>
    </list_item>
    ...
    </scroll_view>
    </list_view>
    

> 更多用法请参考：[list_view_m.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/list_view_m.xml)

在c代码中使用函数list_item_create创建列表项控件。如：
    
    
    widget_t* list_item = list_item_create(scroll_view, 0, 0, 0, 0);
    

> 列表项控件大小一般由列表控制，不需指定xywh参数。

可以用style来实现可点击或不可点击的效果。如：
    
    
    <style name="odd_clickable" border_color="#a0a0a0"  border="bottom" text_color="black">
    <normal     bg_color="#f5f5f5" />
    <pressed    bg_color="#c0c0c0" />
    <over       bg_color="#f5f5f5" />
    </style>
    

> 更多用法请参考：[theme default](https://github.com/zlgopen/awtk/blob/master/design/default/styles/default.xml#L372)

* * *

### 函数

函数名称 | 说明  
---|---  
list_item_cast | 转换为list_item对象(供脚本语言使用)。  
list_item_create | 创建list_item对象  
list_item_get_widget_vtable | 获取 list_item 虚表。  
  
### 事件

事件名称 | 类型 | 说明  
---|---|---  
EVT_CLICK | pointer_event_t | 点击事件。  
  
#### list_item_cast 函数

* * *

  * 函数功能：



> 转换为list_item对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* list_item_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | list_item对象。  
widget | widget_t* | list_item对象。  
  
#### list_item_create 函数

* * *

  * 函数功能：



> 创建list_item对象

  * 函数原型：


    
    
    widget_t* list_item_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### list_item_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 list_item 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* list_item_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 list_item 虚表。
