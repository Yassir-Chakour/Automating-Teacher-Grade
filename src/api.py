from fastapi import FastAPI, Request
from  graph import app

api = FastAPI()

@api.post("/sync-grades")
async def sync_grades(request: Request):
    data = await request.json()

    initial_input = {
        "grades": data.get('students', []),
        "students": [],
        "class_list": [],
        "logs": []
    }

    app.invoke(initial_input)

    return {"status": "success", "message": f"Sync started for {data.get('class_name')}"}
