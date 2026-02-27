## 大端小端扩展函数

### 1.is_little

## > 判断当前 CPU 是否是小端。

#### 原型
    
    
    is_little() => bool
    

#### 示例
    
    
    print(is_little());
    

### 2.htonl

## > 将类型为 uint32_t 的整数，从主机字节顺序转成网络字节顺序。

#### 原型
    
    
    htonl(uint32_t) => uint32_t
    

#### 示例
    
    
    print(htonl(1));
    

### 3.ntohl

## > 将类型为 uint32_t 的整数，从网络字节顺序转成主机字节顺序。

#### 原型
    
    
    ntohl(uint32_t) => uint32_t
    

#### 示例
    
    
    print(ntohl(2));
    

### 4.htons

## > 将类型为 uint16_t 的整数，从主机字节顺序转成网络字节顺序。

#### 原型
    
    
    htons(uint16_t) => uint16_t
    

#### 示例
    
    
    print(htons(3));
    

### 5.ntohs

## > 将类型为 uint16_t 的整数，从网络字节顺序转成主机字节顺序。

#### 原型
    
    
    ntohs(uint16_t) => uint16_t
    

#### 示例
    
    
    print(ntohs(4));
    

### 6.htonf

## > 将类型为单精度的浮点数，从主机字节顺序转成网络字节顺序。

#### 原型
    
    
    htonf(float) => float
    

#### 示例
    
    
    print(htonf(5));
    

### 7.ntohf

## > 将类型为单精度的浮点数，从网络字节顺序转成主机字节顺序。

#### 原型
    
    
    ntohf(float) => float
    

#### 示例
    
    
    print(ntohf(7));
    

### 8.htonll

## > 将类型为 uint64_t 的整数，从主机字节顺序转成网络字节顺序。

#### 原型
    
    
    htonll(uint64_t) => uint64_t
    

#### 示例
    
    
    print(htonll(5));
    

### 9.ntohll

## > 将类型为 uint64_t 的整数，从网络字节顺序转成主机字节顺序。

#### 原型
    
    
    ntohll(uint64_t) => uint64_t
    

#### 示例
    
    
    print(ntohll(1));
    

### 更多示例
    
    
    assert(is_little())
    assert(htonl(0x11223344) == 0x44332211)
    assert(ntohl(0x11223344) == 0x44332211)
    assert(htons(0x1122) == 0x2211)
    assert(ntohs(0x1122) == 0x2211)
    assert(htonll(0x1122334455667788)==0x8877665544332211)
    assert(ntohll(0x1122334455667788)==0x8877665544332211)
    
