from state import AgentState
from utils.supabase_client import get_supabase_client

def sync_grades_back_node(state: AgentState):
    incoming = state['grades']
    supabase = get_supabase_client()

    print(f"🔄 Syncing {len(incoming)} grades to Supabase...")

    for entry in incoming:
        student = entry.get('student_name')
        grade = entry.get('grade')

        if grade:
            try:
                response = (
                    supabase.table("school_data")
                    .update({"grade_note": grade})
                    .eq("student_name", student)
                    .execute()
                )
                pass
            except Exception as e:
                state['logs'].append({f"message": f"Error while trying to save grade, {e}"})

    return state
