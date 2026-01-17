from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(req: Request):
    payload = await req.json()
    return {"ok": True}
