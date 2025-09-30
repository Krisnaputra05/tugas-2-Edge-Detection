import numpy as np
import matplotlib.pyplot as plt
import cv2

# Membaca citra input dari file
img = cv2.imread("img/beras.jpg", cv2.IMREAD_GRAYSCALE)

# Kernel Laplace tajam (8 arah)
kernel_laplace = np.array([[1,  1, 1],
                           [1, -8, 1],
                           [1,  1, 1]])

# Matriks output
output = np.zeros_like(img, dtype=np.float32)

# Hitung respons Laplace
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        region = img[i-1:i+2, j-1:j+2]
        response = np.sum(kernel_laplace * region)
        output[i, j] = response

# Ambil nilai absolut dan normalisasi
output = np.abs(output)
output = (output / np.max(output) * 255).astype(np.uint8)

# Menyimpan citra hasil ke file
plt.imsave("report/hasil_tepi_laplace_tajam.jpg", output, cmap="gray")

# Menampilkan citra hasil
plt.imshow(output, cmap='gray')
plt.axis('off')  # Menyembunyikan sumbu
plt.show()