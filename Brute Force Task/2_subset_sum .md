# Implementasi Algoritma Brute Force pada Subset Sum Problem

## Deskripsi Problem
Diberikan sebuah array bilangan bulat dan sebuah nilai target, cari semua subset dari array tersebut yang jumlah elemen-elemennya sama dengan target.

## Kompleksitas
- **Time Complexity**: O(2^n × n)
  - O(2^n) untuk generate semua subset
  - O(n) untuk menghitung sum setiap subset
- **Space Complexity**: O(2^n) untuk menyimpan semua subset

## Pseudocode

```
ALGORITMA SUBSET_SUM_BRUTE_FORCE

FUNGSI powerset(iterable):
    // Generate semua kemungkinan subset dari iterable
    s ← list(iterable)
    hasil ← []
    
    UNTUK r DARI 0 SAMPAI length(s):
        subset ← combinations(s, r)
        hasil ← hasil + subset
    
    RETURN hasil

FUNGSI UTAMA:
    INPUT:
        arr_A ← array input [3, 5, 9, 12]
        target ← nilai target yang dicari (17)
    
    // LANGKAH 1: Generate semua possible subset (powerset)
    powerset_A ← powerset(arr_A)
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
        PRINT "tidak ada subsets yang sesuai"
    JIKA TIDAK:
        PRINT subsets_target
    
    RETURN subsets_target
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
|-----|---------------------|---------------|
| 4   | 16                  |     ... detik |
| 5   | 32                  |     ... detik |
| 6   | 64                  |     ... detik |

