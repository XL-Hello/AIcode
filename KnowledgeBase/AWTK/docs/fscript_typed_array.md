## typed array 扩展函数

typed_array是一个单一类型的动态数组，里面只能放相同类型的元素。

typed_array 有以下属性：

  * data 缓冲区的指针
  * size 元素的个数
  * capacity 元素的最大个数
  * size_in_bytes 元素的个数 * 元素的大小
  * capacity_in_bytes 元素的最大个数 * 元素的大小



### 1.typed_array_create

## > 创建 typed_array 对象。

#### 原型
    
    
    typed_array_create(type, capacity) => object
    

type 参数为字符串，可选取值如下：

  * i8 表示 int8。
  * i16 表示 int16。
  * i32 表示 int32。
  * i64 表示 int64。
  * u8 表示 uint8。
  * u16 表示 uint16。
  * u32 表示 uint32。
  * u64 表示 uint64。
  * f32 表示 float32。
  * float 表示 double。
  * 其它或默认为int32。



#### 示例
    
    
    var a = typed_array_create("i8", 10);
    

### 2.typed_array_push

## > 追加一个或多个数据。

#### 原型
    
    
    typed_array_push(array, v, ...) => uint32_t
    

> 返回写入数据的个数

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    

### 3.typed_array_pop

## > 弹出最后一个元素

#### 原型
    
    
    typed_array_pop(array) => value
    

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    print(typed_array_pop(a));
    

### 4.typed_array_get

## > 获取指定位置的元素

#### 原型
    
    
    typed_array_get(array, index) => value
    

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    print(typed_array_get(a, 1));
    

### 5.typed_array_set

## > 修改指定位置的元素

#### 原型
    
    
    typed_array_set(array, index, value) => bool
    

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    typed_array_set(a, 1, 4);
    

### 6.typed_array_insert

## > 插入元素到指定位置

#### 原型
    
    
    typed_array_insert(array, index, value) => bool
    

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    typed_array_insert(a, 1, 4);
    

### 7.typed_array_remove

## > 删除指定位置的元素

#### 原型
    
    
    typed_array_remove(array, index) => bool
    

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    typed_array_remove(a, 1);
    

### 8.typed_array_clear

## > 删除全部元素

#### 原型
    
    
    typed_array_clear(array) => bool
    

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    typed_array_clear(a);
    

### 9.typed_array_join

## > 连接全部元素成一个字符串。

#### 原型
    
    
    typed_array_join(array, sep) => str
    

#### 示例
    
    
    var a = typed_array_create("i32", 3);
    typed_array_push(a, 1, 2, 3);
    print(typed_array_join(a, ","));
    

### 更多示例
    
    
    var a=typed_array_create("i32", 10)
    
    assert(typed_array_push(a, 1) == 1)
    assert(a.size, 1);
    assert(a.bytes, 4);
    
    assert(typed_array_push(a, 2, 3) == 2)
    assert(a.size, 3);
    assert(a.bytes, 12);
    assert(typed_array_get(a, 0)==1)
    assert(typed_array_get(a, 1)==2)
    assert(typed_array_get(a, 2)==3)
    
    assert(typed_array_set(a, 0, 11))
    assert(typed_array_set(a, 1, 22))
    assert(typed_array_set(a, 2, 33))
    
    assert(typed_array_get(a, 0)==11)
    assert(typed_array_get(a, 1)==22)
    assert(typed_array_get(a, 2)==33)
    
    assert(typed_array_pop(a), 33);
    assert(typed_array_pop(a), 22);
    assert(typed_array_pop(a), 11);
    assert(a.size == 0);
    
    assert(typed_array_push(a,1, 2, 3) == 3)
    assert(typed_array_remove(a, 0))
    assert(a.size == 2);
    assert(typed_array_remove(a, 1))
    assert(typed_array_remove(a, 0))
    assert(a.size == 0);
    
    assert(typed_array_push(a,1, 2, 3) == 3)
    print(typed_array_join(a, ',') == '1,2,3')
    unset(a);
    
