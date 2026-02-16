# Pseudocode: Coin Change Problem (Algoritma Greedy)

## Tugas Praktikum 1 — Problem: Coin Change (Sistem Koin Kanonik)

---

## Deklarasi:

```
coins       : array of integer    // Daftar pecahan koin yang tersedia
target      : integer             // Nilai yang ingin dipecah
sisa        : integer             // Sisa nilai yang belum dipecah
total_koin  : integer             // Jumlah total koin yang digunakan
result      : dictionary          // Menyimpan detail koin yang digunakan
sorted_coins: array of integer    // Koin yang sudah diurutkan dari besar ke kecil
koin        : integer             // Pecahan koin saat ini
hasil_bagi  : real                // Hasil pembagian sisa dengan pecahan koin
jumlah_koin : integer             // Jumlah koin yang digunakan (hasil floor)
nilai_koin  : integer             // Total nilai dari koin yang diambil
sisa_baru   : integer             // Sisa setelah pengurangan
```

---

## Fungsi:

```
FUNCTION greedy_coin_change(target, coins) -> (total_koin, result)
    // Fungsi untuk menghitung jumlah koin minimum menggunakan algoritma greedy
    // 
    // Input:
    //   target : nilai yang ingin dipecah menjadi koin
    //   coins  : array pecahan koin yang tersedia
    //
    // Output:
    //   total_koin : jumlah total koin yang digunakan
    //   result     : dictionary berisi detail koin yang digunakan

FUNCTION floor(x) -> integer
    // Fungsi untuk membulatkan nilai x ke bawah
    // Input: x (bilangan real)
    // Output: bilangan bulat terbesar yang ≤ x

FUNCTION sort_descending(arr) -> array
    // Fungsi untuk mengurutkan array dari besar ke kecil
    // Input: arr (array of integer)
    // Output: array yang sudah terurut descending
```

---

## Algoritma:

```
ALGORITMA Greedy_Coin_Change

BEGIN
    // Inisialisasi
    coins ← [1, 5, 10, 25]
    target ← 68
    
    // Panggil fungsi greedy
    (total_koin, result) ← greedy_coin_change(target, coins)
    
    // Tampilkan hasil
    OUTPUT "Total Koin = ", total_koin
    FOR EACH (koin, jumlah) IN result DO
        OUTPUT "Koin ", koin, ": ", jumlah, " buah"
    END FOR
END

---

FUNCTION greedy_coin_change(target, coins)
BEGIN
    // Langkah 1: Urutkan koin dari terbesar ke terkecil
    sorted_coins ← sort_descending(coins)
    
    // Langkah 2: Inisialisasi variabel
    sisa ← target
    total_koin ← 0
    result ← {}
    
    // Langkah 3: Iterasi untuk setiap pecahan koin
    FOR EACH koin IN sorted_coins DO
        
        // Jika sisa sudah 0 atau negatif, hentikan
        IF sisa ≤ 0 THEN
            BREAK
        END IF
        
        // Langkah 3a: Bagi nilai sisa dengan pecahan koin
        hasil_bagi ← sisa / koin
        
        // Langkah 3b: Bulatkan ke bawah (floor)
        jumlah_koin ← floor(hasil_bagi)
        
        // Langkah 3c: Jika jumlah koin > 0, proses
        IF jumlah_koin > 0 THEN
            
            // Kalikan hasil pembulatan dengan pecahan koin
            nilai_koin ← jumlah_koin × koin
            
            // Kurangi dari nilai sisa untuk mendapat sisa baru
            sisa_baru ← sisa - nilai_koin
            
            // Simpan hasil ke dictionary
            result[koin] ← jumlah_koin
            
            // Tambahkan ke total koin
            total_koin ← total_koin + jumlah_koin
            
            // Update sisa untuk iterasi berikutnya
            sisa ← sisa_baru
            
        END IF
        
    END FOR
    
    // Kembalikan hasil
    RETURN (total_koin, result)
END FUNCTION
```

---

## Contoh Eksekusi (Target = 68):

| Iterasi | Koin | Hasil Bagi | Floor | Nilai Koin | Sisa Baru |
|---------|------|------------|-------|------------|-----------|
| 1       | 25   | 68/25=2.72 | 2     | 2×25=50    | 68-50=18  |
| 2       | 10   | 18/10=1.80 | 1     | 1×10=10    | 18-10=8   |
| 3       | 5    | 8/5=1.60   | 1     | 1×5=5      | 8-5=3     |
| 4       | 1    | 3/1=3.00   | 3     | 3×1=3      | 3-3=0     |

**Total Koin = 2 + 1 + 1 + 3 = 7 koin**

---

## Kompleksitas:

- **Time Complexity**: O(n log n) untuk sorting + O(n) untuk iterasi = O(n log n)
- **Space Complexity**: O(n) untuk menyimpan hasil

Dimana n adalah jumlah jenis pecahan koin yang tersedia.