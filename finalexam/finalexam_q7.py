from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from collections import defaultdict
import plotly.graph_objects as go

app = FastAPI()

# File containing student records
DATA_FILE = "students.txt"

# Dictionary to track HTTP status codes
status_counts = defaultdict(int)

# Student Model
class Student(BaseModel):
    student_id: int
    name: str
    marks: int

# Read students from file
def read_students():
    students = []
    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:       # skip blank lines
                    continue
                s_id, name, marks = line.split(",")
                students.append({
                    "student_id": int(s_id),
                    "name": name,
                    "marks": int(marks)
                })
    except FileNotFoundError:
        pass

    return students

# Middleware to track status codes
@app.middleware("http")
async def track_status_codes(request: Request, call_next):
    response = await call_next(request)
    status_code = response.status_code
    status_counts[status_code] += 1
    return response

# 1. GET /students/
@app.get("/students/")
def get_students():
    students = read_students()
    return students

# 2. POST /students/
@app.post("/students/", response_model=Student)
def add_student(student: Student):
    students = read_students()

    # Check if student_id already exists
    for s in students:
        if s["student_id"] == student.student_id:
            raise HTTPException(status_code=400, detail="Student ID already exists")

    # Append new student to file
    with open(DATA_FILE, "a") as f:
        f.write(f"{student.student_id},{student.name},{student.marks}\n")

    return student

# 4. GET /students/requests
@app.get("/students/requests", response_class=HTMLResponse)
def show_status_chart():
    if not status_counts:
        return "<h3>No requests have been made yet.</h3>"

    codes = list(status_counts.keys())
    counts = list(status_counts.values())

    fig = go.Figure(
        data=[go.Bar(
            x=codes,
            y=counts,
            text=counts,
            textposition="outside"
        )]
    )

    fig.update_layout(
        title="HTTP Status Code Requests",
        xaxis_title="Status Code",
        yaxis_title="Number of Requests",
        template="plotly_white"
    )

    return fig.to_html(full_html=True)