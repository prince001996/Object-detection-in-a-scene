
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import time
import imutils
from pyimagesearch.panorama import Stitcher

#1 
left =cv2.VideoCapture("http://192.168.43.1:8080/video")
right =cv2.VideoCapture("http://192.168.43.180:8080/video")
a=0

while True:
    a=a+1
    #3
    left_check, left_frame = left.read()
    right_check, right_frame = right.read()
    # stitching code below this
    
    
    
    left_frame = cv2.resize(left_frame, (400,400))
    right_frame = cv2.resize(right_frame, (400,400))
    
    
    
    #stitching code above this
    #4
    cv2.imshow('left', left_frame)
    cv2.imshow('right', right_frame)
    #cv2.imshow("stitched_frame", stitched_frame)
    #time.sleep(1)
    #5
    key = cv2.waitKey(1)
    if(key==ord('q')):
        break
#2
print(a)
left.release()
right.release()
cv2.destroyAllWindows()

