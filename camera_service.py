import cv2

def testside(image, cropy, cropx):
    cropsizey = (image.shape[0] * (1 - cropy)) / 2
    cropsizex = (image.shape[1] * (1 - cropx)) / 2

    startRow = int(cropsizey)
    startCol = int(cropsizex)
    endRow = int(image.shape[0] - cropsizey)
    endCol = int(image.shape[1] - cropsizex)

    image = image[startRow:endRow, startCol:endCol]

    top = image[0:image.shape[0]//2]
    bottom = image[image.shape[0]//2:image.shape[0]]

    topval = cv2.mean(top)
    bottomval = cv2.mean(bottom)

    print(topval)
    print(bottomval)

    if (topval < bottomval) :
        return "N"
    else :
        return "S"


##take webcam feed
#cap = cv2.VideoCapture(0)

#while(True):
#    # Capture frame-by-frame
#    ret, frame = cap.read()
#
#    if (ret == False) :
#	break
#
#    # Our operations on the frame come here
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#    # Display the resulting frame
#    print(testside(gray, 0.25, 0.25))
#
## When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()

# take an image
# print(testside(cv2.imread("1.png", 0), 0.85, 0.5))
