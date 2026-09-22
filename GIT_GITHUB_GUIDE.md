# Getting this project onto GitHub (beginner walkthrough)

This is a one-time setup, then a repeatable 3-command habit. Two ways to get there — pick whichever feels easier.

## Option A: No terminal, all in the browser (easiest first time)

1. Go to [github.com](https://github.com) and sign in (create a free account if you don't have one).
2. Click the **+** in the top-right → **New repository**.
3. Name it `telco-churn-datamining`, keep it **Public** (so it shows up on your portfolio), don't tick "Add a README" (you already have one). Click **Create repository**.
4. On the next page, click **uploading an existing file**.
5. Open your `telco-churn-datamining` folder in Finder, select **everything inside it** (`README.md`, `requirements.txt`, `.gitignore`, and the `notebooks`, `src`, `tests` folders), and **drag them onto the GitHub upload area**.
6. Scroll down, write a commit message like "Initial commit", click **Commit changes**.

Done — your repo is live at `https://github.com/<your-username>/telco-churn-datamining`.

### "But my files are inside folders — how do those get uploaded?"

Drag the **folder itself**, not the files inside it. When you drag a folder onto GitHub's upload area, it uploads everything inside and keeps the structure — so `notebooks/01_churn_analysis.ipynb` lands in the right place automatically. This works in Chrome, Edge, Firefox, and Safari.

The catch: the **"choose your files"** link (the clickable one, next to the drag area) can only pick individual files — macOS won't let you select a folder through it. So for folders you have to drag, not click.

**If dragging isn't working for you**, there's a manual fallback that creates folders as you go:

1. On your repo page, click **Add file** → **Create new file**
2. In the filename box, type the full path including the folder: `notebooks/01_churn_analysis.ipynb`
3. The moment you type the `/`, GitHub turns `notebooks` into a folder in the breadcrumb above — that's how you create folders on GitHub, there's no "new folder" button
4. Paste the file's contents into the editor, scroll down, **Commit new file**
5. Repeat for `src/utils.py` and `tests/test_utils.py`

This is fiddly for a notebook (the `.ipynb` is long JSON), so honestly — if the drag doesn't work, Option B below is less painful than the fallback.

**One thing to watch:** `.gitignore` starts with a dot, which makes it hidden in Finder. Press `Cmd + Shift + .` in Finder to show hidden files so you can select it. If you miss it, it's not fatal — you can add it later.

## Option B: Using git (the real workflow — worth learning once)

This is what every developer actually uses day to day. It feels like more steps the first time, then becomes three commands you'll use for the rest of your life: `git add`, `git commit`, `git push`.

### One-time setup

**1. Install git** (skip if `git --version` already prints something):
- Mac: `git` comes with Xcode Command Line Tools — run `xcode-select --install` in Terminal.
- Windows: download from [git-scm.com](https://git-scm.com/download/win).

**2. Tell git who you are** (run once, ever, on your machine):
```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```

**3. Create the empty repo on GitHub** (same as Option A steps 1–3, but this time tick nothing and don't upload anything — just create it empty). Copy the URL it gives you, looks like:
```
https://github.com/<your-username>/telco-churn-datamining.git
```

### Push your project (first time)

Open Terminal, navigate into your project folder, then:

```bash
cd path/to/telco-churn-datamining
git init
git add .
git commit -m "Initial commit: project scaffold with notebook, utils, tests"
git branch -M main
git remote add origin https://github.com/<your-username>/telco-churn-datamining.git
git push -u origin main
```

What each line does:
- `git init` — turns this folder into a git repo (creates a hidden `.git/` folder tracking history)
- `git add .` — stages every file for the next commit (the `.gitignore` you already have keeps junk like `__pycache__` out)
- `git commit -m "..."` — saves a snapshot with a message describing what changed
- `git branch -M main` — names your default branch `main` (GitHub's convention)
- `git remote add origin ...` — tells your local repo where the GitHub copy lives
- `git push -u origin main` — uploads your commit to GitHub; `-u` remembers this pairing so future pushes are just `git push`

You'll be prompted to authenticate — GitHub now requires a **Personal Access Token** instead of your password:
1. GitHub → click your profile photo → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token
2. Tick the `repo` scope, generate, **copy the token immediately** (you won't see it again)
3. When git asks for your password, paste the token instead

### Making updates later (the habit)

Every time you improve the notebook or fill in a TODO:

```bash
git add .
git commit -m "Complete Section 3: decision tree + pruning"
git push
```

That's the entire day-to-day workflow. Write a commit message that says *what changed*, not "update" — future you (and anyone reviewing your portfolio) will thank you.

## Connecting Google Colab to this GitHub repo

**To open the notebook in Colab:**
1. [colab.research.google.com](https://colab.research.google.com) → File → Open notebook → **GitHub** tab
2. Paste your repo URL or search `<your-username>/telco-churn-datamining`
3. Click `notebooks/01_churn_analysis.ipynb`

**To save your Colab edits back to GitHub** (once you've filled in some TODOs):
1. In Colab: File → **Save a copy in GitHub**
2. Pick the repo, keep the path as `notebooks/01_churn_analysis.ipynb`, write a commit message
3. Click OK — this pushes directly, no terminal needed

This means you never *have* to touch git directly if you don't want to — Colab's "Save a copy in GitHub" button alone is enough to keep this repo updated. Option B above is worth learning anyway, because every software job assumes you know it.

## Making it portfolio-ready

Once you've filled in the TODOs:
- Add 2–3 sentences at the top of the README under a new "Results" heading — your best model's accuracy/AUC, and your one-line business takeaway from Section 8.
- Pin the repo on your GitHub profile (Profile → Customize your pins) so it's the first thing recruiters see.
- If you want it to *look* finished even before every TODO is done, that's fine — real projects show iteration. A repo with clear TODOs and a working baseline is more convincing than a suspiciously too-perfect one.
