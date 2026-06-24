# Praktikum Scraping – Pertemuan 8

This folder contains the **Pertemuan 8** project for the Praktikum Data Scraping course at STIKOM PGRI Banyuwangi. The focus for this meeting is on building and running Python scraping scripts that collect news data, save results to a MySQL database, export cleaned results to Excel, and optionally run as a scheduled/cron task.

---

## ✨ Highlights

- Python scraping scripts using `requests` and `BeautifulSoup`.
- Database integration with MySQL (`mysql-connector-python`).
- Cleaning utilities to normalize and sanitize text before storing.
- Export scraped & cleaned results to Excel using `pandas`.
- A simple cron-friendly wrapper that logs automation results to `log_otomasi.txt`.

---

## 🚀 Files

- `scraping/index.py`  — Main scraping script: cleans text, deep-scrapes article body, saves to `tbl_berita` and `hasil_cleaning`, and exports cleaned rows to `hasil_cleaning.xlsx`.
- `scraping/cron_scraper.py` — Lightweight wrapper function `jalankan_scraper_otomatis()` to run periodic scraping and append status logs to `log_otomasi.txt`.
- `scraping/log_otomasi.txt` — Generated when the cron wrapper runs to record success/failure messages.

---

## 🛠️ Prerequisites

- Python 3.8+
- MySQL server with a database named `db_scraping` and a table `tbl_berita` (scripts will create `hasil_cleaning` if missing).
- Recommended Python packages (install via pip):

```bash
pip install requests beautifulsoup4 mysql-connector-python pandas openpyxl
```

---

## ▶️ How to run

Run the main scraper (deep scraping + export):

```bash
python scraping/index.py
```

Run the cron-style wrapper (records results to `log_otomasi.txt`):

```bash
python scraping/cron_scraper.py
```

Or run the wrapper in `index.py` which now includes a `jalankan_scraper_otomatis()` wrapper that logs results to the same `log_otomasi.txt` file when executed as a script:

```bash
python scraping/index.py
```

---

## 📦 Project Structure

```
Pertemuan8/
├─ scraping/
│  ├─ index.py
│  ├─ cron_scraper.py
│  └─ log_otomasi.txt   # created when the wrapper runs
├─ README.md            # THIS FILE
```

---

## 📚 Notes

- Ensure your MySQL server is running before executing the scripts.
- The scripts perform a basic duplicate check using the `judul` field in `tbl_berita` to avoid repeated inserts.
- If you want to schedule the wrapper on Windows, you can use Task Scheduler to call `python path\to\scraping\index.py` at desired intervals.

---

© {new Date().getFullYear()} Praktikum Data Scraping – STIKOM PGRI Banyuwangi
