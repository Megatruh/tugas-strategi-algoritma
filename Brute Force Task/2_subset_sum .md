# Pseudo Code Implementasi Algoritma Brute Force pada Subset Sum Problem

## Deskripsi Problem

Diberikan sebuah array bilangan bulat dan sebuah nilai target, cari semua subset dari array tersebut yang jumlah elemen-elemennya sama dengan target.

## Kompleksitas

- **Time Complexity**: O(2^n × n)
  - O(2^n) untuk generate semua subset
  - O(n) untuk menghitung sum setiap subset
- **Space Complexity**: O(2^n) untuk menyimpan semua subset

## Pseudocode

### Fungsi Helper: Powerset

```
FUNGSI powerset(iterable):
    // Generate semua kemungkinan subset dari iterable
    // Menggunakan combinations untuk setiap ukuran r
    s ← list(iterable)
    hasil ← []

    UNTUK r DARI 0 SAMPAI length(s):
        subset ← combinations(s, r)
        hasil ← hasil + subset

    RETURN hasil
```

---

### Program 1: Implementasi Subset Sum dengan Input Tunggal

```
ALGORITMA SUBSET_SUM_SINGLE

INPUT:
    arr_A ← [3, 5, 9, 12]
    target ← 17

PROSES:
    // LANGKAH 1: Generate semua possible subset (powerset)
    powerset_A ← list(powerset(arr_A))
    // Hasil: (), (3,), (5,), (9,), (12,), (3,5), (3,9), ..., (3,5,9,12)

    // LANGKAH 2: Hitung jumlah setiap subset
    jumlah_subsets ← []
    UNTUK SETIAP i DARI 0 SAMPAI length(powerset_A)-1:
        sum_subset ← sum(powerset_A[i])
        jumlah_subsets.append(sum_subset)

    // LANGKAH 3: Filter subset yang jumlahnya sama dengan target
    subsets_target ← []
    UNTUK SETIAP j DARI 0 SAMPAI length(jumlah_subsets)-1:
        JIKA jumlah_subsets[j] == target:
            subsets_target.append(powerset_A[j])

    // LANGKAH 4: Tampilkan hasil
    JIKA subsets_target kosong:
        PRINT "tidak ada subsets dari array", arr_A, "yang jumlahnya sesuai dengan target", target
    JIKA TIDAK:
        PRINT "subsets dari array", arr_A, "yang jumlahnya sesuai dengan target", target, "adalah", subsets_target

OUTPUT:
    subsets_target
```

---

### Program 2: Analisis Waktu Runtime dengan Multiple Input

```
ALGORITMA ANALISIS_WAKTU_RUNTIME

INPUT:
    n ← [4, 5, 6]  // Array ukuran yang akan diuji

PROSES:
    PRINT "Analisis Waktu Runtime Algoritma Brute Force pada Implementasi Subset Sum"
    PRINT header tabel

    UNTUK SETIAP x DALAM n:
        // Tentukan array dan target sesuai nilai x
        JIKA x == 4:
            arr_A ← [3, 5, 9, 12]
            target ← 17

        JIKA x == 5:
            arr_A ← [3, 5, 7, 9, 12]
            target ← 12

        JIKA x == 6:
            arr_A ← [3, 4, 7, 6, 9, 12]
            target ← 10

        // Mulai pengukuran waktu
        start ← time.perf_counter()

        // Jalankan algoritma subset sum (sama seperti Program 1)
        powerset_A ← list(powerset(arr_A))

        jumlah_subsets ← []
        UNTUK SETIAP i DARI 0 SAMPAI length(powerset_A)-1:
            jumlah_subsets.append(sum(powerset_A[i]))

        subsets_target ← []
        UNTUK SETIAP j DARI 0 SAMPAI length(jumlah_subsets)-1:
            JIKA jumlah_subsets[j] == target:
                subsets_target.append(powerset_A[j])

        // Akhiri pengukuran waktu
        end ← time.perf_counter()
        waktu_eksekusi ← end - start

        // Tampilkan hasil dalam tabel
        PRINT x, length(powerset_A), waktu_eksekusi

OUTPUT:
    Tabel berisi n, jumlah subset (2^n), dan waktu runtime
```

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
- (3, 5, 9, 12) → 29

### 3. Cari yang Sesuai Target

Filter subset yang jumlahnya sama persis dengan nilai target.

### 4. Output Hasil

Tampilkan semua subset yang memenuhi kriteria.

## Analisis Waktu Eksekusi

| n   | Jumlah Subset (2^n) | Waktu Runtime |
| --- | ------------------- | ------------- |
| 4   | 16                  | ... detik     |
| 5   | 32                  | ... detik     |
| 6   | 64                  | ... detik     |
