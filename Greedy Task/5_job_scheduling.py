# 1. Deklarasi Dataset [Job, Profit, Deadline] sesuai gambar
jobs = [
    ["J1", 100, 2],
    ["J2", 19, 1],
    ["J3", 27, 2],
    ["J4", 25, 1],
    ["J5", 15, 3]
]

# 2. Mencari deadline terbesar untuk menentukan jumlah slot
max_deadline = max(job[2] for job in jobs)

# 3. Inisialisasi papan jadwal dengan None (sebanyak max_deadline)
# Kita gunakan list ukuran max_deadline + 1 agar indeks sesuai dengan jam (1, 2, 3)
jadwal = [None] * (max_deadline + 1)
total_profit = 0

# 4. Strategi Greedy 1: Urutkan job berdasarkan profit secara descending
jobs.sort(key=lambda x: x[1], reverse=True)

print("--- Proses Penjadwalan ---")

# 5. Strategi Greedy 2: Iterasi setiap job dan cek slot kosong
for job in jobs:
    nama, profit, deadline = job
    
    # Cek mundur dari waktu deadline sampai jam 1
    for slot in range(deadline, 0, -1):
        if jadwal[slot] is None:
            jadwal[slot] = nama
            total_profit += profit
            print(f"{nama} berhasil ditaruh di Slot Jam {slot}")
            break  # Job sudah dapat slot, berhenti cek mundur
    else:
        print(f"{nama} gagal dijadwalkan (Slot penuh/Deadline lewat)")

# 6. Menampilkan Hasil Akhir
print("\n--- Hasil Akhir ---")
# Menghilangkan indeks 0 karena kita mulai dari Jam 1
hasil_jadwal = [j for j in jadwal if j is not None]
print(f"Urutan Job yang dikerjakan: {hasil_jadwal}")
print(f"Total Profit Maksimal: {total_profit}")