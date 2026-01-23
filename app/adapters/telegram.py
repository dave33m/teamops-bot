from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Team, User, Reminder
from app.core.parser import parse

router = APIRouter()


@router.post("/webhook")
async def telegram_webhook(req: Request, db: Session = Depends(get_db)):
    payload = await req.json()

    message = payload.get("message") or {}
    text = (message.get("text") or "").strip()

    chat = message.get("chat") or {}
    user = message.get("from") or {}

    chat_id = str(chat.get("id"))
    user_id = str(user.get("id"))
    name = user.get("first_name") or "User"

    # --- /start ---
    if text.startswith("/start"):
        team = db.query(Team).filter_by(
            platform="telegram", external_id=chat_id
        ).first()

        if not team:
            team = Team(platform="telegram", external_id=chat_id)
            db.add(team)
            db.flush()

        member = db.query(User).filter_by(
            team_id=team.id, external_id=user_id
        ).first()

        if not member:
            member = User(
                team_id=team.id,
                external_id=user_id,
                name=name,
            )
            db.add(member)

        db.commit()

        return {
            "method": "sendMessage",
            "chat_id": chat_id,
            "text": "TeamOps is ready. You can now schedule reminders."
        }

    # --- /remind ---
    cmd = parse(text)
    if cmd:
        team = db.query(Team).filter_by(
            platform="telegram", external_id=chat_id
        ).first()

        member = db.query(User).filter_by(
            team_id=team.id, external_id=user_id
        ).first()

        reminder = Reminder(
            team_id=team.id,
            user_id=member.id,
            message=cmd.message,
            run_at=cmd.run_at,
        )

        db.add(reminder)
        db.commit()

        return {
            "method": "sendMessage",
            "chat_id": chat_id,
            "text": f"Reminder set for {cmd.run_at.isoformat()}"
        }

    return {"ok": True}
