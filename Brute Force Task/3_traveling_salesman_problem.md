# Pseudocode - Tugas Praktikum 3: Traveling Salesman Problem (TSP)

## Deskripsi Problem

Diberikan matriks jarak antar kota, tentukan rute terpendek yang mengunjungi semua kota tepat satu kali dan kembali ke kota awal.

**Input:**

- Matriks jarak 4 kota (A, B, C, D)
- Kota awal: A (fixed)

**Matriks Jarak:**

```
      A    B    C    D
  A   0   10   15   20
  B  10    0   35   25
  C  15   35    0   30
  D  20   25   30    0
```

## Kompleksitas

- **Time Complexity**: O((n-1)!)
  - n = jumlah kota
  - Kota awal di-fix, permutasi (n-1) kota lainnya
- **Space Complexity**: O(n!) untuk menyimpan semua rute

---

## Pseudocode

### Fungsi Helper: hitung_jarak_rute

```
FUNGSI hitung_jarak_rute(rute):
    INPUT:
        rute : tuple berisi urutan kota (contoh: ('A', 'B', 'C', 'D'))

    OUTPUT:
        total_jarak : integer total jarak rute (termasuk kembali ke awal)

    PROSES:
        total_jarak ← 0

        // Hitung jarak antar kota berurutan
        UNTUK i DARI 0 SAMPAI length(rute) - 2:
            dari ← kota_index[rute[i]]
            ke ← kota_index[rute[i + 1]]
            total_jarak ← total_jarak + matrix_jarak[dari][ke]

        // Tambahkan jarak kembali ke kota awal
        dari ← kota_index[rute[terakhir]]
        ke ← kota_index[rute[0]]
        total_jarak ← total_jarak + matrix_jarak[dari][ke]

        RETURN total_jarak
```

---

### Program Utama

```
ALGORITMA TSP_BRUTE_FORCE

INPUT:
    matrix_jarak ← [
        [0,  10, 15, 20],   // A
        [10, 0,  35, 25],   // B
        [15, 35, 0,  30],   // C
        [20, 25, 30, 0]     // D
    ]
    kota ← ['A', 'B', 'C', 'D']
    kota_index ← {'A': 0, 'B': 1, 'C': 2, 'D': 3}

PROSES:
    // ====== 1. GENERATE SEMUA PERMUTASI RUTE ======
    // Fix kota awal A, permutasi kota lainnya (B, C, D)
    kota_lain ← ['B', 'C', 'D']
    semua_permutasi ← permutations(kota_lain)

    // Tambahkan A di depan setiap permutasi
    semua_rute ← []
    UNTUK SETIAP p DALAM semua_permutasi:
        rute ← ('A',) + p
        TAMBAHKAN rute KE semua_rute

    PRINT "Jumlah permutasi:", factorial(length(kota_lain)), "rute"
    PRINT "Semua rute:"
    UNTUK SETIAP rute DALAM semua_rute:
        PRINT rute, "→ A"

    // ====== 2. HITUNG TOTAL JARAK SETIAP RUTE ======
    start_time ← waktu_sekarang()

    hasil_rute ← []
    UNTUK SETIAP rute DALAM semua_rute:
        jarak ← hitung_jarak_rute(rute)
        TAMBAHKAN (rute, jarak) KE hasil_rute

    end_time ← waktu_sekarang()

    PRINT "Total jarak setiap rute:"
    UNTUK SETIAP (rute, jarak) DALAM hasil_rute:
        PRINT rute, "→ A :", jarak

    // ====== 3. TENTUKAN RUTE MINIMUM ======
    rute_minimum ← MIN(hasil_rute, berdasarkan jarak)

    PRINT "Rute terpendek:", rute_minimum.rute, "→ A"
    PRINT "Total jarak:", rute_minimum.jarak
    PRINT "Waktu eksekusi:", end_time - start_time

    // ====== 4. JUMLAH RUTE YANG DIPERIKSA ======
    PRINT "Jumlah rute diperiksa:", length(hasil_rute)
    PRINT "Rumus: (n-1)! = (4-1)! = 3! = 6 rute"

OUTPUT:
    - Semua rute dengan jaraknya
    - Rute terpendek: A → B → D → C → A
    - Total jarak: 80
    - Jumlah rute diperiksa: 6
```

---
