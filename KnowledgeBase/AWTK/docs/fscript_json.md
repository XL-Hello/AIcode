## JSON 扩展函数

### 1.json_load

## > 加载 json 数据。

#### 原型
    
    
    json_load(str) => object
    json_load(binary) => object
    json_load(data, size) => object
    

#### 示例
    
    
    var a = json_load('{"name": "fscript", "age": 100}');
    

### 2.json_save

## > 将对象保存为 json 数据。

#### 原型
    
    
    json_save(obj) => binary 
    

#### 示例
    
    
    var a = json_load('{"name": "fscript", "age": 100}');
    json_save(a);
    

### 3.json_save_to_string

## > 将对象保存为字符串数据。

#### 原型
    
    
    json_save_to_string(obj) => string 
    

#### 示例
    
    
    var a = json_load('{"name": "fscript", "age": 100}');
    print(json_save_to_string(a));
    

### 4.ubjson_load

## > 加载 ubjson 数据。

#### 原型
    
    
    ubjson_load(binary) => object
    ubjson_load(data, size) => object
    

#### 示例
    
    
    var a = ubjson_load(file_read_binary("test.ubjson"));
    

### 5.ubjson_save

## > 将对象保存为 ubjson 数据。

#### 原型
    
    
    ubjson_save(obj) => binary
    

#### 示例
    
    
    var a = json_load('{"name": "fscript", "age": 100}');
    var b = ubjson_save(a);
    

### 完整示例
    
    
    //load from string
    var str='{
        "results": [
            {
                "location": {
                    "id": "WS0E9D8WN298",
                    "name": "GuangZhou"
                },
                "now": {
                    "code": "9",
                    "temperature": "30"
                },
                "last_update": "2022-04-28T14:50:00+08:00"
            }
        ],
        "name": "fscript",
        "age": 100
    }'
    var a = json_load(str)
    
    assert(object_get(a, "results.[0].location.id")=="WS0E9D8WN298");
    assert(object_get(a, "results.[0].location.name")=="GuangZhou");
    assert(object_get(a, "results.[0].now.code")=="9");
    assert(object_get(a, "results.[0].now.temperature")=="30");
    assert(object_get(a, "results.[0].last_update")=="2022-04-28T14:50:00+08:00");
    assert(object_get(a, "name")=="fscript");
    assert(object_get(a, "age")==100);
    
    // 获取数组类型节点的子元素个数
    assert(object_get(a, "results.#size")==1);
    
    //save to file
    var b=json_save(a)
    assert(file_write("test.json", b))
    
    //json obj to string
    var c=json_save_to_string(a)
    print(c)
    
    //load from file as text
    a = json_load(file_read_text("test.json"))
    
    assert(object_get(a, "name")=="fscript");
    assert(object_get(a, "age")==100);
    
    //load from file as binary
    a = json_load(file_read_binary("test.json"))
    assert(file_remove("test.json"))
    
    assert(object_get(a, "name")=="fscript");
    assert(object_get(a, "age")==100);
    
    assert(file_remove("test.json"))
    unset(a)
    unset(b)
    unset(c)
    unset(str)
    
