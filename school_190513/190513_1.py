#반전
import numpy as np
import matplotlib.pyplot as plt
import imageio as io

img = io.imread('sample.jpg')
revImg = 255-img

plt.imshow(revImg)
plt.show()
#
# plt.imshow(revImg, cmap='grey')
# plt.show()
#
# for i in range(0, img.shape[0]):
#     for j in range(0, img.shape[1]):
#         img2[i,j] = img[i,j] + 100
#         if img2[i,j] > 255:
#             img2[i,j] = 255
#         if img2[i,n] < 0:
#             img2[i,j] = 0
#
# img2 = np.zeros((img.shape), dtype=np.int16)
#
#
#
#
# plt.imshow(img2, cmap='gray')
# plt.show()
#
#
#
#
