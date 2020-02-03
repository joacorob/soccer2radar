import cv2 as cv
import numpy as np
import math
img = cv.imread('data/circle3.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=1,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    p1 = [x1,y1]
    p2 = [x2,y2]
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    print(distance)
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv.imwrite('field.jpg',img)