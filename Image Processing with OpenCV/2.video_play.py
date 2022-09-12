import cv2
import time

# Video İçe Aktar: capture, cap
cap = cv2.VideoCapture("images/MOT17-04-DPM.mp4")

print("Genişlik: ", cap.get(3))
print("Yükseklik: ", cap.get(4))

if cap.isOpened() == False:
    print("Hata")
    
while True:
    ret, frame = cap.read()
    # frame = videodaki her bir resim
    # ret = işlemin başarılı olup olmadığını kontrol eder.
    
    if ret == True:
        time.sleep(0.01)
        cv2.imshow("Video", frame)  
    else: break

    if cv2.waitKey(1) & 0xFF == 32:
        break
    
cap.release()
cv2.destroyAllWindows()  

        