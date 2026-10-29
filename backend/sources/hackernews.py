import httpx
from backend.models import ResearchResult

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"

# normalize the hits into a list of ResearchResult objects
def normalize_hits(hits):
  
 results = []
    
 for hit in hits:
     if hit.get("url") is None:
        continue
     
     result = ResearchResult(
      title=hit.get("title") or "No title",
      authors=[hit.get("author") or "Unknown"],
      url=hit["url"],
      source="Hacker News",
      published_at=hit.get("created_at"),
      points=hit.get("points"),
    )
     results.append(result)
    
 return results


# get raw data
def search_hackernews(query: str, limit: int):
    search_parameters = {
        "query": query,
        "hitsPerPage": limit
    }
# talk to hacker news api and get results
    response = httpx.get(
        HN_SEARCH_URL, 
        params=search_parameters
     )

    data = response.json()
    hits = data["hits"]
    
    results = normalize_hits(hits)
    return results





