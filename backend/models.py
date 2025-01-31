from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __init__(self, **data):
        super().__init__(**data)
        if self.created_at is None:
            self.created_at = datetime.now()
