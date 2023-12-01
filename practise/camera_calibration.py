import cv2 
import numpy as np 
import os 
import glob 
from tqdm import tqdm
from cv2 import findChessboardCorners
CHECKERBOARD = (7, 6)

criteria = (cv2.TERM_CRITERIA_EPS +
            cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

print(cv2.TERM_CRITERIA_EPS, cv2.TERM_CRITERIA_MAX_ITER)

# Vector for 3D points
threedpoints = []
 
# Vector for 2D points
twodpoints = []
 
 
#  3D points real world coordinates
objectp3d = np.zeros((1, CHECKERBOARD[0]
                      * CHECKERBOARD[1],
                      3), np.float32)
objectp3d[0, :, :2] = np.mgrid[0:CHECKERBOARD[0],
                               0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

# images = glob.glob('C:/Users/kusha/Desktop/CEVI-Summer_School/images/checkerboard/*.JPG')

# for filename in tqdm(images):
#     # print(filename)
#     image = cv2.imread(filename)
#     grayColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#     # Find the chess board corners
#     # If desired number of corners are
#     # found in the image then ret = true
#     ret, corners = cv2.findChessboardCorners(
#                     grayColor, CHECKERBOARD, None)
 
#     # If desired number of corners can be detected then,
#     # refine the pixel coordinates and display
#     # them on the images of checker board
#     if ret == True:
#         threedpoints.append(objectp3d)
 
#         # Refining pixel coordinates
#         # for given 2d points.
#         corners2 = cv2.cornerSubPix(
#             grayColor, corners, (11, 11), (-1, -1), criteria)
 
#         twodpoints.append(corners2)
 
#         # Draw and display the corners
#         image = cv2.drawChessboardCorners(image,
#                                           CHECKERBOARD,
#                                           corners2, ret)
#         cv2.imshow("Corners",image)
 

 
# h,w=image.shape[:2]
 
# ret, matrix, distortion, r_vecs, t_vecs = cv2.calibrateCamera(
#     threedpoints, twodpoints, grayColor.shape[::-1], None, None)

# Displaying required output

matrix = np.array([[3.06224146e+03, 0.00000000e+00, 1.44451093e+03],
                  [0.00000000e+00, 3.15079778e+03, 1.97474407e+03],
                  [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
distortion=[[ 0.32209072, -2.03641822,  0.01080272, -0.00716682 , 4.16449658]]
r_vecs=np.array([[[ 0.29051827],
       [-0.28222892],
       [ 1.56210801]],[[ 0.14290784],
       [-0.33132762],
       [ 1.5988453 ]],[[ 0.02405364],
       [-0.3357228 ],
       [ 1.61314358]]])

t_vecs=[[[ 2.53376261],
       [-3.52591409],
       [ 9.43256466]],[[ 3.10148771],
       [-2.95109867],
       [10.92749462]],[[ 2.57709014],
       [-2.24216381],
       [11.45814184]]]
print(" Camera matrix:")
print(matrix)
 
print("\n Distortion coefficient:")
print(distortion)
 
print("\n Rotation Vectors:")
print(r_vecs)
 
print("\n Translation Vectors:")
print(t_vecs)

def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    
    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
    
    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)


axis = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0], [0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])

cam = cv2.VideoCapture(0)
ret1 = True
while ret1:
    ret1, img = cam.read()
    # print(ret1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
    if ret == True:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        
        # Find the rotation and translation vectors.
        rvecs, tvecs, inliers = cv2.solvePnPRansac(objectp3d, corners2, matrix, distortion)
        
        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, matrix, distortion)
        img = draw(img,corners2,imgpts)
    cv2.imshow('img',img)
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        exit()