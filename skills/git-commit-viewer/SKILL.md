---
name: git-commit-viewer
description: This skill is used when querying Git commit changes by commit hash. Use this skill when users request to view, extract, or analyze code changes from specific commits. Triggers include requests like "show commit abc123", "view commit changes", "get commit details", or "extract commit information".
---

# Git Commit Viewer

## Overview

Query and extract Git commit changes by commit hash, outputting detailed code differences to a Markdown file for easy review and analysis.

## When to Use This Skill

Use this skill when:
- User provides a commit hash and wants to view the changes
- User asks to analyze specific commit modifications
- User needs to extract commit information for documentation or review
- User requests commit details in a structured format

## Workflow

### Step 1: Obtain Required Information

Before executing the commit viewer, obtain the following from the user:

1. **Git repository path**: The absolute path to the Git repository
   - If not provided, ask the user for the project directory
   - Validate that the path exists and contains a `.git` directory

2. **Commit hash**: The commit identifier to query
   - Accept short or full commit hashes
   - Validate that the commit exists in the repository

### Step 2: Execute the Commit Viewer

Use the provided script to extract commit information:

**Option A: Python Script (Recommended)**
```bash
python3 scripts/view_commit.py <repo_path> <commit_hash> [output_dir]
```

**Option B: Bash Script**
```bash
bash scripts/view_commit.sh <repo_path> <commit_hash> [output_dir]
```

**Parameters:**
- `repo_path`: Absolute path to the Git repository
- `commit_hash`: The commit hash to query
- `output_dir`: (Optional) Output directory path. Defaults to `temp/` folder in skill directory

**Example:**
```bash
python3 scripts/view_commit.py /home/user/myproject abc123def
```

### Step 3: Retrieve and Return Output File

After execution:
1. The script creates a Markdown file at `temp/<commit_hash>.md`
2. Read the generated file to display commit changes to the user
3. Return the absolute file path to the user

**Output file format:**
```markdown
# Commit: abc123def

```diff
commit abc123def...
Author: ...
Date: ...

diff --git a/...
...
```
```

## Output Location

- **Default location**: `skills/git-commit-viewer/temp/<commit_hash>.md`
- **Custom location**: Specify via the `output_dir` parameter
- The `temp/` directory is created automatically if it doesn't exist

## Usage Examples

**Example 1: Basic Usage**
```
User: Show me commit abc123 from project /home/user/myapp
→ Execute: python3 scripts/view_commit.py /home/user/myapp abc123
→ Return: /home/xl/dreame/AIcode/skills/git-commit-viewer/temp/abc123.md
```

**Example 2: Custom Output Directory**
```
User: Extract commit def456 from /home/user/backend and save to /tmp/commits
→ Execute: python3 scripts/view_commit.py /home/user/backend def456 /tmp/commits
→ Return: /tmp/commits/def456.md
```

**Example 3: View Recent Commit**
```
User: What changed in the last commit of /home/user/frontend?
→ Execute: cd /home/user/frontend && git log -1 --oneline
→ Then: python3 scripts/view_commit.py /home/user/frontend <hash>
```

## Resources

### scripts/

- `view_commit.py`: Python script for extracting commit information with error handling
- `view_commit.sh`: Bash alternative for environments without Python

### temp/

Auto-generated directory containing output Markdown files:
- Files are named `<commit_hash>.md`
- Each file contains the complete commit diff in Markdown format
- Safe to delete old files to save space

## Error Handling

The script handles common errors:
- **Invalid repository path**: Reports if path doesn't exist or isn't a Git repository
- **Invalid commit hash**: Returns Git error message if commit doesn't exist
- **Permission issues**: Reports if unable to write to output directory

## Notes

- Commit output includes full diff information with syntax highlighting
- The Markdown format uses `diff` code blocks for proper rendering
- Multiple commits can be extracted to separate files in the same session
