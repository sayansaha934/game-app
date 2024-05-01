from pydantic import BaseModel, HttpUrl


class CreateGameRequest(BaseModel):
    name:str
    url:HttpUrl
    author:str


class EditGameRequest(BaseModel):
    name:str
    url:HttpUrl
    author:str