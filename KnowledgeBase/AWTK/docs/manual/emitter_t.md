## emitter_t

### 概述

## 事件分发器, 用于实现观察者模式。

### 函数

函数名称 | 说明  
---|---  
emitter_cast | 转换为emitter对象(供脚本语言使用)。  
emitter_create | 创建emitter对象。  
emitter_deinit | 析构。  
emitter_destroy | 销毁。  
emitter_disable | 禁用。  
emitter_dispatch | 分发事件。如果当前分发的回调函数返回RET_REMOVE，该回调函数将被移出。  
emitter_dispatch_simple_event | 分发事件。  
emitter_enable | 启用。  
emitter_exist | 判断指定的事件和回调函数是否已经注册。  
emitter_find | 通过ID查找emitter_item_t，主要用于辅助测试。  
emitter_forward | 分发事件  
emitter_forward_retarget | 分发事件。并将e->target强制设置为ctx。  
emitter_init | 初始化emitter对象。  
emitter_off | 注销指定事件的处理函数。  
emitter_off_by_ctx | 注销指定事件的处理函数。  
emitter_off_by_func | 注销指定事件的处理函数。  
emitter_off_by_tag | 注销指定事件的处理函数。  
emitter_on | 注册指定事件的处理函数。  
emitter_on_with_tag | 注册指定事件的处理函数。  
emitter_set_on_destroy | 设置一个回调函数，在emitter被销毁时调用(方便脚本语言去释放回调函数)。  
emitter_size | 获取注册的回调函数个数，主要用于辅助测试。  
  
### 属性

属性名称 | 类型 | 说明  
---|---|---  
disable | int32_t | 禁用标志。禁用时dispatch无效。  
  
#### emitter_cast 函数

* * *

  * 函数功能：



> 转换为emitter对象(供脚本语言使用)。

