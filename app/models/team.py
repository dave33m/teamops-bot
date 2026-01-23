from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    platform: Mapped[str] = mapped_column(String(32))  # telegram, slack
    external_id: Mapped[str] = mapped_column(String(128), unique=True)

    users = relationship("User", back_populates="team")
