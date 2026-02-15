# Pseudocode - Tugas Praktikum 4: Password Brute Force Simulation

## Deskripsi Problem

Simulasikan serangan brute force untuk menebak password dengan mencoba semua kemungkinan kombinasi karakter.

**Input:**

- Alfabet: {a, b, c, 1, 2}
- Target password: "b1a"

## Kompleksitas

- **Time Complexity**: O(n^m)
  - n = jumlah karakter alfabet (5)
  - m = panjang password
- **Space Complexity**: O(n^m) untuk menyimpan semua kombinasi

---

## Pseudocode

### Fungsi Helper: generate_kombinasi

```
FUNGSI generate_kombinasi(panjang):
    INPUT:
        panjang : integer panjang password yang di-generate

    OUTPUT:
        kombinasi_str : list semua kombinasi password

    PROSES:
        // Menggunakan cartesian product dengan pengulangan
        // Contoh: product(['a','b'], repeat=2) → aa, ab, ba, bb
        kombinasi ← product(alfabet, repeat=panjang)

        // Gabungkan tuple menjadi string
        kombinasi_str ← []
        UNTUK SETIAP k DALAM kombinasi:
            password ← gabungkan(k)  // ('b','1','a') → "b1a"
            TAMBAHKAN password KE kombinasi_str

        RETURN kombinasi_str
```

---

### Fungsi Helper: brute_force_password

```
FUNGSI brute_force_password(target, panjang):
    INPUT:
        target  : string password yang dicari
        panjang : integer panjang password

    OUTPUT:
        percobaan    : integer jumlah percobaan sampai ditemukan
        password     : string password yang ditemukan (atau None)
        total        : integer total kombinasi

    PROSES:
        kombinasi ← generate_kombinasi(panjang)
        percobaan ← 0

        UNTUK SETIAP password DALAM kombinasi:
            percobaan ← percobaan + 1

            JIKA password == target:
                RETURN percobaan, password, length(kombinasi)

        RETURN -1, None, length(kombinasi)  // Tidak ditemukan
```

---

### Program Utama

```
ALGORITMA PASSWORD_BRUTE_FORCE_SIMULATION

INPUT:
    alfabet ← ['a', 'b', 'c', '1', '2']
    target ← "b1a"

PROSES:
    PRINT "Alfabet yang digunakan:", alfabet
    PRINT "Jumlah karakter alfabet:", length(alfabet)
    PRINT "Target password:", target

    // ====== 1. GENERATE SEMUA KOMBINASI (PANJANG 3) ======
    kombinasi_3 ← generate_kombinasi(3)

    PRINT "Total kombinasi panjang 3:", length(alfabet), "^3 =", length(kombinasi_3)
    PRINT "Semua kombinasi:"
    UNTUK SETIAP i, k DALAM enumerate(kombinasi_3):
        PRINT k

    // ====== 2. BRUTE FORCE MENCARI TARGET ======
    start_time ← waktu_sekarang()
    percobaan, password_found, total ← brute_force_password(target, length(target))
    end_time ← waktu_sekarang()

    JIKA password_found:
        PRINT "Password ditemukan!"
        PRINT "Jumlah percobaan:", percobaan, "dari", total, "kombinasi"
        PRINT "Waktu eksekusi:", end_time - start_time
    JIKA TIDAK:
        PRINT "Password tidak ditemukan"

    // ====== 3. UJI PANJANG 3 DAN PANJANG 4 ======
    UNTUK panjang DALAM [3, 4]:
        kombinasi ← generate_kombinasi(panjang)

        start_time ← waktu_sekarang()
        // Simulasi worst case - iterasi semua kombinasi
        UNTUK SETIAP k DALAM kombinasi:
            // proses
        end_time ← waktu_sekarang()

        PRINT "Panjang:", panjang
        PRINT "Total kombinasi:", length(alfabet), "^", panjang, "=", length(kombinasi)
        PRINT "Waktu generate:", end_time - start_time

    // ====== 4. ANALISIS PERTUMBUHAN KOMPLEKSITAS ======
    PRINT "Tabel pertumbuhan kompleksitas:"
    PRINT "Panjang | Kombinasi | Rumus | Waktu Runtime"

    UNTUK panjang DARI 1 SAMPAI 6:
        start_time ← waktu_sekarang()
        kombinasi ← generate_kombinasi(panjang)
        UNTUK SETIAP k DALAM kombinasi:
            // proses
        end_time ← waktu_sekarang()

        PRINT panjang, length(kombinasi), length(alfabet), "^", panjang, end_time - start_time

OUTPUT:
    - Semua kombinasi password
    - Password ditemukan pada percobaan ke-41
    - Perbandingan waktu panjang 3 vs 4
    - Tabel pertumbuhan kompleksitas
```

---
