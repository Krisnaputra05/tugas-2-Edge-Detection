import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("img/beras.jpg", cv2.IMREAD_GRAYSCALE)

# Operator kernel sobel
kernel_x = np.array([[ -1, 0, 1],
                     [ -2, 0, 2],
                     [ -1, 0, 1]])

kernel_y = np.array([[ -1, -2, -1],
                     [  0,  0,  0],
                     [  1,  2,  1]])

# Matriks output
output = np.zeros_like(img, dtype=np.float32)

# Hitung gradien intensitas dengan konvolusi 
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        Gx = np.sum(kernel_x * img[i-1:i+2, j-1:j+2])
        Gy = np.sum(kernel_y * img[i-1:i+2, j-1:j+2])
        # hitung gx dan gy dengan menjumlahkan hasil perkalian kernel dengan piksel di sekitar

        output[i, j] = np.sqrt(Gx ** 2 + Gy ** 2) # hitung magnitudo gradien (jumlahkan konvolusi Gx dan Gy)

output = (output / np.max(output) * 255).astype(np.uint8)

plt.imsave("report/hasil_tepi_sobel.jpg", output, cmap="gray")

# Menampilkan citra hasil
plt.imshow(output, cmap='gray')
plt.axis('off')
plt.show()
