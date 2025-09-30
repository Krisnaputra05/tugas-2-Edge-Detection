import cv2
from PIL import Image

# Parameter
image_path = 'img/beras.jpg'
output_canny = 'report/hasil_tepi_canny.png'

# Baca citra hitam-putih
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Terapkan Canny Edge Detection
# Threshold bawah = 100, threshold atas = 200 (bisa disesuaikan)
edges = cv2.Canny(img, 100, 200)

# Simpan hasil
cv2.imwrite(output_canny, edges)

# Tampilkan hasil (opsional)
Image.fromarray(edges).show()