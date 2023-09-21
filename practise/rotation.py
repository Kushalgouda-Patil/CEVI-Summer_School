import cv2
import numpy as np
img=cv2.imread("C:\\Users\\kusha\\Desktop\\CEVI-Summer_School\\images\\lena.png",cv2.IMREAD_GRAYSCALE)
shape=img.shape
print(shape)
# cv2.imshow("new_img",img)
# cv2.waitKey(0)
# Translation
translation_matrix1=np.array(
    [
        [1,0,-shape[0]/2],
        [0,1,-shape[1]/2],
        [0,0,1]
    ]
)
rotation_matrix=np.array(
    [
        [np.cos(np.pi/4),-np.sin(np.pi/4),0],
        [np.sin(np.pi/4),np.cos(np.pi/4),0],
        [0,0,1]
    ]
)
diagonal_length=np.sqrt(shape[0]**2 + shape[1]**2)
translation_matrix2=np.array(
    [
        [1,0,int(diagonal_length/2)],
        [0,1,int(diagonal_length/2)],
        [0,0,1]
    ]
)
composition=translation_matrix2 @ (rotation_matrix @ translation_matrix1)

new_img=np.ones((int(diagonal_length),int(diagonal_length)),dtype=np.uint8)*255

for x in range(shape[0]):
    for y in range(shape[1]):
            co=np.array([
                [x],
                [y],
                [1]]) 
            new_co=composition @ co
            new_img[int(new_co[0]),int(new_co[1])]=img[x,y]
            if(x==0 and y==0):
                  print(new_co)


cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.imshow("image",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


