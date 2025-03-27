#!/bin/bash

# NOTE: This file contains instructions and shouldn't be pushed to GitHub.
# To prevent this file from being added to Git, you can either:
# 1. Add it to .gitignore (recommended)
# 2. Move it outside your repository
# 3. Use selective adding instead of 'git add .'

# Add this file to .gitignore to prevent it from being tracked
echo "git_instructions.sh" >> .gitignore

# 1. Check the status of your repository (shows which files have been changed)
git status

# 2. Add files to the staging area (SELECTIVELY to avoid adding this file)
# Instead of 'git add .', use specific paths to exclude this instructions file:
# Example:
# git add proyecto_erp/ ventas/ compras/ productos/ contabilidad/ agenda/ etc.
# DO NOT use 'git add .' unless you want to include this instructions file

# 3. Commit your changes with a descriptive message
git commit -m "Your descriptive commit message"

# 4. Push your changes to GitHub
git push origin main
# If you're working on another branch like 'develop':
# git push origin develop

# Additional useful commands:
# To see your commit history:
# git log --oneline

# To create and switch to a new branch:
# git checkout -b new-branch-name

# To switch to an existing branch:
# git checkout branch-name

# If you've already staged this file and want to unstage it:
# git reset -- git_instructions.sh
