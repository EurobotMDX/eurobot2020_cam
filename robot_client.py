#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json
import time

SERVER_URI = "ws://localhost:6789"
POLAR_DIRECTION = ""
SLEEP_INTERVAL = 1
IS_CONNECTED = False

async def run_robot_client():
    print("Starting robot client...")
    try:
        async with websockets.connect(SERVER_URI) as websocket:
            global POLAR_DIRECTION
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
            global IS_CONNECTED
            IS_CONNECTED = True
    except:
        print("No server found yet.")

#Try to start the camera every seconds until it has found the server
async def start_robot_client():
    while not IS_CONNECTED:
        print("Trying to connect the robot")
        await run_robot_client()
        await asyncio.sleep(SLEEP_INTERVAL)



asyncio.get_event_loop().run_until_complete(start_robot_client())
