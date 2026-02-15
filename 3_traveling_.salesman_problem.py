# Tugas Praktikum 3 — Traveling Salesman Problem (TSP Mini)
# Tujuan: Memahami brute force dengan permutasi (n!)

from itertools import permutations
import time

# Matriks jarak antar kota (A=0, B=1, C=2, D=3)
#        A   B   C   D
matrix_jarak = [
    [0,  10, 15, 20],  # A
    [10, 0,  35, 25],  # B
    [15, 35, 0,  30],  # C
    [20, 25, 30, 0]    # D
]

kota = ['A', 'B', 'C', 'D']
kota_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

def hitung_jarak_rute(rute):
    """Hitung total jarak untuk rute tertentu (kembali ke awal)"""
    total_jarak = 0
    
    for i in range(len(rute) - 1):
        dari = kota_index[rute[i]]
        ke = kota_index[rute[i + 1]]
        total_jarak += matrix_jarak[dari][ke]
    
    # Kembali ke kota awal
    dari = kota_index[rute[-1]]
    ke = kota_index[rute[0]]
    total_jarak += matrix_jarak[dari][ke]
    
    return total_jarak

# ==========================================
# PROGRAM UTAMA
# ==========================================

print("=" * 70)
print("TRAVELING SALESMAN PROBLEM (TSP) - BRUTE FORCE")
print("=" * 70)

print("\nMatriks Jarak:")
print("      A    B    C    D")
for i, row in enumerate(matrix_jarak):
    print(f"  {kota[i]}  {row}")

print()

# ==========================================
# 1. Generate semua permutasi rute (fix kota awal A)
# ==========================================
print("-" * 70)
print("1. GENERATE SEMUA PERMUTASI RUTE (Fix kota awal A)")
print("-" * 70)

# Fix kota awal A, permutasi kota lainnya (B, C, D)
kota_lain = ['B', 'C', 'D']
semua_permutasi = list(permutations(kota_lain))

# Tambahkan A di depan setiap permutasi
semua_rute = [('A',) + p for p in semua_permutasi]

print(f"Kota awal: A (fixed)")
print(f"Kota yang dipermutasi: {kota_lain}")
print(f"Jumlah permutasi: {len(kota_lain)}! = {len(semua_rute)} rute")
print(f"\nSemua rute yang akan diperiksa:")

for i, rute in enumerate(semua_rute, 1):
    rute_str = " → ".join(rute) + " → A"
    print(f"  {i}. {rute_str}")


# ==========================================
# 2. Hitung total jarak setiap rute
# ==========================================
print("-" * 70)
print("2. HITUNG TOTAL JARAK SETIAP RUTE")
print("-" * 70)

start_time = time.perf_counter()

hasil_rute = []
for rute in semua_rute:
    jarak = hitung_jarak_rute(rute)
    hasil_rute.append((rute, jarak))

end_time = time.perf_counter()

print(f"\n{'No':<4} {'Rute':<25} {'Total Jarak':<15}")
print("=" * 50)
for i, (rute, jarak) in enumerate(hasil_rute, 1):
    rute_str = " → ".join(rute) + " → A"
    print(f"{i:<4} {rute_str:<25} {jarak}")

print()

# ==========================================
# 3. Tentukan rute minimum
# ==========================================
print("-" * 70)
print("3. RUTE MINIMUM (TERPENDEK)")
print("-" * 70)

rute_minimum = min(hasil_rute, key=lambda x: x[1])
rute_min_str = " → ".join(rute_minimum[0]) + " → A"

print(f"\nRute terpendek: {rute_min_str}")
print(f"Total jarak   : {rute_minimum[1]}")
print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")

print()

# ==========================================
# 4. Hitung jumlah rute yang diperiksa
# ==========================================
print("-" * 70)
print("4. JUMLAH RUTE YANG DIPERIKSA")
print("-" * 70)

jumlah_rute = len(hasil_rute)
print(f"\nJumlah rute yang diperiksa: {jumlah_rute}")
print(f"Rumus: (n-1)! dimana n = jumlah kota")
print(f"       (4-1)! = 3! = 6 rute")

print()

# ==========================================
# PERTANYAAN
# ==========================================
print("=" * 70)
print("JAWABAN PERTANYAAN")
print("=" * 70)

# 1. Berapa kompleksitasnya?
print("\n1. KOMPLEKSITAS:")
print("   • Time Complexity : O((n-1)!)")
print("   • Untuk n kota, kita perlu memeriksa (n-1)! kemungkinan rute")
print("   • Alasan: kota awal di-fix, sehingga hanya permutasi (n-1) kota lain")
print("   • Kompleksitas FAKTORIAL = pertumbuhan sangat cepat!")

# 2. Jika kota menjadi 10, berapa jumlah rute?
import math
n_10 = 10
rute_10 = math.factorial(n_10 - 1)

print("\n2. JIKA KOTA MENJADI 10:")
print(f"   • Jumlah rute = (10-1)! = 9!")
print(f"   • Jumlah rute = {rute_10:,} rute")
print(f"   • Sangat banyak! Brute force menjadi tidak praktis.")

print()
print("-" * 70)
print("TABEL PERTUMBUHAN KOMPLEKSITAS")
print("-" * 70)
print(f"\n{'Jumlah Kota (n)':<20} {'Jumlah Rute (n-1)!':<25}")
print("=" * 50)
for n in range(4, 13):
    rute = math.factorial(n - 1)
    print(f"{n:<20} {rute:>20,}")

print()
print("KESIMPULAN:")
print("• Brute force TSP sangat tidak efisien untuk n besar")
print("• Perlu algoritma yang lebih baik seperti Dynamic Programming,")
print("  Branch and Bound, atau algoritma heuristik")



