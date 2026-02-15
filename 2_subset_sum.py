# ambil fungsi penghasil powerset dari dokuemntasi python itertools
from itertools import chain, combinations

def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

arr_A = [3,5,9,12]
target = 17

# buat list powerset dari arr_A
powerset_A = list(powerset(arr_A))
# ambil jumlah dari tiap subset dalam powerset_A mengguankan list comprehension
jumlah_subsets = [sum(powerset_A[i]) for i in range(len(powerset_A))]
# ambil subset yang jumlahnya sesuai dengan target
subsets_target = [powerset_A[j] for j in range(len(jumlah_subsets)) if jumlah_subsets[j] == target]
if not subsets_target:
    print(f"tidak ada subsets dari array{arr_A} yang jumlahnya sesuai dengan target {target}")
else : 
    print(f"subsets dari array {arr_A} yang jumlahnya sesuai dengan target {target} adalah {subsets_target}")

# Analisis waktu runtime
print(f"\nAnalisis Waktu Runtime Algoritma Brute Force pada Implementasi Subset Sum")
print('='*57)
print('|'+' '*2 + 'n' + ' '*2  + '|' + ' '*2 + 'Jumlah Subset (2^n)' + ' '*2 + '|' + ' '*2 + 'Waktu Runtime (detik)' + ' '*2 + '|')
print('='*57)

n = [4,5,6]
for x in n:
     
    import time

    start = time.perf_counter()
    if x == 4:
        arr_A = [3,5,9,12]
        target = 17
    
    if x == 5:
        arr_A = [3,5,7,9,12]
        target = 12
    
    if x == 6:
        arr_A = [3,4,7,6,9,12]
        target = 10
    

    # buat list powerset dari arr_A
    powerset_A = list(powerset(arr_A))
    # ambil jumlah dari tiap subset dalam powerset_A mengguankan list comprehension
    jumlah_subsets = [sum(powerset_A[i]) for i in range(len(powerset_A))]
    # ambil subset yang jumlahnya sesuai dengan target
    subsets_target = [powerset_A[j] for j in range(len(jumlah_subsets)) if jumlah_subsets[j] == target]

    end = time.perf_counter()

    print(f"|{' '*2}{len(arr_A)}{' '*2}|{' '*10}{len(powerset_A)}{' '*11}|{' '*8}{end - start:.6f}{' '*9}|")

print('-'*57)



