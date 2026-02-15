# Tugas Praktikum 2 — Subset SUM
# Tujuan: Memahami eksplorasi kombinasi menggunakan brute force

from itertools import chain, combinations
import time

def powerset(iterable):
    """Generate semua subset (powerset) dari iterable"""
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subset_sum_bruteforce(arr, target):
    """Cari semua subset yang jumlahnya sama dengan target"""
    # 1. Generate semua subset
    semua_subset = list(powerset(arr))
    
    # 2. Hitung jumlah setiap subset dan cari yang sesuai target
    subset_target = []
    for subset in semua_subset:
        if sum(subset) == target:
            subset_target.append(subset)
    
    return semua_subset, subset_target

# ==========================================
# PROGRAM UTAMA
# ==========================================

print("=" * 70)
print("SUBSET SUM - BRUTE FORCE")
print("=" * 70)

# Input sesuai soal
arr_A = [3, 5, 9, 12]
target = 17

print(f"\nArray A = {arr_A}")
print(f"Target  = {target}")
print()

# ==========================================
# 1. Generate semua subset (2^n kemungkinan)
# ==========================================
print("-" * 70)
print("1. GENERATE SEMUA SUBSET (2^n kemungkinan)")
print("-" * 70)

semua_subset, subset_target = subset_sum_bruteforce(arr_A, target)

print(f"\nJumlah elemen (n): {len(arr_A)}")
print(f"Total subset: 2^{len(arr_A)} = {len(semua_subset)} subset")
print(f"\nSemua subset:")
for i, subset in enumerate(semua_subset, 1):
    print(f"{subset}")


# ==========================================
# 2. Tampilkan subset yang memenuhi target
# ==========================================
print("-" * 70)
print("2. SUBSET YANG MEMENUHI TARGET")
print("-" * 70)

if not subset_target:
    print(f"\nTidak ada subset dari array {arr_A} yang jumlahnya = {target}")
else:
    print(f"\nSubset yang jumlahnya = {target}:")
    for subset in subset_target:
        elemen_str = " + ".join(map(str, subset))
        print(f"  {subset} → {elemen_str} = {sum(subset)}")

print()

# ==========================================
# 3. Hitung total subset yang diperiksa
# ==========================================
print("-" * 70)
print("3. TOTAL SUBSET YANG DIPERIKSA")
print("-" * 70)

print(f"\nTotal subset yang diperiksa: {len(semua_subset)}")
print(f"Subset yang memenuhi target: {len(subset_target)}")

print()

# ==========================================
# 4. Uji dengan n = 4, 5, 6 dan bandingkan runtime
# ==========================================
print("-" * 70)
print("4. PERBANDINGAN RUNTIME (n = 4, 5, 6)")
print("-" * 70)

test_cases = [
    ([3, 5, 9, 12], 17),           # n = 4
    ([3, 5, 7, 9, 12], 12),        # n = 5
    ([3, 4, 7, 6, 9, 12], 10)      # n = 6
]

print(f"\n{'n':<5} {'Array':<25} {'Target':<8} {'Subset (2^n)':<15} {'Runtime (detik)':<15}")
print("=" * 70)

for arr, tgt in test_cases:
    start = time.perf_counter()
    
    semua, hasil = subset_sum_bruteforce(arr, tgt)
    
    end = time.perf_counter()
    
    print(f"{len(arr):<5} {str(arr):<25} {tgt:<8} {len(semua):<15} {end - start:.6f}")

