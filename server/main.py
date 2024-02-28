import asyncio
import datetime
from typing import Union

from fastapi import FastAPI
import socketio
from fastapi import BackgroundTasks


app = FastAPI()
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
socket_app = socketio.ASGIApp(sio)

app.mount("/", socket_app)


async def send_current_time():
    while True:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await sio.emit("message", current_time)
        await sio.sleep(1)


asyncio.create_task(send_current_time())


@sio.on("connect")
async def connect(sid, environ):
    sio.emit("message", "Hello! " + sid)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@sio.on("message")
async def message(sid, data):
    await sio.emit("message", "Hello! " + data)
