from fastapi import FastAPI

app = FastAPI()
@app.get("/")

# Root endpoint for the API
def root():

 return {"message": "Research bot API is running." }

@app.get("/about")

def about():

 return {"sources": ["Hacker News", "arXiv"],"name": "Research bot" ,"version": "Test:1.0.0" ,"description": "Daily dose of research from various sources." }