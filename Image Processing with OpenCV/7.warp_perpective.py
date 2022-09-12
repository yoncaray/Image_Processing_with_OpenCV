import cv2
import numpy as np

# Resmi İçe Aktarma
img = cv2.imread("images/kart.png")
cv2.imshow("Original", img)

width = 400
height = 500

points1 = np.float32([[202,2],[1,472],[540,148],[340,617]])
points2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(points1, points2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Output", imgOutput)

if cv2.waitKey(0) &0xFF == 13:
    cv2.destroyAllWindows()
    