import cv2
import matplotlib.pyplot as plt

# Parameter
image_path = "img/beras.jpg"
output_canny = "report/hasil_tepi_canny.jpg"

# Baca citra grayscale
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Terapkan Canny Edge Detection
# Threshold bawah = 100, threshold atas = 200 (bisa disesuaikan)
edges = cv2.Canny(img, 100, 200)

# Simpan hasil
cv2.imwrite(output_canny, edges)

# Tampilkan hasil (opsional)
plt.imshow(edges, cmap="gray")
plt.axis("off")
plt.title("Deteksi Tepi Canny")
plt.show()
