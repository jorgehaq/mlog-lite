import pytest
import httpx
from app.main import app

@pytest.mark.anyio
@pytest.mark.parametrize("anyio_backend", ["asyncio"])
async def test_event_flow():
    from app.db import db
    await db.events.delete_many({})

    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://testserver") as client:
        payload = {"service": "axi", "user_id": "u1", "action": "login"}
        r = await client.post("/events/", json=payload)
        assert r.status_code == 200

        r2 = await client.get("/analytics/summary")
        assert r2.status_code == 200
        data = r2.json()
        assert "by_action" in data
        assert "login" in data["by_action"]
