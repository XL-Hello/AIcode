# AWTK API 知识库

## 概述
这是一个从 AWTK_API.chm 转换而来的 AI 知识库。

## 内容
- **总文档数**: 535
- **API 函数数**: 3761
- **分类**: 2

## 文件结构

### unknown (2 个文件)
- README_zh.md
- README.md

### docs (533 个文件)
- docs/self_layouter_default.md
- docs/how_to_use_stb_hyuv_to_rgb.md
- docs/spin_box.md
- docs/children_layouter_list_view.md
- docs/qa.md
- ... 还有 528 个文件

## 使用方法

### 使用 kb_search.py 脚本进行检索

在命令行中直接传入关键词即可完成一次检索，无需额外交互：

```bash
cd /home/xl/dreame/AIcode/KnowledgeBase/AWTK
python3 kb_search.py widget_invalidate
```

也可以显式使用参数，并控制返回结果数量：

```bash
cd /home/xl/dreame/AIcode/KnowledgeBase/AWTK
python3 kb_search.py --keyword "widget_invalidate 如何刷新控件" --max-results 20
```

如果不传任何参数，则进入交互模式，可在菜单中按 1/2/3 选择不同的搜索方式。

### 详细文档
参考 docs/ 目录中的 Markdown 文档。

## 构建信息
- **来源**: AWTK_API.chm
- **转换日期**: {date}
