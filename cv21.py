import cv2

x=cv2.imread(".\\input.png")
print(type(x),x.shape)
cv2.imshow("X",x)
cv2.waitKey(0)

