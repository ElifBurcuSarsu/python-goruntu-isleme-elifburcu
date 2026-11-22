import cv2

img = cv2.imread("test.jpg")

if img is None:
    print("Fotograf bulunamadi.")
    exit()

# Fotoğrafımızı ekrana sığdırmak için alistirma1 de verdiğim değerler.
img = cv2.resize(img, (800, 450))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Kirmizi renk(HSV sisteminde kırmızı renk, H ölçeğinin hem başlangıcında hem sonunda bulunur, bu yüzden iki sınır kullandık.)
alt1 = (0, 100, 100)
ust1 = (10, 255, 255)

alt2 = (170, 100, 100)
ust2 = (179, 255, 255)

maske1 = cv2.inRange(hsv, alt1, ust1)
maske2 = cv2.inRange(hsv, alt2, ust2)

kirmizi = cv2.bitwise_or(maske1, maske2)

# Mavi renk
mavi_alt = (100, 100, 100)
mavi_ust = (130, 255, 255)

mavi = cv2.inRange(hsv, mavi_alt, mavi_ust)

# Sonuclari kaydet
cv2.imwrite("kirmizi_maske.jpg", kirmizi)
cv2.imwrite("mavi_maske.jpg", mavi)

# Ekranda goster
cv2.imshow("Orijinal", img)
cv2.imshow("Kirmizi Maske", kirmizi)
cv2.imshow("Mavi Maske", mavi)

cv2.waitKey(0)
cv2.destroyAllWindows()

