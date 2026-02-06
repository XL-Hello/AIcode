---
name: article-extractor
description: 从 URL（博客文章、文章、教程）中提取清晰的文章内容，并保存为可读文本。当用户想要从 URL 下载、提取或保存不含广告、导航或杂乱信息的文章/博客文章时使用。
allowed-tools: Bash,Write
---

# 文章提取器 (Article Extractor)

此技能可以从网页文章和博客文章中提取主要内容，移除导航、广告、新闻订阅框和其他冗余信息。保存清晰、可读的文本。

## 何时使用此技能

当用户执行以下操作时激活：
- 提供文章/博客 URL 并希望获取文本内容
- 要求“下载这篇文章”
- 想要“从 [URL] 提取内容”
- 要求“将此博客文章保存为文本”
- 需要不含干扰内容的纯净文章文本

## 工作流程

### 优先级顺序：
1. **检查工具是否已安装**（reader 或 trafilatura）
2. **使用最佳可用工具下载并提取文章**
3. **清理内容**（移除多余空格，进行正确格式化）
4. **保存到文件**，以文章标题作为文件名
5. **确认位置**并显示预览

## 安装检查

按以下顺序检查文章提取工具：

### 选项 1：reader（推荐 - Mozilla 的 Readability）

```bash
command -v reader
```

如果未安装：
```bash
npm install -g @mozilla/readability-cli
# 或
npm install -g reader-cli
```

### 选项 2：trafilatura（基于 Python，表现出色）

```bash
command -v trafilatura
```

如果未安装：
```bash
pip3 install trafilatura
```

### 选项 3：备选方案（curl + 简单解析）

如果没有可用工具，使用基础的 curl + 文本提取（虽然不太可靠，但仍然有效）

## 提取方法

### 方法 1：使用 reader（最适合大多数文章）

```bash
# 提取文章
reader "URL" > article.txt
```

**优点：**
- 基于 Mozilla 的 Readability 算法
- 非常擅长移除杂乱信息
- 能够保留文章结构

### 方法 2：使用 trafilatura（最适合博客/新闻）

```bash
# 提取文章
trafilatura --URL "URL" --output-format txt > article.txt

# 或者使用更多选项
trafilatura --URL "URL" --output-format txt --no-comments --no-tables > article.txt
```

**优点：**
- 提取准确度非常高
- 适配各种网站结构
- 支持多种语言

**选项：**
- `--no-comments`: 跳过评论区域
- `--no-tables`: 跳过数据表格
- `--precision`: 优先保证准确度而非法召回率
- `--recall`: 提取更多内容（可能包含一些噪点）

### 方法 3：备选方案（curl + 基础解析）

```bash
# 下载并提取基础内容
curl -s "URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside'}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            if tag in {'p', 'article', 'main', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
                self.in_content = True
        self.current_tag = tag

    def handle_data(self, data):
        if self.in_content and data.strip():
            self.content.append(data.strip())

    def get_content(self):
        return '\n\n'.join(self.content)

parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > article.txt
```

**注意：** 这种方法可靠性较低，但在没有依赖的情况下可以使用。

## 获取文章标题

提取用于文件名的标题：

### 使用 reader：
```bash
# reader 输出带有标题的 markdown，标题在第一行
TITLE=$(reader "URL" | head -n 1 | sed 's/^# //')
```

### 使用 trafilatura：
```bash
# 获取包含标题的元数据
TITLE=$(trafilatura --URL "URL" --json | python3 -c "import json, sys; print(json.load(sys.stdin)['title'])")
```

### 使用 curl (备选)：
```bash
TITLE=$(curl -s "URL" | grep -oP '<title>\K[^<]+' | sed 's/ - .*//' | sed 's/ | .*//')
```

## 文件名创建

为文件系统清理标题：

```bash
# 获取标题
TITLE="来自网站的文章标题"

# 清理文件系统不兼容字符（移除特殊字符，限制长度）
FILENAME=$(echo "$TITLE" | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<' '' | tr '>' '' | tr '|' '-' | cut -c 1-100 | sed 's/ *$//')

# 添加扩展名
FILENAME="${FILENAME}.txt"
```

## 完整工作流

