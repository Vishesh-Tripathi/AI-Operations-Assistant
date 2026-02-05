from fastapi import FastAPI
from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify

app = FastAPI()

@app.post("/run")
def run_task(task: str):
    plan = create_plan(task)
    execution = execute_plan(plan)
    final_output = verify(task, execution)

    return {
        "plan": plan,
        "execution": execution,
        "final_output": final_output
    }
