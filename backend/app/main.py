from fastapi import FastAPI

app = FastAPI(title="Time-Pilot API")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "time-pilot"}
