import requests
from bs4 import BeautifulSoup
import mysql.connector
import os
from datetime import datetime

# Fungsi Log (Materi Pertemuan 1 & 2)
def tulis_log(pesan):
    os.makedirs("Logs", exist_ok=True)
    with open("Logs/log_db.txt", "a") as f:
        f.write(f"[{datetime.now()}] {pesan}\n")

def koneksi_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_scraping"
    )

def scraping_to_mysql():
    url = "https://inet.detik.com/"
    print("Memulai proses scraping dan sinkronisasi database...")
    
    try:
        # 1. Scraping Data
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        # Menggunakan selector yang lebih spesifik untuk mendapatkan link dan gambar
        items = soup.select('a[class*="ph_newsfeed_d"]')
        
        # 2. Koneksi DB dan Inisialisasi
        db = None
        db = koneksi_db()
        cursor = db.cursor()
        
        count_inserted = 0
        
        for item in items[:20]:
            # Membersihkan judul dari whitespace berlebih
            judul = " ".join(item.text.split())
            link = item['href']
            
            # Mengambil link gambar
            img_tag = item.find('img')
            img_url = img_tag.get('src') if img_tag else None
            
            # 3. Validasi Duplicate (Cek apakah judul sudah ada)
            cursor.execute("SELECT id FROM tbl_berita WHERE judul = %s", (judul,))
            result = cursor.fetchone()
            
            if result is None:
                # 4. Scraping Isi Berita (Deep Scraping)
                print(f"   > Mengambil konten: {judul[:40]}...")
                try:
                    res_detail = requests.get(link, headers=headers, timeout=10)
                    soup_detail = BeautifulSoup(res_detail.text, 'html.parser')
                    # DetikInet biasanya menggunakan class detail__body-text untuk isi berita
                    body = soup_detail.select_one('.detail__body-text')
                    isi_berita = body.get_text(separator=' ', strip=True) if body else "Konten tidak ditemukan"
                except Exception as e:
                    isi_berita = f"Gagal mengambil konten: {e}"

                # 5. Insert ke Database
                sql = "INSERT INTO tbl_berita (judul, url_link, url_gambar, isi_berita, waktu_scraping) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (judul, link, img_url, isi_berita, datetime.now()))
                count_inserted += 1
        
        db.commit()
        msg = f"Berhasil sinkronisasi. {count_inserted} data baru ditambahkan."
        print(msg)
        tulis_log(msg)
        
    except Exception as e:
        err_msg = f"Kegagalan sistem: {e}"
        print(err_msg)
        tulis_log(err_msg)
    finally:
        # Menutup cursor dan koneksi dengan aman
        if 'cursor' in locals() and cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

if __name__ == "__main__":
    scraping_to_mysql()