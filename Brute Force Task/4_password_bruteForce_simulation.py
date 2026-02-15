# Tugas Praktikum 4 — Password Brute Force Simulation
# Tujuan: Memahami eksplorasi kombinasi karakter

from itertools import product
import time

# Alfabet yang digunakan
alfabet = ['a', 'b', 'c', '1', '2']

def generate_kombinasi(panjang):
    """Generate semua kombinasi password dengan panjang tertentu"""
    # product menghasilkan cartesian product (dengan pengulangan)
    # Contoh: product(['a','b'], repeat=2) → aa, ab, ba, bb
    kombinasi = list(product(alfabet, repeat=panjang))
    # Gabungkan hasil cartesian product yang berupa tuple menjadi string
    kombinasi_str = [''.join(k) for k in kombinasi]
    return kombinasi_str

def brute_force_password(target, panjang):
    """Brute force untuk mencari password target"""
    kombinasi = generate_kombinasi(panjang)
    percobaan = 0
    
    for password in kombinasi:
        percobaan += 1
        if password == target:
            return percobaan, password, len(kombinasi)
    
    return -1, None, len(kombinasi)  # Tidak ditemukan

# ==========================================
# PROGRAM UTAMA
# ==========================================

print("=" * 60)
print("PASSWORD BRUTE FORCE SIMULATION")
print("=" * 60)
print(f"Alfabet yang digunakan: {alfabet}")
print(f"Jumlah karakter alfabet: {len(alfabet)}")
print()

# Target password
target = "b1a"
print(f"Target password: '{target}'")
print()

# ==========================================
# 1. Generate semua kombinasi (panjang 3)
# ==========================================
print("-" * 60)
print("1. GENERATE SEMUA KOMBINASI (Panjang 3)")
print("-" * 60)

kombinasi_3 = generate_kombinasi(3)
print(f"Total kombinasi untuk panjang 3: {len(alfabet)}^3 = {len(kombinasi_3)}")
print(f"\nSemua kombinasi:")
for i, k in enumerate(kombinasi_3, 1):
    print(f"{k}", end="  ")
    if i % 10 == 0:
        print()
print("\n")

# ==========================================
# 2. Hitung berapa percobaan hingga ditemukan
# ==========================================
print("-" * 60)
print("2. BRUTE FORCE MENCARI TARGET")
print("-" * 60)

start_time = time.perf_counter()
percobaan, password_found, total = brute_force_password(target, len(target))
end_time = time.perf_counter()

if password_found:
    print(f"Password '{target}' DITEMUKAN!")
    print(f"Jumlah percobaan: {percobaan} dari {total} kombinasi")
    print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")
else:
    print(f"Password '{target}' TIDAK DITEMUKAN")
print()

# ==========================================
# 3. Uji panjang 3 dan panjang 4
# ==========================================
print("-" * 60)
print("3. PERBANDINGAN PANJANG 3 DAN PANJANG 4")
print("-" * 60)

for panjang in [3, 4]:
    kombinasi = generate_kombinasi(panjang)
    
    start_time = time.perf_counter()
    # Generate semua kombinasi (simulasi worst case)
    for k in kombinasi:
        pass  # Proses setiap kombinasi
    end_time = time.perf_counter()
    
    print(f"\nPanjang {panjang}:")
    print(f"  Total kombinasi: {len(alfabet)}^{panjang} = {len(kombinasi)}")
    print(f"  Waktu generate: {end_time - start_time:.6f} detik")

print()

# ==========================================
# 4. Analisis pertumbuhan kompleksitas
# ==========================================
print("-" * 60)
print("4. ANALISIS PERTUMBUHAN KOMPLEKSITAS")
print("-" * 60)

print(f"\nDengan alfabet = {len(alfabet)} karakter:")
print()
print(f"{'Panjang':<10} {'Kombinasi':<15} {'Rumus':<15} {'Waktu Runtime':<20}")
print("=" * 60)

for panjang in range(1, 7):
    start_time = time.perf_counter()
    kombinasi = generate_kombinasi(panjang)
    # Simulasi pengecekan setiap kombinasi
    for k in kombinasi:
        pass
    end_time = time.perf_counter()
    
    print(f"{panjang:<10} {len(kombinasi):<15} {len(alfabet)}^{panjang:<12} {end_time - start_time:.6f} detik")

print()
print("-" * 60)
print("KESIMPULAN:")
print("-" * 60)
print(f"• Kompleksitas waktu: O(n^m)")
print(f"  - n = jumlah karakter alfabet ({len(alfabet)})")
print(f"  - m = panjang password")
print(f"• Pertumbuhan EKSPONENSIAL")
print(f"• Setiap penambahan 1 karakter panjang password,")
print(f"  jumlah kombinasi bertambah {len(alfabet)}x lipat")

