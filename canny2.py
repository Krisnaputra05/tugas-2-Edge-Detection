import numpy as np
from scipy import ndimage
import cv2
import matplotlib.pyplot as plt

# Input & Output
image_path = 'img/beras.jpg'
output_canny = 'report/hasil_tepi_canny2.jpg'

# 1. Load image (sudah grayscale)
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
img_array = img.astype(float)

# 2. Gaussian blur
blur_img = ndimage.gaussian_filter(img_array, sigma=1.0)

# 3. Gradient (Sobel)
def gradient_x(img):
    grad = ndimage.convolve(img, np.array([[-1, 0, 1],
                                           [-2, 0, 2],
                                           [-1, 0, 1]]))
    return grad / np.max(np.abs(grad))

def gradient_y(img):
    grad = ndimage.convolve(img, np.array([[-1, -2, -1],
                                           [ 0,  0,  0],
                                           [ 1,  2,  1]]))
    return grad / np.max(np.abs(grad))

fx = gradient_x(blur_img)
fy = gradient_y(blur_img)

# 4. Gradient magnitude & direction
grad_mag = np.hypot(fx, fy)
grad_mag = grad_mag / np.max(grad_mag)
grad_dir = np.degrees(np.arctan2(fy, fx))

# 5. Non-maximum suppression
def closest_dir_function(grad_dir):
    closest = np.zeros(grad_dir.shape)
    for i in range(1, grad_dir.shape[0]-1):
        for j in range(1, grad_dir.shape[1]-1):
            a = grad_dir[i, j]
            if ((-22.5 < a <= 22.5) or (a <= -157.5) or (a > 157.5)):
                closest[i, j] = 0
            elif ((22.5 < a <= 67.5) or (-157.5 < a <= -112.5)):
                closest[i, j] = 45
            elif ((67.5 < a <= 112.5) or (-112.5 < a <= -67.5)):
                closest[i, j] = 90
            else:
                closest[i, j] = 135
    return closest

def non_maximal_suppressor(grad_mag, closest_dir):
    thinned = np.zeros(grad_mag.shape)
    for i in range(1, grad_mag.shape[0]-1):
        for j in range(1, grad_mag.shape[1]-1):
            if closest_dir[i, j] == 0:
                if grad_mag[i, j] > grad_mag[i, j+1] and grad_mag[i, j] > grad_mag[i, j-1]:
                    thinned[i, j] = grad_mag[i, j]
            elif closest_dir[i, j] == 45:
                if grad_mag[i, j] > grad_mag[i+1, j+1] and grad_mag[i, j] > grad_mag[i-1, j-1]:
                    thinned[i, j] = grad_mag[i, j]
            elif closest_dir[i, j] == 90:
                if grad_mag[i, j] > grad_mag[i+1, j] and grad_mag[i, j] > grad_mag[i-1, j]:
                    thinned[i, j] = grad_mag[i, j]
            else:
                if grad_mag[i, j] > grad_mag[i+1, j-1] and grad_mag[i, j] > grad_mag[i-1, j+1]:
                    thinned[i, j] = grad_mag[i, j]
    return thinned / np.max(thinned)

closest_dir = closest_dir_function(grad_dir)
thinned_output = non_maximal_suppressor(grad_mag, closest_dir)

# 6. Hysteresis thresholding
def DFS(img):
    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            if img[i, j] == 1:
                if np.max(img[i-1:i+2, j-1:j+2]) == 2:
                    img[i, j] = 2

def hysteresis_thresholding(img):
    low_ratio, high_ratio = 0.10, 0.30
    diff = np.max(img) - np.min(img)
    t_low = np.min(img) + low_ratio * diff
    t_high = np.min(img) + high_ratio * diff
    temp = np.copy(img)

    for i in range(1, img.shape[0]-1):
        for j in range(1, img.shape[1]-1):
            if img[i, j] > t_high:
                temp[i, j] = 2
            elif img[i, j] < t_low:
                temp[i, j] = 0
            else:
                temp[i, j] = 1

    total_strong = np.sum(temp == 2)
    while True:
        DFS(temp)
        if total_strong == np.sum(temp == 2):
            break
        total_strong = np.sum(temp == 2)

    temp[temp == 1] = 0
    return temp / np.max(temp)

output_img = hysteresis_thresholding(thinned_output)

# 7. Save hasil akhir pakai OpenCV
output_img_uint8 = (output_img * 255).astype(np.uint8)
cv2.imwrite(output_canny, output_img_uint8)

# 8. Tampilkan hasil pakai matplotlib
plt.imshow(output_img_uint8, cmap="gray")
plt.axis("off")
plt.title("Deteksi Tepi Canny")
plt.show()
