import json
from llm.llm_client import call_llm

PLANNER_PROMPT = """
You are a Planner Agent.

Your job:
Convert the user task into a step-by-step execution plan.

STRICT RULES:
- Output ONLY valid JSON
- No markdown, no explanations

TOOL INPUT REQUIREMENTS:
- weather tool MUST include: { "city": "<city_name>" }
- github tool MUST include: { "query": "<search_term>" }
- news tool MUST include: { "topic": "<topic_name>" }

JSON SCHEMA:
{
  "steps": [
    {
      "step_id": number,
      "action": string,
      "tool": "weather" | "github" | "news" | null,
      "input": object
    }
  ]
}
"""

def create_plan(user_task):
    response = call_llm(PLANNER_PROMPT, user_task)
    return json.loads(response)
