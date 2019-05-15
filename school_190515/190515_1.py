#과제1 마스크씌우기
import numpy as np
import imageio as io

kernel = np.array([[1,1,1], [1,1,1], [1,1,1]])

read = io.imread('sample.jpg')

img = np.array(read, dtype=np.int32)

outImg = np.zeros(img.shape, dtype=np.uint8)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if i == 0 or i == img.shape[0]-1:
            outImg[i, j] = img[i, j]
        elif j == 0 or j == img.shape[1]-1:
            outImg[i, j] = img[i, j]
        else:
            outImg[i, j] = (kernel[0,0]*img[i-1,j-1] + kernel[0, 1]*img[i-1, j] + kernel[0, 2]*img[i-1,j+1]
                            + kernel[1,0]*img[i,j-1] + kernel[1, 1]*img[i, j] + kernel[1, 2]*img[i,j+1]
                            + kernel[2,0]*img[i+1,j-1] + kernel[2, 1]*img[i+1, j] + kernel[2, 2]*img[i+1,j+1])/9


io.imwrite('output.jpg', outImg)