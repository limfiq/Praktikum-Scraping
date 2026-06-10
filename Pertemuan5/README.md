# Praktikum Scraping - Pertemuan 5

## Deskripsi
Script ini melakukan scraping berita dari `https://inet.detik.com/`, melakukan validasi duplikat, dan menyimpan data baru ke tabel `tbl_berita_inet` pada database MySQL.

## Struktur Folder
- `index.py` : Script utama untuk scraping, validasi duplicate, dan penyimpanan ke MySQL.
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

Install dependensi dengan:

```bash
pip install requests beautifulsoup4 mysql-connector-python
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
CREATE TABLE tbl_berita_inet (
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
