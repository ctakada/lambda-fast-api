from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}


@app.get("/health")
async def health_check():
    return {"status": "OK"}

handler = Mangum(app)
