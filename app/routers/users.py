from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/me")
def get_user():
    return {"user": "placeholder"}
