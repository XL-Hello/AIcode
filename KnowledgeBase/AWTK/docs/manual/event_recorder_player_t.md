## event_recorder_player_t

### 概述

## 事件录制与重放，用于辅助自动测试和压力测试。

### 函数

函数名称 | 说明  
---|---  
event_recorder_player_start_play | 开始事件重放。  
event_recorder_player_start_record | 开始事件记录。  
event_recorder_player_stop_play | 停止事件重放。  
event_recorder_player_stop_record | 停止事件记录。  
  
#### event_recorder_player_start_play 函数

* * *

  * 函数功能：



> 开始事件重放。

  * 函数原型：


    
    
    ret_t event_recorder_player_start_play (const char* filename, uint32_t times);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | const char* | 存放事件的文件名。  
times | uint32_t | 循环播放的次数。  
  
#### event_recorder_player_start_record 函数

* * *

  * 函数功能：



> 开始事件记录。

  * 函数原型：


    
    
    ret_t event_recorder_player_start_record (const char* filename);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
filename | const char* | 用于保存事件的文件名。  
  
#### event_recorder_player_stop_play 函数

* * *

  * 函数功能：



> 停止事件重放。

  * 函数原型：


    
    
    ret_t event_recorder_player_stop_play ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。  
  
#### event_recorder_player_stop_record 函数

* * *

  * 函数功能：



> 停止事件记录。

  * 函数原型：


    
    
    ret_t event_recorder_player_stop_record ();
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | 返回RET_OK表示成功，否则表示失败。
