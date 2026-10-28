import httpx
from backend.models import ResearchResult

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"


def search_hackernews(query: str, limit: int):
    search_parameters = {
        "query": query,
        "hitsPerPage": limit
    }

    response = httpx.get(
        HN_SEARCH_URL, 
        params=search_parameters
     )

    data = response.json()
    hits = data["hits"]
        
    first_hit = hits[0]


    result = ResearchResult(
      title=first_hit["title"],
      authors=[first_hit["author"]],
      url=first_hit["url"],
      source="Hacker News",
      published_at=first_hit["created_at"],
      points=first_hit.get("points"),
    )
    return result
   # print(first_hit.keys())
   # print(first_hit["title"])
   # print(first_hit["author"])
   #  print(first_hit["url"])
   #  print(first_hit["points"])
   # print(first_hit["created_at"])

   # print(data.keys())


print(search_hackernews("cybersecurity", 2))