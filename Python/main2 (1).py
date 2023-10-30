from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# uvicorn main2:app --reload
app = FastAPI()

users = {
    1: {
        'name': 'john',
        'email': 'bogdan.speaker@gmail.com',
        'phone': "+380671102626",
        'order': 1,
        'Ban': False
    }
}


class User(BaseModel):
    name: str
    email: str
    phone: str
    order: int
    Ban: bool


class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name ": "First Data"}


@app.get("/user/{user_id}")
def get_user(user_id: int = Path(None, description="введите id ученика", gt=-1)):
    return users[user_id]


user_id = 1


@app.post("/user/")
def create_user(user: User):
    global user_id
    user_id = user_id + 1
    if user_id in users:
        return {"error": "student exists"}
    users[user_id] = user
    user_id = user_id
    return users[user_id]


@app.put("/user/")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in user:
        return {"error": "student does not exists"}
    if user.name != None:
        user[user_id].name = user.name
    if user.age != None:
        user[user_id].age = user.age
    if user.year != None:
        user[user_id].year = user.year
    return user[user_id]


@app.delete("/user/")
def delete_user(user_id: int):
    if user_id not in users:
        return {"error": "student does not exists"}
    del users[user_id]
    return {"message": "student deleted successfully"}
