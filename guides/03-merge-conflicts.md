# Step 3: Triggering & Resolving a Merge Conflict

Merge conflicts happen when two people edit the **exact same line** of the **exact same file** and try to merge them. Don't panic—Git is just asking a human to decide which version to keep!

### Phase A: Spring the Trap

1. Make sure **both Partner A and Partner B** are on `main` and up to date:
   `git switch main`
   `git pull`
2. **Both partners** open `team_card.md` and edit **Line 7** (`**Team Name:** ...`).
   - **Rule:** Do NOT tell your partner what Team Name you are typing! Pick completely different names.
3. **Both partners** stage and commit their change directly on `main`:
   `git add team_card.md`
   `git commit -m "Set team name"`

### Phase B: The Collision

1. **Partner A pushes first:**
   `git push` _(Partner A's push succeeds!)_
2. **Partner B tries to push second:**
   `git push`
   **REJECTED!** Git blocks Partner B because Partner A's commit is already on GitHub.
3. **Partner B pulls the changes down:**
   `git pull`
   **`CONFLICT (content): Merge conflict in team_card.md`**

### Phase C: Resolve the Conflict (Together on Partner B's Screen)

1. Open `team_card.md` in your code editor. You will see Git's conflict markers (`<<<<<<< HEAD`, `=======`, and `>>>>>>>`).
2. **Fix it:** Delete the marker lines and rewrite the line so only the final agreed-upon Team Name remains.
3. **Seal the merge:**
   `git add team_card.md`
   `git commit -m "Resolve merge conflict on team name"`
   `git push`
4. **Partner A syncs up:** Partner A runs `git pull` to see the resolved file!