```bash
ARTICLE_URL="https://example.com/article"

# 检查工具
if command -v reader &> /dev/null; then
    TOOL="reader"
    echo "使用 reader (Mozilla Readability)"
elif command -v trafilatura &> /dev/null; then
    TOOL="trafilatura"
    echo "使用 trafilatura"
else
    TOOL="fallback"
    echo "使用备选方法（可能不够准确）"
fi

# 提取文章
case $TOOL in
    reader)
        # 获取内容
        reader "$ARTICLE_URL" > temp_article.txt

        # 获取标题（markdown 中 # 之后的第一行）
        TITLE=$(head -n 1 temp_article.txt | sed 's/^# //')
        ;;

    trafilatura)
        # 从元数据中获取标题
        METADATA=$(trafilatura --URL "$ARTICLE_URL" --json)
        TITLE=$(echo "$METADATA" | python3 -c "import json, sys; print(json.load(sys.stdin).get('title', 'Article'))")

        # 获取纯净内容
        trafilatura --URL "$ARTICLE_URL" --output-format txt --no-comments > temp_article.txt
        ;;

    fallback)
        # 获取标题
        TITLE=$(curl -s "$ARTICLE_URL" | grep -oP '<title>\K[^<]+' | head -n 1)
        TITLE=${TITLE%% - *}  # 移除站点名称
        TITLE=${TITLE%% | *}  # 移除站点名称（另一种格式）

        # 获取内容（基础提取）
        curl -s "$ARTICLE_URL" | python3 -c "
from html.parser import HTMLParser
import sys

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.content = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'aside', 'form'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.skip_tags:
            if tag in {'p', 'article', 'main'}:
                self.in_content = True
        if tag in {'h1', 'h2', 'h3'}:
            self.content.append('\n')

    def handle_data(self, data):
        if self.in_content and data.strip():
            self.content.append(data.strip())

    def get_content(self):
        return '\n\n'.join(self.content)

parser = ArticleExtractor()
parser.feed(sys.stdin.read())
print(parser.get_content())
" > temp_article.txt
        ;;
esac

# 清理文件名
FILENAME=$(echo "$TITLE" | tr '/' '-' | tr ':' '-' | tr '?' '' | tr '"' '' | tr '<>' '' | tr '|' '-' | cut -c 1-80 | sed 's/ *$//' | sed 's/^ *//')
FILENAME="${FILENAME}.txt"

# 移动到最终文件名
mv temp_article.txt "$FILENAME"

# 显示结果
echo "✓ 已提取文章：$TITLE"
echo "✓ 已保存至：$FILENAME"
echo ""
echo "预览（前 10 行）："
head -n 10 "$FILENAME"
```

## 错误处理

### 常见问题

**1. 工具未安装**
- 尝试尝试替代工具 (reader → trafilatura → fallback)
- 建议安装："使用 npm install -g reader-cli 安装 reader"

**2. 付费墙或需要登录**
- 提取工具可能会失败
- 告知用户："此文章需要身份验证。无法提取。"

**3. 无效 URL**
- 检查 URL 格式
- 尝试带或不带重定向的情况

**4. 未提取到内容**
- 网站可能大量使用了 JavaScript
- 尝试备选方法
- 如果提取失败，告知用户

**5. 标题包含特殊字符**
- 为文件系统清理标题
- 移除：`/`, `:`, `?`, `"`, `<`, `>`, `|`
- 替换为 `-` 或直接移除

## 输出格式

### 保存的文件包含：
- 文章标题（如果可用）
- 作者（如果工具可提供）
- 文章正文
- 章节标题
- 无导航、广告或冗余信息

### 哪些内容会被移除：
- 导航菜单
- 广告和推广内容
- 新闻订阅表单
- 相关文章侧边栏
- 评论区域（可选）
- 社交媒体按钮
- Cookie 通知

## 获得最佳效果的建议

**1. 针对大多数文章使用 reader**
- 最全面的工具
- 基于 Firefox 的阅读模式 (Reader View)
- 适用于大多数新闻网站和博客

**2. 在以下情况下使用 trafilatura：**
- 学术文章
- 新闻网站
- 布局复杂的博客
- 非英语内容

**3. 备选方法的局限性：**
- 可能会包含一些噪点
- 段落检测不够精确
- 对于简单网站，有总比没有强

**4. 检查提取质量：**
- 始终向用户展示预览
- 询问内容是否正确
- 如有需要，建议尝试不同的工具

## 使用示例

**简单提取：**
```bash
# 用户："提取 https://example.com/article"
reader "https://example.com/article" > temp.txt
TITLE=$(head -n 1 temp.txt | sed 's/^# //')
FILENAME="$(echo "$TITLE" | tr '/' '-').txt"
mv temp.txt "$FILENAME"
echo "✓ 已保存至：$FILENAME"
```

**带有错误处理：**
```bash
if ! reader "$URL" > temp.txt 2>/dev/null; then
    if command -v trafilatura &> /dev/null; then
        trafilatura --URL "$URL" --output-format txt > temp.txt
    else
        echo "错误：无法提取文章。请安装 reader 或 trafilatura。"
        exit 1
    fi
fi
```

## 最佳实践

- ✅ 提取后始终展示预览（前 10 行）
- ✅ 保存前验证提取是否成功
- ✅ 清理文件名以确保文件系统兼容性
- ✅ 如果主工具失败，尝试备选方法
- ✅ 告知用户使用了哪个工具
- ✅ 保持文件名长度合理（少于 100 个字符）

## 提取完成后

向用户显示：
1. "✓ 已提取：[文章标题]"
2. "✓ 已保存至：[文件名]"
3. 显示预览（前 10-15 行）
4. 文件大小和位置

如有需要，询问：
- "您想让我根据此内容创建一个 Ship-Learn-Next 计划吗？"（如果使用了 ship-learn-next 技能）
- "我应该提取另一篇文章吗？"
