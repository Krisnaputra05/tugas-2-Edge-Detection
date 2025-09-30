import numpy as np
from math import sqrt
from PIL import Image

# Parameter
image_path = 'img/beras.jpg'
output_euclidean = 'report/hasil_tepi_isotropik.jpg'
output_max = 'report/hasil_tepi_isotropik_max.jpg'

# Baca citra hitam-putih
img = Image.open(image_path).convert('L')
img_array = np.array(img, dtype=float)

# Mask isotropik
Kx = np.array([[-1, 0, 1], [-sqrt(2), 0, sqrt(2)], [-1, 0, 1]])
Ky = np.array([[-1, -sqrt(2), -1], [0, 0, 0], [1, sqrt(2), 1]])

rows, cols = img_array.shape
G_euclid = np.zeros((rows, cols))
G_max = np.zeros((rows, cols))

# Loop manual untuk konvolusi
for i in range(1, rows-1):
    for j in range(1, cols-1):
        region = img_array[i-1:i+2, j-1:j+2]
        K1 = np.sum(region * Kx)
        K2 = np.sum(region * Ky)

        # Euclidean
        G_euclid[i, j] = sqrt(K1**2 + K2**2)
        # Nilai maksimum
        G_max[i, j] = max(abs(K1), abs(K2))

# Normalisasi ke 0-255
G_euclid = (G_euclid / G_euclid.max()) * 255
G_max = (G_max / G_max.max()) * 255

G_euclid = G_euclid.astype(np.uint8)
G_max = G_max.astype(np.uint8)

# Simpan hasil citra
Image.fromarray(G_euclid).save(output_euclidean)
Image.fromarray(G_max).save(output_max)

# Tampilkan hasil (opsional)
Image.fromarray(G_euclid).show()
Image.fromarray(G_max).show()
