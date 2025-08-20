import cv2
import numpy as np
import matplotlib.pyplot as plt
img = np.zeros((500,500),dtype=np.uint8)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()

