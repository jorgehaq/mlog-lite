from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

class EventIn(BaseModel):
    service: str
    user_id: str
    action: str
    metadata: Optional[Dict] = None
    timestamp: datetime = datetime.utcnow()

class EventOut(EventIn):
    id: str
