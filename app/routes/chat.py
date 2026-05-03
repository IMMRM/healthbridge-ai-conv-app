from fastapi import APIRouter
from pydantic import BaseModel
from utils.intent_classifier import route_query

router = APIRouter()

class UserRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(req: UserRequest):
    response = route_query(req.message)
    return {"response": response}
