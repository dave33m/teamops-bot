from datetime import datetime
from dataclasses import dataclass


@dataclass
class RemindCommand:
    message: str
    run_at: datetime


def parse(text: str):
    if not text.startswith("/remind"):
        return None

    try:
        _, rest = text.split("/remind", 1)
        body, when = rest.split(" at ")
        message = body.strip()
        run_at = datetime.fromisoformat(when.strip())
        return RemindCommand(message=message, run_at=run_at)
    except Exception:
        return None
