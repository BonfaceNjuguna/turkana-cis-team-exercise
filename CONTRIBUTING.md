# How we work together

These rules mirror how changes reach the real CIS, where merging to `main` publishes to the live site.

## 1. Before you start

- Every piece of work has an **issue**. Assign yourself before you start, so two people do not build the same thing.
- If a task is big, split it into smaller issues (for example "Datasets: upload endpoint" and "Datasets: list page") and link them to the task's issue.
- Pull the latest `main` before creating a branch:

  ```bash
  git switch main
  git pull
  git switch -c task-2/upload-endpoint
  ```

## 2. Branches

Name branches `<task>/<short-description>`, for example:

- `task-0/add-amina`
- `task-1/forecast-endpoint`
- `task-2/netcdf-metadata`
- `task-3/alert-publishing`
- `fix/readme-setup-steps`

One branch, one purpose. If you notice an unrelated problem, open an issue for it instead of fixing it in the same branch.

## 3. Commits

- Commit small, working steps. Each commit message says **what changed and why**, in the imperative:
  - Good: `Reject uploads larger than 50 MB`
  - Good: `Show "forecast unavailable" when Open-Meteo times out`
  - Not useful: `fix`, `changes`, `wip`, `update files`
- Never commit secrets, `.env` files, the database file, uploaded files, `node_modules` or `.venv`. They are already in `.gitignore`.

## 4. Keeping your branch up to date

When `main` moves on, bring the changes into your branch and resolve conflicts **on your branch**, not on `main`:

```bash
git switch main && git pull
git switch task-2/upload-endpoint
git merge main          # or: git rebase main (then push with --force-with-lease)
```

If a conflict touches a teammate's work, talk to them before choosing what to keep.

## 5. Pull requests

- Open a pull request into `main` and fill in the template: what it does, how to test it, screenshots for page changes.
- Keep it focused: under about 400 changed lines is a good target.
- The automatic checks (backend tests, frontend type check and build) must pass.
- Mark it as a **draft** while you are still working, then **Ready for review**.

## 6. Reviews

- **Another team member must approve** every pull request before it is merged. `main` is protected, so this is enforced.
- As a reviewer: run the branch, try the feature, read the code. Ask questions, suggest improvements, and use **Request changes** when something must be fixed. "Looks good" without trying it is not a review.
- As the author: reply to every comment, push fixes as new commits, and mark conversations resolved once addressed.
- Reviews are about the code, never the person.

## 7. Merging

- The author merges once it is approved and green, using **Squash and merge** so `main` keeps one clear commit per pull request.
- The branch is deleted automatically after merging.

## 8. If something goes wrong

- Broke `main`? Open a fix pull request straight away and tell the team. Do not try to rewrite `main`'s history.
- Lost work or a messy branch? Ask for help before using `git push --force` on anything you share with others.
