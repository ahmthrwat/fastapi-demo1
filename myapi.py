# get object called FastAPI from fastapi
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students={
    1:{"name":"ahmed",
       "age":17,
       "class":"12 years"}
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None



@app.get("/")
def index():
    return {"name":"First date"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The Id of the students you want to view", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-by-name1")
def get_student(name: Optional[str]=None):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int,name: Optional[str]=None):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id:int,student: Student):
    if student_id in students:
        return {"Error":"Students exists"}
    
    students[student_id]=student
    return students[student_id]


@app.put("update-student/{student_id}")
def update_student(student_id:int,student:Student):
    if student_id not in students:
        return {"Error":"Students not exists"}
    
    students[student_id]=student
    return students[student_id]

@app.delete("delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Students not exists"}
    
    del students[student_id]
    return {"Messgae":"Students deleted "}