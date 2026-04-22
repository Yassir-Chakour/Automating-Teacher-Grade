from typing import Literal
from src.state import AgentState
from langgraph.graph import StateGraph, START, END
from src.nodes.database import fetch_students_node
from src.nodes.processor import proccess_data_node
from src.nodes.sheets import sheets_managment
from src.nodes.updater import sync_grades_back_node

def route_start(state: AgentState) -> Literal["fetch_data", "sync_grades"]:
    if state.get('grades') and len(state['grades']) > 0:
        return "sync_grades"
    return "fetch_data"

workflow = StateGraph(AgentState)

workflow.add_node("fetch_data", fetch_students_node)
workflow.add_node("proccess_classes", proccess_data_node)
workflow.add_node("sync_sheets", sheets_managment)
workflow.add_node("sync_grades", sync_grades_back_node)

workflow.add_conditional_edges(START, route_start)

workflow.add_edge("fetch_data", "proccess_classes")
workflow.add_edge("proccess_classes", "sync_sheets")
workflow.add_edge("sync_sheets", END)

workflow.add_edge("sync_grades", END)

app = workflow.compile()
