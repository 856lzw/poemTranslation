from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List


class Poem(BaseModel):
    # poem keyword: List[str] = Field(description="关键词",min_items=2,max_items=3)
    content: str = Field(description="古诗文的描述性文本")
