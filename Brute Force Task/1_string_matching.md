# Pseudocode - Tugas Praktikum 1: Pencarian String (Pattern Matching)

## Deskripsi Problem

Diberikan sebuah teks dan pattern, cari semua kemunculan pattern dalam teks menggunakan pendekatan brute force.

**Input:**

- Teks: "ALGORITMASTRATEGIALGORITMA"
- Pattern: "RIT"

## Kompleksitas

- **Time Complexity**: O(n × m)
  - n = panjang teks
  - m = panjang pattern
- **Space Complexity**: O(1) untuk pencarian, O(k) untuk menyimpan hasil (k = jumlah kemunculan)

---

## Pseudocode

### Fungsi Utama: brute_force_string_matching

```
FUNGSI brute_force_string_matching(teks, pattern):
    INPUT:
        teks    : string teks yang akan dicari
        pattern : string pola yang dicari

    OUTPUT:
        indeks_ditemukan   : list indeks kemunculan pattern
        jumlah_perbandingan : integer total perbandingan karakter

    PROSES:
        n ← length(teks)
        m ← length(pattern)

        indeks_ditemukan ← []
        jumlah_perbandingan ← 0

        // Geser pattern dari posisi 0 sampai n-m
        UNTUK i DARI 0 SAMPAI (n - m):
            j ← 0

            // Bandingkan karakter per karakter
            SELAMA j < m:
                jumlah_perbandingan ← jumlah_perbandingan + 1

                JIKA teks[i + j] ≠ pattern[j]:
                    KELUAR DARI LOOP  // Tidak cocok, geser pattern

                j ← j + 1

            // Jika semua karakter cocok (j == m)
            JIKA j == m:
                TAMBAHKAN i KE indeks_ditemukan

        RETURN indeks_ditemukan, jumlah_perbandingan
```

---

### Program Utama

```
ALGORITMA PENCARIAN_STRING_BRUTE_FORCE

INPUT:
    teks ← "ALGORITMASTRATEGIALGORITMA"
    pattern ← "RIT"

PROSES:
    // ====== 1. IMPLEMENTASI ALGORITMA ======
    PRINT "Teks:", teks
    PRINT "Pattern:", pattern
    PRINT "Panjang teks (n):", length(teks)
    PRINT "Panjang pattern (m):", length(pattern)

    start_time ← waktu_sekarang()
    indeks_hasil, total_perbandingan ← brute_force_string_matching(teks, pattern)
    end_time ← waktu_sekarang()

    // ====== 2. TAMPILKAN INDEKS KEMUNCULAN ======
    JIKA indeks_hasil TIDAK KOSONG:
        PRINT "Pattern ditemukan pada indeks:", indeks_hasil
        PRINT "Jumlah kemunculan:", length(indeks_hasil)

        // Visualisasi
        UNTUK SETIAP idx DALAM indeks_hasil:
            PRINT "idx =", idx, "→", teks[idx : idx + length(pattern)]
    JIKA TIDAK:
        PRINT "Pattern TIDAK DITEMUKAN"

    // ====== 3. JUMLAH PERBANDINGAN ======
    PRINT "Total perbandingan karakter:", total_perbandingan
    PRINT "Waktu eksekusi:", end_time - start_time

    // ====== 4. ANALISIS KOMPLEKSITAS ======
    n ← length(teks)
    m ← length(pattern)

    PRINT "Best Case: O(n) - pattern tidak cocok di karakter pertama"
    PRINT "Worst Case: O(n × m) - pattern hampir cocok di setiap posisi"
    PRINT "Average Case: O(n × m)"

OUTPUT:
    - Indeks kemunculan pattern: [4, 21]
    - Jumlah kemunculan: 2 kali
    - Total perbandingan karakter
```

---