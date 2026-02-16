# Minimum Spanning Tree - Kruskal's Algorithm (Greedy)

## Deskripsi

Algoritma Kruskal digunakan untuk mencari Minimum Spanning Tree (MST) dari sebuah graf berbobot. MST adalah himpunan edge yang menghubungkan semua simpul dengan total bobot minimum tanpa membentuk siklus.

## Pseudocode

```
DEKLARASI:
    V           : Jumlah total simpul (A, B, C, D, E = 5 simpul)
    Edges       : List yang berisi [bobot, simpul1, simpul2]
    Parent      : Dictionary untuk menyimpan "Ketua Kelompok" setiap simpul
    MST         : List untuk menyimpan jalur (edges) yang terpilih sebagai solusi
    total_bobot : Variabel untuk menghitung total biaya MST

FUNGSI find(simpul):
    IF Parent[simpul] == simpul THEN
        RETURN simpul
    ELSE
        RETURN find(Parent[simpul])  // Mencari hingga ketemu ketua tertinggi
    END IF
END FUNCTION

FUNGSI union(simpul1, simpul2):
    ketua1 ← find(simpul1)
    ketua2 ← find(simpul2)
    IF ketua1 ≠ ketua2 THEN
        Parent[ketua1] ← ketua2      // Menggabungkan dua wilayah
    END IF
END FUNCTION

ALGORITMA KruskalMST(Edges, V):
    INPUT:  Edges = daftar edge dengan [bobot, simpul1, simpul2]
            V = jumlah simpul dalam graf
    OUTPUT: MST (daftar edge terpilih) dan total_bobot

    // Langkah 1: INISIALISASI Parent
    // Setiap simpul adalah ketua bagi dirinya sendiri
    FOR setiap simpul IN daftar_simpul DO
        Parent[simpul] ← simpul
    END FOR

    // Langkah 2: SORTING Edges
    // Urutkan semua jalur berdasarkan bobot terkecil ke terbesar
    SORT Edges BY bobot ASCENDING

    // Langkah 3: Inisialisasi variabel hasil
    MST ← []
    total_bobot ← 0

    // Langkah 4: LOOPING melalui setiap jalur
    FOR setiap [bobot, u, v] IN Edges DO
        // a. Cari ketua dari simpul u
        ketua_u ← find(u)

        // b. Cari ketua dari simpul v
        ketua_v ← find(v)

        // c. CEK SIKLUS
        IF ketua_u ≠ ketua_v THEN
            // Tidak membentuk siklus, masukkan ke MST
            TAMBAHKAN [u, v, bobot] ke MST
            union(u, v)  // Gabungkan wilayah
            total_bobot ← total_bobot + bobot
        END IF

        // d. CEK BERHENTI
        IF jumlah edge di MST == (V - 1) THEN
            BREAK  // MST sudah lengkap
        END IF
    END FOR

    // Langkah 5: OUTPUT
    RETURN MST, total_bobot
END ALGORITHM
```

## Kompleksitas

- **Time Complexity**: O(E log E) atau O(E log V)
  - Sorting edges: O(E log E)
  - Operasi find/union: O(α(V)) ≈ O(1) per operasi
- **Space Complexity**: O(V + E)

## Contoh Dataset

| Edge | Bobot |
| ---- | ----- |
| A-B  | 2     |
| A-C  | 3     |
| B-C  | 1     |
| B-D  | 4     |
| C-D  | 5     |
| C-E  | 6     |
| D-E  | 2     |

**Jumlah Simpul (V)**: 5

## Hasil MST

| Edge | Bobot |
| ---- | ----- |
| B-C  | 1     |
| A-B  | 2     |
| D-E  | 2     |
| B-D  | 4     |

**Total Bobot MST**: 9
