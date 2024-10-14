from google_play_scraper import app, reviews, Sort

# Mendapatkan informasi aplikasi
result = app('com.tgc.sky.android')

# Mendapatkan ulasan
ulasan, _ = reviews(
    'com.tgc.sky.android',
    lang='id',            # Bahasa Indonesia
    country='id',         # Negara Indonesia
    sort=Sort.NEWEST,     # Urutkan berdasarkan ulasan terbaru
    count=100             # Jumlah ulasan yang ingin diambil
)

# Tentukan rating yang ingin diambil, misalnya 5, 4, atau 3
rating_filter = [5, 4, 3]

# Menyimpan ulasan ke dalam file .txt
with open("ulasan_google_play.txt", "w", encoding="utf-8") as file:
    for idx, ulasan_item in enumerate(ulasan, 1):
        if ulasan_item['score'] in rating_filter:
            file.write(f"Ulasan ke-{idx}:\n")
            file.write(f"Rating: {ulasan_item['score']}\n")
            file.write(f"Nama Pengguna: {ulasan_item['userName']}\n")
            file.write(f"Tanggal: {ulasan_item['at']}\n")
            file.write(f"Ulasan:\n{ulasan_item['content']}\n")
            file.write("-" * 40 + "\n")  # Pembatas antar ulasan

print(f"Ulasan dengan rating {', '.join(map(str, rating_filter))} berhasil disimpan di ulasan_google_play.txt")
