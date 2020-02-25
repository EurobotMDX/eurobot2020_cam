#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json
import time
import camera_service.py

SERVER_URI = "ws://localhost:6789"
SLEEP_INTERVAL = 5

async def run_camera_client():
    print("Starting camera client...")
    async with websockets.connect(SERVER_URI) as websocket:
        while True:
            time.sleep(SLEEP_INTERVAL)   # Delays for x seconds.
            await websocket.send(json.dumps({"client":"camera", "message":"hello"}))


asyncio.get_event_loop().run_until_complete(run_camera_client())
