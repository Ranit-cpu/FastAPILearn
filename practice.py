from fastapi import FastAPI

myapp = FastAPI()

@myapp.get("/")
def index():
    return "Get mapped at /"

@myapp.get("/about")
async def about():
    return "Get mapped at /about"