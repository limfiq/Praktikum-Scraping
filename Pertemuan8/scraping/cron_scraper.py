import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
import os

def jalankan_scraper_otomatis():
    url = "https://inet.detik.com/"
    # path_log = "D:/Prak_Scraping/log_otomasi.txt"
    
    # Mendapatkan path direktori tempat skrip ini berada
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Menggabungkan path direktori dengan nama file log
    path_log = os.path.join(base_dir, "log_otomasi.txt")
    
    try:
        # 1. Request & Parse
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        articles = soup.select('article')
        
        # 2. Koneksi DB
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_scraping"
        )
        cursor = db.cursor()
        
        inserted = 0
        for art in articles[:10]:
            judul_tag = art.select_one('.media__title a') or art.select_one('h3 a')
            if not judul_tag: continue
            
            judul = judul_tag.text.strip()
            link = judul_tag['href']
            
            img_tag = art.select_one('.media__image img') or art.select_one('img')
            img_url = img_tag.get('src') if img_tag else ""
            
            # Cek Duplikasi
            cursor.execute("SELECT id FROM tbl_berita WHERE judul = %s", (judul,))
            if cursor.fetchone() is None:
                sql = "INSERT INTO tbl_berita (judul, url_link, gambar_url, waktu_simpan, kategori) VALUES (%s, %s, %s, %s, 'Teknologi')"
                cursor.execute(sql, (judul, link, img_url, datetime.now()))
                inserted += 1
                
        db.commit()
        cursor.close()
        db.close()
        
        # 3. Catat Log Sukses
        with open(path_log, "a") as log:
            log.write(f"[{datetime.now()}] OTOMASI SUKSES: Berhasil mengarsipkan {inserted} berita baru.\n")
            
    except Exception as e:
        # Catat Log Gagal jika XAMPP mati atau internet putus
        with open(path_log, "a") as log:
            log.write(f"[{datetime.now()}] OTOMASI GAGAL: Error -> {str(e)}\n")

if __name__ == "__main__":
    jalankan_scraper_otomatis()

# import requests
# from bs4 import BeautifulSoup
# import mysql.connector
# from datetime import datetime
# import os

# def jalankan_scraper_otomatis():
#     url = "https://inet.detik.com/"
    
#     # --- PERUBAHAN DI SINI ---
#     # Mendapatkan path direktori tempat skrip ini berada
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     # Menggabungkan path direktori dengan nama file log
#     path_log = os.path.join(base_dir, "log_otomasi.txt")
#     # -------------------------
    
#     try:
#         # ... (sisa kode Anda tetap sama)
        
#         # 1. Request & Parse
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
#         res = requests.get(url, headers=headers)
#         soup = BeautifulSoup(res.text, 'html.parser')
#         articles = soup.select('article')
        
#         # 2. Koneksi DB
#         db = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="db_scraping"
#         )
#         cursor = db.cursor()
        
#         inserted = 0
#         for art in articles[:10]:
#             judul_tag = art.select_one('.media__title a') or art.select_one('h3 a')
#             if not judul_tag: continue
            
#             judul = judul_tag.text.strip()
#             link = judul_tag['href']
            
#             img_tag = art.select_one('.media__image img') or art.select_one('img')
#             img_url = img_tag.get('src') if img_tag else ""
            
#             # Cek Duplikasi
#             cursor.execute("SELECT id FROM tbl_berita WHERE judul = %s", (judul,))
#             if cursor.fetchone() is None:
#                 sql = "INSERT INTO tbl_berita (judul, url_link, gambar_url, waktu_simpan, kategori) VALUES (%s, %s, %s, %s, 'Teknologi')"
#                 cursor.execute(sql, (judul, link, img_url, datetime.now()))
#                 inserted += 1
                
#         db.commit()
#         cursor.close()
#         db.close()
        
#         # 3. Catat Log Sukses
#         with open(path_log, "a") as log:
#             log.write(f"[{datetime.now()}] OTOMASI SUKSES: Berhasil mengarsipkan {inserted} berita baru.\n")
            
#     except Exception as e:
#         # Catat Log Gagal
#         with open(path_log, "a") as log:
#             log.write(f"[{datetime.now()}] OTOMASI GAGAL: Error -> {str(e)}\n")

# if __name__ == "__main__":
#     jalankan_scraper_otomatis()