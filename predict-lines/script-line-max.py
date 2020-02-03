import cv2 as cv
import numpy as np
import math
img = cv.imread('data/circle3.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=1,maxLineGap=10)
max_x1 = 0
max_x2 = 0
max_y1 = 0
max_y2 = 0
max_distance = 0
for line in lines:
    x1,y1,x2,y2 = line[0]
    p1 = [x1,y1]
    p2 = [x2,y2]
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    if distance > max_distance:
        max_x1 = x1
        max_x2 = x2
        max_y1 = y1
        max_y2 = y2
        max_distance = distance
        print(distance)
        cv.line(img,(max_x1,max_y1),(max_x2,max_y2),(0,255,0),2)

cv.imwrite('field.jpg',img)