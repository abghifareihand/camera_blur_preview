# Camera Preview - Gesture Blur

Aplikasi Python sederhana untuk preview kamera yang otomatis memburamkan (blur) layar secara real-time berdasarkan 3 pilihan mode gestur tangan menggunakan AI deteksi tangan (MediaPipe).

---

## 📥 Persiapan Awal (Instalasi Pertama Kali)

Jika Anda baru saja mengkloning atau mengunduh project ini dari GitHub, ikuti langkah-langkah di bawah ini untuk menyiapkan lingkungan Python Anda:

### 1. Masuk ke Folder Proyek
Buka Terminal macOS Anda dan masuk ke direktori proyek:
```bash
cd camera_blur_python
```

### 2. Buat Lingkungan Virtual (Virtual Environment)
Buat virtual environment baru bernama `venv` agar library yang diinstal terisolasi:
```bash
python3 -m venv venv
```

### 3. Aktifkan Virtual Environment
```bash
source venv/bin/activate
```
*(Setelah aktif, Anda akan melihat tanda `(venv)` di sebelah kiri prompt Terminal Anda).*

### 4. Install Semua Dependency Library
Gunakan file `requirements.txt` untuk mengunduh semua library yang diperlukan (OpenCV & MediaPipe):
```bash
pip install -r requirements.txt
```
> [!TIP]
> **Khusus macOS**: Jika Anda mengalami error encoding saat instalasi di Terminal, jalankan perintah dengan parameter tambahan berikut:
> ```bash
> pip install --no-compile -r requirements.txt
> ```

---

## 🛠️ Cara Menjalankan Program (Setelah Instalasi Selesai)

Setelah melakukan persiapan di atas, setiap kali Anda ingin menjalankan program di lain waktu, cukup jalankan perintah ini di Terminal Anda:

```bash
# 1. Masuk ke folder proyek
cd camera_blur_python

# 2. Aktifkan virtual environment
source venv/bin/activate

# 3. Jalankan aplikasi
python main.py
```

---

## 🎮 Kontrol Aplikasi & 3 Mode Deteksi

Anda dapat menekan tombol **`m`** pada keyboard Anda saat aplikasi berjalan untuk beralih (cycle) di antara 3 mode deteksi berikut:

### 1. Mode 0: 1 Tangan (2 Jari) - Default
* **Cara Kerja**: Cukup arahkan satu tangan ke kamera dan angkat **tepat 2 jari** (Telunjuk & Tengah) untuk mengaktifkan blur secara instan.
* Layar akan kembali jernih/normal jika jumlah jari selain 2.

### 2. Mode 1: 2 Tangan (2 Jari)
* **Cara Kerja**: Anda harus menunjukkan **kedua tangan** Anda di layar, dan **masing-masing** tangan harus mengangkat tepat 2 jari secara bersamaan agar layar menjadi blur.
* Mode ini sangat aman dari deteksi tidak sengaja karena memerlukan gestur dari kedua tangan.

### 3. Mode 2: 1 Tangan (Semua Jari Terbuka)
* **Cara Kerja**: Tunjukkan satu tangan dengan **semua jari terbuka** (kelima jari mengembang) ke kamera untuk memburamkan layar.
* Jika tangan Anda mengepal (fist) atau diturunkan, layar otomatis kembali normal/jernih.

---

## 🎹 Kontrol Keyboard Live
* **Tombol `m`**: Mengubah Mode Deteksi (Mode 0 $\rightarrow$ Mode 1 $\rightarrow$ Mode 2 $\rightarrow$ kembali ke Mode 0) secara berurutan.
* **Tombol `q`**: Menutup aplikasi dan mematikan kamera.

---

## ⚠️ Catatan Akses Kamera (macOS)
Saat pertama kali program dijalankan, macOS akan menampilkan dialog pop-up yang meminta izin akses kamera ke terminal/editor (misalnya **Terminal** atau **VS Code**). Pastikan untuk memilih **Allow / OK** (Izinkan).

Jika kamera tidak terbuka atau terjadi error, silakan periksa:
`System Settings` (Pengaturan Sistem) > `Privacy & Security` (Privasi & Keamanan) > `Camera` (Kamera), lalu pastikan aplikasi Terminal atau VS Code Anda sudah dicentang/diaktifkan.
