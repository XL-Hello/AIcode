## main_loop_t

### 概述

## 主循环接口。

### 函数

函数名称 | 说明  
---|---  
main_loop | 获取当前main_loop对象  
main_loop_add_event_source | 添加event_source。  
main_loop_destroy | 销毁main_loop对象。  
main_loop_get_event_source_manager | 获取event source manager  
main_loop_queue_event | 将事件加入到事件队列。  
main_loop_quit | 退出主循环。  
main_loop_recv_event | 从事件队列中获取事件。  
main_loop_remove_event_source | 删除event_source。  
main_loop_remove_event_source_by_tag | 删除event_source。  
main_loop_run | 运行主循环。  
main_loop_set | 设置当前main_loop对象  
main_loop_step | 执行一次迭代。  
main_loop_wakeup | 唤醒主循环。  
  
#### main_loop 函数

* * *

  * 函数功能：



> 获取当前main_loop对象

  * 函数原型：


    
    
    main_loop_t* main_loop ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | main_loop_t* | 返回main_loop对象。  
  
#### main_loop_add_event_source 函数

* * *

  * 函数功能：



> 添加event_source。

  * 函数原型：


    
    
    ret_t main_loop_add_event_source (main_loop_t* l, event_source_t* source);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
source | event_source_t* | event_source对象。  
  
#### main_loop_destroy 函数

* * *

  * 函数功能：



> 销毁main_loop对象。

  * 函数原型：


    
    
    ret_t main_loop_destroy (main_loop_t* l);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
  
#### main_loop_get_event_source_manager 函数

* * *

  * 函数功能：



> 获取event source manager

  * 函数原型：


    
    
    event_source_manager_t* main_loop_get_event_source_manager (main_loop_t* l);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | event_source_manager_t* | 返回event source manager对象。  
l | main_loop_t* | main_loop对象。  
  
#### main_loop_queue_event 函数

* * *

  * 函数功能：



> 将事件加入到事件队列。

  * 函数原型：


    
    
    ret_t main_loop_queue_event (main_loop_t* l, const event_queue_req_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
e | const event_queue_req_t* | 事件。  
  
#### main_loop_quit 函数

* * *

  * 函数功能：



> 退出主循环。

  * 函数原型：


    
    
    ret_t main_loop_quit (main_loop_t* l);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
  
#### main_loop_recv_event 函数

* * *

  * 函数功能：



> 从事件队列中获取事件。

  * 函数原型：


    
    
    ret_t main_loop_recv_event (main_loop_t* l, event_queue_req_t* r);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
r | event_queue_req_t* | 事件。  
  
#### main_loop_remove_event_source 函数

* * *

  * 函数功能：



> 删除event_source。

  * 函数原型：


    
    
    ret_t main_loop_remove_event_source (main_loop_t* l, event_source_t* source);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
source | event_source_t* | event_source对象。  
  
#### main_loop_remove_event_source_by_tag 函数

* * *

  * 函数功能：



> 删除event_source。

  * 函数原型：


    
    
    ret_t main_loop_remove_event_source_by_tag (main_loop_t* l, void* tag);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
tag | void* | tag。  
  
#### main_loop_run 函数

* * *

  * 函数功能：



> 运行主循环。

  * 函数原型：


    
    
    ret_t main_loop_run (main_loop_t* l);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
  
#### main_loop_set 函数

* * *

  * 函数功能：



> 设置当前main_loop对象

  * 函数原型：


    
    
    ret_t main_loop_set (main_loop_t* loop);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
loop | main_loop_t* | main_loop对象。  
  
#### main_loop_step 函数

* * *

  * 函数功能：



> 执行一次迭代。

  * 函数原型：


    
    
    ret_t main_loop_step (main_loop_t* l);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。  
  
#### main_loop_wakeup 函数

* * *

  * 函数功能：



> 唤醒主循环。

  * 函数原型：


    
    
    ret_t main_loop_wakeup (main_loop_t* l);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
l | main_loop_t* | main_loop对象。
