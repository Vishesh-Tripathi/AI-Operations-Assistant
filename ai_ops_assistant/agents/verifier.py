from llm.llm_client import call_llm
import json

VERIFIER_PROMPT = """
You are a Verifier Agent.

TASK:
- Validate execution results
- Ensure completeness
- Fix missing or incorrect information

STRICT RULES:
- Output ONLY valid JSON
- No explanations
- No markdown
- If something is missing, explain inside JSON fields

OUTPUT FORMAT:
{
  "summary": string,
  "data": object
}
"""

def verify(task, execution_results):
    response = call_llm(
        VERIFIER_PROMPT,
        f"User Task: {task}\nExecution Results: {execution_results}"
    )

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        # Fallback: never crash the app
        return {
            "summary": "Verifier returned non-JSON output",
            "raw_output": response,
            "data": execution_results
        }
