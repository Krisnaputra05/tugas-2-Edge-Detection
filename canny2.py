import numpy as np
from math import sqrt, atan2, pi
from PIL import Image

# Parameter
image_path = 'img/beras.jpg'
output_canny = 'report/hasil_tepi_canny2.jpg'
sigma = 1.4  # Gaussian blur
low_thresh = 50
high_thresh = 150

# Baca citra hitam-putih
img = Image.open(image_path).convert('L')
img_array = np.array(img, dtype=float)

# 1. Gaussian smoothing
def gaussian_kernel(size=5, sigma=1.4):
    k = size // 2
    ax = np.arange(-k, k+1)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2)/(2*sigma**2))
    kernel /= 2*np.pi*sigma**2
    kernel /= kernel.sum()
    return kernel

def convolve(img, kernel):
    m, n = kernel.shape
    y, x = img.shape
    pad_h, pad_w = m//2, n//2
    img_padded = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
    out = np.zeros_like(img)
    for i in range(y):
        for j in range(x):
            region = img_padded[i:i+m, j:j+n]
            out[i,j] = np.sum(region * kernel)
    return out

img_smooth = convolve(img_array, gaussian_kernel(5, sigma))

# 2. Gradien (Sobel)
Sobel_x = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Sobel_y = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
Gx = convolve(img_smooth, Sobel_x)
Gy = convolve(img_smooth, Sobel_y)

# 3. Magnitude dan arah gradien
G = np.hypot(Gx, Gy)
G = (G / G.max()) * 255  # Normalisasi 0-255
theta = np.arctan2(Gy, Gx) * 180 / pi
theta[theta < 0] += 180

# 4. Non-maximum suppression
def non_max_suppression(G, theta):
    Z = np.zeros_like(G)
    rows, cols = G.shape
    angle = theta.copy()
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            q = r = 255
            # Round angle to nearest 0, 45, 90, 135
            a = angle[i,j]
            if (0 <= a < 22.5) or (157.5 <= a <= 180):
                q, r = G[i,j+1], G[i,j-1]
            elif (22.5 <= a < 67.5):
                q, r = G[i+1,j-1], G[i-1,j+1]
            elif (67.5 <= a < 112.5):
                q, r = G[i+1,j], G[i-1,j]
            elif (112.5 <= a < 157.5):
                q, r = G[i-1,j-1], G[i+1,j+1]
            if (G[i,j] >= q) and (G[i,j] >= r):
                Z[i,j] = G[i,j]
            else:
                Z[i,j] = 0
    return Z

G_nms = non_max_suppression(G, theta)

# 5. Double threshold + hysteresis
strong = 255
weak = 75
res = np.zeros_like(G_nms)
res[G_nms >= high_thresh] = strong
res[(G_nms >= low_thresh) & (G_nms < high_thresh)] = weak

# Hysteresis dengan iterasi sampai konvergen
rows, cols = res.shape
changed = True
while changed:
    changed = False
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if res[i,j] == weak:
                if np.any(res[i-1:i+2, j-1:j+2] == strong):
                    res[i,j] = strong
                    changed = True
                else:
                    res[i,j] = 0

# Simpan hasil
Image.fromarray(res.astype(np.uint8)).save(output_canny)
Image.fromarray(res.astype(np.uint8)).show()
