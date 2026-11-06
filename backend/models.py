from pydantic import BaseModel, Field
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class SearchRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True) # strip whitespace from string fields

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
    