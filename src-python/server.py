# -*- encoding:utf-8 -*-
import sys
from multiprocessing import Process, Queue, freeze_support

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

@sio.event
async def string_cv2server(sid, data):
    await sio.emit('string_server2client', data)

if __name__ == "__main__":
    freeze_support()
    message_queue = Queue()
    background_process = Process(target=background, args=(message_queue,), daemon=True)
    background_process.start()
    web.run_app(app, port=3000)
