## 写缓冲扩展函数

wbuffer 有以下属性：

  * data 缓冲区的指针
  * cursor 当前写的位置
  * capacity 最大容量



### 1.wbuffer_create

## > 创建 wbuffer 对象。

#### 原型
    
    
    wbuffer_create() => object
    

#### 示例
    
    
    var a = wbuffer_create();
    

### 2.wbuffer_attach

## > 创建 wbuffer 对象，并附加到指定的数据上。

#### 原型
    
    
    wbuffer_attach(str) => object
    wbuffer_attach(binary) => object
    wbuffer_attach(data, size) => object
    

#### 示例
    
    
    var a = wbuffer_attach("hello");
    

### 3.wbuffer_skip

## > 跳过指定长度的数据。

#### 原型
    
    
    wbuffer_skip(wbuffer, size) => bool
    

#### 示例
    
    
    var a = wbuffer_attach("hello");
    print(wbuffer_skip(a, 2));
    

### 4.wbuffer_rewind

## > 重置写入指针到 0。

#### 原型
    
    
    wbuffer_rewind(wbuffer) => bool
    

#### 示例
    
    
    var a = wbuffer_attach("hello");
    print(wbuffer_skip(a, 2));
    print(wbuffer_rewind(a));
    

### 5.wbuffer_write_uint8

## > 写入 uint8_t 类型的数据。

#### 原型
    
    
    wbuffer_write_uint8(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_uint8(a, 0x10) 
    

### 6.wbuffer_write_uint16

## > 写入 uint16_t 类型的数据。

#### 原型
    
    
    wbuffer_write_uint16(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_uint16(a, 0x1122) 
    

### 7.wbuffer_write_uint32

## > 写入 uint32_t 类型的数据。

#### 原型
    
    
    wbuffer_write_uint32(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_uint32(a, 0x11223344) 
    

### 8.wbuffer_write_uint64

## > 写入 uint64_t 类型的数据。

#### 原型
    
    
    wbuffer_write_uint64(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_uint64(a, 0x1122334455667788)
    

### 9.wbuffer_write_int8

## > 写入 int8_t 类型的数据。

#### 原型
    
    
    wbuffer_write_int8(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_int8(a, -10)
    

### 10.wbuffer_write_int16

## > 写入 int16_t 类型的数据。

#### 原型
    
    
    wbuffer_write_int16(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_int16(a, -1122)
    

### 11.wbuffer_write_int32

## > 写入 int32_t 类型的数据。

#### 原型
    
    
    wbuffer_write_int32(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_int32(a, -11223344)
    

### 12.wbuffer_write_int64

## > 写入 int64_t 类型的数据。

#### 原型
    
    
    wbuffer_write_int64(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_int64(a, -1122334455667788)
    

### 13.wbuffer_write_float

## > 写入 float 类型的数据。

#### 原型
    
    
    wbuffer_write_float(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_float(a, -10, -20);
    

### 14.wbuffer_write_double

## > 写入 double 类型的数据。

#### 原型
    
    
    wbuffer_write_double(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_double(a, 10, 20)
    

### 15.wbuffer_write_string

## > 写入 字符串 类型的数据。

#### 原型
    
    
    wbuffer_write_string(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_string(a, "ab", "cd")
    

### 16.wbuffer_write_binary

## > 写入 二进制 类型的数据。

#### 原型
    
    
    wbuffer_write_binary(wbuffer, v, ...) => int32_t
    

> 返回写入数据的长度（字节数）。

#### 示例
    
    
    var a = wbuffer_create()
    wbuffer_write_binary(a, "1234", 4)
    

### 17.wbuffer_get_data

## > 获取 buffer 的指针。

#### 原型
    
    
    wbuffer_get_data(wbuffer) => pointer
    

#### 示例
    
    
    var a = wbuffer_create()
    var b = wbuffer_get_data(a)
    

### 18.wbuffer_get_cursor

## > 获取 buffer 当前的读取位置。

#### 原型
    
    
    wbuffer_get_cursor(wbuffer) => uint32_t
    

#### 示例
    
    
    var a = wbuffer_create()
    print(wbuffer_get_cursor(a))
    

### 19.wbuffer_get_capacity

## > 获取 buffer 的容量。

#### 原型
    
    
    wbuffer_get_capacity(wbuffer) => uint32_t
    

#### 示例
    
    
    var a = wbuffer_create()
    print(wbuffer_get_capacity(a))
    

### 更多示例
    
    
    var a = wbuffer_create()
    wbuffer_write_int8(a, -10) 
    assert(wbuffer_get_cursor(a)==1)
    wbuffer_write_int16(a, -1122) 
    assert(wbuffer_get_cursor(a)==3)
    wbuffer_write_int32(a, -11223344) 
    assert(wbuffer_get_cursor(a)==7)
    wbuffer_write_int64(a, -1122334455667788)
    assert(wbuffer_get_cursor(a)==15)
    
    wbuffer_write_string(a, "hello")
    assert(wbuffer_get_cursor(a)==21)
    
    wbuffer_write_binary(a, "wolrd", 6)
    assert(wbuffer_get_cursor(a)==27)
    
