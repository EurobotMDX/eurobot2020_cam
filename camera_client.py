#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json
import time
import camera_service
import cv2

SERVER_URI = "ws://localhost:6789"
SLEEP_INTERVAL = 2
is_connected = False

async def run_camera_client():
    print("Starting camera client...")
    try:
        async with websockets.connect(SERVER_URI, ping_interval=None) as websocket:
            await asyncio.sleep(SLEEP_INTERVAL)   # Delays for x seconds.

            direction = camera_service.testside(cv2.imread("1.png", 0), 0.85, 0.5)
            await websocket.send(json.dumps({"client":"camera", "message":direction}))

            global is_connected
            is_connected = True
    except:
        print("No server found yet.")

#Try to start the camera every seconds until it has found the server
async def start_camera_client():
    while not is_connected:
        print("Trying to connect the camera")
        await run_camera_client()
        await asyncio.sleep(SLEEP_INTERVAL)


asyncio.get_event_loop().set_debug(True)
asyncio.get_event_loop().run_until_complete(start_camera_client())

# asyncio.get_event_loop().create_task(run_camera_client())
# asyncio.get_event_loop().run_forever()
