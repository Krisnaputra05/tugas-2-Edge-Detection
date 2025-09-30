import numpy as np
import matplotlib.pyplot as plt
import cv2

# Membaca citra input dari file
img = cv2.imread("img/beras.jpg", cv2.IMREAD_GRAYSCALE)

# Operator Prewitt
kernel_x = np.array([[1, 0, -1], 
                      [1, 0, -1], 
                      [1, 0, -1]])

kernel_y = np.array([[1, 1, 1], 
                      [0, 0, 0], 
                      [-1, -1, -1]])

# Matriks output
output = np.zeros_like(img)

# Hitung gradien intensitas
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        Gx = np.sum(kernel_x * img[i-1:i+2, j-1:j+2])
        Gy = np.sum(kernel_y * img[i-1:i+2, j-1:j+2])
        output[i, j] = np.sqrt(Gx ** 2 + Gy ** 2)

# Normalisasi intensitas
output = (output / np.max(output) * 255).astype(np.uint8)

# Menyimpan citra tepi ke file baru
plt.imsave("report/hasil_tepi_prewitt.jpg", output, cmap="gray")

# Menampilkan citra hasil
plt.imshow(output, cmap='gray')
plt.axis('off')  # Menyembunyikan sumbu
plt.show()
