from src.state import AgentState

def proccess_data_node(state: AgentState):
    print("--- 🛠️ PROCESSING DATA & IDENTIFYING CLASSES ---")
    students = state["students"]

    unique_classes = {student["class_name"] for student in students}

    return {"class_list": list(unique_classes)}