# Praktikum Scraping - Pertemuan 5

## Deskripsi
Proyek ini melakukan scraping judul dan isi berita (Deep Scraping) secara otomatis dari `https://inet.detik.com/`. Script dilengkapi dengan validasi duplikasi data, proses pembersihan teks (menghapus tag HTML, emoji, dan karakter non-ASCII), penyimpanan ke database MySQL, serta ekspor hasil akhir ke file Excel.

## Struktur Folder
- `index.py` : Script utama untuk scraping, deep scraping, pembersihan data, dan manajemen database.
- `hasil_cleaning.xlsx` : File output hasil ekspor data yang telah dibersihkan.
- `venv/` : Virtual environment Python (opsional).

## Persiapan
1. Buka terminal di folder `Pertemuan5`.
2. (Opsional) Buat virtual environment:

```bash
python -m venv venv
```

3. Aktifkan virtual environment di Windows:

```bash
.\venv\Scripts\Activate
```

4. Pastikan MySQL berjalan dan database `db_scraping` tersedia.

## Dependensi
Python packages yang digunakan:
- `requests`
- `beautifulsoup4`
- `mysql-connector-python`
- `pandas`
- `openpyxl`

Install dependensi dengan:

```bash
pip install requests beautifulsoup4 mysql-connector-python pandas openpyxl
```

## Konfigurasi Database
Skrip menggunakan koneksi MySQL dengan konfigurasi default di `index.py`:
- host: `localhost`
- user: `root`
- password: `` (kosong)
- database: `db_scraping`

Buat database jika belum ada:

```sql
CREATE DATABASE db_scraping;
```

Buat tabel `tbl_berita_inet` contoh struktur minimal:

```sql
CREATE TABLE tbl_berita (
  id INT AUTO_INCREMENT PRIMARY KEY,
  judul TEXT,
  url_link TEXT,
  gambar_url TEXT,
  waktu_simpan DATETIME
);
```

## Cara Menjalankan
Pastikan virtual environment aktif lalu jalankan:

```bash
python index.py
```

Script akan mengambil 10 berita teratas (sesuaikan `articles[:10]` di `index.py` untuk mengubah jumlah).

## Output
- Data baru akan dimasukkan ke tabel `tbl_berita_inet`.
- Pesan proses dan jumlah data yang disimpan akan ditampilkan di konsol.

## Catatan
- Jika struktur HTML situs berubah, perbarui selector CSS (`.list-content__item`, `.media__title a`, dll.) di `index.py`.
- Sesuaikan kredensial database jika menggunakan user/password berbeda.
- Gunakan virtual environment untuk menjaga dependensi terisolasi.
