from tools.weather_tool import get_weather
from tools.github_tool import search_repos
from tools.news_tool import get_news

def execute_plan(plan):
    results = []

    for step in plan["steps"]:
        tool = step.get("tool")
        inp = step.get("input", {})

        try:
            if tool == "weather":
                city = inp.get("city")
                if not city:
                    raise ValueError("Missing city for weather tool")
                result = get_weather(city)

            elif tool == "github":
                query = inp.get("query")
                limit = inp.get("limit", 20)
                if not query:
                    raise ValueError("Missing query for github tool")
                result = search_repos(query, limit)
            
            elif tool == "news":
                topic = inp.get("topic")
                if not topic:
                    raise ValueError("Missing topic for news tool")
                result = get_news(topic)

            else:
                result = {"message": "No tool required"}

        except Exception as e:
            result = {
                "error": str(e),
                "tool": tool,
                "input": inp
            }

        results.append({
            "step_id": step["step_id"],
            "result": result
        })

    return results
