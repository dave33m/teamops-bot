from datetime import datetime
from sqlalchemy import String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    message: Mapped[str] = mapped_column(String(512))
    run_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    recurring: Mapped[bool] = mapped_column(Boolean, default=False)
    cron: Mapped[str] = mapped_column(String(64), nullable=True)

    fired: Mapped[bool] = mapped_column(Boolean, default=False)
