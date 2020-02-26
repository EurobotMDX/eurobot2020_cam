# Camera Robot Websocket

## Getting Started

The Camera Robot Websocket is a three-ways communication using python websocket.

A client camera is waiting for the data from the camera service
(which reads the compass on the table). As it gets it, it pushes to the server
that then will push it to all the client robot registered on it.

## Install

```
cd <PROJECT_ROOT>
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```

## Start

On three different terminals
```
python3 server.py
```
```
python3 camera_client.py
```
```
python3 robot_client.py
```

## To Do

Make the camera work with the current code.
Current issue may be dued to the install dependancy of opencv.

Maybe: add some security check what client are trying to connect to the server.
Maybe hard code keys for each client that will then be checked by the server.
