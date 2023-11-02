# def fungsi_fx(x, persamaan):
#     return float(eval(persamaan))

fungsi_fx = lambda persamaan, x : float(eval(persamaan))  #lambda ni sama aja kaya buat fungsi biasa, kek diatas
fungsi_gx = lambda persamaan, x  : float(eval(persamaan))

print("\nPentunjuk cara input fungsi f(x) :")
print("Ex: x**2 - 2*x - 3")

print("\nPentunjuk cara input fungsi g(x) :")
print("Ex: 3/(x - 2)")

persamaan_fx = input("\nMasukkan persamaan f(x)\t\t: ")
persamaan_gx = input("Masukkan persamaan g(x)\t\t: ")
xiAwal = int(input("Masukkan X Awal\t\t\t: "))
n = int(input("Masukkan nilai max iterasi\t: "))
e = float(input("Masukkan nilai toleransi error\t:"))

fxi = fungsi_fx(persamaan_fx, xiAwal)
gxi = fungsi_gx(persamaan_gx, xiAwal)

for i in range(2, n + 2):
    if fxi < e:
        break
    else:
        xiSelanjutnya = gxi
        gxi = fungsi_gx(persamaan_fx, xiSelanjutnya)
        fxi = fungsi_fx(persamaan_gx, xiSelanjutnya)

print(f"\nNilai x didapatkan pada saat iterasi ke-{i-1} dengan nilai = {xiSelanjutnya:.2f}\n")
    