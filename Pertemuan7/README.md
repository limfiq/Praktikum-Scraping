# Praktikum Scraping – Pertemuan 7

This repository contains the **Pertemuan 7** project for the Praktikum Data Scraping course at STIKOM PGRI Banyuwangi. The application is built with **Next.js** and showcases a simple news‑scraping portal that fetches data from a local API, displays it in a modern UI, and provides pagination and a detailed modal view for each article.

---

## ✨ Features

- **Responsive Grid** – 1‑column on mobile, 2‑columns on tablet, 3‑columns on desktop.
- **Client‑side Pagination** – 9 articles per page with stylish navigation buttons.
- **Modal Detail View** – Click a card to open a glass‑morphic modal showing the full article, image, and source link.
- **Image handling** – Graceful fallback when an image URL is missing.
- **Date Formatting** – Validates and formats dates, displays "Tanggal tidak valid" when needed.
- **Polished UI** – Gradient background, Inter font, subtle hover effects, and glass‑morphism for a premium look.

---

## 🚀 Getting Started

1. **Install dependencies**
   ```bash
   npm install
   # or using yarn
   yarn install
   ```

2. **Run the development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

3. Open your browser at **[http://localhost:3000](http://localhost:3000)** to view the portal.

---

## 🛠️ Usage

- The front‑end fetches data from the endpoint **`/api/berita`** which returns a JSON payload with fields such as `id`, `judul_asli`, `judul_clean`, `url_gambar`, `waktu_scraping`, and `isi_berita`.
- Click any news card to open the modal with the full article content and a **"Buka Sumber →"** link that opens the original source in a new tab.

---

## 📦 Project Structure

```
Pertemuan7/
├─ src/
│  └─ app/
│     └─ page.tsx      # Main UI component
├─ public/               # Static assets (if any)
├─ README.md             # THIS FILE
└─ next.config.ts        # Next.js configuration
```

---

## 📚 Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com) – utility‑first CSS framework used for styling.
- [Inter Font on Google Fonts](https://fonts.google.com/specimen/Inter)

---

## 📦 Deploy

You can easily deploy this app to **Vercel**:
1. Push the repository to GitHub.
2. Import the project on Vercel and follow the automatic build steps.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have ideas for improvements or find bugs.

---

© {new Date().getFullYear()} Praktikum Data Scraping – STIKOM PGRI Banyuwangi
