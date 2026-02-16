# Fractional Knapsack - Greedy Algorithm

## Deskripsi

Fractional Knapsack adalah masalah optimasi di mana kita dapat mengambil sebagian (fraksi) dari suatu item untuk memaksimalkan nilai total dalam kapasitas tas yang terbatas.

## Pseudocode

```
ALGORITHM FractionalKnapsack(items, kapasitas)
    INPUT:  items = daftar item dengan [nama, berat, nilai]
            kapasitas = kapasitas maksimum tas
    OUTPUT: total_nilai maksimal dan daftar item yang diambil

    // Langkah 1: Hitung rasio nilai/berat untuk setiap item
    FOR setiap item IN items DO
        rasio ← item.nilai / item.berat
        item.rasio ← rasio
    END FOR

    // Langkah 2: Urutkan item berdasarkan rasio secara descending
    SORT items BY rasio DESCENDING

    // Langkah 3: Inisialisasi variabel
    total_nilai ← 0
    sisa_kapasitas ← kapasitas
    hasil_pengambilan ← []

    // Langkah 4: Ambil item dengan strategi greedy
    FOR setiap item IN items DO
        IF sisa_kapasitas ≤ 0 THEN
            BREAK   // Tas sudah penuh
        END IF

        IF item.berat ≤ sisa_kapasitas THEN
            // Ambil item secara penuh (100%)
            sisa_kapasitas ← sisa_kapasitas - item.berat
            total_nilai ← total_nilai + item.nilai
            TAMBAHKAN item.nama (100%) ke hasil_pengambilan
        ELSE
            // Ambil item sebagian (Fractional)
            fraksi ← sisa_kapasitas / item.berat
            nilai_sebagian ← item.nilai × fraksi
            total_nilai ← total_nilai + nilai_sebagian
            TAMBAHKAN item.nama (fraksi × 100%) ke hasil_pengambilan
            sisa_kapasitas ← 0   // Tas sekarang penuh
        END IF
    END FOR

    // Langkah 5: Output hasil
    RETURN hasil_pengambilan, total_nilai
END ALGORITHM
```

## Kompleksitas

- **Time Complexity**: O(n log n) - didominasi oleh proses sorting
- **Space Complexity**: O(n) - untuk menyimpan rasio dan hasil

## Contoh Dataset

| Item | Berat | Nilai | Rasio |
| ---- | ----- | ----- | ----- |
| I1   | 10    | 60    | 6.0   |
| I2   | 20    | 100   | 5.0   |
| I3   | 30    | 120   | 4.0   |

**Kapasitas Tas**: 50
