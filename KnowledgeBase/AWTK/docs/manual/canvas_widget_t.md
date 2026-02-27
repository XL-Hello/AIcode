## canvas_widget_t

### 概述

![image](images/canvas_widget_t_0.png)

画布控件。

画布控件让开发者可以自己在控件上绘制需要的内容。

canvas_widget_t是[widget_t](widget_t.html)的子类控件，widget_t的函数均适用于canvas_widget_t控件。

在xml中使用”canvas”标签创建画布控件。如：
    
    
    <canvas name="paint_vgcanvas" x="0" y="0" w="100%" h="100%" />
    

> 更多用法请参考： [canvas_widget.xml](https://github.com/zlgopen/awtk/blob/master/design/default/ui/vgcanvas.xml)

在c代码中使用函数canvas_widget_create创建画布控件。如：
    
    
    widget_t* canvas = canvas_widget_create(win, 0, 0, win->w, win->h);
    

> 创建之后，需要用widget_on注册EVT_PAINT事件，并在EVT_PAINT事件处理函数中绘制。
    
    
    widget_on(canvas, EVT_PAINT, on_paint_event, canvas);
    

绘制时，可以通过canvas接口去绘制，也可以通过vgcanvas接口去绘制。 先从evt获取canvas对象，再通过canvas_get_vgcanvas从canvas中获取vgcanvas对象。
    
    
    static ret_t on_paint_event(void* ctx, event_t* evt) {
    widget_t* canvas_widget = WIDGET(ctx);
    canvas_t* c = paint_event_cast(evt)->c;
    vgcanvas_t* vg = canvas_get_vgcanvas(c);
    color_t bg = color_init(0xe0, 0xe0, 0xe0, 0xff);
    color_t tc = color_init(0, 0, 0, 0xff);
    rect_t r = rect_init(canvas_widget->x, canvas_widget->y, canvas_widget->w, canvas_widget->h);
    
    vgcanvas_save(vg);
    vgcanvas_clip_rect(vg, r.x, r.y, r.w, r.h);
    vgcanvas_translate(vg, r.x, r.y);
    
    ...
    
    vgcanvas_restore(vg);
    
    return RET_OK;
    }
    

> 完整示例请参考： [canvas demo](https://github.com/zlgopen/awtk-c-demos/blob/master/demos/canvas.c)

参考：

  * [canvas接口描述](canvas_t.html)
  * [vgcanvas接口描述](vgcanvas_t.html)



* * *

### 函数

函数名称 | 说明  
---|---  
canvas_widget_cast | 转换为canvas_widget对象(供脚本语言使用)。  
canvas_widget_create | 创建canvas_widget对象  
canvas_widget_get_widget_vtable | 获取 canvas_widget 虚表。  
  
#### canvas_widget_cast 函数

* * *

  * 函数功能：



> 转换为canvas_widget对象(供脚本语言使用)。

  * 函数原型：


    
    
    widget_t* canvas_widget_cast (widget_t* widget);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | canvas_widget对象。  
widget | widget_t* | canvas_widget对象。  
  
#### canvas_widget_create 函数

* * *

  * 函数功能：



> 创建canvas_widget对象

  * 函数原型：


    
    
    widget_t* canvas_widget_create (widget_t* parent, xy_t x, xy_t y, wh_t w, wh_t h);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | widget_t* | 对象。  
parent | widget_t* | 父控件  
x | xy_t | x坐标  
y | xy_t | y坐标  
w | wh_t | 宽度  
h | wh_t | 高度  
  
#### canvas_widget_get_widget_vtable 函数

* * *

  * 函数功能：



> 获取 canvas_widget 虚表。

  * 函数原型：


    
    
    const widget_vtable_t* canvas_widget_get_widget_vtable ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | const widget_vtable_t* | 成功返回 canvas_widget 虚表。
