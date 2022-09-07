from multiprocessing import Process, Queue
import sys

import socketio
from aiohttp import web
from cv import background


sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

@sio.event
async def connect(sid, environ, auth):
    print("connect ", sid)
    sys.stdout.flush()

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)
    sys.stdout.flush()
    background_process.terminate()

@sio.event
async def image_cv2server(sid, data):
    await sio.emit('image_server2client', data)

if __name__ == "__main__":
    image_queue = Queue()
    background_process = Process(target=background, args=(image_queue,), daemon=True)
    background_process.start()
    web.run_app(app, port=3000)
