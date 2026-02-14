def permutations(iterable, r=None):
    # permutations('ABCD', 2) → AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) → 012 021 102 120 201 210

    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    
    if r > n:
        return []  # Kembalikan list kosong
    
    result = []  # List untuk menyimpan hasil
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    result.append("".join(list(pool[i] for i in indices[:r])))

    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                result.append("".join(list(pool[i] for i in indices[:r])))
                break
        else:
            break
    
    return result  # Kembalikan list hasil

teks = "ALGORITMASTRATEGIALGORITMA"
pattern = 'RIT'

# pecah teks menjadi list karakter
teks_list = list(teks)

print(len(teks_list))

# gabungkan karakter yang berkemungkinaan membentuk pattern
# masuakn dalam kemungkianan_pattern secara berurutan
kemungkianan_pattern = []

for i in range(len(teks_list)):
    if (len(teks_list)- i) > len(pattern): 
        kemungkianan_pattern.append("".join(teks_list[i:i+len(pattern)]))


# cek setiap kemungkinan pattern dengan pattern yang dicari
# kemunculan = len([j for j in kemungkianan_pattern if kemungkianan_pattern[j] == pattern])
temp = []
perbandingan_ke = []
jumlah_perbandingan = 0  # Counter untuk perbandingan

for j in range(len(kemungkianan_pattern)):
    jumlah_perbandingan += 1  # Hitung setiap perbandingan
    if kemungkianan_pattern[j] == pattern:
        perbandingan_ke.append(j+1)
        temp.append(kemungkianan_pattern[j])

kemunculan = len(temp)

# jika kemunculan nilainya 0 karena pattern tidak ditemukan dalam kemungkianan_pattern yang berurutan
# cari pattern dalam kemungkianan_pattern yang dipermutasikan

if kemunculan == 0:
    kemungkinan_baru = permutations(teks, len(pattern))
    for k in kemungkinan_baru:
        jumlah_perbandingan += 1  # Hitung perbandingan permutasi
        if k == pattern:
            kemunculan += 1
    print(f"\nPOLA TIDAK DITEMUKAN SECARA BERURUTAN, NAMUN DITEMUKAN DALAM PERMUTASI !!!")
    print(f"Kemunculan pola '{pattern}' dalam teks: {teks} adalah {kemunculan} kali.")
else  : 
    print(f"\nPOLA DITEMUKAN SECARA BERURUTAN !!!")
    print(f"Kemunculan pola '{pattern}' dalam teks: {teks} adalah {kemunculan} kali.")
    print(f"Perbandingan ke: {perbandingan_ke}")

# Analisis Kompleksitas
print(f"\n=== ANALISIS KOMPLEKSITAS ===")
print(f"Jumlah perbandingan yang dilakukan: {jumlah_perbandingan}")

n = len(teks)
m = len(pattern)

print(f"\n**Worst Case:** O({n} x {m}) = O({n*m})")
print(f"- Pattern tidak ditemukan atau di akhir")
print(f"- Memeriksa semua posisi: {n} x {m} = {n*m} perbandingan")

print(f"\n**Best Case:** O({m})")
print(f"- Pattern ditemukan di posisi pertama")
print(f"- Hanya butuh {m} perbandingan karakter")

print(f"\n**Average Case:** O({n} x {m}) = O({n*m})")
print(f"- Rata-rata memeriksa setengah teks")
print(f"- Tetap linear terhadap panjang teks dan pattern")

print(f"\n**Space Complexity:** O({n})")
print(f"- Menyimpan kemungkinan pattern dalam list")