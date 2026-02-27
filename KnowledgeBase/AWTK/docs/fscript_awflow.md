## awflow 扩展函数

awflow 相关的辅助函数。

### 1\. flow_get

## > 获取流图中变量。

#### 原型
    
    
    flow_get(type, subname) => v
    

#### 示例
    
    
    print(flow_get("global", "value"));
    print(flow_get("msg", "payload"));
    

### 2\. flow_set

## > 修改流图中的变量。

#### 原型
    
    
    flow_set(type, subname, value) => bool
    

#### 示例
    
    
    flow_set('global', 'value', 3);
    flow_set('msg', 'payload', 4);
    
