from fastapi import FastAPI
from backend.models import SearchRequest

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
 return {"query":request.query, "limit": request.limit}