# Huffman Coding - Greedy Algorithm

## Deskripsi

Huffman Coding adalah algoritma kompresi data yang menggunakan pendekatan greedy untuk membangun kode prefix optimal. Karakter dengan frekuensi tinggi mendapat kode lebih pendek, sedangkan karakter dengan frekuensi rendah mendapat kode lebih panjang.

## Pseudocode

```
DEKLARASI:
    Data          : List yang berisi [simbol, frekuensi]
    Nodes         : List untuk menyimpan node-node pohon
    huffman_codes : Dictionary untuk menyimpan kode setiap simbol

STRUKTUR Node:
    char   : Karakter (simbol)
    freq   : Frekuensi kemunculan
    left   : Anak kiri
    right  : Anak kanan

FUNGSI buat_node(char, freq, left, right):
    RETURN Node dengan {char, freq, left, right}
END FUNCTION

FUNGSI cari_kode(node, kode_skrg):
    // Basis: Jika node adalah daun (leaf)
    IF node.char ≠ None THEN
        huffman_codes[node.char] ← kode_skrg
        RETURN
    END IF

    // Rekursi: Telusuri anak kiri dengan tambahan "0"
    IF node.left ≠ None THEN
        cari_kode(node.left, kode_skrg + "0")
    END IF

    // Rekursi: Telusuri anak kanan dengan tambahan "1"
    IF node.right ≠ None THEN
        cari_kode(node.right, kode_skrg + "1")
    END IF
END FUNCTION

ALGORITMA HuffmanCoding(Data):
    INPUT:  Data = daftar simbol dengan [simbol, frekuensi]
    OUTPUT: huffman_codes (kode untuk setiap simbol)

    // Langkah 1: Inisialisasi nodes
    // Buat node untuk setiap simbol
    FOR setiap [simbol, freq] IN Data DO
        node ← buat_node(simbol, freq, None, None)
        TAMBAHKAN node ke Nodes
    END FOR

    // Langkah 2: Bangun Pohon Huffman
    WHILE jumlah Nodes > 1 DO
        // Strategi Greedy: Urutkan berdasarkan frekuensi (ascending)
        SORT Nodes BY freq ASCENDING

        // Ambil dua node dengan frekuensi terkecil
        kiri ← POP node pertama dari Nodes
        kanan ← POP node pertama dari Nodes

        // Gabungkan menjadi node parent baru
        freq_gabungan ← kiri.freq + kanan.freq
        parent ← buat_node(None, freq_gabungan, kiri, kanan)

        // Masukkan parent kembali ke Nodes
        TAMBAHKAN parent ke Nodes
    END WHILE

    // Langkah 3: Ambil akar pohon
    akar_pohon ← Nodes[0]

    // Langkah 4: Generate kode Huffman
    huffman_codes ← {}
    cari_kode(akar_pohon, "")

    // Langkah 5: Hitung statistik kompresi
    total_frekuensi ← SUM(freq dari semua simbol)
    fixed_length ← 3  // Asumsi kode fixed-length 3 bit
    total_bits_original ← total_frekuensi × fixed_length
    total_bits_compressed ← 0

    FOR setiap [simbol, freq] IN Data DO
        kode ← huffman_codes[simbol]
        total_bits_compressed ← total_bits_compressed + (freq × LENGTH(kode))
    END FOR

    penghematan ← ((total_bits_original - total_bits_compressed) / total_bits_original) × 100%

    // Langkah 6: OUTPUT
    RETURN huffman_codes, total_bits_compressed, penghematan
END ALGORITHM
```

## Kompleksitas

- **Time Complexity**: O(n log n)
  - Membangun pohon: O(n log n) karena sorting di setiap iterasi
  - Dengan priority queue (heap): bisa dioptimasi ke O(n log n)
- **Space Complexity**: O(n) untuk menyimpan pohon

## Contoh Dataset

| Simbol | Frekuensi |
| ------ | --------- |
| A      | 5         |
| B      | 9         |
| C      | 12        |
| D      | 13        |
| E      | 16        |
| F      | 45        |

## Hasil Huffman Coding

| Simbol | Frekuensi | Kode Huffman | Panjang Bit |
| ------ | --------- | ------------ | ----------- |
| A      | 5         | 1100         | 4           |
| B      | 9         | 1101         | 4           |
| C      | 12        | 100          | 3           |
| D      | 13        | 101          | 3           |
| E      | 16        | 111          | 3           |
| F      | 45        | 0            | 1           |

## Statistik Kompresi

- **Total Bit Asli**: 300 bit (100 karakter × 3 bit)
- **Total Bit Kompresi**: 224 bit
- **Penghematan Ruang**: ~25.33%
