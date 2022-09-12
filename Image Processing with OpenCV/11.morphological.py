import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/datai_team.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Original"), plt.show()

kernel = np.ones((5,5), dtype = np.uint8)

# Erozyon
erozyon = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(erozyon, cmap="gray"), plt.axis("off"), plt.title("Erozyon"), plt.show()

# Genişleme(dilation)
dilation = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(dilation, cmap="gray"), plt.axis("off"), plt.title("Genişleme(dilation)"), plt.show()

# White Noise
whiteNoise = np.random.randint(0, 2, size = img.shape[:2])
whiteNoise = whiteNoise*255 
plt.figure(), plt.imshow(whiteNoise, cmap="gray"), plt.axis("off"), plt.title("White Noise"), plt.show()

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap="gray"), plt.axis("off"), plt.title("Img with White Noise"), plt.show()

# Açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off"), plt.title("Opening"), plt.show()

# Black Noise
blackNoise = np.random.randint(0, 2, size = img.shape[:2])
blackNoise = blackNoise*-255 
plt.figure(), plt.imshow(blackNoise, cmap="gray"), plt.axis("off"), plt.title("Black Noise"), plt.show()

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap="gray"), plt.axis("off"), plt.title("Img with Black Nois"), plt.show()

# Kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap="gray"), plt.axis("off"), plt.title("Closing(Kapama)"), plt.show()

# Gradient(Gradyan)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap="gray"), plt.axis("off"), plt.title("Gradient"), plt.show()







