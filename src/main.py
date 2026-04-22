from src.graph import app


def run_agent():
    initial_state = {
        "students": [],
        "class_list": [],
        "logs": []
    }

    print("🚀 --- AGENT STARTING ---")

    final_result = app.invoke(initial_state)

    print("✅ --- AGENT FINISHED ---")

    print(f"Processed {len(final_result['class_list'])} classes.")
    for log in final_result.get("logs", []):
        print(f"Log: {log}")


if __name__ == "__main__":
    run_agent()