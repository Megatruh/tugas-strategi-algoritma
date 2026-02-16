# 1. Inisialisasi Dataset [Nama, Berat, Nilai] sesuai gambar
items = [
    ["I1", 10, 60],
    ["I2", 20, 100],
    ["I3", 30, 120]
]

kapasitas_tas = 50

# 2. Langkah Strategi Greedy: Hitung rasio nilai/berat (c.1)
# Kita tambahkan rasio ke dalam list: [Nama, Berat, Nilai, Rasio]
for item in items:
    berat = item[1]
    nilai = item[2]
    rasio = nilai / berat
    item.append(rasio)

# 3. Urutkan descending berdasarkan rasio (indeks ke-3) (c.2)
items.sort(key=lambda x: x[3], reverse=True)

print('='*50)
print(f"{'Nama':<8}{'Berat':<10}{'Nilai':<10}{'Rasio':<10}")
print('='*50)
for x in items:
    nama, berat, nilai, rasio = x
    print(f"{nama:<8}{berat:<10}{nilai:<10}{rasio:<10.2f}")
print('='*50)

total_nilai = 0
sisa_kapasitas = kapasitas_tas
hasil_pengambilan = []

# 4. Ambil item penuh atau sebagian (c.3)
for item in items:
    nama, berat, nilai, rasio = item
    
    if sisa_kapasitas <= 0:
        break
        
    if berat <= sisa_kapasitas:
        # Ambil item secara penuh
        sisa_kapasitas -= berat
        total_nilai += nilai
        hasil_pengambilan.append(f"{nama} (100%)")
    else:
        # Ambil item sebagian (Fractional)
        fraksi = sisa_kapasitas / berat
        nilai_sebagian = nilai * fraksi
        total_nilai += nilai_sebagian
        hasil_pengambilan.append(f"{nama} ({fraksi*100:.0f}%)")
        sisa_kapasitas = 0 # Tas sekarang penuh

# Output Akhir
print(f"Item yang diambil: {', '.join(hasil_pengambilan)}")
print(f"Total Nilai Maksimal: {total_nilai}")
print('='*50)