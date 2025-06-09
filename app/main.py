from fastapi import FastAPI
from app.routers import users, grades, courses

app = FastAPI()

app.include_router(users.router)
app.include_router(grades.router)
app.include_router(courses.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

