# Deteksi Tepi (Edge Detection)

README ini membahas materi Deteksi Tepi (Edge Detection) untuk matakuliah Computer Vision, meliputi algoritma Prewitt, Roberts, Sobel, Isotropik, Laplacian, dan Canny. Deteksi tepi adalah proses penting dalam pengolahan citra digital untuk menemukan batas-batas objek dalam gambar.

## 1. Prewitt

Prewitt adalah operator deteksi tepi berbasis konvolusi yang menggunakan dua kernel (horizontal dan vertikal) untuk menghitung gradien intensitas piksel. Algoritma ini menyoroti perubahan intensitas secara tajam, sehingga tepi objek dapat terdeteksi.

**Kernel Prewitt:**

- Horizontal:
  [-1 0 1]
  [-1 0 1]
  [-1 0 1]
- Vertikal:
  [ 1 1 1]
  [ 0 0 0]
  [-1 -1 -1]

## 2. Roberts

Roberts Cross operator menggunakan dua kernel 2x2 untuk mendeteksi tepi secara diagonal. Algoritma ini menghitung perbedaan antara piksel yang bersebelahan secara diagonal.

**Kernel Roberts:**

- [ 1 0]
  [ 0 -1]
- [ 0 1]
  [-1 0]

## 3. Sobel

Sobel adalah operator deteksi tepi yang mirip dengan Prewitt, namun memberikan bobot lebih besar pada piksel tengah. Sobel menggunakan dua kernel 3x3 untuk mendeteksi tepi secara horizontal dan vertikal, serta lebih tahan terhadap noise.

**Kernel Sobel:**

- Horizontal:
  [-1 0 1]
  [-2 0 2]
  [-1 0 1]
- Vertikal:
  [ 1 2 1]
  [ 0 0 0]
  [-1 -2 -1]

## 4. Isotropik

Operator Isotropik bertujuan mendeteksi tepi tanpa memperhatikan arah tertentu, sehingga hasil deteksi tepi lebih seragam di semua arah. Kernel isotropik biasanya berbentuk lingkaran atau menggunakan bobot yang sama ke segala arah.

## 5. Laplacian

Laplacian adalah operator deteksi tepi berbasis turunan kedua, yang menyoroti area perubahan intensitas yang sangat tajam. Laplacian sering digunakan untuk mendeteksi tepi tanpa memperhatikan arah, namun sensitif terhadap noise.

**Kernel Laplacian (contoh):**

- [ 0 -1 0]
  [-1 4 -1]
  [ 0 -1 0]

## 6. Canny Edge Detection

Canny adalah algoritma deteksi tepi yang paling populer dan kompleks. Algoritma ini terdiri dari beberapa tahap:

1. Noise reduction (Gaussian blur)
2. Perhitungan gradien intensitas
3. Non-maximum suppression
4. Double thresholding
5. Edge tracking by hysteresis

Canny menghasilkan deteksi tepi yang tipis, jelas, dan tahan terhadap noise.

---

**Referensi:**

- Gonzalez & Woods, Digital Image Processing
- Szeliski, Computer Vision: Algorithms and Applications
- OpenCV Documentation

Materi ini digunakan untuk matakuliah Computer Vision, khususnya dalam pengolahan citra digital dan analisis objek.
