# 🏫 Ismagi School Agent

A professional grading automation that bridges a Google Spreadsheet with a Supabase backend. It uses a Python agent to handle complex logic, sheet management, and database syncing.



## 🛠 How it Works

1.  **Initialize:** The teacher triggers a setup from the custom menu. The agent fetches student data from Supabase and builds the class tabs.
2.  **ID-Based Sync:** Every student row is assigned a unique Supabase ID. This acts as a primary key so that grades are always mapped to the correct person, even if names are edited.
3.  **Background Processing:** Tasks are handled as FastAPI `BackgroundTasks` to avoid the 60-second execution limit in Google Apps Script.

## 🚀 Tech Stack

* **Backend:** Python 3.12 + FastAPI + LangGraph
* **Database:** Supabase (PostgreSQL)
* **Infrastructure:** Hetzner VPS + Ubuntu 24.04
* **Deployment:** Coolify (Self-hosted PaaS)
* **Integrations:** Google Sheets API + Google Apps Script

## 📁 Repository Layout

* `/src`: Core Python logic and LangGraph nodes.
* `/apps_script`: JavaScript code for the Google Sheet side.
* `pyproject.toml`: Managed by Poetry.

## ⚙️ Deployment Settings (Coolify)

To deploy this on Coolify, use the following configuration:

* **Build Pack:** Nixpacks
* **Install Command:** `python -m venv --copies /opt/venv && . /opt/venv/bin/activate && pip install poetry && poetry config virtualenvs.create false && poetry install --no-root`
* **Start Command:** `poetry run fastapi run src/api.py --port 8000 --host 0.0.0.0`
* **Exposed Port:** `8000`

## 🔑 Environment Variables

Create a `.env` file with the following keys:
* `SUPABASE_URL`
* `SUPABASE_KEY`
* `SPREADSHEET_ID`

**Note:** `credentials.json` is not stored in Git. For production, it must be added via Coolify's Persistent Storage at `/app/credentials.json`.