# Farhan Esha Putra Kusuma Atmaja
# 247006111066

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
