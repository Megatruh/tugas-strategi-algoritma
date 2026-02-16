# Job Scheduling with Deadlines - Greedy Algorithm

## Deskripsi

Job Scheduling adalah masalah penjadwalan pekerjaan dengan deadline. Tujuannya adalah memaksimalkan total profit dengan menjadwalkan job-job yang memiliki deadline tertentu ke dalam slot waktu yang tersedia.

## Pseudocode

```
DEKLARASI:
    Jobs         : List yang berisi [nama_job, profit, deadline]
    max_deadline : Deadline terbesar dari semua job
    jadwal       : Array untuk menyimpan jadwal (slot waktu)
    total_profit : Total profit dari job yang berhasil dijadwalkan

ALGORITMA JobScheduling(Jobs):
    INPUT:  Jobs = daftar job dengan [nama, profit, deadline]
    OUTPUT: jadwal pekerjaan dan total_profit maksimal

    // Langkah 1: Mencari deadline terbesar
    max_deadline ← MAX(deadline dari semua job)

    // Langkah 2: Inisialisasi slot jadwal
    // Menggunakan array ukuran (max_deadline + 1), indeks 0 tidak dipakai
    FOR i ← 0 TO max_deadline DO
        jadwal[i] ← None
    END FOR
    total_profit ← 0

    // Langkah 3: SORTING - Strategi Greedy
    // Urutkan job berdasarkan profit secara descending
    SORT Jobs BY profit DESCENDING

    // Langkah 4: ITERASI setiap job
    FOR setiap [nama, profit, deadline] IN Jobs DO

        // Cari slot kosong mundur dari deadline sampai slot 1
        FOR slot ← deadline DOWNTO 1 DO
            IF jadwal[slot] == None THEN
                // Slot tersedia, taruh job di sini
                jadwal[slot] ← nama
                total_profit ← total_profit + profit
                PRINT nama + " berhasil ditaruh di Slot " + slot
                BREAK  // Job sudah dapat slot, lanjut ke job berikutnya
            END IF
        END FOR

        // Jika tidak dapat slot sama sekali
        IF job tidak mendapat slot THEN
            PRINT nama + " gagal dijadwalkan"
        END IF
    END FOR

    // Langkah 5: OUTPUT hasil
    hasil_jadwal ← semua job yang ada di jadwal (tidak None)
    RETURN hasil_jadwal, total_profit
END ALGORITHM
```

## Kompleksitas

- **Time Complexity**: O(n² × d)
  - Sorting: O(n log n)
  - Pencarian slot: O(n × d) dimana d = max deadline
- **Space Complexity**: O(d) untuk array jadwal

## Contoh Dataset

| Job | Profit | Deadline |
| --- | ------ | -------- |
| J1  | 100    | 2        |
| J2  | 19     | 1        |
| J3  | 27     | 2        |
| J4  | 25     | 1        |
| J5  | 15     | 3        |

## Hasil Penjadwalan

| Slot | Job |
| ---- | --- |
| 1    | J4  |
| 2    | J1  |
| 3    | J5  |

**Urutan Job**: J1, J4, J5  
**Total Profit**: 140
