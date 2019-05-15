#과제2 SIFT descriptor로 키포인트 추출 및 키포인트 매칭
import cv2

img1 = cv2.imread('sift_sample_1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('sift_sample_2.jpg', cv2.IMREAD_GRAYSCALE)

sift = cv2.xfeatures2d_SIFT.create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []

for m, n in matches:
    if m.distance < 1*n.distance:
        good.append([m])

out = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

cv2.imwrite('sift_keypoint_matched.jpg', out)