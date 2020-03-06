import cv2
import json
from flask import g
from server_config import *
import os
import sys
import time
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))


# def testside(image, cropy, cropx):
#
#     time.sleep(0)
#     start = time.time()
#
#     topval = 0
#     bottomval = 0
#
#     while((time.time() - start) < 1):
#
#         cropsizey = (image.shape[0] * (1 - cropy)) / 2
#         cropsizex = (image.shape[1] * (1 - cropx)) / 2
#
#         startRow = int(cropsizey)
#         startCol = int(cropsizex)
#         endRow = int(image.shape[0] - cropsizey)
#         endCol = int(image.shape[1] - cropsizex)
#
#         image = image[startRow:endRow, startCol:endCol]
#
#         top = image[0:image.shape[0]/2]
#         bottom = image[image.shape[0]/2:image.shape[0]]
#
#         topmean = cv2.mean(top)[0]
#         bottommean  = cv2.mean(bottom)[0]
#
#         if (topmean > bottommean):
#             topval += 1
#         else:
#             bottomval += 1
#
#     if (topval < bottomval):
#         return "N"
#     else:
#         return "S"

def testside(cropy, cropx):
    time.sleep(0)
    start = time.time()

    topval = 0
    bottomval = 0

    ##take webcam feed
    cap = cv2.VideoCapture(0)

    while ((time.time() - start) < 5):

        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        if (ret == False):
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cropsizey = (image.shape[0] * (1 - cropy)) / 2
        cropsizex = (image.shape[1] * (1 - cropx)) / 2

        startRow = int(cropsizey)
        startCol = int(cropsizex)
        endRow = int(image.shape[0] - cropsizey)
        endCol = int(image.shape[1] - cropsizex)

        image = image[startRow:endRow, startCol:endCol]

        top = image[0:image.shape[0] / 2]
        bottom = image[image.shape[0] / 2:image.shape[0]]

        topmean = cv2.mean(top)[0]
        bottommean = cv2.mean(bottom)[0]

        print(topmean)
        print(bottommean)

        if (topmean > bottommean):
            topval += 1
        else:
            bottomval += 1
    cap.release()

    print(topval)
    print(bottomval)

    if (topval < bottomval):
        return "N"
    else:
        return "S"

@app.route("/start")
def start():
    print("Getting polar direction")
    data = {}
    data['polarity'] = testside(cv2.imread("1.png", 0), 0.85, 0.5)
    with open('stored.json', 'w') as outfile:
        json.dump(data, outfile)

    return "Got polar direction"


@app.route("/polar_direction")
def polar_direction():
    print("Returning polar direction")
    with open('stored.json') as json_file:
        data = json.load(json_file)
        return data['polarity']
