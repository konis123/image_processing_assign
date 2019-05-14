#과제2 히스토그램 평활화
import numpy as np
import matplotlib.pyplot as plt
import imageio as io

img = io.imread('low_contrast.jpg')
des = np.zeros((img.shape), dtype=np.int16)

des_value = np.zeros(256, dtype=np.uint8)

hist, bins = np.histogram(img.flatten(), 256, [0,256])
cdf = hist.cumsum()
print(cdf)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        des[i,j] = int( round(cdf[img[i,j]] / (800*800) * 255) )
        if des[i, j] > 255:
            des[i, j] = 255
        if des[i, j] < 0:
            des[i, j] = 0


plt.imshow(des, cmap='gray')
plt.show()




