from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_name():
    return {"Name": "Henrique Lopes"}