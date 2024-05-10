from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello12": "World :D"}