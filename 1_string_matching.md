# PSEUDOCODE - STRING MATCHING DENGAN BRUTE FORCE

==================================================

## FUNCTION DECLARATIONS

**FUNCTION** `permutations(iterable, r)`

- **INPUT**: `iterable` (string atau list), `r` (panjang permutasi)
- **OUTPUT**: list berisi semua permutasi dengan panjang r
- **PROCESS**: Generate semua permutasi menggunakan algoritma berbasis indeks

---

## VARIABLE DECLARATIONS

**GLOBAL VARIABLES:**

```
teks                    : string     // Teks yang akan dicari
pattern                 : string     // Pola yang dicari
teks_list               : list       // Teks dalam bentuk list karakter
kemungkianan_pattern    : list       // List kemungkinan pattern berurutan
temp                    : list       // List temporary untuk pattern yang cocok
perbandingan_ke         : list       // List indeks perbandingan yang cocok
jumlah_perbandingan     : integer    // Counter jumlah perbandingan
kemunculan              : integer    // Jumlah kemunculan pattern
n                       : integer    // Panjang teks
m                       : integer    // Panjang pattern
```

---

## ALGORITHM

### ALGORITHM 1: `permutations(iterable, r)`

```
BEGIN
    pool ← tuple(iterable)
    n ← length(pool)

    IF r IS None THEN
        r ← n
    END IF

    IF r > n THEN
        RETURN empty_list
    END IF

    result ← empty_list
    indices ← [0, 1, 2, ..., n-1]
    cycles ← [n, n-1, n-2, ..., n-r+1]

    // Tambahkan permutasi pertama
    APPEND join(pool[indices[0..r-1]]) TO result

    WHILE n > 0 DO
        FOR i FROM r-1 DOWNTO 0 DO
            cycles[i] ← cycles[i] - 1

            IF cycles[i] = 0 THEN
                // Rotasi indices
                indices[i..] ← indices[i+1..] + indices[i..i]
                cycles[i] ← n - i
            ELSE
                j ← cycles[i]
                SWAP indices[i] WITH indices[-j]
                APPEND join(pool[indices[0..r-1]]) TO result
                BREAK inner loop
            END IF
        END FOR

        IF no break occurred THEN
            BREAK outer loop
        END IF
    END WHILE

    RETURN result
END
```

---

### ALGORITHM 2: `main_string_matching`

```
BEGIN
    // ========== INISIALISASI ==========
    teks ← "ALGORITMASTRATEGIALGORITMA"
    pattern ← "RIT"
    teks_list ← list(teks)

    PRINT length(teks_list)

    // ========== BUAT LIST KEMUNGKINAN PATTERN BERURUTAN ==========
    kemungkianan_pattern ← empty_list

    FOR i FROM 0 TO length(teks_list)-1 DO
        IF (length(teks_list) - i) > length(pattern) THEN
            substring ← join(teks_list[i..i+length(pattern)-1])
            APPEND substring TO kemungkianan_pattern
        END IF
    END FOR

    // ========== CEK SETIAP KEMUNGKINAN DENGAN BRUTE FORCE ==========
    temp ← empty_list
    perbandingan_ke ← empty_list
    jumlah_perbandingan ← 0

    FOR j FROM 0 TO length(kemungkianan_pattern)-1 DO
        jumlah_perbandingan ← jumlah_perbandingan + 1

        IF kemungkianan_pattern[j] = pattern THEN
            APPEND (j+1) TO perbandingan_ke
            APPEND kemungkianan_pattern[j] TO temp
        END IF
    END FOR

    kemunculan ← length(temp)

    // ========== PENCARIAN DALAM PERMUTASI (JIKA TIDAK DITEMUKAN) ==========
    IF kemunculan = 0 THEN
        kemungkinan_baru ← permutations(teks, length(pattern))

        FOR EACH k IN kemungkinan_baru DO
            jumlah_perbandingan ← jumlah_perbandingan + 1

            IF k = pattern THEN
                kemunculan ← kemunculan + 1
            END IF
        END FOR

        PRINT "POLA TIDAK DITEMUKAN SECARA BERURUTAN, NAMUN DITEMUKAN DALAM PERMUTASI !!!"
        PRINT "Kemunculan pola", pattern, "dalam teks:", teks, "adalah", kemunculan, "kali."
    ELSE
        PRINT "POLA DITEMUKAN SECARA BERURUTAN !!!"
        PRINT "Kemunculan pola", pattern, "dalam teks:", teks, "adalah", kemunculan, "kali."
        PRINT "Perbandingan ke:", perbandingan_ke
    END IF

    // ========== ANALISIS KOMPLEKSITAS ==========
    PRINT ""
    PRINT "=== ANALISIS KOMPLEKSITAS ==="
    PRINT "Jumlah perbandingan yang dilakukan:", jumlah_perbandingan
    PRINT ""

    n ← length(teks)
    m ← length(pattern)

    // Worst Case
    PRINT "**Worst Case:** O(n × m) = O(", n*m, ")"
    PRINT "  - Pattern tidak ditemukan atau di akhir"
    PRINT "  - Memeriksa semua posisi:", n, "×", m, "=", n*m, "perbandingan"
    PRINT ""

    // Best Case
    PRINT "**Best Case:** O(m)"
    PRINT "  - Pattern ditemukan di posisi pertama"
    PRINT "  - Hanya butuh", m, "perbandingan karakter"
    PRINT ""

    // Average Case
    PRINT "**Average Case:** O(n × m) = O(", n*m, ")"
    PRINT "  - Rata-rata memeriksa setengah teks"
    PRINT "  - Tetap linear terhadap panjang teks dan pattern"
    PRINT ""

    // Space Complexity
    PRINT "**Space Complexity:** O(n)"
    PRINT "  - Menyimpan kemungkinan pattern dalam list"
END
```
