import httpx
from backend.models import ResearchResult

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"

# normalize the hits into a list of ResearchResult objects
def normalize_hits(hits):
  
 results = []

    # Skip results without an external article URL.
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
    
    try:      
      # talk to hacker news api and get results
     response = httpx.get(
        HN_SEARCH_URL, 
        params=search_parameters
     )

     response.raise_for_status() # detects if the request failed and raises an exception
   
    except httpx.HTTPError: 
      print("Hacker News request failed ")
      return [] # return empty list on failure & immediately exit the function

    
    data = response.json()
    hits = data["hits"]
    
    results = normalize_hits(hits)
    return results


# temporary test code to verify the function works
# results = search_hackernews("machine learning", 2);
# print(results);
