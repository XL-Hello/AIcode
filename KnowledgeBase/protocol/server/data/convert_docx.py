#!/usr/bin/env python3
import re
from docx import Document
from docx.document import Document as _Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

MONOSPACE_FONTS = {
    'Consolas', 'Courier New', 'Monaco', 'Menlo', 'Source Code Pro',
    'JetBrains Mono', 'Fira Code'
}

def iter_block_items(parent):
    """
    遍历文档中的所有块级元素（段落、表格等），并保持它们在文档中的原始顺序。
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise TypeError("expected Document or _Cell")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def extract_paragraph_text(para):
    """
    提取段落文本。
    优化点：直接使用 para.text 保证所有字符（包括之前被过滤的删除线文本）都被完整转换。
    """
    return para.text

def is_code_paragraph(para):
    """识别代码段落（通过样式名或等宽字体检测）"""
    style_name = para.style.name if para.style and para.style.name else ''
    if any(kw.lower() in style_name.lower() for kw in ['Code', '代码', 'Console', 'Preformatted']):
        return True

    # 检查等宽字体
    non_empty_runs = [run for run in para.runs if run.text and run.text.strip()]
    if not non_empty_runs:
        return False

    monospace_runs = 0
    for run in non_empty_runs:
        font_name = run.font.name or ''
        if font_name in MONOSPACE_FONTS:
            monospace_runs += 1

    # 这里的阈值设为大部分为等宽字体，提高容错率
    return monospace_runs > 0 and monospace_runs >= len(non_empty_runs) * 0.8

def get_heading_level(para):
    """获取标题级别（支持多国语言习惯）"""
    style_name = para.style.name if para.style and para.style.name else ''
    # 匹配 Heading 1-6, 标题 1-6, Title 等
    m = re.search(r'(Heading|标题|Title)\s*(\d)?', style_name, re.I)
    if m:
        if m.group(1).lower() == 'title':
            return 1
        return int(m.group(2)) if m.group(2) else 1
    return 0

def extract_cell_text(cell):
    """提取单元格全部内容，保证内部多段落不丢失"""
    lines = []
    for para in cell.paragraphs:
        text = extract_paragraph_text(para)
        if text:
            lines.append(text)
    return '\n'.join(lines)

def convert_docx_to_md(docx_path, md_path):
    try:
        doc = Document(docx_path)
    except Exception as e:
        print(f"打开文档失败: {e}")
        return

    md_lines = []
    in_code_block = False
    
    # 按照文档原始顺序遍历元素
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            text = extract_paragraph_text(block)
            
            # 处理标题
            h_level = get_heading_level(block)
            if h_level > 0:
                if in_code_block:
                    md_lines.append('```')
                    in_code_block = False
                md_lines.append(f"{'#' * h_level} {text.strip()}")
                md_lines.append('')
                continue

            # 处理空行或代码块边界
            if not text.strip():
                if in_code_block:
                    md_lines.append('```')
                    in_code_block = False
                md_lines.append('')
                continue
            
            if is_code_paragraph(block):
                if not in_code_block:
                    md_lines.append('```')
                    in_code_block = True
                md_lines.append(text)
            else:
                if in_code_block:
                    md_lines.append('```')
                    in_code_block = False
                md_lines.append(text)
                md_lines.append('') # 普通段落后增加空行
                
        elif isinstance(block, Table):
            if in_code_block:
                md_lines.append('```')
                in_code_block = False
            
            md_lines.append('')
            for i, row in enumerate(block.rows):
                # 过滤重复单元格（针对合并单元格的情况，虽然 MD 不支持，但保证内容不乱）
                cells_content = []
                for cell in row.cells:
                    cell_text = extract_cell_text(cell)
                    # 替换管道符和换行符以符合 MD 表格规范
                    cell_text = cell_text.replace('|', '\\|').replace('\n', '<br>')
                    cells_content.append(cell_text.strip())
                
                md_lines.append('| ' + ' | '.join(cells_content) + ' |')
                
                # 第一行作为表头后跟分隔线
                if i == 0:
                    md_lines.append('| ' + ' | '.join(['---'] * len(row.cells)) + ' |')
            
            md_lines.append('')

    if in_code_block:
        md_lines.append('```')
    
    # 保存文件
    try:
        with open(md_path, 'w', encoding='utf-8') as f:
            # 过滤多余的新行
            content = '\n'.join(md_lines)
            content = re.sub(r'\n{3,}', '\n\n', content)
            f.write(content.strip() + '\n')
        print(f"转换完成: {md_path}")
    except Exception as e:
        print(f"写入文件失败: {e}")

if __name__ == '__main__':
    convert_docx_to_md(
        '/home/xl/dreame/AIcode/KnowledgeBase/protocol/server/data/接口协议规范.docx',
        '/home/xl/dreame/AIcode/KnowledgeBase/protocol/server/data/接口协议规范.md'
    )
