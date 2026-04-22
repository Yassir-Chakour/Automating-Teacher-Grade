from src.utils.supabase_client import get_supabase_client
from src.state import AgentState

def fetch_students_node(state: AgentState):
    print("--- 🔍 FETCHING STUDENTS FROM DATABASE ---")
    supabase = get_supabase_client()

    try:
        query = supabase.table("school_data").select("student_name, class_name")
        students = query.execute()

        print(f"Successfully fetched {len(students.data)} students")
        return {"students": students.data}

    except Exception as e:
        print(f"Failed to fetch students from database: {e}")
        return {"students": []}
