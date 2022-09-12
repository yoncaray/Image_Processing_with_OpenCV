import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# Bluring(detayı azaltır, gürültüyü engeller)
img = cv2.imread("images/NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Original"), plt.show()

# Ortalama Blur (Bulanıklaştırma Yöntemi)
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Ortalama Blur"), plt.show()

# Gaussian Blur
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gauss Blur"), plt.show()

# Medyan Blur
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis("off"),plt.title("Medyan Blur"), plt.show()

# Gaussian Noise 
def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy
    
# Normalize et, aktar
img = cv2.imread("images/NYC.jpg")  
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255 
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Original2"), plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoisyImage), plt.axis("off"), plt.title("Gauss Noisy"), plt.show()

# Gauss Blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7) 
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("With Gauss Blur"), plt.show()

# Salt-Pepper Noise
def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    # salt
    num_salt = np.ceil(amount*image.size*s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    # pepper
    num_pepper = np.ceil(amount*image.size*s_vs_p)  
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    return noisy

spImage = saltPepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("Salt Pepper Noise")

# Medyan Blur
mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("With Median Blur")
 
    
    
    
    
    
    
