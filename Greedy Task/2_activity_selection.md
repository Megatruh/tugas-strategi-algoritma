# Pseudocode: Activity Selection Problem (Algoritma Greedy)

## Tugas Praktikum 2 — Problem: Activity Selection

---

## Deklarasi:

```
dataset                 : array of [nama, start, finish]  // Daftar aktivitas dengan waktu mulai dan selesai
nama                    : string                          // Nama aktivitas
start                   : integer                         // Waktu mulai aktivitas
finish                  : integer                         // Waktu selesai aktivitas
aktivitas_terpilih      : array of string                 // Daftar aktivitas yang dipilih
waktu_selesai_terakhir  : integer                         // Waktu selesai dari aktivitas terakhir yang dipilih
akt                     : array [nama, start, finish]     // Aktivitas saat ini dalam iterasi
```

---

## Fungsi:

```
FUNCTION sort_by_finish_time(dataset) -> array
    // Fungsi untuk mengurutkan aktivitas berdasarkan waktu selesai (finish time)
    // 
    // Input:
    //   dataset : array of [nama, start, finish]
    //
    // Output:
    //   array yang sudah terurut berdasarkan finish time (ascending)

FUNCTION activity_selection(dataset) -> (aktivitas_terpilih, total)
    // Fungsi untuk memilih aktivitas maksimum yang tidak overlap
    // menggunakan algoritma greedy
    //
    // Input:
    //   dataset : array of [nama, start, finish]
    //
    // Output:
    //   aktivitas_terpilih : array nama aktivitas yang dipilih
    //   total              : jumlah aktivitas yang dipilih
```

---

## Algoritma:

```
ALGORITMA Activity_Selection

BEGIN
    // Inisialisasi dataset aktivitas
    dataset ← [
        ["A1", 1, 4],
        ["A2", 3, 5],
        ["A3", 0, 6],
        ["A4", 5, 7],
        ["A5", 8, 9]
    ]
    
    // Panggil fungsi activity selection
    (aktivitas_terpilih, total) ← activity_selection(dataset)
    
    // Tampilkan hasil
    OUTPUT "Aktivitas yang dipilih: ", aktivitas_terpilih
    OUTPUT "Total aktivitas: ", total
END

---

FUNCTION activity_selection(dataset)
BEGIN
    // Langkah 1: Urutkan aktivitas berdasarkan finish time (ascending)
    dataset ← sort_by_finish_time(dataset)
    
    // Langkah 2: Inisialisasi variabel
    aktivitas_terpilih ← []
    waktu_selesai_terakhir ← 0
    
    // Langkah 3: Iterasi untuk setiap aktivitas
    FOR EACH akt IN dataset DO
        
        // Ekstrak nama, start, dan finish dari aktivitas
        nama ← akt[0]
        start ← akt[1]
        finish ← akt[2]
        
        // Langkah 3a: Cek apakah aktivitas tidak overlap
        // Aktivitas tidak overlap jika waktu mulai >= waktu selesai terakhir
        IF start >= waktu_selesai_terakhir THEN
            
            // Langkah 3b: Tambahkan aktivitas ke daftar terpilih
            aktivitas_terpilih.append(nama)
            
            // Langkah 3c: Update waktu selesai terakhir
            waktu_selesai_terakhir ← finish
            
        END IF
        
    END FOR
    
    // Kembalikan hasil
    RETURN (aktivitas_terpilih, length(aktivitas_terpilih))
END FUNCTION
```

---

## Contoh Eksekusi:

### Dataset Awal:
| Aktivitas | Start | Finish |
|-----------|-------|--------|
| A1        | 1     | 4      |
| A2        | 3     | 5      |
| A3        | 0     | 6      |
| A4        | 5     | 7      |
| A5        | 8     | 9      |

### Setelah Diurutkan (berdasarkan Finish Time):
| Aktivitas | Start | Finish |
|-----------|-------|--------|
| A1        | 1     | 4      |
| A2        | 3     | 5      |
| A3        | 0     | 6      |
| A4        | 5     | 7      |
| A5        | 8     | 9      |

### Proses Seleksi:
| Iterasi | Aktivitas | Start | Finish | Kondisi (start >= waktu_selesai) | Dipilih? | waktu_selesai_terakhir |
|---------|-----------|-------|--------|----------------------------------|----------|------------------------|
| 1       | A1        | 1     | 4      | 1 >= 0 ✓                         | Ya       | 4                      |
| 2       | A2        | 3     | 5      | 3 >= 4 ✗                         | Tidak    | 4                      |
| 3       | A3        | 0     | 6      | 0 >= 4 ✗                         | Tidak    | 4                      |
| 4       | A4        | 5     | 7      | 5 >= 4 ✓                         | Ya       | 7                      |
| 5       | A5        | 8     | 9      | 8 >= 7 ✓                         | Ya       | 9                      |

### Hasil:
- **Aktivitas yang dipilih**: [A1, A4, A5]
- **Total aktivitas**: 3

---

## Strategi Greedy:

Pilih aktivitas dengan **waktu selesai (finish time) paling awal** yang tidak overlap dengan aktivitas yang sudah dipilih sebelumnya.

---

## Kompleksitas:

- **Time Complexity**: O(n log n) untuk sorting + O(n) untuk iterasi = O(n log n)
- **Space Complexity**: O(n) untuk menyimpan hasil

Dimana n adalah jumlah aktivitas dalam dataset.
