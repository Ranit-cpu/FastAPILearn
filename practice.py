from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

myapp = FastAPI()

@myapp.get("/blog")             # Path operation Decorator
def index(limit = 10, published:bool = True, sort: Optional[str] = None):
    #return published
    if published:
        return {f'List of {limit} blogs {published}'}
    else:
        return {f'List of {limit} blogs'}

@myapp.get('/blog/unpublished')
async def unpublished():
    return {'All Unpublished blogs are listed here'}

@myapp.get('/blog/{id}')
async def show(id:int):
    # fetch blog with id = id
    return {'Id =': id}

@myapp.get('/blog/{id}/comments')
async def comments(id:int):
    # fetch blog comments with id = id
    return {f'data = comments of ':id}


class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]

@myapp.post('/blog')
async def create_blog(request:Blog):
    return {f'Blog is created with title {request.title}, with body {request.body} and published at {request.published_at}'}
