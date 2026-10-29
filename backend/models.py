from pydantic import BaseModel, Field
from datetime import datetime

class SearchRequest(BaseModel):
    query: str = Field(min_length= 1, max_length = 200)
    limit: int = Field(default= 10, ge= 1, le= 50)


class ResearchResult(BaseModel):
    title: str
    authors: list[str]
    url: str
    source: str
    published_at: datetime | None = None
    points: int | None = None
    score: int = 0
    