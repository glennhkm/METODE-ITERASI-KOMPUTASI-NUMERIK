import math


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value  # Keluar dari loop dan kembalikan nilai jika input valid
        except ValueError:
            print("Input tidak valid! Mohon periksa kembali input Anda")


def fungsi(persamaan, x): 
    return float(eval(persamaan))


print("\n==== Panduan penggunaan operator ====")
print("| Operator tambah : +               |")
print("| Operator kurang : -               |")
print("| Operator kali : *                 |")
print("| Operator bagi : /                 |")
print("| Operator pangkat : **             |")
print("| Operator akar : math.sqrt(x)      |")
print("| Operator EXP : math.exp(x)        |")
print("=====================================\n")

persamaan_fx = input('Masukkan persamaan f(x)\t\t\t: ')
persamaan_gx = input('Masukkan persamaan g(x)\t\t\t: ')

xiAwal = get_float_input("Masukkan pendekatan awal (x0)\t\t: ")
n = get_float_input("Masukkan jumlah maksimum iterasi (N)\t: ")
e = get_float_input("Masukkan toleransi error (e)\t\t: ")

print()
print("="*83)
print(f"{'|':<3}{'Iterasi':<10}{'|':<3}{'xi':<20}{'|':<3}{'g(xi)':<20}{'|':<3}{'f(xi)':<20}{'|':<1}")
print("="*83)

for i in range(1, int(n) + 2):
    gxi = fungsi(persamaan_gx, xiAwal)
    fxi = fungsi(persamaan_fx, xiAwal)

    print(f"{'|':<3}{i:<10}{'|':<3}{xiAwal:<20.6f}{'|':<3}{gxi:<20.6f}{'|':<3}{fxi:<20.6f}{'|':<1}")

    if fxi < e:
        print("-"*83)  # End of the table
        print(
            f"\nNilai x didapatkan pada saat iterasi ke-{i} dengan nilai = {xiAwal:.2f}\n")
        break
    xiAwal = gxi

else:
    print("-"*83)  # End of the table
    print(
        f"\nMaksimum jumlah iterasi telah tercapai, Maka nilai x akan diambil pada (Nilai maksimum iterasi + 1), yaitu x = {xiAwal:.2f}.\n")
