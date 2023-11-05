# def fungsi_fx(x, persamaan):
#     return float(eval(persamaan))

fungsi_fx = lambda persamaan, x : float(eval(persamaan))  #lambda ni sama aja kaya buat fungsi biasa, kek diatas
fungsi_gx = lambda persamaan, x  : float(eval(persamaan))

persamaan_fx = input('Masukkan persamaan f(x) : ')
persamaan_gx = input('Masukkan persamaan g(x) : ')
xiAwal = int(input('Masukkan X Awal : '))
n = int(input("Masukkan nilai n : "))
e = float(0.0001)

for i in range(1, n + 2):
    gxi = fungsi_gx(persamaan_gx, xiAwal)
    fxi = fungsi_fx(persamaan_fx, xiAwal)
    #tampilin table disini
    if fxi < e:
        break
    xiAwal = gxi
    

print(f"\nNilai x didapatkan pada saat iterasi ke-{i} dengan nilai = {xiAwal:.2f}\n")
