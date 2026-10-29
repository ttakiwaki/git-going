# Git & GitHub Workshop Takeaway Cheat Sheet

## 1. One-Time Setup

Run these once on a new computer so Git knows who you are and behaves nicely:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
git config pull.rebase false # We did this to show how merge commits work.

```

---

## 2. The Core Daily Loop

The 5 commands you will use 90% of the time:

| Command               | What It Does                                                            |
| :-------------------- | :---------------------------------------------------------------------- |
| `git pull`            | Downloads and merges the latest changes from GitHub to your computer    |
| `git status`          | Shows modified files (red = unstaged, green = staged and ready)         |
| `git add <file>`      | Stages a specific file for commit (use `git add .` to stage everything) |
| `git commit -m "Msg"` | Saves a permanent snapshot of your staged changes with a description    |
| `git push`            | Uploads your committed snapshots to GitHub                              |

---

## 3. Starting & Connecting a Repo

**Option A: Starting from scratch on your laptop**

```bash
git init                                        # Creates hidden .git folder
git remote add origin <[https://github.com/](https://github.com/)...>  # Links folder to GitHub URL
git push -u origin main                         # Pushes & remembers branch link
```

**Option B: Downloading an existing repo from GitHub**

```bash
git clone <[https://github.com/](https://github.com/)...>              # Downloads project + history
```

---

## 4. Branches & History

Never push experimental code directly to `main`. Use a branch instead!

| Command                            | What It Does                                                         |
| :--------------------------------- | :------------------------------------------------------------------- |
| `git branch`                       | Lists all local branches (the `*` shows which one you are on)        |
| `git switch -c <branch-name>`      | Creates a new branch and switches to it immediately                  |
| `git switch main`                  | Switches back to the `main` branch                                   |
| `git push -u origin <branch-name>` | Publishes your new branch to GitHub so you can open a Pull Request   |
| `git log --oneline`                | Shows a clean, compact list of past commits (press **`q`** to exit!) |

---

## 5. Hidden Files (Dotfiles), `.env`, & `.gitignore`

- **Dotfiles:** Any file or folder starting with a `.` (like `.git`, `.env`, `.gitignore`) is hidden by default.
  - **Terminal:** Run `ls -a` to see hidden files.
  - **Mac Finder:** Press `Cmd + Shift + .`
  - **Windows Explorer:** Click **View → Show → Hidden items**
- **`.env`:** Stores secret API keys and passwords locally. **Never push this to GitHub.**
- **`.gitignore`:** A list of files/folders Git will completely ignore. Add `.env` inside `.gitignore` _before_ staging files.
- **Emergency Fix:** Accidentally committed `.env` before ignoring it? Untrack it without deleting it from your laptop:
  ```bash
  git rm --cached .env
  git commit -m "Stop tracking .env"
  git push
  ```
  _(Note: Immediately regenerate your leaked API keys—the old key is still visible in past commit history!)_

---

## 6. Merge Conflicts

When two people edit the **exact same line of the same file**, Git pauses and adds conflict markers to the file:

```markdown
<<<<<<< HEAD
Your local changes on your computer
=======

Incoming changes pulled down from GitHub

> > > > > > > 9f3a1b2...
```

**How to fix it in 3 steps:**

1. **Edit the file:** Delete the `<<<<<<< HEAD`, `=======`, and `>>>>>>>` lines, keeping only the final code you want.
2. **Stage & Commit:** Run `git add <file>` and `git commit -m "Resolve merge conflict"`.
3. **Upload:** Run `git push`.
