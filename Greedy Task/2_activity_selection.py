# Dataset Uji [Nama, Start, Finish]
dataset = [
    ["A1", 1, 4],
    ["A2", 3, 5],
    ["A3", 0, 6],
    ["A4", 5, 7],
    ["A5", 8, 9]
]

# 1. Urutkan berdasarkan finish time (indeks ke-2)
dataset.sort(key=lambda x: x[2])

# 2. Pilih aktivitas pertama (finish paling kecil)
aktivitas_terpilih = []
waktu_selesai_terakhir = 0

# 3. Iterasi untuk mengecek overlap
for akt in dataset:
    nama, start, finish = akt
    # Jika waktu mulai >= waktu selesai aktivitas sebelumnya
    if start >= waktu_selesai_terakhir:
        aktivitas_terpilih.append(nama)
        waktu_selesai_terakhir = finish

# Cetak hasil
print("Aktivitas yang dipilih:", aktivitas_terpilih)
print("Total aktivitas:", len(aktivitas_terpilih))