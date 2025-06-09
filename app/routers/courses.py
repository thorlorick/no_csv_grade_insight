from fastapi import APIRouter

router = APIRouter(prefix="/courses")

@router.get("/")
def get_courses():
    return {"courses": "placeholder"}

