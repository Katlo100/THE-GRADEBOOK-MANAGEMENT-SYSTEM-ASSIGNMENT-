# Gradebook web app

This repository includes a Flask website for managing students and their grades. The existing `Section ... .py` files are standalone command-line assignment versions; the website is started from `app.py`.

## Run locally

Requires Python 3.10 or later.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>. Add students, record subject grades (0–100), and view each student's grade count and average. Student records are stored in `instance/gradebook.sqlite3` by default. You can set `DATABASE_PATH` to use another SQLite file.

## Deploy on Render

1. Push this branch to GitHub and merge it into `main` (or deploy this branch directly).
2. In Render, choose **New → Blueprint**, connect this repository, and select the branch containing `render.yaml`.
3. Accept the Blueprint configuration. Render will build the app and provide its public URL when deployment finishes.
4. Open the URL and confirm the page loads. The `/health` endpoint should return `{"status":"ok"}`.

The Blueprint creates a free web service and generates a `SECRET_KEY`. The free service's local filesystem is temporary, so its SQLite records can be lost when the service restarts or is redeployed. For persistent grade data, attach persistent storage and set `DATABASE_PATH` to a file on that storage, or connect the app to a managed database before using it for real student records. Keep student information private and use an appropriate hosting plan and access controls for real data.
