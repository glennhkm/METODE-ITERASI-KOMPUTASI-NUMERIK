import math


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value  # Keluar dari loop dan kembalikan nilai jika input valid
        except ValueError:
            print("Input tidak valid! Mohon periksa kembali input Anda")

# lambda ni sama aja kaya buat fungsi biasa, kek diatas


def fungsi_fx(persamaan, x): return float(eval(persamaan))
def fungsi_gx(persamaan, x): return float(eval(persamaan))


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
print("="*83)
print(f"{'|':<3}{'Iterasi':<10}{'|':<3}{'xi':<20}{'|':<3}{'g(xi)':<20}{'|':<3}{'f(xi)':<20}{'|':<1}")
print("="*83)

for i in range(1, int(n) + 2):
    gxi = fungsi_gx(persamaan_gx, xiAwal)
    fxi = fungsi_fx(persamaan_fx, xiAwal)

    print(f"{'|':<3}{i:<10}{'|':<3}{xiAwal:<20}{'|':<3}{gxi:<20}{'|':<3}{fxi:<20}{'|':<1}")

    if fxi < e:
        print("-"*83)  # End of the table
        print(
            f"\nNilai x didapatkan pada saat iterasi ke-{i} dengan nilai = {xiAwal:.2f}\n")
        break
    xiAwal = gxi

    if i == n + 2:
        print("-"*83)  # End of the table
        print(
            f"\nMaksimum jumlah iterasi telah tercapai, Maka nilai x akan diambil pada iterasi + 1, yaitu x = {xiAwal}.\n")
