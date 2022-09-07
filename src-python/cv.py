from multiprocessing import Process, Queue
import sys
import time
import base64

import cv2
import socketio
from aiohttp import web


def convert_image_to_jpeg(image):
    # Encode frame as jpeg
    frame = cv2.imencode('.jpg', image)[1].tobytes()
    # Encode frame in base64 representation and remove
    # utf-8 encoding
    frame = base64.b64encode(frame).decode('utf-8')
    return frame

def background(image_queue):
    sio = socketio.Client()
    sio.connect('http://localhost:3000')

    cap = cv2.VideoCapture('example.mp4')
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    while(True):
        frame_start_time = time.time()
        ret, frame = cap.read()
        if not ret:
            # play again
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        # do something with frame

        scale_factor = 0.25
        new_width, new_height = int(width * scale_factor), int(height * scale_factor)
        frame = cv2.resize(frame, (new_width, new_height))
        jpeg = convert_image_to_jpeg(frame)
        # if the data sent is too large,
        # the process will be killed without any error message
        sio.emit('image_cv2server', jpeg)
        frame_remain_time = time.time() - frame_start_time
        if (frame_remain_time < 1/fps):
            time.sleep(1/fps - frame_remain_time)
