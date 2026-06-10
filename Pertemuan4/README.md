# Praktikum Scraping - Pertemuan 4

## Deskripsi
Proyek ini melakukan scraping judul berita dari halaman `https://inet.detik.com/`, menyimpan data mentah ke database MySQL, melakukan proses pembersihan data, menyimpan hasil cleaning ke tabel `hasil_cleaning`, dan mengekspor data cleaned ke file Excel.

## Struktur Proyek
- `index.py` : Script utama yang melakukan scraping, pembersihan data, penyimpanan ke database, dan ekspor ke Excel.
- `hasil_cleaning.xlsx` : Contoh output Excel hasil ekspor.
- `venv/` : Virtual environment Python (opsional, jika digunakan).

## Persiapan
1. Buka terminal di folder `Pertemuan4`.
2. Buat virtual environment (opsional tetapi direkomendasikan):

```bash
python -m venv venv
```

3. Aktifkan virtual environment di Windows:

```bash
.\venv\Scripts\Activate
```

4. Pastikan MySQL berjalan dan database `db_scraping` tersedia.

5. Install dependensi Python.

## Dependensi
Pastikan Python dan MySQL sudah terpasang.

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
Skrip menghubungkan ke database MySQL dengan konfigurasi default:
- host: `localhost`
- user: `root`
- password: `` (kosong)
- database: `db_scraping`

Sebelum menjalankan, buat database MySQL jika belum ada:

```sql
CREATE DATABASE db_scraping;
```

Pastikan tabel `tbl_berita` sudah tersedia. Contoh struktur minimal:

```sql
CREATE TABLE tbl_berita (
  id INT AUTO_INCREMENT PRIMARY KEY,
  judul TEXT,
  url_link TEXT,
  url_gambar TEXT,
  waktu_scraping DATETIME
);
```

Tabel `hasil_cleaning` akan dibuat otomatis oleh script jika belum ada.

## Cara Menjalankan
Pastikan virtual environment sudah aktif jika digunakan.

Jalankan script dengan:

```bash
python index.py
```

Output yang diharapkan:
- Data mentah disimpan di tabel `tbl_berita`
- Data hasil cleaning disimpan di tabel `hasil_cleaning`
- File Excel `hasil_cleaning.xlsx` dibuat di folder `Pertemuan4`

## Catatan
- Jika ingin mengubah jumlah berita yang diambil, sesuaikan slicing `daftar_berita[:25]` di `index.py`.
- Jika terjadi error koneksi database, cek kredensial dan pastikan MySQL berjalan.
