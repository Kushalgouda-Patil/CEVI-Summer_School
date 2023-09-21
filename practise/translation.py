import cv2
import numpy as np
img=cv2.imread("C:\\Users\\kusha\\Desktop\\CEVI-Summer_School\\images\\lena.png",cv2.IMREAD_GRAYSCALE)

# # Translation
# translation_matrix=np.array(
#     [
#         [1,0,50],
#         [0,1,0],
#         [0,0,1]
#     ]
# )
# shape=img.shape
# new_img=np.zeros(shape)

# for i in range(shape[0]):
#     for j in range(shape[1]):
#         try:
#             co=np.array([i,j,1]) 
#             new_co=np.dot(translation_matrix,co)
#             new_img[int(new_co[0]),int(new_co[1])]=img[i,j]
#         except:
#             pass
# cv2.imshow("new_img",new_img)
# cv2.waitKey(0)
shape=img.shape
translation_matrix1=np.array(
    [
        [1,0,-shape[0]/2],
        [0,1,-shape[1]/2],
        [0,0,1]
    ]
)
rotation_matrix=np.array(
    [
        [np.cos(np.pi/2),-np.sin(np.pi/2),0],
        [np.sin(np.pi/2),np.cos(np.pi/2),0],
        [0,0,1]
    ]
)
translation_matrix2=np.array(
    [
        [1,0,shape[0]],
        [0,1,0],
        [0,0,1]
    ]
)
composition=translation_matrix2 @ rotation_matrix
new_img=np.zeros((512,512),dtype=np.uint8)

for x in range(shape[0]):
    for y in range(shape[1]):
            try:
                co=np.array([
                    [x],
                    [y],
                    [1]]) 
                new_co=composition @ co
                new_img[int(new_co[0]),int(new_co[1])]=img[x,y]
                if(x==0 and y==1):
                    print(int(new_co[0]),int(new_co[1]))
            except:
                 pass


cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cv2.imshow("image",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()