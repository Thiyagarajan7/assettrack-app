from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ui():
    return {"msg": "Web UI running"}
