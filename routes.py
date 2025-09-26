from fastapi import APIRouter
from app.models import EventIn, EventOut
from app.db import db
from bson import ObjectId
from collections import Counter

router = APIRouter()

@router.post("/events/", response_model=EventOut)
async def create_event(event: EventIn):
    doc = event.dict()
    result = await db.events.insert_one(doc)
    return {**doc, "id": str(result.inserted_id)}

@router.get("/events/")
async def list_events(limit: int = 50):
    cursor = db.events.find().sort("timestamp", -1).limit(limit)
    events = []
    async for e in cursor:
        e["id"] = str(e["_id"])
        del e["_id"]
        events.append(e)
    return {"items": events}

@router.get("/analytics/summary")
async def analytics_summary():
    cursor = db.events.find()
    actions = []
    async for e in cursor:
        actions.append(e.get("action"))
    summary = Counter(actions)
    return {"by_action": dict(summary), "total": len(actions)}