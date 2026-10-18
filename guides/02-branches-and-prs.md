# Step 2: Branches & Pull Requests

Never push experimental code directly to `main`. Instead, create a branch!

1. **Create and switch to a new branch:**
   Use your own name for the branch so it doesn't collide with your partner's branch:
   `git switch -c feat/add-my-name`
2. **Stage and commit your `.gitignore` update (and add your name to `team_card.md` under Partner A or B—do NOT touch the Team Name line yet!):**
   `git status`
   `git add .gitignore team_card.md`
   `git commit -m "Ignore .env and add my name to roster"`
3. **Check the commit history:**
   `git log --oneline`
4. **Push your branch to GitHub:**
   `git push -u origin feat/add-my-name`
5. **Open a Pull Request (PR):**
   - Go to the repository on GitHub.com.
   - Click the green **"Compare & pull request"** button.
   - Click **"Create pull request"**, review the diff, and click **"Merge pull request"**.
6. **Sync your local `main` branch:**
   `git switch main`
   `git pull`
