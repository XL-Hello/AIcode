## debugger_t

### 概述

## 调试器接口。

### 函数

函数名称 | 说明  
---|---  
debugger_attach | 附近到指定的代码片段。  
debugger_clear_break_points | 清除全部断点。  
debugger_continue | 执行到下一个断点。  
debugger_deinit | 释放资源。  
debugger_dispatch_messages | dispatch_messages(仅适用于客户端)  
debugger_get_break_points | 获取断点列表。  
debugger_get_callstack | 获取当前线程的callstack。  
debugger_get_callstack_ex | 获取当前线程的callstack。  
debugger_get_code | 获取代码。  
debugger_get_current_frame | 获取当前callstack的frame。  
debugger_get_current_thread_id | 获取当前线程 ID。  
debugger_get_debuggers | 获取调试器列表。  
debugger_get_global | 获取全局对象。  
debugger_get_local | 获取局部变量对象。  
debugger_get_self | 获取self对象。  
debugger_get_state | 获取调试状态。  
debugger_get_threads | 获取线程(仅用于调试原生程序，脚本不支持)。  
debugger_get_var | 获取变量的详细信息。  
debugger_is_paused | 查看当前是否处于暂停状态。  
debugger_is_paused_or_running | 查看当前是否处于暂停运行状态。  
debugger_is_running | 查看当前是否处于运行状态。  
debugger_launch | 执行代码。  
debugger_launch_app | 执行程序(仅用于调试原生程序，脚本不支持)。  
debugger_load_config | 加载配置。  
debugger_lock | 锁定debugger对象。  
debugger_match | 检查code_id是否与当前debugger匹配。  
debugger_pause | 暂停运行。  
debugger_remove_break_point | 清除断点。  
debugger_remove_break_point_ex | 清除断点。  
debugger_restart | 重新运行。  
debugger_set_break_point | 设置断点。  
debugger_set_break_point_ex | 设置断点。  
debugger_set_current_frame | 从callstack中选择当前的frame。  
debugger_set_current_thread_id | 设置当前处于哪个一个线程的上下文中。  
debugger_set_state | 设置状态。  
debugger_step_in | 进入函数。  
debugger_step_loop_over | 执行下一条语句(跳过循环)  
debugger_step_out | 执行到函数结束。  
debugger_step_over | 执行到下一行代码。（不进入函数）  
debugger_stop | 终止程序运行。  
debugger_unlock | 解锁debugger对象。  
debugger_update_code | 更新代码。  
  
#### debugger_attach 函数

* * *

  * 函数功能：



