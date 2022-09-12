import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("images/img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread("images/img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (600,400))
img2 = cv2.resize(img2, (600,400))

# Karıştırılmış resim = img1*alpha + img2*beta
blended = cv2.addWeighted(src1=img1, alpha= 0.2, src2=img2, beta=0.8, gamma=0)

plt.figure(), plt.imshow(img1), plt.axis("off")
plt.figure(), plt.imshow(img2), plt.axis("off")
plt.figure(), plt.imshow(blended), plt.axis("off")
