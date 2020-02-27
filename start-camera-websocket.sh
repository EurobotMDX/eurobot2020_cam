#!/bin/bash

python3 server.py &
python3 camera_client.py &
python3 robot_client.py
