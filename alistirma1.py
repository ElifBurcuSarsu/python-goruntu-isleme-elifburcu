import cv2
img = cv2.imread("test.jpg")
if img is None:
    print("Fotograf bulunamadi.")
    exit()
img = cv2.resize(img, (800, 450))
print("Boyut:", img.shape)
# 2) Griye cevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 3) Bulaniklastir (gurultuyu azaltir)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# 4) Kenarlari bul
edges = cv2.Canny(blur, 150, 250)
# 5) Sonucu kaydet ve goster
cv2.imwrite("canny_150_250.jpg", edges)
cv2.imshow('Kenarlar', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()