# 1. Inisialisasi Dataset [Simbol, Frekuensi]
data = [
    ['A', 5], ['B', 9], ['C', 12], 
    ['D', 13], ['E', 16], ['F', 45]
]

# 2. Struktur Node sederhana menggunakan Dictionary
# Kita pakai dictionary supaya tidak perlu buat class rumit
def buat_node(char, freq, left=None, right=None):
    return {
        'char': char,
        'freq': freq,
        'left': left,
        'right': right
    }

# 3. Membangun Pohon Huffman dengan List Biasa
# Kita masukkan semua data awal ke dalam list 'nodes'
nodes = [buat_node(item[0], item[1]) for item in data]

while len(nodes) > 1:
    # Langkah Greedy: Urutkan berdasarkan frekuensi terkecil (Ascending)
    nodes.sort(key=lambda x: x['freq'])
    
    # Ambil dua yang paling kecil
    kiri = nodes.pop(0)
    kanan = nodes.pop(0)
    
    # Gabungkan jadi satu orang tua (parent)
    baru = buat_node(None, kiri['freq'] + kanan['freq'], kiri, kanan)
    
    # Masukkan kembali ke list untuk di-sort lagi di loop berikutnya
    nodes.append(baru)

akar_pohon = nodes[0]

# 4. Fungsi Rekursif untuk mencari kode (0 dan 1)
huffman_codes = {}
def cari_kode(node, kode_skrg=""):
    if node['char'] is not None:
        huffman_codes[node['char']] = kode_skrg
        return
    
    if node['left']:
        cari_kode(node['left'], kode_skrg + "0")
    if node['right']:
        cari_kode(node['right'], kode_skrg + "1")

cari_kode(akar_pohon)

# 5. Output dan Perhitungan Statistik
total_frekuensi = sum(item[1] for item in data)
fixed_length = 3
total_bits_original = total_frekuensi * fixed_length
total_bits_compressed = 0

print(f"{'Simbol':<8} | {'Freq':<5} | {'Kode':<8} | {'Bit'}")
print("-" * 40)

for simbol, freq in sorted(data):
    kode = huffman_codes[simbol]
    panjang = len(kode)
    total_bits_compressed += freq * panjang
    print(f"{simbol:<8} | {freq:<5} | {kode:<8} | {panjang}")

print("\n" + "="*40)
print(f"Total Bit Asli       : {total_bits_original} bit")
print(f"Total Bit Kompresi   : {total_bits_compressed} bit")
print(f"Penghematan Ruang    : {((total_bits_original - total_bits_compressed) / total_bits_original) * 100:.2f}%")