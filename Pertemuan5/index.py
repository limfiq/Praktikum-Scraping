import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime

# Fungsi melakukan koneksi ke database MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_scraping"
    )

# Fungsi utama untuk scraping dan simpan data
def sinkronisasi_data_detik():
    url = "https://inet.detik.com/"
    print(f"Mengirim permintaan ke: {url}")
    
    try:
        # TAHAP 1: REQUEST & PARSE
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.select('.list-content__item')
        
        # TAHAP 2: KONEKSI DATABASE
        conn = get_db_connection()
        cursor = conn.cursor()
        
        data_baru_tersimpan = 0
        
        for art in articles[:10]: # Mengambil 10 data teratas
            judul_tag = art.select_one('.media__title a')
            if not judul_tag:
                continue
                
            judul = judul_tag.text.strip()
            link = judul_tag['href']
            
            img_tag = art.select_one('.media__image img')
            img_url = img_tag.get('src') if img_tag else ""
            
            # TAHAP 3: VALIDASI DATA GANDA (DUPLICATE CHECK)
            query_cek = "SELECT id FROM tbl_berita_inet WHERE judul = %s"
            cursor.execute(query_cek, (judul,))
            result = cursor.fetchone()
            
            if result is None:
                # Jika data belum ada, lakukan INSERT
                query_insert = """
                INSERT INTO tbl_berita_inet (judul, url_link, gambar_url, waktu_simpan) 
                VALUES (%s, %s, %s, %s)
                """
                nilai_data = (judul, link, img_url, datetime.now())
                cursor.execute(query_insert, nilai_data)
                data_baru_tersimpan += 1
                print(f" Saved: {judul[:40]}...")
        
        # Commit untuk menyimpan perubahan permanen di database
        conn.commit()
        print(f"\n Proses selesai. Berhasil menambahkan {data_baru_tersimpan} data baru.")
        
    except mysql.connector.Error as db_err:
        print(f"❌ Terjadi kesalahan pada Database: {db_err}")
    except Exception as e:
        print(f"❌ Terjadi kegagalan sistem: {e}")
    finally:
        # Menutup jalur koneksi data demi keamanan
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Koneksi database ditutup dengan aman.")

if __name__ == "__main__":
    sinkronisasi_data_detik()