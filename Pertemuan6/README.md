# Praktikum Scraping – Pertemuan 6

This repository contains the **Pertemuan 6** project for the Praktikum Data Scraping course at STIKOM PGRI Banyuwangi. The application is a **Next.js** based news‑scraping portal that demonstrates fetching data from a local API and displaying it in a clean, responsive UI.

---

## ✨ Features

- **Simple Card Layout** – Displays news items in a responsive grid (1 column on mobile, 2 on tablet, 3 on desktop).
- **Data Fetching** – Retrieves articles from the endpoint **`/api/berita`**.
- **Image Handling** – Shows article images when available, with a graceful fallback for missing images.
- **Date Formatting** – Parses timestamps and displays them in Indonesian locale, with a fallback message when the date is invalid.
- **Basic Styling** – Uses Tailwind CSS for a clean look and integrates the Inter font via `next/font`.

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

- The front‑end fetches the list of news articles from **`/api/berita`**, which returns a JSON payload with fields such as `id`, `judul_asli`, `judul_clean`, `url_gambar`, `waktu_scraping`, and `isi_berita`.
- Each article is displayed in a card showing the image, title, category badge, and formatted date.

---

## 📦 Project Structure

```
Pertemuan6/
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

You can deploy the app to **Vercel** with the following steps:
1. Push the repository to GitHub.
2. Import the project on Vercel and follow the automatic build process.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have ideas for improvements or discover bugs.

---

© {new Date().getFullYear()} Praktikum Data Scraping – STIKOM PGRI Banyuwangi
