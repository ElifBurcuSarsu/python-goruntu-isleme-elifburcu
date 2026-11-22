
import cv2

kamera = cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()

    if not ret:
        print("Kamera goruntusu alinamadi.")
        break

    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    kenar = cv2.Canny(gri, 50, 50)

    cv2.imshow("Normal Kamera", kare)
    cv2.imshow("Kenar Tespiti", kenar)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()
