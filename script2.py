import cv2 as cv2
import numpy as np
import math

img = cv2.imread('data/field4.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 15  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50  # minimum number of pixels making up a line
max_line_gap = 20  # maximum gap in pixels between connectable line segments
line_image = np.copy(img) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                    min_line_length, max_line_gap)

print(lines)
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
        cv2.line(img,(max_x1,max_y1),(max_x2,max_y2),(0,255,0),2)

cv2.imwrite('field.jpg',img)