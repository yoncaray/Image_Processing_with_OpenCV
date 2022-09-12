import cv2
import numpy as np

# Resim Oluştur
img = np.zeros((512,512,3), np.uint8)
cv2.imshow("Black Picture", img)
print(img.shape)

# Çizgi
# (resim, başlangıç nok., bitiş nok., renk, kalınlık)
cv2.line(img, (0,0), (512,512), (255,0,0), 3) # BGR = (0,255,0)
cv2.imshow("Line", img)

# Dikdörtgen
# (resim, başlangıç, bitiş, renk)
cv2.rectangle(img, (0,0), (256,256), (0,255,0), cv2.FILLED)
cv2.imshow("Rectangle", img)

# Çember
# (resim, merkez, yarıçap, renk)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Circle", img)

# Metin
# (resim, metin, başlangıç, font, kalınlık, renk)
cv2.putText(img, "Picture", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Text", img)

if cv2.waitKey(0) & 0xFF == 13:
    cv2.destroyAllWindows()
    