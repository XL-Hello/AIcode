#!/usr/bin/env python3
"""
Git Commit Viewer Script
根据commit号查询相关代码变更并输出到Markdown文件
"""

import os
import subprocess
import sys
from pathlib import Path


def get_commit_info(repo_path: str, commit_hash: str) -> str:
    """
    获取指定commit的详细信息
    
    Args:
        repo_path: Git仓库的绝对路径
        commit_hash: Commit哈希值
    
    Returns:
        git show命令的输出结果
    """
    try:
        # 切换到仓库目录
        original_dir = os.getcwd()
        os.chdir(repo_path)
        
        # 执行 git show 命令
        result = subprocess.run(
            ['git', 'show', commit_hash],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        # 恢复原始目录
        os.chdir(original_dir)
        
        if result.returncode != 0:
            return f"错误: 无法获取commit信息\n{result.stderr}"
        
        return result.stdout
        
    except Exception as e:
        return f"错误: {str(e)}"


def save_to_markdown(content: str, output_path: str, commit_hash: str) -> str:
    """
    将commit信息保存到Markdown文件
    
    Args:
        content: git show的输出内容
        output_path: 输出文件的绝对路径
        commit_hash: Commit哈希值
    
    Returns:
        输出文件的绝对路径
    """
    # 确保输出目录存在
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Commit: {commit_hash}\n\n")
        f.write("```diff\n")
        f.write(content)
        f.write("\n```\n")
    
    return output_path


def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("用法: python view_commit.py <repo_path> <commit_hash> [output_dir]")
        print("  repo_path: Git仓库的绝对路径")
        print("  commit_hash: Commit哈希值")
        print("  output_dir: 输出目录路径(可选,默认为技能目录下的temp文件夹)")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    commit_hash = sys.argv[2]
    
    # 验证仓库路径
    if not os.path.exists(repo_path):
        print(f"错误: 路径不存在: {repo_path}")
        sys.exit(1)
    
    if not os.path.exists(os.path.join(repo_path, '.git')):
        print(f"错误: 不是Git仓库: {repo_path}")
        sys.exit(1)
    
    # 确定输出目录
    if len(sys.argv) >= 4:
        output_dir = sys.argv[3]
    else:
        # 默认使用技能目录下的temp文件夹
        script_dir = Path(__file__).parent.parent
        output_dir = script_dir / 'temp'
    
    # 获取commit信息
    print(f"正在获取commit {commit_hash} 的信息...")
    commit_info = get_commit_info(repo_path, commit_hash)
    
    # 生成输出文件路径
    output_file = Path(output_dir) / f"{commit_hash}.md"
    
    # 保存到文件
    save_to_markdown(commit_info, str(output_file), commit_hash)
    
    print(f"✓ Commit信息已保存到: {output_file}")
    print(f"文件路径: {output_file}")
    
    return str(output_file)


if __name__ == "__main__":
    main()
