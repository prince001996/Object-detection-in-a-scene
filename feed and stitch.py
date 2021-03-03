import cv2
import numpy as np
import time
import imutils
from pyimagesearch.panorama import Stitcher

left =cv2.VideoCapture("http://192.168.43.1:8080/video")
right =cv2.VideoCapture("http://192.168.43.180:8080/video")
while True:
    start = time.time()
    left_check, left_frame = left.read()
    right_check, right_frame = right.read()
    # stitching code below this
    


    
    # load the two images and resize them to have a width of 400 pixels
    # (for faster processing)
    imageA = left_frame
    imageB = right_frame
   
    imageA = imutils.resize(imageA, width=400)
    imageB = imutils.resize(imageB, width=400)

    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

    
    cv2.imshow("Image A", imageA)
    cv2.imshow("Image B", imageB)
    cv2.imshow("Result", result)
    end = time.time()
    print(end - start)
    #time.sleep(1)
    key = cv2.waitKey(1)
    if(key==ord('q')):
        break

left.release()
right.release()
cv2.destroyAllWindows()

