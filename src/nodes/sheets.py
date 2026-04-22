import gspread
from src.state import AgentState
from src.utils.google_client import google_client

def sheets_managment(state: AgentState):
    sh = google_client()
    classes = state['class_list']
    students = state['students']
    existing_titles = [ws.title for ws in sh.worksheets()]

    for cls in classes:
        if cls not in existing_titles:
            worksheet = sh.add_worksheet(title=cls, rows=100, cols=100)
            data_to_write = [['Student Name', 'Grades']]

            for student in students:
                if student['class_name'] == cls:
                    data_to_write.append([student['student_name'], ""])

            worksheet.update('A1', data_to_write)
            print(f"Worksheet {cls} created with {len(data_to_write) - 1} students.")
            existing_titles.append(cls)
        else:
            print(f"Worksheet '{cls}' already exists. Skipping...")
