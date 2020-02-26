#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json
import time

SERVER_URI = "ws://localhost:6789"
POLAR_DIRECTION = ""

async def run_robot_client():
    POLAR_DIRECTION = ""
    print("Starting robot client...")
    async with websockets.connect(SERVER_URI) as websocket:
        while POLAR_DIRECTION == "":
            # {"sender":"server", "message":"N"}
            data = await websocket.recv()

            message = json.loads(data)
            print(data)
            if(message["sender"] == "server"):
                POLAR_DIRECTION = message["message"]
                print("New direction received from server: ", POLAR_DIRECTION)
            else:
                logging.error("Not intended recipient: {}", data)



asyncio.get_event_loop().run_until_complete(run_robot_client())
