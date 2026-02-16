"""
Tugas Praktikum 1 — Problem: Coin Change (Sistem Koin Kanonik)
Algoritma Greedy untuk menentukan jumlah koin minimum

Koin tersedia: {1, 5, 10, 25}
Target: 68

Strategi Greedy: Ambil koin terbesar ≤ target
"""

import math

def greedy_coin_change(target, coins):
    """
    Menghitung jumlah koin minimum menggunakan algoritma greedy.
    
    Mekanisme:
    1. Bagi nilai dengan pecahan koin terbesar
    2. Bulatkan ke bawah (floor)
    3. Kalikan hasil pembulatan dengan pecahan koin
    4. Kurangi dari nilai awal untuk mendapat sisa
    5. Ulangi dengan sisa menggunakan pecahan berikutnya
    
    Parameters:
        target: Nilai yang ingin dipecah
        coins: List pecahan koin yang tersedia
    
    Returns:
        total_coins: Jumlah total koin yang digunakan
        result: Dictionary berisi detail koin yang digunakan
    """
    # Urutkan koin dari terbesar ke terkecil
    sorted_coins = sorted(coins, reverse=True)
    
    sisa = target
    total_coins = 0
    result = {}
    
    print(f"Target awal: {target}")
    print("-" * 40)
    
    for koin in sorted_coins:
        if sisa <= 0:
            break
            
        # Langkah 1: Bagi nilai sisa dengan pecahan koin
        hasil_bagi = sisa / koin
        
        # Langkah 2: Bulatkan ke bawah (floor)
        jumlah_koin = math.floor(hasil_bagi)
        
        if jumlah_koin > 0:
            # Langkah 3: Kalikan hasil pembulatan dengan pecahan koin
            nilai_koin = jumlah_koin * koin
            
            # Langkah 4: Kurangi dari nilai sisa untuk mendapat sisa baru
            sisa_baru = sisa - nilai_koin
            
            # Tampilkan langkah-langkah
            print(f"Pecahan koin: {koin}")
            print(f"  → {sisa} / {koin} = {hasil_bagi:.2f}")
            print(f"  → Dibulatkan ke bawah: {jumlah_koin}")
            print(f"  → Nilai koin: {jumlah_koin} × {koin} = {nilai_koin}")
            print(f"  → Sisa: {sisa} - {nilai_koin} = {sisa_baru}")
            print()
            
            # Simpan hasil
            result[koin] = jumlah_koin
            total_coins += jumlah_koin
            sisa = sisa_baru
    
    return total_coins, result



# Koin yang tersedia
coins = [1, 5, 10, 25]

# Target yang ingin dicapai
target = 68

print("=" * 50)
print("ALGORITMA GREEDY - COIN CHANGE PROBLEM")
print("=" * 50)
print(f"Koin tersedia: {coins}")
print(f"Target: {target}")
print("=" * 50)
print()

# Jalankan algoritma greedy
total_coins, result = greedy_coin_change(target, coins)

# Tampilkan hasil akhir
print("=" * 50)
print("HASIL AKHIR")
print("=" * 50)
print("\nDetail koin yang digunakan:")
for koin, jumlah in sorted(result.items(), reverse=True):
    print(f"  Koin {koin}: {jumlah} buah")

print(f"\nTotal Koin = {total_coins}")

# Verifikasi
total_nilai = sum(koin * jumlah for koin, jumlah in result.items())
print(f"Verifikasi: {' + '.join([f'{jumlah}×{koin}' for koin, jumlah in sorted(result.items(), reverse=True)])} = {total_nilai}")

