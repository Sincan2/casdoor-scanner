Casdoor Scanner - Pemindai KerentananSebuah skrip sederhana untuk mendeteksi kerentanan pada platform Casdoor secara otomatis.📜 DeskripsiSkrip ini dirancang untuk membantu para peneliti keamanan dan administrator sistem dalam mengidentifikasi potensi kerentanan pada implementasi Casdoor. Alat ini dapat membuat pengguna baru dengan hak istimewa melalui endpoint SCIM yang terekspos, yang menandakan adanya kesalahan konfigurasi keamanan.✨ FiturPemindaian Cepat: Secara efisien memeriksa endpoint yang rentan.Dua Mode Operasi: Mendukung pemindaian target tunggal atau pemindaian massal dari daftar file.Penambahan Protokol Otomatis: Secara otomatis menambahkan http:// jika target dimasukkan tanpa protokol.Output Jelas: Menampilkan hasil yang mudah dibaca dengan informasi kredensial jika berhasil.Mudah Digunakan: Antarmuka baris perintah yang sederhana dan intuitif.🔍 Dorks (Pencarian)Gunakan dorks berikut pada mesin pencari IoT untuk menemukan target yang berpotensi rentan:Fofa:body="urn:ietf:params:scim:schemas:core:2.0:User"
Shodan:http.html:"urn:ietf:params:scim:schemas:core:2.0:User"
Google:intext:"urn:ietf:params:scim:schemas:core:2.0:User"
🚀 InstalasiUntuk menggunakan skrip ini, ikuti langkah-langkah berikut:Kloning Repositorigit clone https://github.com/Sincan2/casdoor-scanner.git
cd casdoor-scanner
Catatan: Ganti casdoor-scanner dengan nama repositori Anda yang sebenarnya jika berbeda.Instal KetergantunganSkrip ini memerlukan beberapa pustaka Python. Instal dengan perintah di bawah ini:pip install requests termcolor
Atau jika Anda memiliki file requirements.txt:pip install -r requirements.txt
🛠️ PenggunaanPastikan Anda memberikan izin eksekusi pada skrip (hanya perlu dilakukan sekali):chmod +x pindai.py
Ada dua cara untuk menjalankan pemindai:1. Memindai Target TunggalLangsung berikan IP atau domain sebagai argumen../pindai.py [IP_TARGET:PORT]
Contoh:./pindai.py 4.201.155.100:8080
2. Memindai dari Daftar FileBuat sebuah file (misalnya targets.txt) dan isi dengan daftar target (satu per baris).4.201.155.100:8080
contoh.com
123.45.67.89:8000
Jalankan skrip dengan argumen --file../pindai.py --file targets.txt
Contoh Output Jika Berhasil[*] Memindai target: http://4.201.155.100:8080

🔥[TARGET RENTAN DITEMUKAN]🔥
➡️ Target: http://4.201.155.100:8080/scim/Users
💚 Nama Pengguna: aBcDeFgHiJkL
💚 Kata Sandi: 1a2b3c4d5e6f
--------------------------------------------------
👨‍💻 Kredit & KontribusiAlat ini dikembangkan dan dikelola oleh Sincan2.Kontribusi, laporan bug, atau permintaan fitur sangat kami hargai! Jangan ragu untuk membuat issue atau pull request.⚠️ Penafian (Disclaimer)Alat ini dibuat untuk tujuan pendidikan dan penelitian keamanan yang sah. Pengguna bertanggung jawab penuh atas tindakan mereka sendiri. Pengembang tidak bertanggung jawab atas penyalahgunaan atau kerusakan yang disebabkan oleh program ini. Gunakan dengan bijak dan hanya pada sistem yang Anda miliki izin untuk mengujinya.📄 LisensiProyek ini dilisensikan di bawah Lisensi MIT.
