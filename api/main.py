from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fakedb = []

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None



@app.get("/")
def read_root():
    return {
        "greetings": "Welcome to LearnCodeOnline.in"
    }

@app.get("/courses")
def getCourses():
    return fakedb

@app.get("courses/{course_id}")
def getACourse(course_id: int):
    course = 
