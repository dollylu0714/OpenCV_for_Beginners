"""
Gradient: is a directional change in the intensity or color in the image. 
- Laplacian
- Sobel
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./images/sudoku.png", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("./images/messi5.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)


titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'laplacian']
images = [img, lap, sobelX, sobelY, sobelCombined, laplacian]

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
