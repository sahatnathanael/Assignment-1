a = float(input("Masukkan nilai ujian teori anda = "))
b = float(input("Masukkan nilai ujian praktik anda = "))

if (a>=70 and b>=70) : # kondisi 1
    print("Selamat, anda lulus!") # aksi true 1
elif (a>=70 and b<70) : # kondisi 2
    print("Anda harus mengulang ujian praktik!") # aksi true 2
elif (a<70 and b>=70) : # kondisi 3
    print("Anda harus mengulang ujian teori!") # aksi true 3
else : # kondisi 4
    print("Anda harus mengulang ujian praktik dan teori") # aksi false 1
print("End of program")









