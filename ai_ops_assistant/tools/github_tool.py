import requests
from tools.retry import retry

def _search_repos(query, limit):
    url = f"https://api.github.com/search/repositories?q={query}"
    res = requests.get(url, timeout=5)
    res.raise_for_status()

    items = res.json()["items"][:limit]

    return [
        {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        }
        for repo in items
    ]

def search_repos(query, limit):
    return retry(lambda: _search_repos(query, limit))
