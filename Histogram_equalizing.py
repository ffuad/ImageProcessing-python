# -*- coding: utf-8 -*-
"""
@author: mthff
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
Histogram equalize 
freq[]
prob[] = freq/dim*dim
cdf[] = 0 to i
cdf*255
round(cdf)
mapping
"""

img =  cv2.imread('histogram.jpg', cv2.IMREAD_GRAYSCALE)
#plt.hist(img.ravel(), 256, [0, 256])


height, width = img.shape

freq = np.zeros(256, dtype = np.int32)
prob = np.zeros(256, dtype = np.float32)
cdf = np.zeros(256, dtype = np.float32)

for i in range(height):
    for j in range(width):
        freq[img[i][j]] += 1

N = height * width
for i in range(255):
    prob[i] = freq[i]/N

cdf[0] = prob[0]*255
for i in range(1,255):
    cdf[i] = cdf[i-1] + prob[i]*255

for i in range(255):
    cdf[i] = round(cdf[i])

result = img.copy()
for i in range(height):
    for j in range(width):
        result[i][j] = cdf[img[i][j]]
plt.title("output")    
plt.imshow(result, cmap="gray")
plt.show()

plt.hist(result.ravel(), 256, [0, 256])


