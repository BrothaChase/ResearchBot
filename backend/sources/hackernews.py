import httpx
import logging
from backend.models import ResearchResult

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"
logger = logging.getLogger(__name__) # recieve or create a logger 

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
        params=search_parameters,
        timeout=5.0
     )

     response.raise_for_status() # detects if the request failed and raises an exception

   # store caught exception in variable error
    except httpx.TimeoutException:
       logger.warning("Hacker News request timed out")
       return []

    except httpx.HTTPError as error:
       logger.error("Hacker News request failed: %s", error)
       return [] # return empty list on failure & immediately exit the function

    
    data = response.json()
    hits = data["hits"]
    
    results = normalize_hits(hits)
    return results


# temporary test code to verify the function works
results = search_hackernews("machine learning", 2);
print(results);
