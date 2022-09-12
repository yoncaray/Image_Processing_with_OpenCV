import cv2

img = cv2.imread("images/lenna.png")
print("Image Shape: ", img.shape)
cv2.imshow("Original", img)

# Boyutlandırma
imgResized = cv2.resize(img, (400,400))
print("Resized Shape: ", imgResized.shape)
cv2.imshow("Resized Img", imgResized)

# Kırpma
imgCropped = img[:200, :300] # height-width
print("Cropped Shape: ", imgCropped.shape)
cv2.imshow("Cropped Img", imgCropped)

if cv2.waitKey(0) & 0xFF == 32: # space
    cv2.destroyAllWindows()
  

        