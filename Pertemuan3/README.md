# Praktikum Scraping - Pertemuan 3

## Deskripsi
Project ini melakukan scraping berita dari `https://inet.detik.com/`, menyimpan data ke database MySQL, dan mencatat aktivitas ke log.

## Struktur Folder
- `index.py` : Script utama untuk scraping judul berita, menyimpan ke tabel `tbl_berita`, dan mengoutput ke database.
- `latihan.py` : Script dengan fungsi tambahan untuk scraping, validasi duplikat, deep scraping isi berita, dan logging ke file.
- `hasil.txt` : Output teks hasil scraping dasar dari `index.py`.
- `Logs/` : Folder berisi file log `log_db.txt` untuk menyimpan aktivitas dan error.
- `venv/` : Virtual environment Python (opsional).

## Persiapan
1. Buka terminal di folder `Pertemuan3`.
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
Python packages yang digunakan:
- `requests`
- `beautifulsoup4`
- `mysql-connector-python`

Install dependensi dengan:

```bash
pip install requests beautifulsoup4 mysql-connector-python
```

## Konfigurasi Database
Skrip menggunakan database MySQL dengan konfigurasi default:
- host: `localhost`
- user: `root`
- password: `` (kosong)
- database: `db_scraping`

Pastikan database sudah dibuat:

```sql
CREATE DATABASE db_scraping;
```

Contoh struktur tabel `tbl_berita` minimal:

```sql
CREATE TABLE tbl_berita (
  id INT AUTO_INCREMENT PRIMARY KEY,
  judul TEXT,
  url_link TEXT,
  url_gambar TEXT,
  isi_berita TEXT,
  waktu_scraping DATETIME
);
```

## Cara Menjalankan
Pastikan virtual environment sudah aktif jika digunakan.

Jalankan script dari dalam folder `Pertemuan3`:

```bash
python index.py
```

atau untuk versi dengan logging dan deep scraping:

```bash
python latihan.py
```

## Output
- `tbl_berita` akan diisi dengan data hasil scraping.
- `Logs/log_db.txt` akan mencatat aktivitas dan error (untuk `latihan.py`).
- `hasil.txt` akan menampung output teks hasil scraping dasar (`index.py`).

## Catatan
- `latihan.py` melakukan validasi duplicate berdasarkan judul sebelum insert.
- Jika situs berubah, selector CSS dan struktur parsing perlu disesuaikan.
