# fish_detect-Deteksi-ikan-sederhana

link download data set : https://drive.google.com/file/d/1cNNHDwdxyj0JemUsG6vsZSLkz4Af3P7V/view?usp=sharing

![kumpulan_ikan](https://github.com/user-attachments/assets/3682bfc5-0fac-4976-a969-055404a9545e)



![image](https://github.com/user-attachments/assets/fb6c6125-ee20-46e9-9405-609a98d8da2b)

# 🐟 Fish Detection using YOLOv8

**fish_detect** adalah program pendeteksi objek ikan menggunakan model deep learning **YOLOv8**. Program ini sederhana, dijalankan melalui skrip Python, dan menggunakan model hasil pelatihan dalam format `.pt`. Sangat cocok untuk pengujian cepat model deteksi objek tanpa GUI.

---

## 📂 Struktur Proyek
fish_detect/
├── fish_detect.py # Script utama untuk menjalankan deteksi
├── fishgen.pt # Model YOLOv8 terlatih untuk ikan / download di link diatas
├── image.jpg # Gambar yang akan dideteksi (contoh)
└── README.md # Dokumentasi proyek ini

### Catatan Penting (NOTE)
🔹 Pastikan gambar yang ingin dideteksi sudah diunduh dan disimpan di direktori yang sama dengan file fish_detect.py.
🔹 Ganti atau sesuaikan nama file gambar (misalnya image.jpg) di dalam kode fish_detect.py agar sesuai dengan gambar yang kamu gunakan.

#### 🛠️ Program ini masih dalam tahap pengembangan.

Untuk saat ini, fungsinya hanya terbatas pada mendeteksi ikan dalam gambar. Program belum mendukung penyimpanan hasil ke database, integrasi sistem lain, atau fitur tambahan seperti pelacakan video.

Fitur-fitur lanjutan sedang direncanakan untuk rilis mendatang.
