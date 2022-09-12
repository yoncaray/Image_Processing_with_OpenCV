import cv2

# İçe Aktarma
img = cv2.imread("images/messi5.jpg", 0) # 0 değeri resmi siyah-beyaz olmasını sağlar.
# Görselleştirme
cv2.imshow("Messi", img)

if cv2.waitKey(0) &0xFF == 13: # enter
    cv2.destroyAllWindows()
elif cv2.waitKey(0) &0xFF == ord('s'):
    cv2.imwrite("images/messi_gray.png", img)
    cv2.destroyAllWindows()
    