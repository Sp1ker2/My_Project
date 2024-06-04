import uvicorn
from fastapi import FastAPI
from app.database import  engine
from app import models
from app.routers import authors, categories, tags, posts

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(authors.router)
app.include_router(categories.router)
app.include_router(tags.router)
app.include_router(posts.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


