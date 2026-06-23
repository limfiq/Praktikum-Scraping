import { db } from '@/lib/db';

async function getBerita() {
  const [rows] = await db.query(
    'SELECT * FROM hasil_cleaning ORDER BY waktu_scraping DESC LIMIT 12'
  );
  return rows as any[];
}

export default async function DashboardBerita() {
  const dataBerita = await getBerita();

  return (
    <main className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-6xl mx-auto">
        <header className="mb-10 text-center">
          <h1 className="text-4xl font-bold text-blue-800">News Scraper Dashboard</h1>
          <p className="text-gray-600 mt-2">Visualisasi Data Hasil Cleaning - Pertemuan 6</p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {dataBerita.map((berita) => (
            <div key={berita.id} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow">
              {berita.url_gambar && (
                <img 
                  src={berita.url_gambar} 
                  alt={berita.judul_clean} 
                  className="w-full h-48 object-cover"
                />
              )}
              <div className="p-5">
                <span className="text-xs font-semibold text-blue-500 uppercase tracking-wide">
                  {new Date(berita.waktu_scraping).toLocaleDateString('id-ID')}
                </span>
                <h2 className="mt-2 text-xl font-bold text-gray-900 leading-tight">
                  {berita.judul_clean}
                </h2>
                <p className="mt-3 text-gray-600 text-sm line-clamp-3">
                  {berita.isi_berita}
                </p>
                <a 
                  href={berita.url_link} 
                  target="_blank" 
                  className="mt-4 inline-block text-blue-600 font-semibold hover:underline"
                >
                  Baca Selengkapnya &rarr;
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
