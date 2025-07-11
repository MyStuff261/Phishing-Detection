from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from algorithm import analyze 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/classify")
async def classify(request: Request):
    data = await request.json()
    text = data.get("text", "")
    result = analyze(text)
    return {"message": result}
