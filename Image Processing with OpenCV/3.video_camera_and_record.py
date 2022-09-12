import cv2

cap = cv2.VideoCapture(0) # 0 değeri hangi kamera olduğunu gösteriyor.

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# Video Kaydet
writer = cv2.VideoWriter("images/video_kaydi.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))
# cv2.VideoWriter_fourcc = çerçeveleri sıkıştırmak için kullanılan 4 karakterli code kodu
# (*"DİVX") = Windows için 
# 20 değeri video akışının hızı

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    # Save
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()
