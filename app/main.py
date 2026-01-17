from fastapi import FastAPI
from app.adapters.telegram import router as telegram_router

app = FastAPI(title="TeamOps Bot")

app.include_router(telegram_router, prefix="/telegram")

@app.get("/health")
def health():
    return {"status": "ok"}
