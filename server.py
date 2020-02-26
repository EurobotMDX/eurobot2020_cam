#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets

logging.basicConfig()

STATE = {"value": 0}

CLIENTS = set()

MESSAGE = "undefined"


async def notify_direction(message):
    if CLIENTS:  # asyncio.wait doesn't accept an empty list
        data = json.dumps({"sender": "server", "message": message})
        await asyncio.wait([client.send(data) for client in CLIENTS])


async def register(websocket):
    CLIENTS.add(websocket)


async def unregister(websocket):
    CLIENTS.remove(websocket)


async def handler(websocket, path):
    print("Starting Server ...")
    await register(websocket)
    try:
        # {"sender":"camera", "message":"N"}
        async for message in websocket:
            data = json.loads(message)
            if data["client"] == "camera":
                print("I will send dat to the robot ", data["message"])
                await notify_direction(data["message"])
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)


start_server = websockets.serve(handler, "localhost", 6789)

asyncio.get_event_loop().set_debug(True)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
