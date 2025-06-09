from fastapi import APIRouter

router = APIRouter(prefix="/grades")

@router.get("/")
def get_grades():
    return {"grades": "placeholder"}

