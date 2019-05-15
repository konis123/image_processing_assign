#SIFT
import cv2

img = cv2.imread('sift_sample_1.jpg', cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d_SIFT.create()
kp, des = sift.detectAndCompute(img, None)

out = cv2.drawKeypoints(img, kp, img)
cv2.imwrite('sift_keypoint.jpg', out)
