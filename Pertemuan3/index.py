import requests  
from bs4 import BeautifulSoup  
import mysql.connector
from datetime import datetime

def ambil_judul_detik():  
    url = "https://inet.detik.com/"  
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Konfigurasi Database
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'db_scraping'
    }

    conn = None
    try:
        # Inisialisasi koneksi database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        print("✅ Terhubung ke database.")

        response = requests.get(url, headers=headers)  

        if response.status_code == 200:  
            # Parsing HTML  
            soup = BeautifulSoup(response.text, 'html.parser')  
            # Mencari semua elemen judul berita  
            daftar_berita = soup.select('a[class*="ph_newsfeed_d"]')  
            
            if not daftar_berita:  
                print("❌ Tidak ditemukan judul berita di halaman.")
            else:  
                waktu_sekarang = datetime.now()
                
                for berita in daftar_berita[:25]: # Ambil 25 berita pertama  
                    img_tag = berita.find('img')
                    img_url = img_tag.get('src') if img_tag else None
                    # Membersihkan judul dari spasi berlebih dan baris baru
                    judul = " ".join(berita.text.split())
                    link = berita['href']

                    # Query Insert ke MySQL
                    sql = "INSERT INTO tbl_berita (judul, url_link, url_gambar, waktu_scraping) VALUES (%s, %s, %s, %s)"
                    val = (judul, link, img_url, waktu_sekarang)
                    
                    cursor.execute(sql, val)
                    print(f"Disimpan: {judul[:50]}...")

                conn.commit()
                print(f"✅ Berhasil menyimpan {cursor.rowcount} data ke database.")
        else:  
            print(f"❌ Gagal terhubung ke detik.com (Status: {response.status_code})")  

    except mysql.connector.Error as err:
        print(f"❌ Error Database: {err}")
    except Exception as e:
        print(f"❌ Error Terjadi: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("🔌 Koneksi database ditutup.")

ambil_judul_detik() 

 