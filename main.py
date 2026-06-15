from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_follow_up

app = FastAPI()

class AnswerInput(BaseModel):
    answer: str

@app.post("/follow-up")
def get_follow_up(data: AnswerInput):
    return generate_follow_up(data.answer)