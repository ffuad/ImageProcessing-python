# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:10:18 2022

@author: mthff
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

point = (0,0)
def click_event(event, x, y, flags, params):
    global point
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        point = (x,y)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
        point = (x,y)
    
    


img = cv2.imread('aa.jpg', 0)
img1 = cv2.resize(img, (400, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('image', img1)   
cv2.setMouseCallback('image', click_event)  
cv2.waitKey(0) 
cv2.destroyAllWindows()

#point = click_event(event, x, y, flags, params)

B = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

plt.title("kernel")
plt.imshow(B, cmap="gray")
plt.show()

A = img1
A = 1.0*(A > 150)
plt.title("Input Image")
plt.imshow(A, cmap="gray")
plt.show()


X = np.zeros((A.shape[0],A.shape[0]), 'float64')
X[point[0]  , point[1]] = 255
plt.title("X image")
plt.imshow(X, cmap='gray')

A_C = np.zeros((A.shape[0],A.shape[0]), 'float64')
A_C = 255 - A
plt.title('A_C')
plt.imshow(A_C, cmap="gray")
plt.show()

Xp = X

#print(A_C)
while(1):
    
    dia = cv2.dilate(X, B, iterations = 3)
# =============================================================================
#     plt.title('dilation')
#     plt.imshow(dia, cmap = 'gray')
#     plt.show() 
#     
# =============================================================================
    X = cv2.bitwise_and(dia, A_C)
    
    if (Xp == X).all():
        break
    Xp = X    
# =============================================================================
#     plt.title('Xp')
#     plt.imshow(Xp, cmap = 'gray')
#     plt.show()
#     
# =============================================================================
 
plt.title('X')
plt.imshow(X, cmap = 'gray')
plt.show() 
out =  X.copy()
out = cv2.bitwise_or(out, A)
#out[:,:] = np.where(X[:][:]==255, 0, 255)

plt.title('output')
plt.imshow(out, cmap = 'gray')
plt.show