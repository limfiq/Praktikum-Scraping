# Praktikum Scraping - Pertemuan 2

## Deskripsi
Project ini melakukan scraping judul berita dari halaman `https://inet.detik.com/`, menyimpan hasil ke file `hasil.txt`, dan menampilkan hasil di konsol.

## Struktur Folder
- `index.py` : Script utama untuk scraping dan menyimpan hasil ke `hasil.txt`.
- `hasil.txt` : Output teks hasil scraping.
- `Scrapling/` : Subfolder tambahan (isi subfolder dapat berisi latihan atau eksperimen scraping lain).
- `venv/` : Virtual environment Python (opsional).

## Persiapan
1. Buka terminal di folder `Pertemuan2`.
2. Buat virtual environment (opsional tetapi direkomendasikan):

```bash
python -m venv venv
```

3. Aktifkan virtual environment di Windows:

```bash
.\venv\Scripts\Activate
```

4. Install dependensi Python.

## Dependensi
Python packages yang digunakan:
- `requests`
- `beautifulsoup4`

Install dependensi dengan:

```bash
pip install requests beautifulsoup4
```

## Cara Menjalankan
Pastikan virtual environment sudah aktif jika digunakan.

Jalankan script dari dalam folder `Pertemuan2`:

```bash
python index.py
```

## Output
- `hasil.txt` akan dibuat atau diperbarui dengan daftar judul berita dan link dari Detik.
- Konsol akan menampilkan daftar hasil scraping.

## Catatan
- Jika struktur HTML situs berubah, selector CSS di `index.py` harus diperbarui.
- Script mengambil 25 judul pertama sesuai baris `for berita in daftar_berita[:25]`.
