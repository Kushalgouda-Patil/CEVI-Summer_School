import cv2
import numpy as np
img=np.zeros((300,300),np.uint8)
img2=np.ones((300,300),np.uint8)
img2[:,150:]*=255
img3=np.ones((300,300),np.uint8)
for i in range(300):
    for j in range(300):
        if j>=i and j<300-i :
            img3[i][j]*=255
        elif i>=j and j>300-i:
            img3[i][j]*=255
        else:
            img3[i][j]*=0

img4=np.clip((np.random.randn(300,300)*100).astype(np.uint8),0,255)
#Y = 0.299 R + 0.587 G + 0.114 B
img5=cv2.imread("balloon.jpg")
cv2.imshow("img",img5)
cv2.waitKey(0)
'''
01  02 03 04 05
11 12 13 14 15
21 22 23 24 25
31 32 33 34 35
41 42 43 44 45'''