主要给脚本语言使用。

  * 函数原型：


    
    
    emitter_t* emitter_cast (emitter_t* emitter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | emitter_t* | 对象。  
emitter | emitter_t* | emitter对象。  
  
#### emitter_create 函数

* * *

  * 函数功能：



> 创建emitter对象。

  * 函数原型：


    
    
    emitter_t* emitter_create ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | emitter_t* | 对象。  
  
#### emitter_deinit 函数

* * *

  * 函数功能：



> 析构。

  * 函数原型：


    
    
    ret_t emitter_deinit (emitter_t* emitter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
  
#### emitter_destroy 函数

* * *

  * 函数功能：



> 销毁。

  * 函数原型：


    
    
    ret_t emitter_destroy (emitter_t* emitter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
  
#### emitter_disable 函数

* * *

  * 函数功能：



> 禁用。

禁用后emitter_dispatch无效，但可以注册和注销。

  * 函数原型：


    
    
    ret_t emitter_disable (emitter_t* emitter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
  
#### emitter_dispatch 函数

* * *

  * 函数功能：



> 分发事件。如果当前分发的回调函数返回RET_REMOVE，该回调函数将被移出。 禁用状态下，本函数不做任何事情。

  * 函数原型：


    
    
    ret_t emitter_dispatch (emitter_t* emitter, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 如果当前分发的回调函数返回RET_STOP，dispatch中断分发，并返回RET_STOP，否则返回RET_OK。  
emitter | emitter_t* | emitter对象。  
e | event_t* | 事件对象。  
  
#### emitter_dispatch_simple_event 函数

* * *

  * 函数功能：



> 分发事件。 对emitter_dispatch的包装，分发一个简单的事件。 如果当前分发的回调函数返回RET_STOP，dispatch中断分发，并返回RET_STOP，否则返回RET_OK。

  * 函数原型：


    
    
    ret_t emitter_dispatch_simple_event (emitter_t* emitter, uint32_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t |   
emitter | emitter_t* | emitter对象。  
type | uint32_t | 事件类型。  
  
#### emitter_enable 函数

* * *

  * 函数功能：



> 启用。

  * 函数原型：


    
    
    ret_t emitter_enable (emitter_t* emitter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
  
#### emitter_exist 函数

* * *

  * 函数功能：



> 判断指定的事件和回调函数是否已经注册。

  * 函数原型：


    
    
    bool_t emitter_exist (emitter_t* emitter, uint32_t etype, event_func_t handler, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示已经注册，否则表示没有注册。  
emitter | emitter_t* | emitter对象。  
etype | uint32_t | 事件类型。  
handler | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### emitter_find 函数

* * *

  * 函数功能：



> 通过ID查找emitter_item_t，主要用于辅助测试。

  * 函数原型：


    
    
    emitter_item_t* emitter_find (emitter_t* emitter, uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | emitter_item_t* | 若存在,返回id对应的emitter_item_t，否则返回NULL。  
emitter | emitter_t* | emitter对象。  
id | uint32_t | emitter_on返回的ID。  
  
#### emitter_forward 函数

* * *

  * 函数功能：



> 分发事件

  * 函数原型：


    
    
    ret_t emitter_forward (void* ctx, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ctx | void* | emitter对象。  
e | event_t* | 分发的事件。  
  
#### emitter_forward_retarget 函数

* * *

  * 函数功能：



> 分发事件。并将e->target强制设置为ctx。

  * 函数原型：


    
    
    ret_t emitter_forward_retarget (void* ctx, event_t* e);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
ctx | void* | emitter对象。  
e | event_t* | 分发的事件。  
  
#### emitter_init 函数

* * *

  * 函数功能：



> 初始化emitter对象。

  * 函数原型：


    
    
    emitter_t* emitter_init (emitter_t* emitter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | emitter_t* | 对象。  
emitter | emitter_t* | emitter对象。  
  
#### emitter_off 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t emitter_off (emitter_t* emitter, uint32_t id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
id | uint32_t | emitter_on返回的ID。  
  
#### emitter_off_by_ctx 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t emitter_off_by_ctx (emitter_t* emitter, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
ctx | void* | 事件处理函数上下文。  
  
#### emitter_off_by_func 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t emitter_off_by_func (emitter_t* emitter, uint32_t etype, event_func_t handler, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
etype | uint32_t | 事件类型。  
handler | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### emitter_off_by_tag 函数

* * *

  * 函数功能：



> 注销指定事件的处理函数。

  * 函数原型：


    
    
    ret_t emitter_off_by_tag (emitter_t* emitter, uint32_t tag);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
tag | uint32_t | tag。  
  
#### emitter_on 函数

* * *

  * 函数功能：



> 注册指定事件的处理函数。

  * 函数原型：


    
    
    uint32_t emitter_on (emitter_t* emitter, uint32_t etype, event_func_t handler, void* ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于emitter_off。  
emitter | emitter_t* | emitter对象。  
etype | uint32_t | 事件类型。  
handler | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
  
#### emitter_on_with_tag 函数

* * *

  * 函数功能：



> 注册指定事件的处理函数。

  * 函数原型：


    
    
    uint32_t emitter_on_with_tag (emitter_t* emitter, uint32_t etype, event_func_t handler, void* ctx, uint32_t tag);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 返回id，用于emitter_off。  
emitter | emitter_t* | emitter对象。  
etype | uint32_t | 事件类型。  
handler | event_func_t | 事件处理函数。  
ctx | void* | 事件处理函数上下文。  
tag | uint32_t | tag。  
  
#### emitter_set_on_destroy 函数

* * *

  * 函数功能：



> 设置一个回调函数，在emitter被销毁时调用(方便脚本语言去释放回调函数)。

  * 函数原型：


    
    
    ret_t emitter_set_on_destroy (emitter_t* emitter, uint32_t id, tk_destroy_t on_destroy, void* on_destroy_ctx);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
emitter | emitter_t* | emitter对象。  
id | uint32_t | emitter_on返回的ID。  
on_destroy | tk_destroy_t | 回调函数。  
on_destroy_ctx | void* | 回调函数上下文。  
  
#### emitter_size 函数

* * *

  * 函数功能：



> 获取注册的回调函数个数，主要用于辅助测试。

  * 函数原型：


    
    
    uint32_t emitter_size (emitter_t* emitter);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint32_t | 回调函数个数。  
emitter | emitter_t* | emitter对象。  
  
#### disable 属性

* * *

> 禁用标志。禁用时dispatch无效。

  * 类型：int32_t

特性 | 是否支持  
---|---  
可直接读取 | 是  
可直接修改 | 否
