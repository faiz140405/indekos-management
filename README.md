# Kost Management System (Django)

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Aplikasi web pengelolaan kost (indekos) yang dibangun menggunakan Django Framework. Dirancang untuk memudahkan pemilik kost dalam mengelola properti, kamar, dan data penyewa secara efisien.

## Daftar Isi
- [Tentang Proyek](#tentang-proyek)
- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Struktur Proyek](#struktur-proyek)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Langkah-Langkah Instalasi dan Menjalankan Proyek](#langkah-langkah-instalasi-dan-menjalankan-proyek)
  - [1. Clone Repositori](#1-clone-repositori)
  - [2. Buat dan Aktifkan Lingkungan Virtual](#2-buat-dan-aktifkan-lingkungan-virtual)
  - [3. Instal Dependensi Python](#3-instal-dependensi-python)
  - [4. Konfigurasi Database](#4-konfigurasi-database)
  - [5. Jalankan Migrasi Database](#5-jalankan-migrasi-database)
  - [6. Buat Akun Superuser (Admin)](#6-buat-akun-superuser-admin)
  - [7. Jalankan Server Pengembangan](#7-jalankan-server-pengembangan)
- [Mengakses Aplikasi](#mengakses-aplikasi)
- [Panel Admin](#panel-admin)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

---

## Tentang Proyek
Proyek ini adalah sistem pengelolaan kost yang bertujuan untuk menyederhanakan tugas-tugas administratif bagi pemilik kost, sekaligus menyediakan antarmuka yang ramah pengguna bagi calon penyewa untuk mencari informasi kost. Sistem ini dikembangkan sebagai proyek pembelajaran dan demonstrasi kemampuan dalam pengembangan web menggunakan Django.

## Fitur Utama
* **Manajemen Kost:** Menambah, mengedit, dan menghapus data properti kost (nama, alamat, deskripsi).
* **Manajemen Kamar:** Mengelola detail setiap kamar termasuk nomor kamar, tipe (AC/Non-AC, Kamar Mandi Dalam/Luar), harga sewa, dan status ketersediaan.
* **Halaman Promosi (Landing Page):** Tampilan depan yang menarik untuk memperkenalkan kost.
* **Daftar Kost & Detail Kamar:** Halaman untuk menampilkan daftar kost yang tersedia beserta detail kamar di setiap kost.
* **Halaman "Tentang Kami" & "Kontak":** Informasi mengenai proyek/organisasi dan cara menghubungi.
* **Panel Admin yang Intuitif:** Menggunakan Django Jazzmin untuk antarmuka admin yang modern dan mudah digunakan dalam mengelola semua data.
* **Statistik Kamar:** Tampilan grafik sederhana di halaman daftar kost untuk ringkasan ketersediaan kamar (tersedia vs terisi).

**(Akan Datang/Rencana Fitur):**
* Manajemen Penyewa
* Sistem Pembayaran Sewa
* Pencarian dan Filter Kamar
* Upload Gambar Kost/Kamar
* Sistem Notifikasi

## Teknologi yang Digunakan
* **Backend:**
    * [Python](https://www.python.org/)
    * [Django Framework](https://www.djangoproject.com/)
    * [Matplotlib](https://matplotlib.org/) (untuk visualisasi statistik)
    * [Pillow](https://python-pillow.org/) (untuk ImageField di Django, jika digunakan)
* **Frontend:**
    * [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
    * [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
    * [Bootstrap 5](https://getbootstrap.com/) (untuk desain responsif dan komponen UI)
* **Database:**
    * [SQLite](https://www.sqlite.org/index.html) (default untuk pengembangan)
* **Version Control:**
    * [Git](https://git-scm.com/)
    * [GitHub](https://github.com/)
## Persyaratan Sistem
* Python 3.8+
* pip (biasanya sudah terinstal dengan Python)
* Lingkungan virtual (venv disarankan)
* Git

## Langkah-Langkah Instalasi dan Menjalankan Proyek

### 1. Clone Repositori (Jika Anda Mengunduh dari GitHub)
Jika Anda mengunduh proyek ini dari GitHub, buka terminal Anda dan clone repositori ini:
```bash
git clone [https://github.com/faiz140405/kost-management.git](https://github.com/faiz140405/kost-management.git) # Ganti dengan URL repositori Anda jika berbeda
cd kost-management # Masuk ke direktori proyek

python -m venv venv_kost
# Untuk Windows:
.\venv_kost\Scripts\activate
# Untuk macOS/Linux:
source venv_kost/bin/activate

pip freeze > requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
