from fastapi import FastAPI
from pydantic import BaseModel
from translator import translate_text

app = FastAPI()

class RequestModel(BaseModel):
    text: str
    to: str = "pt"

@app.post("/translate")
def translate(req: RequestModel):
    return {"translated": translate_text(req.text, req.to)}
