# Git Setup and Remote Repository Connection Guide

This guide explains how to connect your local Python project to a remote Git repository and push your code.

## Prerequisites
- Git installed on your system
- A GitHub account and repository created
- Terminal/Command line access

## Step-by-Step Process

### 1. Initialize Local Git Repository
```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialize Git repository
git init
```

### 2. Create .gitignore File
Create a `.gitignore` file to exclude unnecessary files:
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Jupyter Notebook
.ipynb_checkpoints

# pytest
.pytest_cache/

# mypy
.mypy_cache/
```

### 3. Add Remote Repository
```bash
# Add your remote repository URL
git remote add origin https://github.com/username/repository-name.git

# Verify remote connection
git remote -v
```

### 4. Stage and Commit Files
```bash
# Add all files to staging area
git add .

# Commit with a descriptive message
git commit -m "Initial commit: Project setup"
```

### 5. Push to Remote Repository
```bash
# Push to remote repository (first time)
git push -u origin main

# For subsequent pushes
git push
```

## Common Git Commands for Daily Use

### Basic Workflow
```bash
# Check repository status
git status

# Add specific files
git add filename.py

# Add all changes
git add .

# Commit changes
git commit -m "Descriptive commit message"

# Push changes to remote
git push
```

### Pulling Updates
```bash
# Fetch and merge changes from remote
git pull origin main

# Or simply (if tracking is set up)
git pull
```

### Branch Management
```bash
# Create and switch to new branch
git checkout -b feature-branch-name

# Switch between branches
git checkout main
git checkout feature-branch-name

# List all branches
git branch

# Merge branch into main
git checkout main
git merge feature-branch-name
```

### Checking History
```bash
# View commit history
git log

# View compact history
git log --oneline

# View changes in last commit
git show
```

## Troubleshooting

### Common Issues and Solutions

1. **Authentication Issues**
   ```bash
   # Use personal access token instead of password
   # Or set up SSH keys for GitHub
   ```

2. **Merge Conflicts**
   ```bash
   # Pull latest changes first
   git pull origin main
   
   # Resolve conflicts manually in files
   # Then add and commit
   git add .
   git commit -m "Resolve merge conflicts"
   ```

3. **Undo Last Commit (if not pushed)**
   ```bash
   git reset --soft HEAD~1
   ```

4. **Remove File from Tracking**
   ```bash
   git rm --cached filename
   ```

## Best Practices

1. **Commit Messages**: Use clear, descriptive commit messages
2. **Frequent Commits**: Commit small, logical changes frequently
3. **Pull Before Push**: Always pull latest changes before pushing
4. **Use Branches**: Create feature branches for new development
5. **Review Changes**: Use `git status` and `git diff` before committing

## Example Workflow for This Project

```bash
# Daily workflow for 100 Days Python Challenge
cd /Users/roshankumar/Documents/Projects/100day_pythonCoding_challenge/100daysPython

# Check current status
git status

# Add new day's work
git add "Day X/"

# Commit with day information
git commit -m "Day X: [Brief description of what was learned/built]"

# Push to GitHub
git push

# Example commit messages:
# "Day 1: Basic Python syntax and variables"
# "Day 2: Data types and user input"
# "Day 15: Coffee machine project completed"
```

## Repository Information
- **Remote URL**: https://github.com/rosN100/100day_pythonCoding_challenge.git
- **Main Branch**: main
- **Project**: 100 Days Python Coding Challenge

---

*This guide covers the essential Git commands for managing your Python project. For more advanced Git features, refer to the official Git documentation.*
