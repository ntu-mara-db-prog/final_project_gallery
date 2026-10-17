# Final Project Gallery

A Streamlit gallery of the 14 NTU-MARA Database & Programming group final projects.

## Adding a team's link

Edit `projects.py` and fill in that group's `app_url` (and optionally `repo_url`; `members` are GitHub usernames). A project with an empty `app_url` shows as **Coming soon**. Commit and push; Streamlit Cloud redeploys automatically.

## Adding a screenshot

Drop the image into `screenshots/` named by group number, e.g. `screenshots/group-03.png` (`.png`, `.jpg`, `.jpeg` or `.webp`). It's cropped to 16:9 from the top automatically; without one, the card shows a placeholder.

## Run locally

Dependencies are managed with [uv](https://docs.astral.sh/uv/).

```bash
uv sync                       # create .venv and install from uv.lock
uv run streamlit run app.py
```

Add or upgrade a package:

```bash
uv add plotly                 # add a dependency (updates pyproject.toml and uv.lock)
uv lock --upgrade-package streamlit
```

Always commit `uv.lock` — Streamlit Cloud installs from it.

## Deploy to Streamlit Community Cloud

1. Push these files to the root of `ntu-mara-db-prog/final_project_gallery`.
2. At [share.streamlit.io](https://share.streamlit.io), choose **Create app** → pick the repo, branch `main`, main file `app.py`.
3. Under **Advanced settings**, set Python to **3.12** to match `.python-version`.
4. Optionally set a custom subdomain (e.g. `ntu-mara-gallery`).

Don't add a `requirements.txt` alongside `uv.lock`; Cloud uses only one dependency file, and `uv.lock` takes priority.

## Files

| File | Purpose |
|---|---|
| `app.py` | The gallery page |
| `projects.py` | Project list — the only file you need to edit |
| `screenshots/` | One image per group (`group-01.png` … `group-14.png`) |
| `pyproject.toml` | Project metadata and dependencies |
| `uv.lock` | Exact pinned versions (used by Streamlit Cloud) |
| `.python-version` | Python version for uv |
| `.streamlit/config.toml` | Theme |
