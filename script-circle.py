import cv2 as cv
import numpy as np
import math
img = cv.imread('data/circle3.png')
output = img.copy()
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# detect circles in the image
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.2, 100)
 
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
 
    # loop over the (x, y) coordinates and radius of the circles
    r_max = 0
    y_max = 0
    x_max = 0
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        if r > r_max:
            x_max = x
            y_max = y
            r_max = r

    cv.circle(output, (x_max, y_max), r_max, (0, 255, 0), 4)
    cv.rectangle(output, (x_max - 5, y_max - 5), (x_max + 5, y_max + 5), (0, 128, 255), -1)
 
    # show the output image
    cv.imwrite('field-circle.jpg',output)