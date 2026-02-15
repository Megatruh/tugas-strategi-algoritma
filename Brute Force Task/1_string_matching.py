# Tugas Praktikum 1 — Pencarian String (Pattern Matching)
# Tujuan: Memahami konsep eksplorasi semua kemungkinan posisi substring

import time

def brute_force_string_matching(teks, pattern):
    """
    Algoritma Brute Force untuk Pattern Matching
    Mencari semua kemunculan pattern dalam teks
    """
    n = len(teks)
    m = len(pattern)
    
    indeks_ditemukan = []  # Menyimpan indeks kemunculan pattern
    jumlah_perbandingan = 0  # Counter perbandingan karakter
    
    # Geser pattern dari posisi 0 sampai n-m
    for i in range(n - m + 1):
        j = 0
        
        # Bandingkan karakter per karakter
        while j < m:
            jumlah_perbandingan += 1  # Hitung setiap perbandingan
            
            if teks[i + j] != pattern[j]:
                break  # Tidak cocok, geser pattern
            j += 1
        
        # Jika semua karakter cocok
        if j == m:
            indeks_ditemukan.append(i)
    
    return indeks_ditemukan, jumlah_perbandingan

# ==========================================
# PROGRAM UTAMA
# ==========================================

print("=" * 70)
print("PENCARIAN STRING (PATTERN MATCHING) - BRUTE FORCE")
print("=" * 70)

# Input sesuai soal
teks = "ALGORITMASTRATEGIALGORITMA"
pattern = "RIT"

print(f"\nTeks    : \"{teks}\"")
print(f"Pattern : \"{pattern}\"")
print(f"Panjang teks (n)    : {len(teks)}")
print(f"Panjang pattern (m) : {len(pattern)}")
print()

# ==========================================
# 1. Implementasi algoritma pencarian string brute force
# ==========================================
print("-" * 70)
print("1. IMPLEMENTASI ALGORITMA BRUTE FORCE")
print("-" * 70)

print("\nProses pencarian:")
print("  - Geser pattern dari posisi 0 sampai n-m")
print("  - Di setiap posisi, bandingkan karakter per karakter")
print("  - Jika cocok semua, catat indeks")

start_time = time.perf_counter()
indeks_hasil, total_perbandingan = brute_force_string_matching(teks, pattern)
end_time = time.perf_counter()

print()

# ==========================================
# 2. Tampilkan indeks kemunculan pattern
# ==========================================
print("-" * 70)
print("2. INDEKS KEMUNCULAN PATTERN")
print("-" * 70)

if indeks_hasil:
    print(f"\nPattern \"{pattern}\" ditemukan pada indeks: {indeks_hasil}")
    print(f"Jumlah kemunculan: {len(indeks_hasil)} kali")
else:
    print(f"\nPattern \"{pattern}\" TIDAK DITEMUKAN dalam teks.")

print()

# ==========================================
# 3. Hitung jumlah perbandingan karakter
# ==========================================
print("-" * 70)
print("3. JUMLAH PERBANDINGAN KARAKTER")
print("-" * 70)

print(f"\nTotal perbandingan karakter: {total_perbandingan}")
print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")

# Detail perbandingan
n = len(teks)
m = len(pattern)
print(f"\nDetail:")
print(f"  - Posisi yang diperiksa: {n - m + 1} posisi (dari 0 sampai {n-m})")
print(f"  - Setiap posisi dibandingkan maksimal {m} karakter")

print()

# ==========================================
# 4. Analisis kompleksitas waktu
# ==========================================
print("-" * 70)
print("4. ANALISIS KOMPLEKSITAS WAKTU")
print("-" * 70)

print(f"\nDimana: n = {n} (panjang teks), m = {m} (panjang pattern)")

print(f"\n• BEST CASE: O(n)")
print(f"  - Pattern tidak cocok di karakter pertama setiap posisi")
print(f"  - Hanya 1 perbandingan per posisi")
print(f"  - Total: {n - m + 1} perbandingan")

print(f"\n• WORST CASE: O(n x m) = O({n} x {m}) = O({n * m})")
print(f"  - Pattern hampir cocok di setiap posisi")
print(f"  - Contoh: teks = \"AAAAAA\", pattern = \"AAB\"")
print(f"  - Maksimal: {n - m + 1} x {m} = {(n - m + 1) * m} perbandingan")

print(f"\n• AVERAGE CASE: O(n x m)")
print(f"  - Tergantung distribusi karakter")
print(f"  - Biasanya mendekati O(n) untuk teks acak")


