# 协议文档知识库

## 概述
这是整理后的物联网设备协议规范文档知识库，包含MQTT和HTTPS协议的详细说明。

## 内容
- **总文档数**: 4
- **分类**: 3 (设备管理、设备控制、设备报告)
- **协议类型**: MQTT、HTTPS

## 文件结构

### 索引文档 (1 个文件)
- 00-索引.md: 文档目录索引

### 分类文档 (3 个文件)
- 设备管理.md: 绑定Token获取等管理类协议
- 设备控制.md: 设备控制相关协议
- 设备报告.md: 属性报告和事件报告协议

## 使用方法

### 使用 protocol_retriever.py 脚本进行检索

在命令行中直接传入关键词即可完成一次检索：

```bash
cd /home/xl/dreame/AIcode/KnowledgeBase/protocol/server
python3 protocol_retriever.py "设备控制"
```

也可以指定返回结果数量：

```bash
cd /home/xl/dreame/AIcode/KnowledgeBase/protocol/server
python3 protocol_retriever.py "属性报告" --top_n 2
```

#### 示例输出

```bash
xl@dre:~/dreame/AIcode/KnowledgeBase/protocol/server$ python3 protocol_retriever.py "设备控制" --top_n 2
检索关键词: 设备控制
检索结果 (2 个):
1. docs/设备控制.md (相关度: 22)
   行1: # 设备控制
   行3: ## 设备控制 (deviceCtrl)

2. docs/00-索引.md (相关度: 12)
   行8: ## 2. 设备控制
   行9: 1. [设备控制 (deviceCtrl)](设备控制.md#deviceCtrl)
```

### 直接浏览文档
参考 docs/ 目录中的 Markdown 文档，或从 00-索引.md 开始浏览。

## 构建信息
- **来源**: 接口协议规范.md (原始协议文档)
- **整理日期**: 2026-02-27
- **工具**: protocol_retriever.py (检索脚本)