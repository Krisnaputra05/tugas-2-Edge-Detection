import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("img/beras.jpg", cv2.IMREAD_GRAYSCALE)

# Kernel Laplace (turunan kedua)
kernel_laplace = np.array([[0,  1, 0],
                           [1, -4, 1],
                           [0,  1, 0]])

# Matriks output
output = np.zeros_like(img, dtype=np.float32)

# Hitung respons Laplace dengan konvolusi
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        region = img[i-1:i+2, j-1:j+2]
        response = np.sum(kernel_laplace * region)
        output[i, j] = response

# Ambil nilai absolut dan normalisasi
output = np.abs(output)
output = (output / np.max(output) * 255).astype(np.uint8)

plt.imsave("report/hasil_tepi_laplace.jpg", output, cmap="gray")

plt.imshow(output, cmap='gray')
plt.axis('off') 
plt.show()