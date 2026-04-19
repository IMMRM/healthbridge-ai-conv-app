from fastapi import FastAPI
from pydantic import BaseModel
from utils.intent_classifier import route_query

app = FastAPI()

class UserRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: UserRequest):
    response = route_query(req.message)
    return {"response": response}