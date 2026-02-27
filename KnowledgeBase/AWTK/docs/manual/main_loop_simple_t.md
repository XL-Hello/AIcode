## main_loop_simple_t

### 概述

![image](images/main_loop_simple_t_0.png)

## 简单的主循环。

### 函数

函数名称 | 说明  
---|---  
main_loop_post_key_event | 发送按键事件。  
main_loop_post_multi_gesture_event | 发送多点触控事件。  
main_loop_post_pointer_event | 发送指针事件。  
main_loop_post_touch_event | 发送触摸事件。  
main_loop_simple_init | 初始化main_loop_simple_t对象。  
main_loop_simple_reset | 销毁main_loop_simple_t对象。  
  
#### main_loop_post_key_event 函数

* * *

  * 函数功能：



> 发送按键事件。

  * 函数原型：


    
    
    ret_t main_loop_post_key_event (main_loop_t* l, bool_t pressed, uint8_t key);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | 主循环对象。  
pressed | bool_t | 是否按下。  
key | uint8_t | 按键。  
  
#### main_loop_post_multi_gesture_event 函数

* * *

  * 函数功能：



> 发送多点触控事件。

  * 函数原型：


    
    
    ret_t main_loop_post_multi_gesture_event (main_loop_t* l, multi_gesture_event_t* event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | 主循环对象。  
event | multi_gesture_event_t* | 事件。  
  
#### main_loop_post_pointer_event 函数

* * *

  * 函数功能：



> 发送指针事件。

  * 函数原型：


    
    
    ret_t main_loop_post_pointer_event (main_loop_t* l, bool_t pressed, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | 主循环对象。  
pressed | bool_t | 是否按下。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### main_loop_post_touch_event 函数

* * *

  * 函数功能：



> 发送触摸事件。

  * 函数原型：


    
    
    ret_t main_loop_post_touch_event (main_loop_t* l, event_type_t event_type, xy_t x, xy_t y);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | 主循环对象。  
event_type | event_type_t | 事件类型(EVT_TOUCH_DOWN/EVT_TOUCH_UP/EVT_TOUCH_MOVE)。  
x | xy_t | x坐标。  
y | xy_t | y坐标。  
  
#### main_loop_simple_init 函数

* * *

  * 函数功能：



> 初始化main_loop_simple_t对象。

  * 函数原型：


    
    
    main_loop_simple_t* main_loop_simple_init (int w, int h, main_loop_queue_event_t queue_event, main_loop_recv_event_t recv_event);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | main_loop_simple_t* | 返回main_loop_simple_t对象。  
w | int | 宽度。  
h | int | 高度。  
queue_event | main_loop_queue_event_t | 队列事件处理函数。  
recv_event | main_loop_recv_event_t | 接收事件处理函数。  
  
#### main_loop_simple_reset 函数

* * *

  * 函数功能：



> 销毁main_loop_simple_t对象。

  * 函数原型：


    
    
    ret_t main_loop_simple_reset (main_loop_simple_t* loop);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
loop | main_loop_simple_t* | main_loop_simple_t对象。
