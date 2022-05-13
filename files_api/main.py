import uvicorn
from fastapi import FastAPI, UploadFile
from db import Database
import aiohttp

app = FastAPI()


@app.get("/")
async def root():
    return {"title": "Files Api"}


@app.post("/scan-file")
async def add_file(file: UploadFile):
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "https://beta.nimbus.bitdefender.net:443/liga-ac-labs-cloud/blackbox-scanner/",
                data={'file': await file.read()}) as resp:
            res = await resp.json()
            print(res)
            db = Database()
            await db.insert_data(res)
            return res


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
