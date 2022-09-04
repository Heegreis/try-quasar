import sys
from time import sleep
import socketio
from aiohttp import web
import multiprocessing as mp


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

def background():
    count = 0
    while True:
        count += 1
        print(f'This is python background {count}')
        sys.stdout.flush()
        sleep(1)

if __name__ == "__main__":
    web.run_app(app, port=3000)
    print('background')
    sys.stdout.flush()
    background()
