from fastapi import APIRouter

router = APIRouter()



@router.post("/run_digest")
def run_digest():
    return {"status": "digest triggered (mock)"}