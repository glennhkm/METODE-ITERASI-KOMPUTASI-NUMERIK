# def fungsi_fx(x, persamaan):
#     return float(eval(persamaan))

fungsi_fx = lambda persamaan, x : float(eval(persamaan))  #lambda ni sama aja kaya buat fungsi biasa, kek diatas
fungsi_gx = lambda persamaan, x  : float(eval(persamaan))

persamaan_fx = input('Masukkan persamaan f(x) : ')
persamaan_gx = input('Masukkan persamaan g(x) : ')
xiAwal = int(input('Masukkan X Awal : '))
n = int(input("Masukkan nilai n : "))
e = float(0.0001)
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
    