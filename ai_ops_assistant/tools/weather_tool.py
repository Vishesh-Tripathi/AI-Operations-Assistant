import requests
import os
from tools.retry import retry

def _fetch_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )
    res = requests.get(url, timeout=5)
    res.raise_for_status()
    data = res.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }

def get_weather(city):
    return retry(lambda: _fetch_weather(city))
