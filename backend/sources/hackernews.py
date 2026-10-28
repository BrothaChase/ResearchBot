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

    results = []
    for hit in hits:
     result = ResearchResult(
      title=hit["title"],
      authors=[hit["author"]],
      url=hit["url"],
      source="Hacker News",
      published_at=hit["created_at"],
      points=hit.get("points"),
    )
     results.append(result)
    

    print(type(results))
    print(len(results))
    print(type(results[0]))
    return results
  
   # print(first_hit.keys())
   # print(first_hit["title"])
   # print(first_hit["author"])
   #  print(first_hit["url"])
   #  print(first_hit["points"])
   # print(first_hit["created_at"])

   # print(data.keys())


search_hackernews("cybersecurity", 2)