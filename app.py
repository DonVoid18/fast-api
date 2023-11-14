from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
app = FastAPI()

posts = [

]

# POST MODEL
class Post(BaseModel):
  id: int
  title: str
  content: Optional[Text]
  created_at: datetime = datetime.now()
  published_at: datetime = datetime.now()
  published: bool

@app.get("/")
def read_root():
  return {"Hello": "World"}


# return los datos

@app.get("/posts")
def get_posts():
  return posts

# create post

@app.post("/posts")
def create_post(post: Post):
  print(post)
  posts.append(post)
  return post