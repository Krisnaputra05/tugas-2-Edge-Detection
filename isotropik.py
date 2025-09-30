import numpy as np
import matplotlib.pyplot as plt
import cv2
from math import sqrt

# Input & Output
image_path = "img/beras.jpg"
output_isotropik = "report/hasil_tepi_isotropik.jpg"

# Baca citra grayscale pakai OpenCV
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Kernel isotropik
Kx = np.array([[-1, 0, 1],
               [-sqrt(2), 0, sqrt(2)],
               [-1, 0, 1]])

Ky = np.array([[-1, -sqrt(2), -1],
               [0, 0, 0],
               [1, sqrt(2), 1]])

# Matriks hasil
rows, cols = img.shape
G = np.zeros_like(img, dtype=np.float32)

# Konvolusi manual
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = img[i-1:i+2, j-1:j+2]
        gx = np.sum(Kx * region)
        gy = np.sum(Ky * region)
        
        # Magnitudo gradien
        G[i, j] = np.sqrt(gx**2 + gy**2)

# Normalisasi 0–255
G = (G / G.max() * 255).astype(np.uint8)

# Simpan hasil
cv2.imwrite(output_isotropik, G)

# Tampilkan hasil (opsional)
plt.imshow(G, cmap="gray")
plt.axis("off")
plt.title("Deteksi Tepi Isotropik")
plt.show()
