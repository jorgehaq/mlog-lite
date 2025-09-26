from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="MLOG-Lite",
    version="1.0.0",
    description="Centralized logging & analytics microservice"
)

app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "ok"}