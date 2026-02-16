# Pseudocode - Tugas Praktikum 2: Subset Sum Problem

**Nama:** Farhan Esha Putra Kusuma Atmaja  
**NIM:** 247006111066

## Deskripsi Problem

Diberikan sebuah array bilangan bulat dan sebuah nilai target, cari semua subset dari array tersebut yang jumlah elemen-elemennya sama dengan target.

**Input:**

- Array A = {3, 5, 9, 12}
- Target = 17

## Kompleksitas

- **Time Complexity**: O(2^n × n)
  - O(2^n) untuk generate semua subset
  - O(n) untuk menghitung sum setiap subset
- **Space Complexity**: O(2^n) untuk menyimpan semua subset

---

## Pseudocode

### Fungsi Helper: powerset

```
FUNGSI powerset(iterable):
    INPUT:
        iterable : array atau list yang akan di-generate subsetnya

    OUTPUT:
        hasil : semua kemungkinan subset (powerset)

    PROSES:
        // Generate semua subset dari iterable
        // Menggunakan chain.from_iterable dan combinations
        // powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

        s ← list(iterable)

        // Gabungkan semua combinations dengan ukuran r dari 0 sampai length(s)
        RETURN chain.from_iterable(combinations(s, r) UNTUK r DARI 0 SAMPAI length(s))
```

---

### Fungsi Helper: subset_sum_bruteforce

```
FUNGSI subset_sum_bruteforce(arr, target):
    INPUT:
        arr    : array bilangan bulat
        target : nilai target yang dicari

    OUTPUT:
        semua_subset  : list semua subset yang di-generate
        subset_target : list subset yang jumlahnya sama dengan target

    PROSES:
        // 1. Generate semua subset
        semua_subset ← list(powerset(arr))

        // 2. Hitung jumlah setiap subset dan cari yang sesuai target
        subset_target ← []

        UNTUK SETIAP subset DALAM semua_subset:
            JIKA sum(subset) == target:
                TAMBAHKAN subset KE subset_target

        RETURN semua_subset, subset_target
```

---

### Program Utama

```
ALGORITMA SUBSET_SUM_BRUTE_FORCE

INPUT:
    arr_A ← [3, 5, 9, 12]
    target ← 17

PROSES:
    PRINT "SUBSET SUM - BRUTE FORCE"
    PRINT "Array A =", arr_A
    PRINT "Target =", target

    // ====== 1. GENERATE SEMUA SUBSET (2^n kemungkinan) ======
    semua_subset, subset_target ← subset_sum_bruteforce(arr_A, target)

    PRINT "Jumlah elemen (n):", length(arr_A)
    PRINT "Total subset: 2^", length(arr_A), "=", length(semua_subset), "subset"

    PRINT "Semua subset:"
    UNTUK SETIAP i, subset DALAM enumerate(semua_subset):
        PRINT subset

    // ====== 2. TAMPILKAN SUBSET YANG MEMENUHI TARGET ======
    JIKA subset_target KOSONG:
        PRINT "Tidak ada subset dari array", arr_A, "yang jumlahnya =", target
    JIKA TIDAK:
        PRINT "Subset yang jumlahnya =", target, ":"
        UNTUK SETIAP subset DALAM subset_target:
            elemen_str ← gabungan elemen dengan " + "
            PRINT subset, "→", elemen_str, "=", sum(subset)

    // ====== 3. HITUNG TOTAL SUBSET YANG DIPERIKSA ======
    PRINT "Total subset yang diperiksa:", length(semua_subset)
    PRINT "Subset yang memenuhi target:", length(subset_target)

    // ====== 4. UJI DENGAN n = 4, 5, 6 DAN BANDINGKAN RUNTIME ======
    test_cases ← [
        ([3, 5, 9, 12], 17),         // n = 4
        ([3, 5, 7, 9, 12], 12),      // n = 5
        ([3, 4, 7, 6, 9, 12], 10)    // n = 6
    ]

    PRINT "Tabel Perbandingan Runtime:"
    PRINT "n | Array | Target | Subset (2^n) | Runtime"

    UNTUK SETIAP (arr, tgt) DALAM test_cases:
        start ← time.perf_counter()

        semua, hasil ← subset_sum_bruteforce(arr, tgt)

        end ← time.perf_counter()

        PRINT length(arr), arr, tgt, length(semua), (end - start)

OUTPUT:
    - Semua subset dengan sum masing-masing
    - Subset yang memenuhi target: (5, 12) dan (3, 5, 9)
    - Total subset diperiksa: 16
    - Tabel perbandingan runtime untuk n = 4, 5, 6
```

---

## Penjelasan Langkah Algoritma

### 1. Generate Powerset (2^n subset)

Untuk array dengan n elemen, akan dihasilkan 2^n kemungkinan subset (termasuk subset kosong).

**Contoh**: arr_A = [3, 5, 9, 12]

- Total subset = 2^4 = 16 subset

### 2. Hitung Sum Setiap Subset

Setiap subset dijumlahkan semua elemennya.

**Contoh**:

- () → 0
- (3,) → 3
- (5,) → 5
- (3, 5) → 8
- (5, 12) → 17 ✓
- (3, 5, 9) → 17 ✓
- (3, 5, 9, 12) → 29

### 3. Cari yang Sesuai Target

Filter subset yang jumlahnya sama persis dengan nilai target.

### 4. Output Hasil

Tampilkan semua subset yang memenuhi kriteria.

---

## Jawaban Pertanyaan

### 1. Mengapa kompleksitasnya O(2^n)?

- Setiap elemen dalam array memiliki 2 pilihan: dimasukkan ke subset atau tidak
- Untuk n elemen, total kombinasi = 2 × 2 × ... × 2 (n kali) = 2^n
- Kita harus memeriksa SEMUA 2^n subset untuk mencari target
- Maka kompleksitas waktu = O(2^n)

### 2. Apa dampaknya jika n = 20?

- Jumlah subset = 2^20 = 1,048,576 subset
- Harus memeriksa lebih dari 1 JUTA subset!
- Untuk n = 30: 2^30 = 1,073,741,824 subset (≈ 1 miliar)
- KESIMPULAN: Brute force tidak praktis untuk n besar!

---

## Analisis Waktu Eksekusi

| n   | Jumlah Subset (2^n) | Waktu Runtime  |
| --- | ------------------- | -------------- |
| 4   | 16                  | ~0.00005 detik |
| 5   | 32                  | ~0.00006 detik |
| 6   | 64                  | ~0.00008 detik |
