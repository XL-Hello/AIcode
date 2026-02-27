## network_interface_t

### 概述

## 网卡接口。

### 函数

函数名称 | 说明  
---|---  
network_interface_create | 网卡接口创建函数。  
network_interface_destroy | 网卡接口销毁函数。  
network_interface_disable | 网卡接口禁能函数。  
network_interface_enable | 网卡接口使能函数。  
network_interface_get_ipaddr | 网卡接口获取IP地址。  
network_interface_get_macaddr | 网卡接口获取MAC地址。  
network_interface_get_quality | 网卡接口获取通信质量。  
network_interface_get_status | 网卡接口获取状态。  
network_interface_set_dhcp | 网卡接口设置DNS。  
network_interface_set_dns | 网卡接口设置DNS。  
network_interface_set_gateway | 网卡接口设置DNS。  
network_interface_set_ipaddr | 网卡接口设置IP地址。  
network_interface_set_wifi_ap | 网卡接口设置WIFI AP模式。  
network_interface_set_wifi_sta | 网卡接口设置WIFI STA模式。  
  
#### network_interface_create 函数

* * *

  * 函数功能：



> 网卡接口创建函数。

  * 函数原型：


    
    
    network_interface_t* network_interface_create (const char* interface, network_interface_type_t type);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | network_interface_t* | 网卡接口对象。  
interface | const char* | 网卡名。  
type | network_interface_type_t | 网卡接口类型。  
  
#### network_interface_destroy 函数

* * *

  * 函数功能：



> 网卡接口销毁函数。

  * 函数原型：


    
    
    void network_interface_destroy (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | void | 。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_disable 函数

* * *

  * 函数功能：



> 网卡接口禁能函数。

  * 函数原型：


    
    
    ret_t network_interface_disable (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_enable 函数

* * *

  * 函数功能：



> 网卡接口使能函数。

  * 函数原型：


    
    
    ret_t network_interface_enable (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_get_ipaddr 函数

* * *

  * 函数功能：



> 网卡接口获取IP地址。

  * 函数原型：


    
    
    char * network_interface_get_ipaddr (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char * | 返回IP地址成功，NULL失败。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_get_macaddr 函数

* * *

  * 函数功能：



> 网卡接口获取MAC地址。

  * 函数原型：


    
    
    char * network_interface_get_macaddr (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | char * | 返回MAC地址成功，NULL失败。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_get_quality 函数

* * *

  * 函数功能：



> 网卡接口获取通信质量。

  * 函数原型：


    
    
    int network_interface_get_quality (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 对于无线网络返回信号RSSI的绝对值， 对于有线网络，返回10、100、1000M带宽。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_get_status 函数

* * *

  * 函数功能：



> 网卡接口获取状态。

  * 函数原型：


    
    
    int network_interface_get_status (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | int | 0表示未连接，1表示连接成功，-1表示操作失败。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_set_dhcp 函数

* * *

  * 函数功能：



> 网卡接口设置DNS。

  * 函数原型：


    
    
    ret_t network_interface_set_dhcp (network_interface_t * interface);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
  
#### network_interface_set_dns 函数

* * *

  * 函数功能：



> 网卡接口设置DNS。

  * 函数原型：


    
    
    ret_t network_interface_set_dns (network_interface_t * interface, const char* dns);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
dns | const char* | 网卡dns。  
  
#### network_interface_set_gateway 函数

* * *

  * 函数功能：



> 网卡接口设置DNS。

  * 函数原型：


    
    
    ret_t network_interface_set_gateway (network_interface_t * interface, const char* gateway, const char* dev);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
gateway | const char* | 网卡网关。  
dev | const char* | 出口网卡设备名。  
  
#### network_interface_set_ipaddr 函数

* * *

  * 函数功能：



> 网卡接口设置IP地址。

  * 函数原型：


    
    
    ret_t network_interface_set_ipaddr (network_interface_t * interface, const char* ipaddr, const char* netmask);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
ipaddr | const char* | 网卡IP。  
netmask | const char* | 网卡MASK。  
  
#### network_interface_set_wifi_ap 函数

* * *

  * 函数功能：



> 网卡接口设置WIFI AP模式。

  * 函数原型：


    
    
    ret_t network_interface_set_wifi_ap (network_interface_t * interface, const char* essid, const char* passwd, network_interface_wifi_auth_t   auth, uint8_t  channel, network_interface_wifi_freq_t   freq, uint8_t  hidden);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
essid | const char* | wifi帐号 。  
passwd | const char* | wifi密码。  
auth | network_interface_wifi_auth_t | wifi认证方式。  
channel | uint8_t | wifi通道。  
freq | network_interface_wifi_freq_t | wifi频段。  
hidden | uint8_t | wifi是否隐藏。  
  
#### network_interface_set_wifi_sta 函数

* * *

  * 函数功能：



> 网卡接口设置WIFI STA模式。

  * 函数原型：


    
    
    ret_t network_interface_set_wifi_sta (network_interface_t * interface, const char* essid, const char* passwd, network_interface_wifi_auth_t   auth);
    

  * 参数说明：

参数 | 类型 | 说明  
---|---|---  
返回值 | ret_t | RET_OK表示成功，否则失败。  
interface | network_interface_t * | 网卡对象。  
essid | const char* | wifi帐号 。  
passwd | const char* | wifi密码。  
auth | network_interface_wifi_auth_t | wifi认证方式。
