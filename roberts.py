import numpy as np
import matplotlib.pyplot as plt
import cv2

# Membaca citra input dari file
img = cv2.imread("img/beras.jpg", cv2.IMREAD_GRAYSCALE)

# Operator Roberts
kernel_x = np.array([[1, 0], [0, -1]])
kernel_y = np.array([[0, 1], [-1, 0]])

# Matriks output
output = np.zeros_like(img)

# Hitung gradien intensitas
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        Gx = np.sum(kernel_x * img[i:i + 2, j:j + 2])
        Gy = np.sum(kernel_y * img[i:i + 2, j:j + 2])
        output[i, j] = np.sqrt(Gx ** 2 + Gy ** 2)

# Gunakan nilai intensitas maksimum
max_val = np.max(output)
for i in range(output.shape[0]):
    for j in range(output.shape[1]):
        output[i, j] = max(output[i, j], 0)

plt.imsave("report/hasil_tepi_roberts.jpg", output, cmap="gray")
