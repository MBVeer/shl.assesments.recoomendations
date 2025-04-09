from fastapi import FastAPI, Request
from pydantic import BaseModel
from recommender import recommend_assessments

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/recommend")
def get_recommendations(input: InputText):
    results = recommend_assessments(input.text)
    return {"recommendations": results}
