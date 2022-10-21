# Menginput nilai variabel
a = input("Masukkan nilai a = ")
b = input("Masukkan nilai b = ")

# Mencetak nilai variabel
print("Variabel a = ", a)
print("Variabel b = ", b)

# Mencetak hasil operasi kedua variabel dengan String Format
print("Hasil penggabungan {0} & {1} = %s".format(a,b) %(a+b))

# Konversi nilai variabel
a = int(a)
b = int(b)
print("Hasil penjumlahan {0} + {1} = %d".format(a,b) %(a+b))
print("Hasil pembagian {0} / {1} = %d".format(a,b) %(a/b))
