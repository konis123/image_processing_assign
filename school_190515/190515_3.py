#CV로 blur처리(mean filter)
import numpy as np
import cv2

img = cv2.imread('sample.jpg', cv2.IMREAD_REDUCED_COLOR_2)
blurred = cv2.blur(img, (3,3))
outImg = np.hstack((img, blurred))
cv2.imshow("output!", outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()