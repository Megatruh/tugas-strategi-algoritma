# Minimum Spanning Tree - Kruskal's Algorithm (Greedy)

# DEKLARASI
# V: Jumlah total simpul
V = 5

# Edges: List yang berisi [bobot, simpul1, simpul2]
edges = [
    [2, 'A', 'B'],
    [3, 'A', 'C'],
    [1, 'B', 'C'],
    [4, 'B', 'D'],
    [5, 'C', 'D'],
    [6, 'C', 'E'],
    [2, 'D', 'E']
]

# Parent: Dictionary untuk menyimpan "Ketua Kelompok" setiap simpul
parent = {}

# MST: List untuk menyimpan jalur (edges) yang terpilih sebagai solusi
mst = []

# total_bobot: Variabel untuk menghitung total biaya MST
total_bobot = 0


# FUNGSI find(simpul): Mencari ketua tertinggi
def find(simpul):
    if parent[simpul] == simpul:
        return simpul
    else:
        return find(parent[simpul])  # Mencari hingga ketemu ketua tertinggi


# FUNGSI union(simpul1, simpul2): Menggabungkan dua wilayah
def union(simpul1, simpul2):
    ketua1 = find(simpul1)
    ketua2 = find(simpul2)
    if ketua1 != ketua2:
        parent[ketua1] = ketua2  # Menggabungkan dua wilayah


# ALGORITMA UTAMA

# 1. INISIALISASI Parent: Setiap simpul adalah ketua bagi dirinya sendiri
simpul_list = ['A', 'B', 'C', 'D', 'E']
for simpul in simpul_list:
    parent[simpul] = simpul

print("=" * 50)
print("KRUSKAL'S ALGORITHM - MINIMUM SPANNING TREE")
print("=" * 50)

# 2. SORTING Edges: Urutkan semua jalur berdasarkan bobot terkecil ke terbesar
edges.sort(key=lambda x: x[0])

print("\nDaftar Edge setelah diurutkan:")
print(f"{'Bobot':<10}{'Simpul 1':<12}{'Simpul 2':<12}")
print("-" * 34)
for edge in edges:
    print(f"{edge[0]:<10}{edge[1]:<12}{edge[2]:<12}")

print("\n" + "=" * 50)
print("PROSES SELEKSI EDGE:")
print("=" * 50)

# 3. LOOPING melalui setiap jalur [bobot, u, v] di Edges
for bobot, u, v in edges:
    # a. Cari ketua dari simpul u
    ketua_u = find(u)
    # b. Cari ketua dari simpul v
    ketua_v = find(v)
    
    # c. CEK SIKLUS: Jika ketua_u != ketua_v (tidak membentuk siklus)
    if ketua_u != ketua_v:
        # Masukkan jalur [u, v] ke dalam MST
        mst.append([u, v, bobot])
        # Jalankan union(u, v) untuk menggabungkan wilayah
        union(u, v)
        # Tambahkan bobot ke total_bobot
        total_bobot += bobot
        print(f"✓ Edge ({u}-{v}) dengan bobot {bobot} DIPILIH")
    else:
        print(f"✗ Edge ({u}-{v}) dengan bobot {bobot} DITOLAK (membentuk siklus)")
    
    # d. CEK BERHENTI: Jika jumlah jalur di MST sudah mencapai (V - 1)
    if len(mst) == V - 1:
        print("\nMST sudah lengkap (V-1 edge)!")
        break

# 4. OUTPUT: Tampilkan daftar jalur di MST dan total_bobot
print("\n" + "=" * 50)
print("HASIL MINIMUM SPANNING TREE:")
print("=" * 50)
print(f"\n{'Edge':<15}{'Bobot':<10}")
print("-" * 25)
for edge in mst:
    print(f"{edge[0]}-{edge[1]:<12}{edge[2]:<10}")
print("-" * 25)
print(f"Total Bobot MST: {total_bobot}")
print("=" * 50)
