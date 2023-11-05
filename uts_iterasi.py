import math


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value  # Keluar dari loop dan kembalikan nilai jika input valid
        except ValueError:
            print("Input tidak valid! Mohon periksa kembali input Anda")

fungsi_fx = lambda persamaan, x : float(eval(persamaan))  #lambda ni sama aja kaya buat fungsi biasa, kek diatas
fungsi_gx = lambda persamaan, x  : float(eval(persamaan))

print("=====Panduan penggunaan operator=====")
print("| Operator tambah : +               |")
print("| Operator kurang : -               |")
print("| Operator kali : *                 |")
print("| Operator bagi : /                 |")
print("| Operator pangkat : **             |")
print("| Operator akar : math.sqrt(x)      |")
print("| Operator EXP : math.exp(x)        |")
print("=====================================")

persamaan_fx = input('Masukkan persamaan f(x) : ')
persamaan_gx = input('Masukkan persamaan g(x) : ')

xiAwal = get_float_input("Masukkan pendekatan awal (x0): ")
n = get_float_input("Masukkan jumlah maksimum iterasi (N): ")
e = get_float_input("Masukkan toleransi error (e): ")

print()
print(f"{'Iterasi':<10}{'xi':<20}{'g(xi)':<20}{'f(xi)':<20}")

for i in range(1, int(n) + 2):
    gxi = fungsi_gx(persamaan_gx, xiAwal)
    fxi = fungsi_fx(persamaan_fx, xiAwal)
    
    print(f"{i:<10}{xiAwal:<20}{gxi:<20}{fxi:<20}")
    
    if fxi < e:
        print(f"\nNilai x didapatkan pada saat iterasi ke-{i} dengan nilai = {xiAwal:.2f}\n")
        break
    xiAwal = gxi
    
    if i == n + 2:
        print(f"\nMaksimum jumlah iterasi telah tercapai, Maka nilai x akan diambil pada iterasi + 1, yaitu x = {xiAwal}.\n")
      
      
