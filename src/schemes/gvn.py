from pydantic import BaseModel, Field

class Govna(BaseModel):
    von: bool = Field(default=True)
    color: str
    vkusnost: int = Field(ge=-3,le=10)
    count: int =  Field(ge=0, le=999)

class MisieGovna(BaseModel):
    von: bool = Field(default=True)
    color: str
    vkusnost: int
    zvozd: int