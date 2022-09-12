import cv2
import numpy as np

img = cv2.imread("images/lenna.png")
cv2.imshow("Original", img)

# Yatay
h = np.hstack((img,img))
cv2.imshow("Horizontal", h)

# Dikey
v = np.vstack((img,img))
cv2.imshow("Vertical", v)

if cv2.waitKey(0) &0xFF == 13:
    cv2.destroyAllWindows()
    