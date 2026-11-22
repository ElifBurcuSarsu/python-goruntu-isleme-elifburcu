# Görüntü İşleme Alıştırmaları – Gözlem Notları

## Alıştırma 1 – Canny Kenar Tespiti
Bu alıştırmada aynı fotoğraf üzerinde Canny fonksiyonunu 50–100, 100–200 ve 150–250 eşik değerleriyle denedim.
- **50–100:** Çiçeklerin yaprakları, vazoların desenleri ve masadaki küçük ayrıntılar daha fazla algılandı.
- **100–200:** Bazı ince çizgiler kayboldu ancak vazoların ve masanın temel kenarları görünmeye devam etti.
- **150–250:** Algılanan kenar sayısı daha da azaldı. Özellikle çiçeklerdeki ince ayrıntıların ve masa yüzeyindeki çizgilerin bir kısmı kayboldu.
Eşik değerlerini yükselttikçe daha az kenarın algılandığını gördüm.

## Alıştırma 2 – Webcam ile Canlı Kenar Tespiti
Bilgisayar kamerasından `cv2.VideoCapture(0)` ile canlı görüntü alıp her kareye Canny kenar tespiti uyguladım. Kameraya bir şişe ve tabletimin arka kılıfını gösterdim. Şişenin dış hatları, etiketindeki yazılar, tablet kılıfının kenarları ve ortasındaki dairesel bölüm kenar görüntüsünde belirginleşti. Nesneleri hareket ettirdiğimde kenar görüntüsünün de anlık olarak değiştiğini gözlemledim.
Dolayısıyla bu denemede aynı işlemin yalnızca sabit fotoğraflara değil, canlı kamera görüntülerine de uygulanabildiğini gördüm.

## Alıştırma 3 – HSV ile Renk Maskeleme
Önce fotoğrafı `cv2.COLOR_BGR2HSV` ile HSV renk uzayına çevirdim. Ardından `cv2.inRange()` kullanarak kırmızı ve mavi renkler için ayrı maskeler oluşturdum.
Maskelemede seçilen renkler beyaz, geri kalan kısımlar siyah gösterildi. Ancak bazı renkli bölgelerin tamamen seçilmediğini fark ettim. Bunun seçilen HSV alt ve üst sınırlarından, ortamdaki ışık koşullarından ve renk tonu farklılıklarından kaynaklandığını düşünüyorum.
