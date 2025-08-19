
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("img2.jpg")

(h,w)= img.shape[:2]



circle = cv2.circle(img,(100,100),50,(0,0,255),3)

RM = cv2.getRotationMatrix2D((w//2,h//2),90,1.0)
rotated=cv2.warpAffine(img,RM,(w,h))
plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
plt.show()