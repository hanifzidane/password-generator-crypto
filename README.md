# 🔐 Crypto Password Manager

Aplikasi sederhana untuk menyimpan password secara aman menggunakan
Python, SQLite, dan enkripsi Fernet. Semua password disimpan secara
terenkripsi, dan hanya bisa dibuka menggunakan file `secret.key`.

## 🖼️ Tampilan Screenshot Aplikasi

(Ganti file screenshot sesuai kebutuhan) -
`screenshots/menu-utama.png` - `screenshots/tambah-password.png` -
`screenshots/liat-password.png`

## 🚀 Cara Instalasi & Menjalankan Project

Pastikan Python sudah terinstal di sistem Anda. Untuk pengguna Mac /
Linux, buat virtual environment dengan:

``` bash
python3 -m venv venv
source venv/bin/activate
```

Setelah environment aktif, install semua dependensi dengan:

``` bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum ada, buat file tersebut lalu isi
dengan:

    cryptography

Kemudian generate file enkripsi `secret.key` dengan menjalankan:

``` bash
python - <<EOF
from cryptography.fernet import Fernet
open("secret.key","wb").write(Fernet.generate_key())
print("secret.key berhasil dibuat!")
EOF
```

Setelah itu jalankan aplikasi dengan:

``` bash
python main.py
```

## 📁 Struktur Folder Project

    crypto-password-manager/
    ├── main.py
    ├── crypto.py
    ├── database.py
    ├── passwords.db
    ├── secret.key
    ├── requirements.txt
    └── screenshots/

## ⚠️ .gitignore

    passwords.db
    secret.key
    __pycache__/

## 🛠️ Troubleshooting

-   InvalidToken → secret.key tidak cocok.
-   ModuleNotFoundError: cryptography → jalankan
    `pip install cryptography`.

## 🎉 Selesai!
