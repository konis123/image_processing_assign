#CV로 blur처리(salt&pepper noise 제거)
import numpy as np
import cv2

img = cv2.imread('sp_noise.jpg', cv2.IMREAD_REDUCED_COLOR_2)
blurred = cv2.medianBlur(img, 5)
outImg = np.hstack((img, blurred))
cv2.imshow("Noise reduction Result!", outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()