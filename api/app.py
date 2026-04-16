from fastapi import FastAPI
from prometheus_client import generate_latest
from common.metrics import REQ

app = FastAPI()

@app.get("/")
def home():
    REQ.inc()
    return {"msg": "API OK"}

@app.get("/metrics")
def metrics():
    return generate_latest()
