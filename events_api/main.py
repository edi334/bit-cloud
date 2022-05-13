import uvicorn
from fastapi import FastAPI
from models import Response, Event, BaseResponse
from db import Database

app = FastAPI()


@app.get("/")
async def root():
    return {"title": "Events Api"}


@app.post("/events", response_model=Response)
async def add_event(event: Event) -> Response:
    db = Database()
    risk = await db.find_data(key=event.file.file_hash)
    r = risk['risk_level'] if risk is not None else -1
    return Response(file=BaseResponse(hash=event.file.file_hash, risk_level=r),
                    process=BaseResponse(hash=event.last_access.hash, risk_level=r))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8010)
