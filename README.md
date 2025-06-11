---

# Casdoor Scanner - Pemindai Kerentanan

Sebuah skrip sederhana untuk mendeteksi kerentanan pada platform **Casdoor** secara otomatis.

---

## 📜 Deskripsi

Skrip ini dirancang untuk membantu para peneliti keamanan dan administrator sistem dalam mengidentifikasi potensi kerentanan pada implementasi Casdoor.

Alat ini mengeksploitasi potensi celah dengan membuat pengguna baru melalui **endpoint SCIM** yang terbuka — sebuah indikasi dari kesalahan konfigurasi keamanan.

---

## ✨ Fitur

* ⚡ **Pemindaian Cepat**: Secara efisien memeriksa endpoint yang rentan.
* 🔄 **Dua Mode Operasi**:

  * Pemindaian target tunggal.
  * Pemindaian massal dari daftar file.
* 🌐 **Penambahan Protokol Otomatis**: Otomatis menambahkan `http://` jika target tidak mencantumkan protokol.
* 📊 **Output Jelas**: Menampilkan hasil yang mudah dibaca dengan informasi kredensial jika berhasil.
* 🧾 **Mudah Digunakan**: Antarmuka baris perintah yang sederhana dan intuitif.

---

## 🔍 Dorks (Pencarian)

Gunakan dork berikut di mesin pencari IoT untuk menemukan target yang berpotensi rentan:

* **Fofa**:

  ```
  body="urn:ietf:params:scim:schemas:core:2.0:User"
  ```
* **Shodan**:

  ```
  http.html:"urn:ietf:params:scim:schemas:core:2.0:User"
  ```
* **Google**:

  ```
  intext:"urn:ietf:params:scim:schemas:core:2.0:User"
  ```

---

## 🚀 Instalasi

### 1. Kloning Repositori

```bash
git clone https://github.com/Sincan2/casdoor-scanner.git
cd casdoor-scanner
```

> 📌 **Catatan**: Jangan Ganti Pembuatnya Wedhoes Tolol Dongo.

### 2. Instal Ketergantungan

```bash
pip install requests termcolor
```

Atau jika Anda memiliki file `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Penggunaan

Pastikan Anda memberikan izin eksekusi pada skrip (hanya perlu dilakukan sekali):

```bash
chmod +x pindai.py
```

### 1. Memindai Target Tunggal

```bash
./pindai.py [IP_TARGET:PORT]
```

**Contoh:**

```bash
./pindai.py 4.201.155.100:8080
```

### 2. Memindai dari Daftar File

Buat file `targets.txt` dan isi dengan daftar target (satu per baris):

```
4.201.155.100:8080
contoh.com
123.45.67.89:8000
```

Jalankan skrip:

```bash
./pindai.py --file targets.txt
```

---

## 📌 Contoh Output Jika Berhasil

```
[*] Memindai target: https://54.70.145.252

🔥[TARGET RENTAN DITEMUKAN]🔥
➡️ Target: https://54.70.145.252/scim/Users
💚 Nama Pengguna: wRj2kQ92N9W9
💚 Kata Sandi: NYHeAM4VvuUH

--------------------------------------------------
```

---

## 👨‍💻 Kredit & Kontribusi

Alat ini dikembangkan oleh **Sincan2**.

Kontribusi, laporan bug, dan permintaan fitur sangat dihargai!
Silakan buat **issue** atau **pull request** jika ingin berkontribusi.

---

## ⚠️ Penafian (Disclaimer)

Alat ini dibuat **hanya untuk tujuan pendidikan dan penelitian keamanan yang sah**.
Gunakan **hanya pada sistem yang Anda miliki izin untuk mengujinya**.

> Pengembang tidak bertanggung jawab atas penyalahgunaan atau kerusakan yang disebabkan oleh program ini.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **MIT License**.

---
