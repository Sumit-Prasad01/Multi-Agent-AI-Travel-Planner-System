from tavily import TavilyClient
from src.config import settings

client = TavilyClient(
    api_key = settings.TAVILY_API_KEY
)

def tavily_search(query : str, max_results : int = 5) -> str:

    response = client.search(
        query = query,
        max_results = max_results
    )

    results = []

    for i, r in enumerate(response['results'], 1):
        title = r.get("title", "unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()

        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)