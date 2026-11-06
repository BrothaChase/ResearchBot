import logging
from fastapi import FastAPI
from backend.models import SearchRequest
from backend.sources.hackernews import search_hackernews

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

app = FastAPI()

@app.get("/")
# Root endpoint for the API
def root():
 return {"message": "Research bot API is running." }

@app.get("/about")
def about():
 return {"sources": ["Hacker News", "arXiv"],"name": "Research bot" ,"version": "Test:1.0.0" ,"description": "Daily dose of research from various sources." }

@app.post("/search")
def search(request:SearchRequest):
 results = search_hackernews(request.query, request.limit)
 return {
  "query":request.query, 
  "limit": request.limit, 
  "results": results
 
  }
 