> 附近到指定的代码片段。

  * 函数原型：


    
    
    ret_t debugger_attach (debugger_t* debugger, const char* lang, const char* code_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
lang | const char* | 代码的语言。  
code_id | const char* | 代码的ID。  
  
#### debugger_clear_break_points 函数

* * *

  * 函数功能：



> 清除全部断点。

  * 函数原型：


    
    
    ret_t debugger_clear_break_points (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_continue 函数

* * *

  * 函数功能：



> 执行到下一个断点。 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    ret_t debugger_continue (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_deinit 函数

* * *

  * 函数功能：



> 释放资源。

  * 函数原型：


    
    
    ret_t debugger_deinit (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_dispatch_messages 函数

* * *

  * 函数功能：



> dispatch_messages(仅适用于客户端)

  * 函数原型：


    
    
    ret_t debugger_dispatch_messages (debugger_t* debugger, uint32_t timeout, uint32_t* ret_num);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
timeout | uint32_t | 超时时间(毫秒)。  
ret_num | uint32_t* | 返回处理命令个数。  
  
#### debugger_get_break_points 函数

* * *

  * 函数功能：



> 获取断点列表。

  * 函数原型：


    
    
    ret_t debugger_get_break_points (debugger_t* debugger, binary_data_t* break_points);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
break_points | binary_data_t* | 断点列表(每行一个)。  
  
#### debugger_get_callstack 函数

* * *

  * 函数功能：



> 获取当前线程的callstack。

  * 函数原型：


    
    
    tk_object_t* debugger_get_callstack (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回堆栈信息。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_get_callstack_ex 函数

* * *

  * 函数功能：



> 获取当前线程的callstack。 备注： 1，如果 tk_object_t 的 callstack.#size 返回来的长度小于 levels 的话，就已经全部拿完了。 2，返回值和 debugger_get_callstack 是一样的。

  * 函数原型：


    
    
    tk_object_t* debugger_get_callstack_ex (debugger_t* debugger, uint32_t start, uint32_t levels, uint64_t thread_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回堆栈信息。  
debugger | debugger_t* | debugger对象。  
start | uint32_t | 堆栈 startFrame。  
levels | uint32_t | 堆栈层数。（如果是输入 0 的话，就获取最大层数）  
thread_id | uint64_t | 线程 id。  
  
#### debugger_get_code 函数

* * *

  * 函数功能：



> 获取代码。

  * 函数原型：


    
    
    ret_t debugger_get_code (debugger_t* debugger, binary_data_t* code);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
code | binary_data_t* | 代码。  
  
#### debugger_get_current_frame 函数

* * *

  * 函数功能：



> 获取当前callstack的frame。 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    int32_t debugger_get_current_frame (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int32_t | 成功返回frame序数(0表示当前)，失败返回-1。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_get_current_thread_id 函数

* * *

  * 函数功能：



> 获取当前线程 ID。 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    uint64_t debugger_get_current_thread_id (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | uint64_t | 成功返回线程 ID，失败返回 0。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_get_debuggers 函数

* * *

  * 函数功能：



> 获取调试器列表。

  * 函数原型：


    
    
    ret_t debugger_get_debuggers (debugger_t* debugger, binary_data_t* debuggers);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
debuggers | binary_data_t* | 调试器列表(每行一个)。  
  
#### debugger_get_global 函数

* * *

  * 函数功能：



> 获取全局对象。 处于暂停状态才能执行本命令。 返回数据结构请参考：https://microsoft.github.io/debug-adapter-protocol/specification#Requests_Variables

  * 函数原型：


    
    
    tk_object_t* debugger_get_global (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回全局对象。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_get_local 函数

* * *

  * 函数功能：



> 获取局部变量对象。 返回数据结构请参考：https://microsoft.github.io/debug-adapter-protocol/specification#Requests_Variables 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    tk_object_t* debugger_get_local (debugger_t* debugger, uint32_t frame_index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回局部变量对象。  
debugger | debugger_t* | debugger对象。  
frame_index | uint32_t | frame序数(0开始)。  
  
#### debugger_get_self 函数

* * *

  * 函数功能：



> 获取self对象。 返回数据结构请参考：https://microsoft.github.io/debug-adapter-protocol/specification#Requests_Variables 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    tk_object_t* debugger_get_self (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回self对象。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_get_state 函数

* * *

  * 函数功能：



> 获取调试状态。

  * 函数原型：


    
    
    debugger_program_state_t debugger_get_state (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | debugger_program_state_t | 返回调试状态。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_get_threads 函数

* * *

  * 函数功能：



> 获取线程(仅用于调试原生程序，脚本不支持)。 返回数据结构请参考: https://microsoft.github.io/debug-adapter-protocol/specification#Requests_Threads 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    tk_object_t* debugger_get_threads (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回全局对象。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_get_var 函数

* * *

  * 函数功能：



> 获取变量的详细信息。 返回数据结构请参考：https://microsoft.github.io/debug-adapter-protocol/specification#Requests_Variables
> 
> 处于暂停状态才能执行本命令。 可以为路径，如: * a.name 为结构a下的成员name。 * a.names[1].first为结构a下的成员names数组中第二个元素下的first成员。

  * 函数原型：


    
    
    tk_object_t* debugger_get_var (debugger_t* debugger, const char* path);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | tk_object_t* | 返回全局对象。  
debugger | debugger_t* | debugger对象。  
path | const char* | 变量名或路径。为空或NULL时，返回全部变量。  
  
#### debugger_is_paused 函数

* * *

  * 函数功能：



> 查看当前是否处于暂停状态。

  * 函数原型：


    
    
    bool_t debugger_is_paused (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示处于暂停运行状态。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_is_paused_or_running 函数

* * *

  * 函数功能：



> 查看当前是否处于暂停运行状态。

  * 函数原型：


    
    
    bool_t debugger_is_paused_or_running (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示处于暂停运行状态。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_is_running 函数

* * *

  * 函数功能：



> 查看当前是否处于运行状态。

  * 函数原型：


    
    
    bool_t debugger_is_running (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示处于暂停运行状态。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_launch 函数

* * *

  * 函数功能：



> 执行代码。

  * 函数原型：


    
    
    ret_t debugger_launch (debugger_t* debugger, const char* lang, const binary_data_t* code);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
lang | const char* | 代码的语言。  
code | const binary_data_t* | 代码。  
  
#### debugger_launch_app 函数

* * *

  * 函数功能：



> 执行程序(仅用于调试原生程序，脚本不支持)。

  * 函数原型：


    
    
    ret_t debugger_launch_app (debugger_t* debugger, const char* program, const char* work_dir, int argc, char** argv);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
program | const char* | 程序。  
work_dir | const char* | 工作目录。  
argc | int | 参数个数。  
argv | char** | 参数列表。  
  
#### debugger_load_config 函数

* * *

  * 函数功能：



> 加载配置。

  * 函数原型：


    
    
    ret_t debugger_load_config (debugger_t* debugger, const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger  
filename | const char* | 配置文件名。  
  
#### debugger_lock 函数

* * *

  * 函数功能：



> 锁定debugger对象。

  * 函数原型：


    
    
    ret_t debugger_lock (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_match 函数

* * *

  * 函数功能：



> 检查code_id是否与当前debugger匹配。

  * 函数原型：


    
    
    bool_t debugger_match (debugger_t* debugger, const char* code_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | bool_t | 返回TRUE表示匹配到。  
debugger | debugger_t* | debugger对象。  
code_id | const char* | 代码ID。  
  
#### debugger_pause 函数

* * *

  * 函数功能：



> 暂停运行。 暂停后才能执行next/step_xxx等函数。

  * 函数原型：


    
    
    ret_t debugger_pause (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_remove_break_point 函数

* * *

  * 函数功能：



> 清除断点。

  * 函数原型：


    
    
    ret_t debugger_remove_break_point (debugger_t* debugger, uint32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
line | uint32_t | 代码行号。  
  
#### debugger_remove_break_point_ex 函数

* * *

  * 函数功能：



> 清除断点。

  * 函数原型：


    
    
    ret_t debugger_remove_break_point_ex (debugger_t* debugger, const char* position);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
position | const char* | 位置(函数名或文件名:行号)。  
  
#### debugger_restart 函数

* * *

  * 函数功能：



> 重新运行。

  * 函数原型：


    
    
    ret_t debugger_restart (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_set_break_point 函数

* * *

  * 函数功能：



> 设置断点。

  * 函数原型：


    
    
    ret_t debugger_set_break_point (debugger_t* debugger, uint32_t line);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
line | uint32_t | 代码行号。  
  
#### debugger_set_break_point_ex 函数

* * *

  * 函数功能：



> 设置断点。

  * 函数原型：


    
    
    ret_t debugger_set_break_point_ex (debugger_t* debugger, const char* position);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
position | const char* | 位置(函数名或文件名:行号)。  
  
#### debugger_set_current_frame 函数

* * *

  * 函数功能：



> 从callstack中选择当前的frame。 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    ret_t debugger_set_current_frame (debugger_t* debugger, uint32_t frame_index);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
frame_index | uint32_t | frame序数(0表示当前)  
  
#### debugger_set_current_thread_id 函数

* * *

  * 函数功能：



> 设置当前处于哪个一个线程的上下文中。 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    ret_t debugger_set_current_thread_id (debugger_t* debugger, uint64_t thread_id);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
thread_id | uint64_t | 线程 id  
  
#### debugger_set_state 函数

* * *

  * 函数功能：



> 设置状态。

  * 函数原型：


    
    
    ret_t debugger_set_state (debugger_t* debugger, debugger_program_state_t state);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
state | debugger_program_state_t | 状态。  
  
#### debugger_step_in 函数

* * *

  * 函数功能：



> 进入函数。 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    ret_t debugger_step_in (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_step_loop_over 函数

* * *

  * 函数功能：



> 执行下一条语句(跳过循环) 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    ret_t debugger_step_loop_over (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_step_out 函数

* * *

  * 函数功能：



> 执行到函数结束。 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    ret_t debugger_step_out (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_step_over 函数

* * *

  * 函数功能：



> 执行到下一行代码。（不进入函数） 处于暂停状态才能执行本命令。

  * 函数原型：


    
    
    ret_t debugger_step_over (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_stop 函数

* * *

  * 函数功能：



> 终止程序运行。

  * 函数原型：


    
    
    ret_t debugger_stop (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_unlock 函数

* * *

  * 函数功能：



> 解锁debugger对象。

  * 函数原型：


    
    
    ret_t debugger_unlock (debugger_t* debugger);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
  
#### debugger_update_code 函数

* * *

  * 函数功能：



> 更新代码。

  * 函数原型：


    
    
    ret_t debugger_update_code (debugger_t* debugger, const binary_data_t* code);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
debugger | debugger_t* | debugger对象。  
code | const binary_data_t* | 代码。
