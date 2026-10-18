# Step 1: Secrets, Dotfiles, and `.gitignore`

When building projects or competing in hackathons, you will use API keys and passwords stored in a hidden `.env` file. Let's make sure you never accidentally leak them on GitHub.

1. **Create your `.env` file:**
   Duplicate `.env.example` and rename the copy to `.env`:
   `cp .env.example .env` **or** copy it manually in your file explorer. This file is hidden by default, so you may need to enable hidden files to see it.
2. **Add a fake secret:**
   Open `.env` in your editor and change `SECRET_API_KEY` and `NAME` to whatever you want.
3. **Test the script:**
   `python3 app.py`
4. **Check `git status`:**
   `git status`
   **Notice that `.env` is listed in red under Untracked files!** If you ran `git add .` right now, your secret key would be uploaded to the public internet.
5. **Shield it with `.gitignore`:**
   Open `.gitignore`, add `.env` on a new line at the bottom, and save the file.
6. **Verify it vanished:**
   Run `git status` again. `.env` is now invisible to Git, while `.gitignore` is ready to be committed!
