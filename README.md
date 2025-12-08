

````md
# Git Practice Project

This repository is used to practice core **Git concepts and workflows** commonly used in real-world projects.

---

## Topics Covered

- Push and Pull
- Commit naming conventions
- Feature branching
- Merging branches
- Rebase and squash
- Conflict resolution
- Cherry-picking commits
- Stashing changes

---

## Feature Branching

All changes are made using feature branches following this format:

```text
feature/short-description
````

Example:

```text
feature/add-multiplication
```

---

## Common Commands Practiced

```bash
git add .
git commit -m "Meaningful commit message"
git push -u origin branch-name
git pull origin main
git merge feature/branch-name
git rebase main
git rebase -i HEAD~n
git cherry-pick <commit-hash>
git stash
```

---

## Conflict Resolution

Conflicts are resolved by editing files manually, staging the changes, and completing the merge or rebase.

---

## Objective

The purpose of this repository is to develop confidence in Git workflows and maintain a clean, readable commit history.

---

