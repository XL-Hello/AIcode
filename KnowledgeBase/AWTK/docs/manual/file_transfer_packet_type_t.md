## file_transfer_packet_type_t

### 概述

文件传输包的类型。

### 常量

名称 | 说明  
---|---  
FILE_TRANSFER_PACKET_META | 文件元数据包(sender->receiver)。  
FILE_TRANSFER_PACKET_DATA | 文件数据包(sender->receiver)。  
FILE_TRANSFER_PACKET_ACK | 文件数据确认包(sender<-receiver)。  
FILE_TRANSFER_PACKET_NACK | 文件数据错误确认包(sender<-receiver)。  
FILE_TRANSFER_PACKET_REQ | 请求开始传输包(sender<-receiver)。
