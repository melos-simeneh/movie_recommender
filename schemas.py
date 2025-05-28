from pydantic import BaseModel

class MovieRequest(BaseModel):
    title: str
    num_recs: int = 5
