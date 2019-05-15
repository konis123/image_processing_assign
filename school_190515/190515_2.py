#CV로 히스토그램 평활화
import numpy as np
import cv2

img = cv2.imread('low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
outImg = np.hstack((img, equ))
cv2.imshow("Equalization by openCV", outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()