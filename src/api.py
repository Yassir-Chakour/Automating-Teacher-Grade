from fastapi import FastAPI, Request
from src.graph import app
api = FastAPI()

@api.post("/start-setup")
async def start_setup():
    print("🚀 Remote Trigger: Starting Setup Mission...")

    initial_state = {
        "grades": [],
        "students": [],
        "class_list": [],
        "logs": []
    }

    app.invoke(initial_state)

    return {"status": "success", "message": "Setup mission started"}


@api.post("/sync-grades")
async def sync_grades(request: Request):
    data = await request.json()

    initial_input = {
        "grades": data.get('students', []),
        "logs": []
    }

    app.invoke(initial_input)

    return {"status": "success", "message": f"Sync started for {data.get('class_name')}"}
