# Pseudocode - Tugas Praktikum 1: Pencarian String (Pattern Matching)

**Nama:** Farhan Esha Putra Kusuma Atmaja  
**NIM:** 247006111066

## Deskripsi Problem

Diberikan sebuah teks dan pattern, cari semua kemunculan pattern dalam teks menggunakan pendekatan brute force.

**Input:**

- Teks: "ALGORITMASTRATEGIALGORITMA"
- Pattern: "RIT"

## Kompleksitas

- **Time Complexity**: O(n × m) untuk pencarian berurutan, O(n!) jika menggunakan permutasi
  - n = panjang teks
  - m = panjang pattern
- **Space Complexity**: O(n) untuk menyimpan kemungkinan pattern

---

## Pseudocode

### Fungsi Helper: permutations

```
FUNGSI permutations(iterable, r):
    INPUT:
        iterable : string atau list yang akan dipermutasi
        r        : panjang permutasi yang diinginkan (default = panjang iterable)

    OUTPUT:
        result : list berisi semua permutasi dengan panjang r

    PROSES:
        pool ← tuple(iterable)
        n ← length(pool)

        JIKA r adalah None:
            r ← n

        JIKA r > n:
            RETURN []  // List kosong

        result ← []
        indices ← [0, 1, 2, ..., n-1]
        cycles ← [n, n-1, n-2, ..., n-r+1]

        // Tambahkan permutasi pertama
        TAMBAHKAN gabungan(pool[indices[0..r-1]]) KE result

        SELAMA n > 0:
            UNTUK i DARI r-1 TURUN KE 0:
                cycles[i] ← cycles[i] - 1

                JIKA cycles[i] == 0:
                    // Rotasi indices
                    indices[i..] ← indices[i+1..] + indices[i..i]
                    cycles[i] ← n - i
                JIKA TIDAK:
                    j ← cycles[i]
                    TUKAR indices[i] DENGAN indices[-j]
                    TAMBAHKAN gabungan(pool[indices[0..r-1]]) KE result
                    KELUAR DARI LOOP

            JIKA tidak ada break:
                KELUAR DARI WHILE

        RETURN result
```

---

### Program Utama

```
ALGORITMA PENCARIAN_STRING_BRUTE_FORCE

INPUT:
    teks ← "ALGORITMASTRATEGIALGORITMA"
    pattern ← "RIT"

PROSES:
    // ====== INISIALISASI ======
    teks_list ← list(teks)  // Pecah teks menjadi list karakter
    PRINT length(teks_list)

    // ====== 1. GENERATE KEMUNGKINAN PATTERN BERURUTAN ======
    // Gabungkan karakter yang berkemungkinan membentuk pattern
    kemungkianan_pattern ← []

    UNTUK i DARI 0 SAMPAI length(teks_list) - 1:
        JIKA (length(teks_list) - i) > length(pattern):
            substring ← gabungan(teks_list[i : i + length(pattern)])
            TAMBAHKAN substring KE kemungkianan_pattern

    // ====== 2. CEK SETIAP KEMUNGKINAN DENGAN BRUTE FORCE ======
    temp ← []
    perbandingan_ke ← []
    jumlah_perbandingan ← 0

    UNTUK j DARI 0 SAMPAI length(kemungkianan_pattern) - 1:
        jumlah_perbandingan ← jumlah_perbandingan + 1

        JIKA kemungkianan_pattern[j] == pattern:
            TAMBAHKAN (j + 1) KE perbandingan_ke
            TAMBAHKAN kemungkianan_pattern[j] KE temp

    kemunculan ← length(temp)

    // ====== 3. JIKA TIDAK DITEMUKAN, CARI DALAM PERMUTASI ======
    JIKA kemunculan == 0:
        // Pattern tidak ditemukan secara berurutan
        // Cari dalam permutasi
        kemungkinan_baru ← permutations(teks, length(pattern))

        UNTUK SETIAP k DALAM kemungkinan_baru:
            jumlah_perbandingan ← jumlah_perbandingan + 1

            JIKA k == pattern:
                kemunculan ← kemunculan + 1

        PRINT "POLA TIDAK DITEMUKAN SECARA BERURUTAN, NAMUN DITEMUKAN DALAM PERMUTASI !!!"
        PRINT "Kemunculan pola", pattern, "dalam teks:", teks, "adalah", kemunculan, "kali."

    JIKA TIDAK:
        PRINT "POLA DITEMUKAN SECARA BERURUTAN !!!"
        PRINT "Kemunculan pola", pattern, "dalam teks:", teks, "adalah", kemunculan, "kali."
        PRINT "Perbandingan ke:", perbandingan_ke

    // ====== 4. ANALISIS KOMPLEKSITAS ======
    n ← length(teks)
    m ← length(pattern)

    PRINT "=== ANALISIS KOMPLEKSITAS ==="
    PRINT "Jumlah perbandingan yang dilakukan:", jumlah_perbandingan

    PRINT "Worst Case: O(n × m) =", n × m
    PRINT "Best Case: O(m) =", m
    PRINT "Average Case: O(n × m) =", n × m

OUTPUT:
    - Pola ditemukan secara berurutan
    - Kemunculan: 2 kali
    - Perbandingan ke: [5, 22]
```

---

## Penjelasan Langkah Algoritma

### 1. Inisialisasi

- Pecah teks menjadi list karakter (teks_list)
- Siapkan variabel untuk menyimpan hasil

### 2. Generate Kemungkinan Pattern

- Geser window sepanjang m (panjang pattern) dari posisi 0 sampai n-m
- Setiap window disimpan sebagai kandidat pattern

### 3. Pencarian Berurutan

- Bandingkan setiap kandidat dengan pattern
- Jika cocok, catat posisi perbandingan

### 4. Pencarian Permutasi (Fallback)

- Jika tidak ditemukan secara berurutan
- Generate semua permutasi dari teks dengan panjang m
- Cari pattern dalam permutasi tersebut

---

## Jawaban Pertanyaan

### 1. Berapa kompleksitas worst-case?

- **O(n × m)** untuk pencarian berurutan
- **O(n!)** jika harus mencari dalam permutasi
- n = panjang teks, m = panjang pattern

### 2. Kapan brute force menjadi tidak efisien?

- Ketika teks sangat panjang (n besar)
- Ketika pattern panjang (m besar)
- Ketika harus menggunakan permutasi (n! sangat besar)
- Solusi: Gunakan KMP, Boyer-Moore, atau Rabin-Karp
